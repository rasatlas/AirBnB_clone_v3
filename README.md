# 0x05. AirBnB clone - RESTful API
`Python` `Back-end` `API` `Webserver` `Flask`

## Resources</br>
__Read or watch:__
- [Learn REST: A RESTful Tutorial](https://www.restapitutorial.com/)
- [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
- [HTTP access control (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [Flask cheatsheet](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/301/flask_cheatsheet.pdf)
- [What are Flask Blueprints, exactly?](https://stackoverflow.com/questions/24420857/what-are-flask-blueprints-exactly)
- [Flask](https://palletsprojects.com/p/flask/)
- [Modular Applications with Blueprints](https://flask.palletsprojects.com/en/3.0.x/blueprints/)
- [Flask tests](https://flask.palletsprojects.com/en/3.0.x/testing/)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)

## Learning Objectives</br>
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), __without the help of google:__

### General
- What REST means
- What API means
- What CORS means
- What is an API
- What is a REST API
- What are other type of APIs
- Which is the HTTP method to retrieve resource(s)
- Which is the HTTP method to create a resource
- Which is the HTTP method to update resource
- Which is the HTTP method to delete resource
- How to request REST API

## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3` (`version 3.4.3`)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (`version 1.7`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests
- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- You have to use the [unittest module](https://docs.python.org/3/library/unittest.html)
- All your test files should be python files (extension: `.py`)
- All your test files and folders should start by `test_`
- Your file organization in the tests folder should be the same as your project: ex: for `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`

### Install Flask
```Bash
$ pip3 install Flask
```

## Tasks</br>
__0. Restart from scratch!__
