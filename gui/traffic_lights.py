import tkinter as tk

class TrafficLightSimulator:
    def __init__(self, master):
        """Initializes the main application window and components."""
        self.master = master
        self.master.title("Traffic Light Simulator")
        self.master.geometry("200x400")
        self.master.resizable(False, False)

        # The core knowledge base for the traffic light phases
        # Format: (red_light, yellow_light, green_light)
        self.phases = (
            (True, False, False),  # Red
            (True, True, False),   # Red and Yellow
            (False, False, True),  # Green
            (False, True, False)   # Yellow
        )
        self.current_phase_index = 0

        # Create the canvas for the traffic light housing and lights
        self.canvas = tk.Canvas(
            self.master,
            width=100,
            height=250,
            bg="black",
            highlightthickness=0
        )
        self.canvas.pack(pady=20)

        # Create the circles for the lights (initially off)
        # Store the IDs to easily change their color later
        self.red_light_id = self.canvas.create_oval(
            25, 25, 75, 75, fill="gray", outline="white"
        )
        self.yellow_light_id = self.canvas.create_oval(
            25, 100, 75, 150, fill="gray", outline="white"
        )
        self.green_light_id = self.canvas.create_oval(
            25, 175, 75, 225, fill="gray", outline="white"
        )

        # Create the control buttons
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack()

        self.next_button = tk.Button(
            self.button_frame,
            text="Next",
            command=self.next_phase
        )
        self.next_button.pack(side=tk.LEFT, padx=10)

        self.quit_button = tk.Button(
            self.button_frame,
            text="Quit",
            command=self.quit_app
        )
        self.quit_button.pack(side=tk.LEFT, padx=10)

        # Initialize the first phase
        self.update_lights()

    def update_lights(self):
        """
        Updates the colors of the lights based on the current phase.
        This method is designed to work with any changes to the self.phases tuple.
        """
        red_state, yellow_state, green_state = self.phases[self.current_phase_index]

        # Use a list of light IDs and their corresponding states
        light_ids = [self.red_light_id, self.yellow_light_id, self.green_light_id]
        light_states = [red_state, yellow_state, green_state]
        active_colors = ["red", "yellow", "green"]
        
        # Iterate through the lights and set the correct color
        for i, light_id in enumerate(light_ids):
            is_on = light_states[i]
            color = active_colors[i] if is_on else "gray"
            self.canvas.itemconfig(light_id, fill=color)

    def next_phase(self):
        """
        Advances the simulation to the next phase, cycling back to the start
        when the end of the phases tuple is reached.
        """
        # Increment the phase index and wrap it around
        self.current_phase_index = (self.current_phase_index + 1) % len(self.phases)
        self.update_lights()

    def quit_app(self):
        """Exits the application."""
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficLightSimulator(root)
    root.mainloop()
