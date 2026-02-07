"""
Objectives
Improving the student's skills in creating decorators and operating with them.
Scenario
Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
Apply your decorator to those functions to ensure that the time of the function executions can be monitored.
"""
from datetime import datetime
import time

def execution_monitor(func):
    """Decorator that prints a timestamp and execution duration."""
    def wrapper(*args, **kwargs):
        # 1. Capture start time and human-readable timestamp
        start_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        t1 = time.perf_counter()
        
        # 2. Execute the function
        result = func(*args, **kwargs)
        
        # 3. Capture end time
        t2 = time.perf_counter()
        end_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 4. Calculate duration in milliseconds
        duration_ms = (t2 - t1) * 1000
        
        # 5. Print the requested status message
        print(f"[{func.__name__.upper()}] started on {start_timestamp}, finished on {end_timestamp}")
        print(f"Time taken: {duration_ms:.4f} ms")
        print("-" * 30)
        
        return result
    return wrapper

# --- Applying the Decorator ---

@execution_monitor
def add_numbers(a, b):
    time.sleep(0.1)  # Simulating some work
    return a + b

@execution_monitor
def multiply_numbers(a, b):
    time.sleep(0.05) # Simulating some work
    return a * b

# --- Execution ---

print(f"Result of Addition: {add_numbers(10, 25)}")
print(f"Result of Multiplication: {multiply_numbers(5, 5)}")