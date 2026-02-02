import tkinter as tk

class TrafficLightSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light Simulator")

        # Create the canvas for the traffic lights
        self.canvas = tk.Canvas(root, width=150, height=400, bg="black")
        self.canvas.pack(pady=20)

        # Draw the three circles for the lights
        self.red_light = self.canvas.create_oval(30, 30, 120, 120, fill="gray")
        self.yellow_light = self.canvas.create_oval(30, 150, 120, 240, fill="gray")
        self.green_light = self.canvas.create_oval(30, 270, 120, 360, fill="gray")

        # Define the light durations in milliseconds
        self.durations = {
            "green": 5000,
            "yellow": 2000,
            "red": 5000
        }

        self.current_state = "red"
        self.transition_lights()

    def transition_lights(self):
        # Turn all lights off
        self.canvas.itemconfig(self.red_light, fill="gray")
        self.canvas.itemconfig(self.yellow_light, fill="gray")
        self.canvas.itemconfig(self.green_light, fill="gray")

        # Turn on the correct light based on the current state
        if self.current_state == "red":
            self.canvas.itemconfig(self.red_light, fill="red")
            next_state = "green"
            duration = self.durations["red"]
        elif self.current_state == "green":
            self.canvas.itemconfig(self.green_light, fill="green")
            next_state = "yellow"
            duration = self.durations["green"]
        else: # yellow
            self.canvas.itemconfig(self.yellow_light, fill="yellow")
            next_state = "red"
            duration = self.durations["yellow"]

        self.current_state = next_state
        
        # Schedule the next transition
        self.root.after(duration, self.transition_lights)

if __name__ == "__main__":
    root = tk.Tk()
    simulator = TrafficLightSimulator(root)
    root.mainloop()