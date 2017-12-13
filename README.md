# Sleepgood Backend API
***

##  To run the app, follow the following steps:
***

### First off, install the following system dependencies:

- Python 3.4+
- virtualenv
- postgres or postgresql


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

```$ pip3 install -r requirements.txt```

5. create a file named `.env` in `<project root/sleepdiary_backend/.env` and copy this:

```
DEBUG=true
SECRET_KEY=%s+pe5$g$47hf!gv()^h^y&98_!%l-9_0au-#4*k&&pz22@!(^
POSTGRES_DB=sleepdiary
POSTGRES_USER=marmot
POSTGRES_PASSWORD=sl33p4!
DB_SERVICE=localhost
DB_PORT=5432
```


6. Create a postgresql table with the user and password required by the application:
 

```
$ sudo su - postgres (linux)
$ psql
$ create user marmot with password sl33p4!;
$ create database sleepdiary owner marmot;
$ \q
$ exit
```

7. Apply database migrations:

```
(venv)$ cd <project>
(venv)$ python manage.py migrate

```
or if using container
```
docker-compose run web /usr/local/bin/python manage.py migrate
```

7. Run the application on port 8000:

```$ python manage.py runserver 8000```

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
