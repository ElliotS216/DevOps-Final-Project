'''
The Category class groups related tasks and events together. It provides organizational 
structure within the planner.
'''

# DONE: create a Category class
# Done: write a constructor with the attributes category_name and description. Each of these attributes
#       will be passed in as arguments. They should be set to each of the attributes accordingly.
class Category:
    def __init__(self, category_name, description):
        self.description = description
        self.category_name = category_name



    # Done: write the getters and setters for each of the attributes. They must have the format
    #       "get_attributeName" or "set_attributeName"

    # getters
    def get_description(self):
        return self.description

    def get_category_name(self):
        return self.category_name

    #setters
    def set_description(self, description):
        self.description = description

    def set_category_name(self, category_name):
        self.category_name = category_name

    # Done: write a method called to_dict. This method should return a Category object that has been
    #       converted into a dictionary where each of the attribute names and its corresponding
    #       value turned into a key-value pair. The dictionary keys should be the exact same as the
    #       attribute names.
    def to_dict(self):
        return{
            "description": self.description,
            "category_name": self.category_name
        }

    # DONE: write a static method called from_dict which accepts a dictionary object as an argument.
    #       Each entry in the dictionary corresponds to a Category attribute. Create and return a Category
    #       object using the data extracted from the dictionary.
    @staticmethod
    def from_dict(data):
        return Category(
            data["category_name"],
            data["description"]
        )

