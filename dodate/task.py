# DONE: import the datetime library
import datetime

'''
The Task class represents an actionable to-do item. Tasks have descriptive information 
and a status (incomplete, in progress, completed).
'''

# Done: create a Task class
class Task:
    # Done: write a constructor with the attributes task_name, todays_focus, description,
    #       due_date, status, weight, steps, and category_name. Each of these attributes 
    #       will be passed in as arguments. They should be set to each of the attributes accordingly.
    def __init__(self, task_name, todays_focus, description, due_date, status, weight, steps, category_name):
        self.task_name = task_name
        self.todays_focus = todays_focus
        self.description = description
        self.due_date = due_date
        self.status = status
        self.weight = weight
        self.steps = steps
        self.category_name = category_name

    # DONE: Write the getters and setters for each of the attributes. They must have the format
    #       "get_attributeName" or "set_attributeName"

    # Getters
    def get_task_name(self):
        return self.task_name

    def get_todays_focus(self):
        return self.todays_focus

    def get_description(self):
        return self.description

    def get_due_date(self):
        return self.due_date

    def get_status(self):
        return self.status

    def get_weight(self):
        return self.weight

    def get_steps(self):
        return self.steps

    def get_category_name(self):
        return self.category_name

    # Setters
    def set_task_name(self, task_name):
        self.task_name = task_name

    def set_todays_focus(self, todays_focus):
        self.todays_focus = todays_focus

    def set_description(self, description):
        self.description = description

    def set_due_date(self, due_date):
        self.due_date = due_date

    def set_status(self, status):
        self.status = status

    def set_weight(self, weight):
        self.weight = weight

    def set_steps(self, steps):
        self.steps = steps

    def set_category_name(self, category_name):
        self.category_name = category_name



    # DONE: write a method called to_dict. This method should return a Task object that has been
    #       converted into a dictionary where each of the attribute names and its corresponding 
    #       value turned into a key-value pair. The dictionary keys should be the exact same as the
    #       attribute names.
    def to_dict(self):
        return{
        "task_name": self.task_name,
        "todays_focus": self.todays_focus,
        "description": self.description,
        "due_date": self.due_date,
        "status": self.status,
        "weight": self.weight,
        "steps": self.steps,
        "category_name": self.category_name
        }

    # DONE: write a static method called from_dict which accepts a dictionary object as an argument.
    #       Each entry in the dictionary corresponds to a Task attribute. Create and return a Task 
    #       object using the data extracted from the dictionary.
    @staticmethod
    def from_dict(data):
        return Task(
            data["task_name"],
            data["todays_focus"],
            data["description"],
            data["due_date"],
            data["status"],
            data["weight"],
            data["steps"],
            data["category_name"]
        )

    # Done: Write a methdo called update_task that accepts all attributes as arugments. It then sets
    #       each of the Task object's attributes to the given arguments. If any of the arugments was
    #       not given a value, the should be set to None as default. The attributes should only be 
    #       updated if a value was passed.
    def update_task(self, task_name=None, todays_focus=None, description=None, due_date=None, status=None, weight=None, steps=None, category_name=None):
        if task_name is not None:
            self.task_name = task_name
        if todays_focus is not None:
            self.todays_focus = todays_focus
        if description is not None:
            self.description = description
        if due_date is not None:
            self.due_date = due_date
        if status is not None:
            self.status = status
        if weight is not None:
            self.weight = weight
        if steps is not None:
            self.steps = steps
        if category_name is not None:
            self.category_name = category_name


    # DONE: Write a method called is_overdue that accepts a date object as an argument representing 
    #       today's date. If the task was not given a due date or if the status is completed, return false. 
    #       Otherwise, format the due date with the following equation:
    #           due date = datetime.date.fromisoformat(Task object's due date)
    #       Use the datetime call exactly as it was given to you. After formatting, make sure the today 
    #       argument is populated. If the argument is Nonetype, set it equal to datetime.date.today()
    #       Finally, return true if the due date is less than today's date or false if not.

    ###################################
    #       Step Managment            #
    ###################################
    def is_overdue(self, date):
        # If no due date OR task is completed → not overdue
        if self.due_date is None or self.status == "completed":
            return False

        # Convert due date string to date object
        # had ai help with writing the datetime formula
        due_date = datetime.date.fromisoformat(self.due_date)

        # If there is not a date assigned use todays date
        if date is None:
            date = datetime.date.today()

        # Return True if overdue
        return due_date < date

    # DONE: Write a method called add_step that is passed a step title as an argument.
    #       It then creates a new step and adds it to the Task's list of steps.
    #       Steps are each a dictionary with the keys "step" and "status". The "step" key
    #       should have the value of the title sent as an argument. The "status" key should
    #       be set to "incomplete" when created.
    # create a method and take in step title as an argument
    def add_step(self, step_title):
        new_step = {
            "step": step_title,
            "status": "incomplete"
        }
        self.steps.append(new_step)

    # DONE: Write a method called toggle_step that accepts a step index as an argument.
    #       The specified step's status should be set according to the following key.
    '''
     Current Status          New Status
    ------------------------------------
     incomplete       ->      started
     started          ->      completed
     completed        ->      incomplete
    '''
    def toggle_step(self, step_index):
        step = self.steps[step_index]

        if step["status"] == "incomplete":
            step["status"] = "started"
        elif step["status"] == "started":
            step["status"] = "completed"
        elif step["status"] == "completed":
            step["status"] = "incomplete"


    # DONE: Write a method called edit_step that accepts a step index and a new title as arugments.
    #       The specified step should be updated.
    # used AI to help create this method because I had no Idea where to start
    def edit_step(self, step_index, new_title):
        self.steps[step_index]["step"] = new_title



    # DONE: Write a method called remove_step that accepts a step index as an argument.
    #       The specified step should be removed from the Task's list of steps.
    def remove_step(self, step_index):
        self.steps.pop(step_index)
