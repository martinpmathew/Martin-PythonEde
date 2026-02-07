"""
Objectives
improving the student's skills in operating with static and class methods
Scenario
Create a class representing a luxury watch;
The class should allow you to hold a number of watches created in the watches_created class variable. The number could be fetched using a class method named get_number_of_watches_created;
the class may allow you to create a watch with a dedicated engraving (text). As this is an extra option, the watch with the engraving should be created using an alternative constructor (a class method), as a regular __init__ method should not allow ordering engravings;
the regular __init__ method should only increase the value of the appropriate class variable;
The text intended to be engraved should follow some restrictions:

it should not be longer than 40 characters;
it should consist of alphanumerical characters, so no space characters are allowed;
if the text does not comply with restrictions, an exception should be raised;
before engraving the desired text, the text should be validated against restrictions using a dedicated static method.

Create a watch with no engraving
Create a watch with correct text for engraving
Try to create a watch with incorrect text, like 'foo@baz.com'. Handle the exception
After each watch is created, call class method to see if the counter variable was increased
"""

class LuxuryWatch:
    # Class variable to track all watches created
    watches_created = 0

    @classmethod
    def get_number_of_watches_created(cls):
        """Class method to fetch the current count of watches."""
        return cls.watches_created

    def __init__(self):
        """Regular constructor (no engraving allowed here)."""
        LuxuryWatch.watches_created += 1
        self.engraving = None

    @staticmethod
    def validate_engraving(text):
        """Static method: A utility to check if text meets luxury standards."""
        if len(text) > 40:
            return False
        if not text.isalnum():  # Checks if alphanumeric AND has no spaces/symbols
            return False
        return True

    @classmethod
    def create_with_engraving(cls, text):
        """Alternative constructor (Class Method)."""
        if cls.validate_engraving(text):
            # Create the instance using the class reference
            new_watch = cls() 
            new_watch.engraving = text
            return new_watch
        else:
            raise ValueError(f"Invalid engraving: '{text}'. Must be alphanumeric and max 40 chars.")

# --- Testing the Scenario ---

# 1. Create a watch with no engraving
watch1 = LuxuryWatch()
print(f"Watch 1 created. Total: {LuxuryWatch.get_number_of_watches_created()}")

# 2. Create a watch with correct text
try:
    watch2 = LuxuryWatch.create_with_engraving("Anniversary2026")
    print(f"Watch 2 created with engraving: {watch2.engraving}")
    print(f"Total watches: {LuxuryWatch.get_number_of_watches_created()}")
except ValueError as e:
    print(e)

# 3. Try to create a watch with incorrect text
try:
    print("Attempting to engrave 'foo@baz.com'...")
    watch3 = LuxuryWatch.create_with_engraving("foo@baz.com")
except ValueError as e:
    print(f"Caught expected error: {e}")

# Final count check
print(f"Final watch count: {LuxuryWatch.get_number_of_watches_created()}")