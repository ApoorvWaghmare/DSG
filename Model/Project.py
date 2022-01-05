from mongoengine import Document, StringField

class Project(Document):

    #################################### member variable ####################################
    name = StringField()
    description = StringField()

    #################################### member functions ###################################
    #----------------------------------------------------------------------------------------
    def to_json(self):

        data = {
            "id": str(self.pk),
            "name": self.name,
            "description": self.description
        }

        return data