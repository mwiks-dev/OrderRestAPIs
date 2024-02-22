import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import CustomerSerializer, OrderSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer, Order


oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def index(request):

    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    # print(token)
    request.session["user"] = token

    userinfo = token.get('userinfo',{})
    # print(userinfo)

    # Extract user details from userinfo
    code = userinfo.get('sub')  # Auth0 user ID
    username = userinfo.get('nickname')
    email = userinfo.get('email')
    first_name = userinfo.get('given_name','')
    second_name = userinfo.get('family_name','')


    # Get the user model
    User = get_user_model()

    # Check if a user with this email already exists
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # No user was found, so create a new user
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=second_name)
        # Here, you might set other fields on the user object before saving
        user.set_unusable_password()  # Optional: Set an unusable password since auth is handled by Auth0
        user.save()
    else:
        # User exists, so you might want to update any details
        user.first_name = first_name
        user.last_name = second_name
        user.save()

    # customer, customer_created = Customer.objects.get_or_create(user=user)
    # customer.name = first_name + ' ' + second_name
    # customer.code = code
    # customer.save()



    # Log the user in (you might need to customize this part)
    auth_login(request, user,backend='django.contrib.auth.backends.ModelBackend')

    return redirect(request.build_absolute_uri(reverse("index")))


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

class CustomerCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access this view


    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = CustomerSerializer(data=request.data)
        
        if serializer.is_valid():
            # Check if the customer already exists for this user
            customer, created = Customer.objects.get_or_create(user=user, defaults=serializer.validated_data)
            if not created:
                # Update existing customer data if needed
                for key, value in serializer.validated_data.items():
                    setattr(customer, key, value)
                customer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderCreateView(LoginRequiredMixin,APIView):

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
