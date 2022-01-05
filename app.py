from flask import Flask
import mongoengine as db

from Controller.Experiment_controller import Experiment_controller
from Controller.Project_controller import Project_controller


if __name__ == "__main__":

    # connect to mongodb
    try:
        db.connect(host = "mongodb://localhost:27017/DSG")
        print()
    except: 
        print("error connecting to database")

    # creating flask app
    app = Flask(__name__)
    # registering routes
    Experiment_controller.register(app, route_base = "/experiments")
    Project_controller.register(app, route_base = "/projects")

    # run server
    app.run(port = 80, debug = True)