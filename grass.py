from pico2d import load_image


class Grass:
    def __init__(self):
        self.x, self.y = 400, 30
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
