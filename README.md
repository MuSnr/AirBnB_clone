# 0x00. AirBnB clone - The console
![hbnb](https://github.com/MuSnr/AirBnB_clone/assets/108272722/ec78ff0d-60b4-4b3f-ad7a-0ff76110939d)

## AirBnB clone
The project entails an implementation of a replica of an AirBnB website. When this project is finished, it will have:
*A command interpreter, similar to a shell, that can manipulate data without a graphical user interface (for development and debugging)
*A front-end website with both dynamic and static features
*An extensive database for controlling the backend features
*An API that offers a channel of communication between the system's front and back ends.

## Concept Review
It is helpful to keep in mind the following ideas as you work through this code base to finish this project.
*How to create a package in Python
*How to use the cmd module in Python to create a command interpreter
*What is unit testing and how can you implement project ?
*How a Class is Serialized and Deserialized
*Writing and reading JSON files
*How to handle the time difference(date/time)
*What's a UUID?
*How to use and what *args is
*How to utilize **kwargs and what is it?
*How a function handles named arguments

## Phase One(Console)
In order to provide an abstraction between objects and their storage and persistence, the initial step involves manipulating a robust storage system. In order to do this, I'll:

*set up a parent class called BaseModel to handle my future instances' initialization, serialization, and deserialization.
*create a basic serialization/deserialization flow: Dictionary \-> JSON string \-> Instance \-> doc
*Create all the AirBnB classes (User, State, City, Place, etc.) that derive from BaseModel.
*create the project's initial abstracted storage engine: storing files.
*create all unittests in order to verify our storage engine and all of our classes.
*Make a model of the data.
*Create, modify, delete, and other object operations with a console or command interpreter
*Save and maintain items in files (JSON files) S

