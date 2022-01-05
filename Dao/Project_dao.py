from Model.Project import Project


class Project_dao():

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
    def get_all(self):

        projects = Project.objects()
        return projects

    #----------------------------------------------------------------------------------------
    def get_by_id(self, input_id):
        
        projects = Project.objects(pk = input_id)
        return projects[0]

    #----------------------------------------------------------------------------------------
    def get_by_name(self, input_name):

        projects = Project.objects(name = input_name)
        return projects

    #----------------------------------------------------------------------------------------
    def get_by_description(self, input_description):

        projects = Project.objects(description__contains = input_description)
        return projects

    #----------------------------------------------------------------------------------------
    # add
    #----------------------------------------------------------------------------------------
    def add_project(self, input_name, input_description):

        project = Project(name = input_name, 
                          description = input_description)
        project.save()

    #----------------------------------------------------------------------------------------
    # delete
    #----------------------------------------------------------------------------------------
    def delete_project(self, input_id):

        project = Project.objects(pk = input_id)
        project.delete()
    