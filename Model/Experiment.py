from mongoengine import Document, IntField, StringField, DynamicField

class Experiment(Document):

    #################################### member variable ####################################
    name = StringField()
    project_id = StringField()
    parent_experiment_id = StringField()
    parameters_involved = DynamicField()

    #################################### member functions ###################################

    #----------------------------------------------------------------------------------------
    def to_json(self):

        data = {
            "id": str(self.pk),
            "name": self.name,
            "project_id": self.project_id,
            "parent_experiment_id": self.parent_experiment_id,
            "parameters_involved": self.parameters_involved
        }

        return data