from sense_hat import SenseHat
import time

class Lighting:
    def __init__(self):
        self.sense = SenseHat()
        self.sense.clear()

    def load_state(self):
        colors = [
            [255, 0, 0],
            [255, 165, 0],
            [255, 255, 0],
            [0, 128, 0],
            [0, 0, 255],
            [75, 0, 130],
            [238, 130, 238],
        ]

        for rotation in [0, 90, 180, 270]:
            self.sense.clear()
            for i in range(8):
                self.sense.set_pixel(i, 0, colors[i % len(colors)])
            self.sense.set_rotation(rotation)
            time.sleep(0.2)

        time.sleep(1)
        self.sense.clear()

    def listening_state(self):
        colors = [
            [0, 0, 255],
            [0, 128, 0],
        ]

        for i in range(10):
            self.sense.clear()
            for j in range(8):
                self.sense.set_pixel(j, 4, colors[i % 2])
                self.sense.set_pixel(4, j, colors[(i + 1) % 2])
            time.sleep(0.5)

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
