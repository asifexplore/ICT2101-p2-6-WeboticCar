# FlaskIntroduction

This repo has been updated to work with `Python v3.8` and up.

### How To Run ###
1. Install `virtualenv` & other dependencies:
 ```
 $ pip install virtualenv
 $ pip install flask
 $ pip install flask_sslify
```

2. Open a terminal in the project root directory and run:
Windows:
```
$ virtualenv env
```
Mac:
```
$ venv env
```

3. Then run the command:
```
Windows:
$ .\env\Scripts\activate
Mac:
$ source env/bin/activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```

### Development Workflow ###

A total of 7 branches will be used: Master, Development, Angie, Asif, Marven, Nadzim and Kok Hwee.

Master branch will be the pristine ntergrated branch bug and error free.
It will only be committed after the tests have been done at the Development branch.

Development branch will be used for testing where we intergrate our individual components together
to test out all the features. Only when it is bug and error free, then it will be committed to
the Master branch.

Angie, Asif, Marven, Nadzim and Kok Hwee branches will be used to to test our own individual components.
Once it is bug and error free, it will be commited to the Development branch.



### UAT section ###
3 mins to cover the system


### Whitebox Testing ###
animated gif or short one min video
