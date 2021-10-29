# FlaskIntroduction

This repo has been updated to work with `Python v3.8` and up.

### How To Run
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
$ source venv/bin/activate
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