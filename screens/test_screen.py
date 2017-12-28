import gui


class TestScreen(gui.Screen):
    def __init__(self):
        super().__init__()

        done = gui.Sprite("done", 10, 10)
        self.group.add(done)
