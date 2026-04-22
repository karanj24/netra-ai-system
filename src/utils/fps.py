import time

class FPS:
    def __init__(self):
        self.prev_time = 0

    def get_fps(self):
        curr_time = time.time()
        fps = 1 / (curr_time - self.prev_time) if self.prev_time != 0 else 0
        self.prev_time = curr_time
        return int(fps)