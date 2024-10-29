
class TrafficLight:
    """
    Model a traffic light that cycles through red, yellow, and green.
    """

    def __init__(self, color="red"):
        """
        Constructor to initialize the traffic light's color.
        @param color: String, initial color of the traffic light ("red" by default)
        """
        self._color = color

    # Getter for color
    def get_color(self):
        """
        @return: String, the current color of the traffic light.
        """
        return self._color

    # Setter for color
    def set_color(self, color):
        """
        Set the traffic light to a specific color.
        @param color: String, the color to set ("red", "yellow", or "green").
        """
        if color in ["red", "yellow", "green"]:
            self._color = color
        else:
            print("Invalid color! Use 'red', 'yellow', or 'green'.")

    # Method to change to the next color in the sequence
    def change_color(self):
        """
        Change the traffic light to the next color in the cycle.
        """
        if self._color == "red":
            self._color = "green"
        elif self._color == "green":
            self._color = "yellow"
        elif self._color == "yellow":
            self._color = "red"
        print(f"The traffic light is now {self._color}.")

    # __str__ method for a user-friendly print
    def __str__(self):
        """
        @return: String, a human-readable representation of the traffic light.
        """
        return f"TrafficLight(color={self._color})"

    # __repr__ method for an official string representation
    def __repr__(self):
        """
        @return: String, an evaluable string representation of the object.
        """
        return f"TrafficLight('{self._color}')"