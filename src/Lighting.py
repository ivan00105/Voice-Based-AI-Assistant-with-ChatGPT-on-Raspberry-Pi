from sense_hat import SenseHat
import time
import threading

class Lighting:
    def __init__(self):
        self.sense = SenseHat()
        self.sense.clear()
        self.running = False

    def _load_state(self):
        circle = [
            [4, 3],
            [4, 2],
            [5, 2],
            [5, 3],
            [5, 4],
            [4, 4],
            [3, 4],
            [3, 3],
            [3, 2],
            [2, 2],
            [2, 3],
            [2, 4]
        ]

        color = [0, 0, 255]

        while self.running:
            self.sense.clear()
            for point in circle:
                x = point[0]
                y = point[1]
                self.sense.set_pixel(x, y, color)

            color, circle[-1] = circle.pop(), circle[-1]

            time.sleep(0.1)

        self.sense.clear()

    def load_state(self):
        self.running = True
        self.thread = threading.Thread(target=self._load_state)
        self.thread.start()

    def _listening_state(self):
        colors = [
            [0, 0, 255],
            [0, 128, 0],
        ]

        while self.running:
            self.sense.clear()
            for i in range(2):
                color = colors[i]
                for j in range(8):
                    self.sense.set_pixel(j, 3, color)
                    self.sense.set_pixel(j, 4, color)
                    self.sense.set_pixel(3, j, color)
                    self.sense.set_pixel(4, j, color)
                time.sleep(0.5)

        self.sense.clear()

    def listening_state(self):
        self.running = True
        self.thread = threading.Thread(target=self._listening_state)
        self.thread.start()

    def close(self):
        self.running = False
        if self.thread.is_alive():
            self.thread.join()
        self.sense.clear()

if __name__ == "__main__":
    lighting = Lighting()
    lighting.load_state()
    time.sleep(5)  # Simulate other tasks running
    lighting.close()
    time.sleep(2)
    lighting.listening_state()
    time.sleep(5)  # Simulate other tasks running
    lighting.close()
