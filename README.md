# Awwwards Clone
[![License: MIT]()](LICENSE)
[![codebeat badge]()]()

## Description
This a web application built using Python, Django and Postgresql.The app is a clone  of the Awwwards web app, you can view posted projects that contains the title, a screenshot of the landing page and the project description. As a user you can post project to be reviewed by other users.One can also rate and review other users' projects, as well as searching for a specific project, view your own and other users' projects. The user can also view their profile page.


## Author

Joshua Kimani


## DB diagram
![Awards]()
![Link to dbdiagram.io](https://dbdiagram.io/d/5e6d2c634495b02c3b883ee2)




# Installation

## Clone
    
```bash
    git clone https://github.com/JKimani77/Awards-.git
    
```
##  Create virtual environment
```bash
    python -m venv virtual
    
```
## Activate virtual and install requirements.txt
```bash
   $ virtual/Scripts/activate
   $ pip install -r requirements.txt
    
```
## Run initial migration
```bash
   $ python3.6 manage.py makemigrations awards
   $ python3.6 manage.py migrate
    
```


## Run app
```bash
   $ python manage.py runserver
    
```

## Test class

```bash
    $ python manage.py test
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Technologies Used
    Python Shell
    Python 3.7
    Django
    Bootstrap Materialize
    HTML
    CSS
    PostgreSQL
    Django Rest Framework


## Known Bugs

There are no known bugs

## Copyright
Copyright (C) 2020 ~ J.Kimani
