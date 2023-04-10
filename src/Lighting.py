from sense_hat import SenseHat
from time import sleep

class Lighting:
    def __init__(self):
        self.sense = SenseHat()
        self.sense.clear()

    def load_state(self):
        self.sense.clear()
        for angle in range(0, 360, 45):
            self.sense.set_rotation(angle)
            self.sense.set_pixel(3, 0, 255, 255, 255)
            sleep(0.1)
            self.sense.clear()

    def listening_state(self):
        self.sense.clear()
        for angle in range(0, 360, 45):
            self.sense.set_rotation(angle)
            self.sense.set_pixel(0, 3, 0, 255, 0)
            sleep(0.1)
            self.sense.clear()

    def close(self):
        self.sense.clear()
# Example usage:
lighting = Lighting()

lighting.load_state()
sleep(2)

lighting.listening_state()
sleep(2)

lighting.close()