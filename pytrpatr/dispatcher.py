



class Understanding(object):
    def __init__(self, definition, interpretation):
        self.definition     = definition
        self.interpretation = interpretation



class Rule:
    def condition(self, *args, **kwargs):
        return False

    def action(self, *args, **kwargs):
        pass


class Dispatcher(object):
    def __init__(self):
        self.rules = []
        self.nothing_matched

    def __call__(self, *args, **kwargs):
        for r in self.rules:
            if r.condition(*args, **kwargs):
                return r.action(*args, **kwargs)

        return self.otherwise(*args, **kwargs)

