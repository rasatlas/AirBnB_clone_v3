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
__0. Restart from scratch!__</br>
No no no! We are already too far in the project to restart everything.
</br>
But once again, let’s work on a new codebase.
</br>
For this project you will fork this [codebase](https://github.com/alexaorrico/AirBnB_clone_v2):

- Update the repository name to `AirBnB_clone_v3`
- Update the `README.md`:
	- Add yourself as an author of the project
	- Add new information about your new contribution
	- Make it better!
- If you’re the owner of this codebase, create a new repository called `AirBnB_clone_v3` and copy over all files from `AirBnB_clone_v2`

<hr style="height: .5px;">

__1. Never fail!__</br>
<p>Since the beginning we’ve been using the `unittest` module, but do you know why `unittests` are so important? Because when you add a new feature, you refactor a piece of code, etc… you want to be sure you didn’t break anything.</p>

<p>At Holberton, we have a lot of tests, and they all pass! Just for the Intranet itself, there are:</p>

- 5,213 assertions (as of 08/20/2018)
- 13,061 assertions (as of 01/25/2021)

<p>The following requirements must be met for your project:</p>

- all current tests must pass (don’t delete them…)
- add new tests as much as you can (tests are mandatory for some tasks)

```Bash
guillaume@ubuntu:~/AirBnB_v3$ python3 -m unittest discover tests 2>&1 | tail -1
OK
guillaume@ubuntu:~/AirBnB_v3$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v3$ 
```

<hr style="height: .5px;">

__2. Improve storage__</br>
<p>Update `DBStorage` and `FileStorage`, adding two new methods. __All changes should be done in the branch__ `storage_get_count`:</p>

<p>A method to retrieve one object:</p>

- Prototype: `def get(self, cls, id)`:
	- `cls`: class
	- `id`: string representing the object ID
- Returns the object based on the class and its ID, or `None` if not found
<p>A method to count the number of objects in storage:</p>

- Prototype: `def count(self, cls=None):`
	- cls: class (optional)
- Returns the number of objects in storage matching the given class. If no class is passed, returns the count of all objects in storage.
<p>Don’t forget to add new tests for these 2 methods on each storage engine.</p>

```Bash
guillaume@ubuntu:~/AirBnB_v3$ cat test_get_count.py
#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))

guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./test_get_count.py 
All objects: 1013
State objects: 27
First state: [State] (f8d21261-3e79-4f5c-829a-99d7452cd73c) {'name': 'Colorado', 'updated_at': datetime.datetime(2017, 3, 25, 2, 17, 6), 'created_at': datetime.datetime(2017, 3, 25, 2, 17, 6), '_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fc0103a8e80>, 'id': 'f8d21261-3e79-4f5c-829a-99d7452cd73c'}
guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ ./test_get_count.py 
All objects: 19
State objects: 5
First state: [State] (af14c85b-172f-4474-8a30-d4ec21f9795e) {'updated_at': datetime.datetime(2017, 4, 13, 17, 10, 22, 378824), 'name': 'Arizona', 'id': 'af14c85b-172f-4474-8a30-d4ec21f9795e', 'created_at': datetime.datetime(2017, 4, 13, 17, 10, 22, 378763)}
guillaume@ubuntu:~/AirBnB_v3$ 
```
<p>For this task, you __must__ make a pull request on GitHub.com, and ask at least one of your peer to review and merge it.</p>

- Files: File: `models/engine/db_storage.py`, `models/engine/file_storage.py`, `tests/test_models/test_engine/test_db_storage.py`, `tests/test_models/test_engine/test_file_storage.py`

<hr style="height: .5px;">

__3. Status of your API__
<p>It’s time to start your API!</p>

<p>Your first endpoint (route) will be to return the status of your API:</p>

```Bash
guillaume@ubuntu:~/AirBnB_v3$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
...
```

<p>In another terminal:</p>

```Bash
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/status
{
  "status": "OK"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET -s http://0.0.0.0:5000/api/v1/status -vvv 2>&1 | grep Content-Type
< Content-Type: application/json
guillaume@ubuntu:~/AirBnB_v3$ 
```

<p>Magic right? (No need to have a pretty rendered output, it’s a JSON, only the structure is important)</p>

<p>Ok, let starts:</p>

- Create a folder `api` at the root of the project with an empty file `__init__.py`
- Create a folder `v1` inside `api`:
	- create an empty file `__init__.py`
	- create a file `app.py`:
		- create a variable `app`, instance of `Flask`
		- import `storage` from `models`
		- import `app_views` from `api.v1.views`
		- register the blueprint `app_views` to your Flask instance `app`
		- declare a method to handle `@app.teardown_appcontext` that calls `storage.close()`
		- inside `if __name__ == "__main__":`, run your Flask server (variable `app`) with:
			- host = environment variable `HBNB_API_HOST` or `0.0.0.0` if not defined
			- port = environment variable `HBNB_API_PORT` or `5000` if not defined
			- `threaded=True`
- Create a folder `views` inside `v1`:
	- create a file `__init__.py`:
		- import `Blueprint` from `flask doc`
		- create a variable `app_views` which is an instance of `Blueprint` (url prefix must be `/api/v1`)
		- wildcard import of everything in the package `api.v1.views.index` => PEP8 will complain about it, don’t worry, it’s normal and this file (`v1/views/__init__.py`) won’t be check.
	- create a file `index.py`
		- import `app_views` from `api.v1.views`
		- create a route `/status` on the object `app_views` that returns a JSON: `"status": "OK"` (see example)
</br>

File: `api/__init__.py`, `api/v1/__init__.py`, `api/v1/views/__init__.py`, `api/v1/views/index.py`, `api/v1/app.py`

<hr style="height: .5px;">

__4. Some stats?__
