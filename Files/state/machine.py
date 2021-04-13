import walking_state


class Machine(object):

    def __init__(self):
        self.state = walking_state.StoppedState()

    def on_event(self, event):
        self.state = self.state.on_event(event)
