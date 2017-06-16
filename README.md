Structure of the app is to be a python-MySQL powered DB app powered by Flask. Still looking for optimal UI/UX framework that will conform to that

I am using this site to walk through the app:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates

Prior to running the app: 
1) ensure Flask is downloaded into the root directory of your app. See part one of the above tutorial for installation and setup details

key commands::
run flask 2 ways,

First way is type python interpreter first followed by scripts
$ flask\Scripts\python run.py

acivate virtual environment first
$ flask\Scripts\activate
$ python run.py


(below is from the author of the site)

=========

A decently featured microblogging web application written in Python and Flask that I'm developing in my Flask Mega-Tutorial series that begins [here](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Installation
------------

The tutorial referenced above explains how to setup a virtual environment with all the required modules.

The sqlite database must also be created before the application can run, and the `db_create.py` script takes care of that. See the [Database tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database) for the details.

Running
-------

To run the application in the development web server just execute `run.py` with the Python interpreter from the flask virtual environment.

