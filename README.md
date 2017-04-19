Welcome!

This is an api that is simple and is primarily used for testing purposes. This api requires the following packages to be installed through pip:

Flask
Flask-RESTful
Flask-JWT
Flask-SQLAlchemy
uwsgi     # Only for production deployment (such as Heroku)
psycopg2  # Only for production deployment (such as Heroku)

Please feel free to clone as use this code as neccessary. Note, there are some security flaws (such as the secret_key for JWT being visible) since this is a test app with no sensitive data. 
Since this is a fully functional application, if you intend to use and modify this code for production purposes, please patch this vulnerability before proceeding if this is going to end up on github for any reason at all.

If you would like a basic run-down of the functionality of this application, please feel free to download the JSON files from the 'postman import items' folder and import the collection, as well as the environment variables to test at your leisure.
To run the application, please simply enter the following command after installing the above libraries. 

```
python run.py
```
