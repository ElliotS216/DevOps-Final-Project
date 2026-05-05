'''
The Event class represents a scheduled occurrence such as a meeting, appointment, 
or gathering. Unlike tasks, events are typically tied to a specific date or time 
and do not have progress states.
'''

# DONE: create an Event class
class Event:
    # DONE: write a constructor with the attributes event_name, description, date, start_time,
    #       end_time, and category_name. Each of these attributes  will be passed in as arguments. 
    #       They should be set to each of the attributes accordingly.
    def __init__(self, event_name, description, date, start_time, end_time, category_name):
        self.event_name = event_name
        self.description = description
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.category_name = category_name
    # write the getters and setters for each of the attributes. They must have the format
    #       "get_attributeName" or "set_attributeName"

    # getters
    def get_event_name(self):
        return self.event_name

    def get_description(self):
        return self.description

    def get_date(self):
        return self.date

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_category_name(self):
        return self.category_name

    #setters
    def set_event_name(self, event_name):
        self.event_name = event_name

    def set_description(self, description):
        self.description = description

    def set_date(self, date):
        self.date = date

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def set_category_name(self, category_name):
        self.category_name = category_name

    # DONE: write a method called to_dict. This method should return an Event object that has been
    #       converted into a dictionary where each of the attribute names and its corresponding 
    #       value turned into a key-value pair. The dictionary keys should be the exact same as the
    #       attribute names.
    def to_dict(self):
        return{
            "event_name": self.event_name,
            "description": self.description,
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "category_name": self.category_name
        }

    # DONE: write a static method called from_dict which accepts a dictionary object as an argument.
    #       Each entry in the dictionary corresponds to an Event attribute. Create and return an Event 
    #       object using the data extracted from the dictionary.

    # @staticmethod is used when a function belongs to the class but does not use self
    @staticmethod
    def from_dict(data):
        return Event(
            data["event_name"],
            data["description"],
            data["date"],
            data["start_time"],
            data["end_time"],
            data["category_name"]
        )