Welcome!

This is an api that is simple and is primarily used for testing purposes. This api requires the following packages to be installed through pip:

```
Flask
Flask-RESTful
Flask-JWT
Flask-SQLAlchemy
uwsgi     # Only for production deployment (such as Heroku)
psycopg2  # Only for production deployment (such as Heroku)
```

Please feel free to clone as use this code as neccessary. Note, there are some security flaws (such as the secret_key for JWT being visible) since this is a test app with no sensitive data. 
Since this is a fully functional application, if you intend to use and modify this code for production purposes, please patch this vulnerability before proceeding if this is going to end up on github for any reason at all.

If you would like a basic run-down of the functionality of this application, please feel free to download the JSON files from the 'postman import items' folder and import the collection, as well as the environment variables to test at your leisure.
To run the application, please simply enter the following command after installing the above libraries. 

```
python run.py
```

<h3><b>Please be sure and go through and replace the uri's with your own uri's for each project after downloading. On C# projects, this is marked by a TODO and can be seen via the Task List on Visual Studio. On the web app, this is found on the Script.js file within the project.</b></h3>

<h2>
    Other related github repositories:
</h2>
<ul>
    <li>Web App (jQuery): <a href="https://github.com/btvanhooser/simple-lending-web-app">Repository</a></li>
    <li>Smart Client (C#): <a href="https://github.com/btvanhooser/SimpleLenderSmartClient">Repository</a></li>
    <li>Lender Admin Tool (C#): <a href="https://github.com/btvanhooser/LenderAdmin">Repository</a></li>
    <li>Web UI Tester (C#): <a href="https://github.com/btvanhooser/LendingWebUITester">Repository</a></li>
    <li>Load Tester (C#): <a href="https://github.com/btvanhooser/LendingAPILoadTester">Respository</a></li>
</ul>

<h2>Postman Collection for API Testing</h2>
<a href="https://www.getpostman.com/collections/290e4ea8841a7580e1dc">Get collection here</a>