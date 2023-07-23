from fastapi import FastAPI

app = FastAPI()

students = [
    {'name': 'student 1', 'age': 20 },
    {'name': 'student 2', 'age': 21 },
    {'name': 'student 3', 'age': 36 }
]

@app.get('/students')
def user_list():
    return{'students': students}

# from flask import Flask
# app = Flask(__name__)

# @app.route('/students')
# def hello_world():
#     return{'students': students}

# if __name__ == '__main__':
#     app.run(debug=True,port=6379)