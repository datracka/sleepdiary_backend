# Sleepgood Backend API
***

##  To run the app, follow the following steps:
***

### First off, install the following system dependencies:

- Python 3.4+
- python3-dev
- virtualenv
- python3-pip
- postgresql
- libpq-dev

---

### Then build the application:

1. Clone the repository:

```$ git clone https://github.com/abunuwas/sleepgood-pyBackend.git```

2. ```cd``` into sleepgood-pyBackend and create a virtual environment and bind it to Python3:

..2.1. In Linux/Unix:

```$ virtualenv venv --python=python3```

..2.2. In Windows:

```$ virtualenv venv --python=<path\to\python3.exe>```

3. Activate the virtual environment:

..3.1. In Linux/Unix:

```
$ source venv/bin/activate
(venv)$ 
``` 

..3.2. In Windows:

```
$ venv\Scripts\activate
```

4. Install the Python dependencies:

```$ pip install -r requirements.txt```

5. Create a postgresql table with the user and password required by the application:

```
$ sudo su - postgres
$ psql
$ create user marmot with password 'sleepgood';
$ create database sleepdiary owner marmot;
$ \q
$ exit
```

6. Apply database migrations:

```
(venv)$ cd sleepgood
(venv)$ python manage.py migrate
```

7. Run the application on port 8080:

```$ python manage.py runserver 8080```

8. ENJOY :D!!

***

Styleguide: https://www.python.org/dev/peps/pep-0008/

***

# TODO 

***

### First milestone ()

* PUT update
* DELETE delete

### Second Milestone

* Create script for laoding test values (user carlos)
* deploy to a server!
* Postgress
* allow user based calendar
