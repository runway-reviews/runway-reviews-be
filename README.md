# Runway Reviews

## Tech Stack 
---
[Python](https://www.python.org/) - The project is developed with Python 3.12.1. Ensure that Python and pip (Python's package installer) are in your system's PATH. 
[Django REST Framework](https://www.django-rest-framework.org/) - This was used to ensure a scalable and secure connection between the front and backend services. 

## Getting Started
---
1. Clone the Repository - clone this repository to your local machine
2. Install - Navigate into the newly cloned repository and install the dependencies. </br>
   ```
   pip install django
   pip install djangorestframework
   pip install -r requirements.txt
   ```
4. Set up a virtual environment - Go to your project directory and create a virtual environment.
   ```
   python3 -m venv .venv
   ```
6. Activate the virtual environment
   ```
   . .venv/bin/activate
   ```
7. Run migrations
   ```
   python manage.py migrate
   ```
9. Start the Django server
    ```
   python manage.py runserver
    ```

## API Endpoints
---
The base url for the following endpoints is 

Airports

Users

Reviews


