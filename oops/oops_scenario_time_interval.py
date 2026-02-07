"""
Objectives
improving the student's skills in operating with special methods
Scenario
Create a class representing a time interval;
the class should implement its own method for addition, subtraction on time interval class objects;
the class should implement its own method for multiplication of time interval class objects by an integer-type value;
the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
check the argument type, and in case of a mismatch, raise a TypeError exception.
"""

class TimeInterval:
    def __init__(self, *, hours=0, minutes=0, seconds=0):
        # Validate that arguments are integers
        for label, val in [("hours", hours), ("minutes", minutes), ("seconds", seconds)]:
            if not isinstance(val, int):
                raise TypeError(f"The '{label}' parameter must be an integer.")

        # Normalize time immediately to keep logic simple
        # (e.g., 70 seconds becomes 1 minute and 10 seconds)
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self._from_seconds(total_seconds)

    def _from_seconds(self, total_seconds):
        """Helper to set attributes from a raw second count."""
        # 3600 is the number of seconds in one hour 60 * 60
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def _to_seconds(self):
        """Helper to convert current attributes back to seconds."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Addition is only supported between TimeInterval objects.")
        return TimeInterval(seconds=self._to_seconds() + other._to_seconds())

    def __sub__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Subtraction is only supported between TimeInterval objects.")
        result_seconds = self._to_seconds() - other._to_seconds()
        if result_seconds < 0:
            raise ValueError("TimeInterval cannot be negative.")
        return TimeInterval(seconds=result_seconds)

    def __mul__(self, multiplier):
        if not isinstance(multiplier, int):
            raise TypeError("Multiplication is only supported with an integer.")
        return TimeInterval(seconds=self._to_seconds() * multiplier)

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"


# Initialization
t1 = TimeInterval(hours=2, minutes=30, seconds=15)
t2 = TimeInterval(hours=1, minutes=45, seconds=0)

print(f"Time 1: {t1}")  # 02:30:15
print(f"Time 2: {t2}")  # 01:45:00

# Addition
print(f"Added: {t1 + t2}")  # 04:15:15

# Multiplication
print(f"Tripled: {t1 * 3}")  # 07:30:45
