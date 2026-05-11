# dispatcher.py

class Dispatcher:
    """
    消息分发器
    """

    def __init__(self):
        self.handlers = {}
