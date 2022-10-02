class Dog:
    """A simple model of a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to command"""
        print(f"{self.name} rolled over!")
    
    def play_dead(self):
        """Simulates a dog playing dead"""
        print(f"{self.name} plays dead.")

#Make an Instance
my_dog = Dog('Buddy', 7)
print(f"My dog {my_dog.name} is my best friend.")
print(f"{my_dog.name} is {my_dog.age} years old.")

your_dog = Dog('Gunner', 4)
print(f"Hello {your_dog.name}, its very nice to meet you.")
print(f"So {your_dog.name} is {your_dog.age} years old?")

#Call method
my_dog.roll_over()
my_dog.sit()
your_dog.play_dead()

    