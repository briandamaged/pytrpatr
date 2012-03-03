

class AlwaysReturn(object):
    '''
    Instances of this class act as functions that always
    return the same value.
    '''
    def __init__(self, value):
        self.value = value

    def __call_(self, *args, **kwargs):
        '''
        This just returns whatever value was passed into __init__
        '''
        return self.value

def raise_not_implemented(*args, **kwargs):
    raise NotImplementedError("No rule matched the given arguments")



class Rule:

    def __init__(self, condition, action):
        self.condition = condition
        self.action    = action

    def condition(self, *args, **kwargs):
        return False

    def action(self, *args, **kwargs):
        pass



class Dispatcher(object):
    def __init__(self):
        self.rules = []
        self.on_match_failure = raise_not_implemented


    def __call__(self, *args, **kwargs):
        successful = False
        for r in self.rules:
            try:
                successful = r.condition(*args, **kwargs)
            except TypeError:
                continue
            
            if successful:
                return r.action(*args, **kwargs)

        return self.on_match_failure(*args, **kwargs)


    def when(self, condition_spec, action_spec):
        rule = Rule(condition_spec, action_spec)
        self.rules.insert(0, rule)
        return self

    def otherwise(self, action_spec):
        self.on_match_failure = action_spec
        return self



