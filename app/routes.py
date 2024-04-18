from flask import Flask     # from the flask module import the Flask class

app = Flask(__name__)       # Create an instance of the Flask class

@app.get("/")
@app.get("/aboutme")        # Flask decorator that maps view functions to routes
def aboutMe():              # View function
    me = {                  # Python dictionary
        "first_name": "Adam",
        "last_name": "Schmidt",
        "hobbies": "Coding",
        "is_online": True
    }
    return me               # When you return a dict from a view function, it becomes JSON

