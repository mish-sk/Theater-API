# Theater API Service

Welcome to the Theater API Service!

The Theater API is a RESTful web service for managing theater-related information. This API allows users to manage plays, theater halls, users, reservations, tickets, etc. The API provides endpoints for various operations such as creating, reading, updating, and deleting resources. It also includes JWT authentication to secure the endpoints.
## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [License](#license)

## Features
- User management
- Plays management
- Tickets  management
- JWT authentication


### Installation


Before getting started with Theater API Service, ensure that you have Python installed on your system. If Python is not installed, you can download and install it from the [official Python website](https://www.python.org/downloads/).

Once Python is installed, you can proceed with the following steps to set up Theater API Service:



```
git clone https://github.com/mish-sk/Theater-API.git
cd Theater-API
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

### Set up the database:
    
- Create the migrations:
   ```sh
   python manage.py makemigrations
   ```
    
- Run the migrations:
   ```sh
   python manage.py migrate
   ```
### Create a superuser:

 ```sh
 python manage.py createsuperuser
 ```

### Start the development server:
 ```sh
 python manage.py runserver
 ```


## License

This project is licensed under the MIT License.

---
