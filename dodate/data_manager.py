
# DONE: import the json module and the Planner class
import json
from planner import Planner

'''
The Data_Manager class handles persistence. It is responsible for loading planner 
data from storage and saving planner data back to storage.
'''

# DONE: create a Data_Manager class
class Data_Manager:
    # DONE: write a constructor with the attribute file_path which is sent as an argument
    def __init__(self, file_path):
        self.file_path = file_path


    # DONE: write a method called open_planner. It will open the file specified in the file_path
    #       attribute and
    #       read the data from it.
    #       It will then use the json loads command to
    #       convert the json object to a dictionary.
    #       The dictionary should then be used to create a Planner object using the from_dict method
    #       return the resulting object.
    def open_planner(self):
        # open the file specified in the file_path
        file = open(self.file_path, 'r')
        # use the json load command
        # json.load also reads the data
        json_data = json.load(file)
        #need to close the file
        file.close()

        # convert the json object to a dictionary
        planner = Planner.from_dict(json_data)
        # return the new object
        return planner
    
    # DONE: Write a method called save_planner that accepts a Planner object as an argument.
    #       It should then open the file from the file_path attribute in write mode.
    #       It will then convert the Planner to a dictionary and use the json dump command to write
    #       the dictionary to the file.
    def save_planner(self, planner_object):
        with open(self.file_path, 'w') as file:
            planner_dict = planner_object.to_dict()
            json.dump(planner_dict, file)
