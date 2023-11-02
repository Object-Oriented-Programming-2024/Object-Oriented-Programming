class LightBulb:
    def __init__(self, is_on=False, brightness_level=0):
        self.is_on = is_on
        self.brightness_level = brightness_level

    # The below methods regulate the Lightbulb state.
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness_level = level
        else:
            print("Brightness level should be between 0 and 100.")

    def __str__(self):
        return (f"Lightbulb ({'On' if self.is_on else 'Off'}), "
                f"Brightness: {self.brightness_level}%")


# Create a Lightbulb object
my_lightbulb = LightBulb()

# Display initial state
print(my_lightbulb)

# Turn on the lightbulb and set the brightness
my_lightbulb.turn_on()
my_lightbulb.set_brightness(75)

# Display updated state
print(my_lightbulb)

# Turn off the lightbulb
my_lightbulb.turn_off()

# Display final state
print(my_lightbulb)