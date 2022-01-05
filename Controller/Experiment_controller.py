#from flask import Blueprint
import os
import json
from flask import Response, render_template, request
from flask_classful import FlaskView, route
#from werkzeug import secure_filename
from Dao.Experiment_dao import Experiment_dao

class Experiment_controller(FlaskView):

    #################################### member variable ####################################

    #################################### member functions ###################################
    #----------------------------------------------------------------------------------------
    # constructor
    #----------------------------------------------------------------------------------------
    def __init__(self):

        pass

    #----------------------------------------------------------------------------------------
    # get
    #----------------------------------------------------------------------------------------
    @route("all_experiments", methods = ["GET"])
    def get_all_experiments(self):
    
        experiment_dao = Experiment_dao()

        experiments = []
        for experiment in experiment_dao.get_all():
            experiments.append(experiment.to_json())

        return Response(response = json.dumps(experiments),
                        status = 200,
                        mimetype = "application/json")

    #----------------------------------------------------------------------------------------
    # add
    #----------------------------------------------------------------------------------------
    @route("add_experiment", methods = ["GET", "POST"])
    def add_experiment(self):

        if request.methode == "POST":

            f = request.files["file1"]
            #f.save( os.path.join("D:\Current Projects\DSGit\Uploaded files", ) )

        return render_template("Add_experiment.html")

