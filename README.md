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
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/290e4ea8841a7580e1dc#?env%5BHeroku%5D=W3siZW5hYmxlZCI6dHJ1ZSwia2V5IjoibGVuZGluZy1iYXNlLXVybCIsInZhbHVlIjoiaHR0cHM6Ly9zaW1wbGUtbGVuZGluZy1hcGkuaGVyb2t1YXBwLmNvbSIsInR5cGUiOiJ0ZXh0In0seyJlbmFibGVkIjp0cnVlLCJrZXkiOiJqd3RfdG9rZW4iLCJ2YWx1ZSI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUpwWkdWdWRHbDBlU0k2TVN3aWJtSm1Jam94TkRrek1EQXhNREUzTENKcFlYUWlPakUwT1RNd01ERXdNVGNzSW1WNGNDSTZNVFE1TXpBd05EWXhOMzAubFZJTm9HRHJwMXZwX1V6eVNzN3k4cWN3RXo1U2tXSldMQ01VNjZUWHYxcyIsInR5cGUiOiJ0ZXh0In1d)