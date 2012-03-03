
class JUST:
    def __init__(self, value):
        self.value = value


class NOT(object):
    def __init__(self, expression):
        self.expression = expression


class AND(object):
    def __init__(self, *terms):
        self.terms = terms

class OR(object):
    def __init__(self, *terms):
        self.terms = terms

