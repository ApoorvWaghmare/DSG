#from flask import Blueprint
import json
from flask import Response, render_template
from flask_classful import FlaskView, route
from Dao.Project_dao import Project_dao

class Project_controller(FlaskView):

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
    @route("all_projects", methods = ["GET"])
    def get_all_projects(self):
    
        project_dao = Project_dao()

        projects = []
        for project in project_dao.get_all():
            projects.append(project.to_json())

        return Response(response = json.dumps(projects),
                        status = 200,
                        mimetype = "application/json")

    #----------------------------------------------------------------------------------------
    @route("all_projects_html", methods = ["GET"])
    def all_projects_html(self):

        project_dao = Project_dao()

        names = []
        for project in project_dao.get_all():
            temp_dict = project.to_json()
            name = temp_dict["name"]
            names.append(name)
    
        return render_template("home.html", num_names = len(names), names = names)

    #----------------------------------------------------------------------------------------
    # add
    #----------------------------------------------------------------------------------------

