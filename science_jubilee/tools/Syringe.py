from .Tool import Tool, ToolStateError


class Syringe(Tool):
    def __init__(self, index, name):
        super().__init__(index, name)
