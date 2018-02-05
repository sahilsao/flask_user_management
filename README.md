## Overview

This Flask application contains the basic user management functionality (register, login, logout) to demonstrate the use of py.test.

## Motivation

After reading Brian Okken's book (Python Testing with py.test), I was convinced that I should learn about py.test and then figure out how to use it to test Flask applications.

## How to Run

In the top-level directory:

    $ export FLASK_APP=main.py
    $ flask run

## Key Python Modules Used

- Flask: micro-framework for web application development
- Jinga2 - templating engine
- SQLAlchemy - ORM (Object Relational Mapper)
- Flask-Bcrypt - password hashing
- Flask-Login - support for user management
- Flask-WTF - simplifies forms

This application is written using Python 3.6.

## Unit Testing

TBD