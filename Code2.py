class Person:
  """A class that represents a person."""

  def __init__(self, name, age):
    """Initializes the Person object."""
    self.name = name
    self.age = age

  def greet(self):
    """Prints a greeting to the user."""
    print("Hello, my name is {} and I am {} years old.".format(self.name, self.age))

# Create a Person object.
alice = Person("Alice", 25)

# Call the greet() method on the Person object.
alice.greet()
