import state


class StoppedState(state.State):
    """
    This state indicates that SpotMicro stands
    """

    def on_event(self, event):
        if event == "walk":
            return WalkState()
        return self


class WalkState(state.State):
    """
    This state indicates the first walking state
    """

    def on_event(self, event):
        if event == "stop":
            return StoppedState()
        return self
