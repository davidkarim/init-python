import os, random

# Our hello world function
def say_hello(name):
    print(f"Hello {name}!")

# Use the __name__ variable to check if we are running as a script or a module
if __name__ == "__main__":
    # Running as a script instead of an imported module
    say_hello("David")
    print("Your current working directory is: " + os.getcwd())
    rand = random.randint(1, 100)
    print(f"Here's a random number between 1 and 100: {rand}")
