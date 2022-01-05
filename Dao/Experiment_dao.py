from Model.Experiment import Experiment



class Experiment_dao:

    #################################### member variable ####################################

    #################################### member functions ###################################
    #----------------------------------------------------------------------------------------
    # constructor
    #----------------------------------------------------------------------------------------
    def __init__(self):

        pass
    #----------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------
    def get_all(self):

        experiments = Experiment.objects()
        return experiments

    #----------------------------------------------------------------------------------------
    def get_by_id(self, input_id):
        
        experiments = Experiment.objects(pk = input_id)
        return experiments[0]

    #----------------------------------------------------------------------------------------
    def get_by_name(self, input_name):

        experiments = Experiment.objects(name = input_name)
        return experiments

    #----------------------------------------------------------------------------------------
    def get_by_project_id(self, input_project_id):

        experiments = Experiment.objects(project_id = input_project_id)
        return experiments

    #----------------------------------------------------------------------------------------
    def get_by_parent_experiment_id(self, input_parent_experiment_id):

        experiments = []
        for experiment in Experiment.objects(parent_experiment_id = input_parent_experiment_id):

            if experiment.parent_experiment_id != "":
                experiments.append(experiment)

        return experiments

    #----------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------
    def add_experiment(self, input_name, input_project_id, input_parent_experiment_id, input_parameters_involved):

        experiment = Experiment(name = input_name, 
                                project_id = input_project_id, 
                                parent_experiment_id = input_parent_experiment_id, 
                                parameters_involved = input_parameters_involved)
        experiment.save()

    #----------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------
    def delete_experiment(self, input_id):

        experiments = Experiment.objects(pk = input_id)
        experiments.delete()

    #----------------------------------------------------------------------------------------
    def delete_all_under_project(self, input_project_id):

        experiments = Experiment.objects(project_id = input_project_id)
        for experiment in experiments:
            experiment.delete()

