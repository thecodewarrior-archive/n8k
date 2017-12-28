import gui


class TestScreen(gui.Screen):
    def __init__(self):
        super().__init__()

        done = gui.CameraSprite()
        done.rect.width = 100
        done.rect.height = 100
        self.group.add(done)
