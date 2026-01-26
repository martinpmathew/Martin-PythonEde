import json

class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model

def encode_vehicle(q):
    if isinstance(q, Vehicle):
        return q.__dict__
    else:
        raise TypeError(q.__class__.__name__ + 'is not JSON serializable')
    
def decode_vehicle(ve):
    return Vehicle(ve['name'], ve['model'])

# Write your code here.
vehicle = Vehicle("Hyundai", "i20")
json_str = json.dumps(vehicle, default=encode_vehicle)
new_vehicle = json.loads(json_str, object_hook=decode_vehicle)

print(json_str)
print(type(json_str))


print(new_vehicle.__dict__)
print(type(new_vehicle))




# Objectives

# Learn how to:

#     use the json module and its basic facilities;
#     encode and decode JSON strings from/to Python objects.

# Scenario

# Take a look at these two screenshots. They present two different use cases of the same program:

# Command prompt -- python 01.py

# Command prompt -- python 02.py

# Your task is to write a code which has exactly the same conversation with the user and:

#     defines a class named Vehicle, whose objects can carry the vehicle data shown above (the structure of the class should be deducted from the above dialog — call it "reverse engineering" if you want)
#     defines a class able to encode the Vehicle object into an equivalent JSON string;
#     defines a class able to decode the JSON string into the newly created Vehicle object.

# Of course, some basic data validity checks should be done, too. We're sure you're careful enough to protect your code from reckless users.
