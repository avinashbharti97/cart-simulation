# cart-simulation

#installing prerequisites
```
$ sudo apt-get update
$ sudo apt-get install python3 python3-pip virtualenvwrapper python-dev libpq-dev
```

#create virtual env
- move to the cloned project directory
```
$ virtualenv -p /usr/bin/python3 env
```

- activate the virtualenv
```
$ source env/bin/activate
```

#Installing and Running the project
```
$ cd task
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```


#APIs
```
    "add-product": "http://127.0.0.1:8000/api/add-product/",
    "add-user": "http://127.0.0.1:8000/api/add-user/",
    "create-cart": "http://127.0.0.1:8000/api/create-cart/"

    ## to get user cart
    http://127.0.0.1:8000/api/get-user-cart/<userId>/


    ## to get notification
    http://127.0.0.1:8000/api/get-user-notification/<userId>/

    
```
