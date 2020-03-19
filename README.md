# Avvards Clone
[![License: MIT]()](LICENSE)


## Description
The application will allow a user to post a project he/she has created and get it reviewed by his/her peers. 

A project can be rated based on 3 different criteria:

Design,
Usability,
Content,


## Author

Joshua Kimani


## DB diagram
(![Awards](https://user-images.githubusercontent.com/38456207/76689597-8ac3fd00-6648-11ea-84e4-c11540ab0da9.png)





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
    
    Python 3.7
    Django
    Bootstrap 4
    HTML
    Javascript
    PostgreSQL
    


## Known Bugs

There are no known bugs

## Copyright
Copyright (C) 2020 ~ J.Kimani

