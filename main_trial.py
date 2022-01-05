import mongoengine as db
from Model.Experiment import Experiment
from Model.Project import Project


try:
    db.connect(host = "mongodb://localhost:27017/DSG")
    print()
except: 
    print("error connecting to database")


"""
print("\nCreate a project")
project = Project(
                  name = "trial_prkjljlkjloject",
                  description = "This is a trial project")

project.save()
print(project.id)
"""


project = Project.objects(name = 'trial_prkjljlkjloject')
print(project.to_json())
print(project[0].pk)
#print(project.name)


"""
print("Create book")
experiment = Experiment(name = "trial", 
                        project_id = , 
                        parent_experiment_id, 
                        parameters_involved):

experiment.save()
"""