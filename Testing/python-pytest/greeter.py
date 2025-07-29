class Greeter:
    # Constructor method that gets called automatically when an object is created
    def __init__(self, name):  
        self.name = name  
        # self is a pointer over here
        # 'self.name' is assigned the value passed when the object is created

    # Method to return a greeting message
    def say_hello(self):
        return f"Hello, {self.name}"  # Returns a formatted string using the object's 'name'
