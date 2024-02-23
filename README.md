# ORDER APP REST API'S

### 23rd February 2024

## Author  
  
[Mwikali](https://github.com/mwiks-dev)  
  
# Description  
This is an app that contains restful API's that allows users to authenticate using Auth0,create customer profiles, create orders and receive texts once an order is created.

##  Live Link  
 

## User Story  
  
* Allow customer creation/input 
* Allow order creation/input 
* Allow user authentication and authorization via OpenID Connect 
* When an order is added, send the customer an SMS alerting them   

  
## Setup and Installation  
  
##### Clone the repository:  
 ```bash 
 git@github.com:mwiks-dev/OrderRestAPIs.git
```
##### Navigate into the folder and install requirements  
 ```bash 
    cd OrderRestAPIs 
    pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
    - python3 -m venv virtual 
    - source env/bin/activate  
```  
##### Setup Database  
  Since we are using an SQLite Database run migrations using the commands below
 ```bash 
python manage.py makemigrations TestApp
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```

##### Setup Auth0 credentials 
 Add the credentials needed in your own dotenv file as guided by the .env.example file

##### Setup AfricasTalking Credentials
 Add the credentials needed in your own dotenv file as guided by the .env.example file

##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
## Known Bugs  
* There are no known bugs  
  
## Support and Contact Information 

Incase of any contributions fork the repo and make any substantial changes.
Incase of any ideas,suggestions or complaints feel free to connect with me on mwikali119@gmail.com 

## License
MIT
Copyright (c) 2024 **Order App**