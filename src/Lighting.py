from sense_hat import SenseHat
import time

class Lighting:
    def __init__(self):
        self.sense = SenseHat()
        self.sense.clear()

    def load_state(self):
        for angle in range(0, 361, 90):
            if angle == 360:
                angle = 0
            self.sense.set_rotation(angle)
            self.sense.show_letter("O", text_colour=[0, 255, 0])
            time.sleep(0.25)
        self.sense.clear()

    def listening_state(self):
        for angle in range(0, 361, 90):
            if angle == 360:
                angle = 0
            self.sense.set_rotation(angle)
            self.sense.show_letter("L", text_colour=[0, 0, 255])
            time.sleep(0.25)
        self.sense.clear()

    def close(self):
        self.sense.clear()

if __name__ == "__main__":
    lighting = Lighting()
    lighting.load_state()
    time.sleep(2)
    lighting.listening_state()
    time.sleep(2)
    lighting.close()
