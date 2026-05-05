# Done: import the task, category, and event classes
from task import Task
from event import Event
from category import Category
# Done: import the task, category, and event classes
from task import Task
from category import Category
from event import Event
# Done: import the datetime library
from datetime import datetime
from datetime import timedelta

'''
The Planner class is the central coordinating component of the system. It owns and manages 
all categories, tasks, and events. Most application behavior ultimately routes through this class.
'''

# Done: create a Planner class
class Planner:
    # DONE: write a constructor with the attributes name, categories, tasks, and events.
    #       Each of these attributes will be passed in as arguments. They should be set
    #       to each of the attributes accordingly.
    #       If categories, tasks, or events were passed as Nonetypes, set them equal to 
    #       an empty list.
    def __init__(self, name, categories, tasks, events):
        self.name = name
        self.categories = categories
        self.tasks = tasks
        self.events = events

    # DONE: write the getters and setters for each of the attributes. They must have the format
    #       "get_attributeName" or "set_attributeName"
    #getters
    def get_name(self):
        return self.name

    def get_categories(self):
        return self.categories

    def get_tasks(self):
        return self.tasks

    def get_events(self):
        return self.events

    #setters
    def set_name(self, name):
        self.name = name

    def set_categories(self, categories):
        self.categories = categories

    def set_tasks(self, tasks):
        self.tasks = tasks

    def set_events(self, events):
        self.events = events



    # DONE: write a method called to_dict. This methods should turn a Planner object into a dictionary.
    #       It should return a dictionary where each attribute and its value is a key value pair. The key 
    #       should have the exact same name as the attribute. Categories, tasks, and events are stored
    #       as lists; each item in those lists will need to be converted to a dictionary as well. Using
    #       the to_dict method from each of those classes create lists of category, task, and event dictionaries
    #       to use for the corresponding values in the dictionary.
    def to_dict(self):
        cats = []
        for category in self.categories:
            # convert each object into a dictionary
            category_dictionary = category.to_dict()
            # add dictionary to list
            cats.append(category_dictionary)
        # cats holds a list of dictionaries

        tasks_list = []
        for tasks in self.tasks:
            tasks_dictionary = tasks.to_dict()
            tasks_list.append(tasks_dictionary)

        event_list = []
        for events in self.events:
            events_dictionary = events.to_dict()
            event_list.append(events_dictionary)

        return{
            "name": self.name,
            "categories": cats,
            "tasks": tasks_list,
            "events": event_list
        }

    # cateories -> take a list of category objects belonging to the planner and turn it into a list of dictionaries
    #   cannot do this on the whole list
    #   has to be individually -> loop
    # "category":



    # DONE: write a static method called from_dict. This method should take in a dictionary object as an
    #       argument. It will then create a Planner object using the key value pairs. The keys will
    #       correspond directly with the names of the Planner attributes.
    #       For each of the attributes in a Planner, pull the data from the planner dictionary. You will
    #       need to convert each of the categories, events, and tasks to objects as well by calling the
    #       from_dict method of each class. Those lists of objects should be used sent as the arguments
    #       for the Planner object--not the dictionaries from the raw data.
    @staticmethod
    def from_dict(data_dict):

        categories = []
        tasks = []
        events = []
        '''
        ORIGINAL:
        for c in data_dict["categories"]:
            categories.append(Category.from_dict(c))
        '''
        category_list = data_dict["categories"]
        for c in category_list:
            new_category = Category.from_dict(c)
            categories.append(new_category)

        for t in data_dict["tasks"]:
            tasks.append(Task.from_dict(t))

        for e in data_dict["events"]:
            events.append(Event.from_dict(e))

        return Planner(
            data_dict["name"],
            categories,
            tasks,
            events,
        )

    # DONE: write a method called create_task that is passed each of the attributes for a Task object
    #       EXCEPT for the steps. It should use the data received as arguments to create a task object
    #       sending an empty list for the steps. Once the object has been created, append it to the 
    #       Planner's list of tasks.


    # Done: write a method called create_task that is passed each of the attributes for a Task objectd
    #########################################
    #            Task Methods               #
    #########################################
    def create_task(self,  task_name, todays_focus, description, due_date, status, weight, category_name):

        task = Task(task_name, todays_focus, description, due_date, status, weight, [], category_name)

        self.tasks.append(task)

    # Done: write a method called set_task_status that is passed the index of a task. Get the task from
    #       the Planner's list of tasks according to its index and find its current status. According to
    #       the list below, set the status to the correct new value.
    def set_task_status(self, index):
        #This gets the index of the task you want to set the status of
        task = self.tasks[index]

        # using the getter in task to get the status of the current task
        current_status = task.get_status()

        # using the setter to set the new status
        if current_status == "incomplete":
            task.set_status("in progress")

        elif current_status == "in progress":
            task.set_status("completed")

        elif current_status == "completed":
            task.set_status("incomplete")

    '''
     Current Status          New Status
    ------------------------------------
     incomplete       ->      started
     started          ->      completed
     completed        ->      incomplete
    '''

    # Done: write a method called set_task_todays_focus which is passed the index of a task. Get that task
    #       from the Planner's list of tasks according to its index. Call the set_todays_focus method from 
    #       the Task class on that object.
    def set_task_todays_focus(self, index):

        # creates an object with the value of what the task is from the lit of tasks
        task = self.tasks[index]

        # AI helped me make this line
        current = task.get_todays_focus()

        # using the set method in the task class add todays focus
        task.set_todays_focus(not current)


    # DONE: Write a method called delete_task that will take an index as an argument. It will then delete
    #       the task at that index for the Planner object
    def delete_task(self, task_index,):
        self.tasks.pop(task_index)


    # Done: Write a method called add_task_step that will take in a task index and a step title as arguments.
    #       It will then call the add_step method on the Task object at the specified index in the Planner's 
    #       task list.
    def add_task_step(self, task_index, step):
        task = self.tasks[task_index]
        task.add_step(step)
        

    # DONE: Write a method called toggle_task_step that takes in a task index and a step index as arguments.
    #       It will then call the toggle_step method on the Task object at the specified index in the Planner's
    #       task list.
    def toggle_task_step(self, task_index, step_index):
        task = self.tasks[task_index]
        task.toggle_step(step_index)

    # DONE: Write a method called edit_task_step that takes a task index, a step index, and a new step title 
    #       as arguments. It will then call the edit_step method on the specified Task object.
    def edit_task_step(self, task_index, step_index, new_step_title):
        task = self.tasks[task_index]
        task.edit_step(step_index,new_step_title)


    # DONE: Write a method called remove_task_step that will take a task index and a step index as arguments.
    #       It will then call the remove_step on the specified Task object.
    def remove_task_step(self, task_index, step_index):
        task = self.tasks[task_index]
        task.remove_step(step_index)

    # DONE: Write a method called edit_task that will take a task index, task name, focus bool, description, 
    #       due date, status, and weight as arguments. Call the update_task method on the specified Task.
    def edit_task(self, task_index, task_name, focus, description, due_date, status, weight):
        task = self.tasks[task_index]
        task.update_task(task_name, focus, description, due_date, status, weight)

    # DONE: Write a method called get_task_by_index that accepts a task index as an arugment.
    #       It should return the specified task from the Planner's task list.
    def get_task_by_index(self, task_index):
        task = self.tasks[task_index]
        return task


    # DONE: Write a method called get_overdue tasks that accepts a date object as the argument representing today.
    #       You will need a list to store the overdue tasks. For each task in the Planner's task list, determine if 
    #       the task is overdue using the is_overdue method. If it is, add it to the list of overdue tasks and return 
    #       the list when done.
    # used AI to help me get started on this method whith an outline to help with the though process
    def get_overdue_tasks(self, today):
        # 1. create empty list
        overdue_list = []

        # 2. loop through self.tasks
        for task in self.tasks:

            # 3. check if task is overdue
            if task.is_overdue(today):

                # 4. add to list if true
                # it is formated like this because you want to append the task to the overdue list
                overdue_list.append(task)
        # 5. return list
        return overdue_list

    
    # DONE: Write a method called get_due_soon that accepts a date object as the argument representing today. This method
    #       will search for any tasks due within a week. To do so, find the date 7 days from now with the equation:
    #       end date = today's date + datetime.timedelta(days=7)
    #       Use the datetime call exactly as it was provided to you. You will then need to iterate through the tasks in the
    #       Planner.  If the task's due date is greater than or equal to today's and less than or equal to the end of the week,
    #       add it to the list of tasks due soon and return when done. Tasks that were not given a due date or are already
    #       completed should not be added to the list.

    # used ai to help make this one

    def get_due_soon(self, date):
        # getting the end date for the if statement
        end_date = date + timedelta(days=7)

        # due soon list
        task_due_soon_list = []

        # make a for loop that iterates through the tasks
        for task in self.tasks:
            
            # make an if statment saying if duedate is in 7 days display
            if task.due_date is not None and task.status != "completed":

                # had ai help with converting the due date
                due_date = datetime.fromisoformat(task.due_date).date()

                #check range
                # ai helped me expand the range of what I had. I had exactly 7 days before
                if due_date >= date and due_date <= end_date:

                    #append
                    # I need to apped what I found to the list
                    task_due_soon_list.append(task)

        return task_due_soon_list


    # DONE: Write a method called get_tasks_in_todays_focus. For each task in the Planner's task list, add it to a list
    #       collecting tasks where the todays_focus is set to True. Return the list of tasks in today's focus.
    def get_tasks_in_todays_focus(self):
        # for loop going over the planner task (self.tasks) and add it to a list if the task is in todays focus

        # making list to put the tasks in
        list_of_todays_tasks = []

        for task in self.tasks:

            # check if task is in todays task
            if task.todays_focus == True:
                list_of_todays_tasks.append(task)

        return list_of_todays_tasks


    # DONE: write a method called get_task_status_counts. It should create a dictionary with each status as a key. The
    #       count for each status should start at a 0. For each task in the Planner, increment the count for the correct
    #       status in the dictionary. Return the dictionary when done.

    # had ai help me with the thought process
    def get_task_status_counts(self):

        # create dictionaries with zero values
        # just need 1 dictionary with all the values not 3 septrate ones
        status_dict = {"incomplete": 0,
                        "in progress": 0,
                        "completed": 0 }

        # loop throug tasks
        for task in self.tasks:

            # 3. get status
            status = task.get_status()

            # 4. increment correct count
            # ai help me with this part
            status_dict[status] += 1
            # would I need to make 3 if statements for each of the statuses

        # 5. return dictionary
        return status_dict

    # DONE: Write a method called get_incomplete_by_category. It should create a dictionary with each category as a key.
    #       There should also be a variable to count the number of not complete tasks. The count for each category should 
    #       start at 0. 
    #   For each task in the Planner, increment the count for the category that task is in only if the status
    #       is not "completed". Return a dictionary that has 2 key-value pairs: one pair has the key "total" with the value 
    #       of the number of tasks that are not complete and another pair with the key "byCategory" that has the value of the
    #       dictionary.

    # Had heavy help on this method ask about the thought process in this method
    def get_incomplete_by_category(self):

        #set the total and make the dictionary
        total = 0
        category_dict = {}

        #loop throught the tasks in planner
        for task in self.tasks:

            # check if task status does not equal complete
            if task.status != "completed":

                # if so total + 1
                total += 1

                #set category to the current tasks category name
                category = task.get_category_name()

                # check if the category is not in the dictionary
                if category not in category_dict:
                    # if not add it to the dictionary and set its number to zero
                    category_dict[category] = 0
                
                # add 1 to the number of tasks with this category
                category_dict[category] += 1

        # return a dictionary with the total and category 
        return {
            "total": total,
            "byCategory": category_dict
        }
    
    #########################################
    #          Category Methods             #
    #########################################

    # DONE: Write a method called get_category_by_index that is passed a category index as an argument. Return
    #       the requested Category object from the Planner's list of categories
    def get_category_by_index(self, category_index):
        category = self.categories[category_index]
        return category


    # Done: Write a method called add_category that accepts a name and description as arugments.
    #       Create a new Category object and add it to the Planner's list of categories.
    def add_category(self, name, description):
        # create a new category object
        category = Category(name, description)
        
        #append it to the Planner's list of categories.
        self.categories.append(category)


    # DONE: Write a method called edit_category that accepts a category index, name and description
    #       as arguments. It will then call the setters for the specified Category object.
    def edit_category(self, category_index , name, description):
        # get the category index and store it in an object
        category = self.categories[category_index]

        # call the setters and change the category stuff
        category.set_category_name(name)
        category.set_description(description)
        


    # DONE: Write a method called remove_category_by_index that accepts a category index as an argument.
    #       It then remvoes the specified Category object from the Planner's list of categories.
    def remove_category_by_index(self, category_index):
        self.categories.pop(category_index)


    #########################################
    #            Event Methods              #
    #########################################

    # DONE: Write a method called get_event_by_index that accepts an index as an argument. It then
    #       returns the specified Event object from the Planner's list of events.
    def get_event_by_index(self, event_index):
        #get event index
        event = self.events[event_index]

        #return event
        return event


    # DONE: Write a method called add_event that accepts an event name, description, date, start time,
    #       end time, and category name as arguments. It then creates a new Event object and adds it 
    #       to the Planner's list of events.
    def add_event(self, name, description, date, start_time, end_time, category_name):
        #create new category
        event = Event(name, description, date, start_time, end_time, category_name)

        #append new category
        self.events.append(event)

    # DONE: Write a method called remove_event_by_index that accepts an index as an argument. It then
    #       removes the specified index from the Planner's list of events.
    def remove_event_by_index(self, event_index):
        self.events.pop(event_index)

    # DONE: Write a method called set_event_category that accepts an event index and a category name. 
    #       Set the corresponding Event object's category to the specified category name.
    def set_event_category(self, event_index, category_name):
        # get the index of the event that you want to change
        event = self.events[event_index]

        #use setters to change the event information
        event.set_category_name(category_name)



    # DONE: Write a method called get_upcoming_events that accepts a date object as the arument representing
    #       today's date. It should calculate the date exactly 7 days from today with the equation:
    #       end date = today's date + datetime.timedelta(days=7)
    #       Use the datetime call exactly as it was provided to you. 
    #       You will then need to iterate through the
    #       Planner's list of events. Collect all events in a list where there is a date and the date is greater
    #       than or equal to today and less than or equal to 7 days from now. Return the list of events happening
    #       within the next week.
    def get_upcoming_events(self, date):
        # calculate the date
        end_date = date + timedelta(days=7)

        # make the list to store all the stuff
        events_due_soon = []

        # loop through planners list of events
        for event in self.events:
            # make an if statment saying if duedate is in 7 days display
            if event.date is not None:
                #check range
                if event.date >= date and event.date <= end_date:
                    #append
                    events_due_soon.append(event)

        return events_due_soon



    # DONE: write a method called get_todays_events that accepts a date object as an argument representing
    #       today's date. Iterate throught the Planner's list of events to find event's who's date matches
    #       today's date. Collect those events in a list and return them.
    def get_todays_events(self, date):
        # what the stuff will go in
        results = []

        # iterate through the events in planner
        for event in self.events:
            # check if event's date matches today's date.
            if event.date == date:
                results.append(event)
        return results