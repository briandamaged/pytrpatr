import types
import collections
from functools import wraps


def memoized(f):
    cache = {}
    @wraps(f)
    def memo(*args):
        try:
            return cache[args]
        except KeyError:
            retval = f(*args)
            cache[args] = retval
            return retval
    return memo



@memoized
def type_checker(t):
    return lambda x: isinstance(x, t)


class just:
    def __init__(self, value):
        self.value = value


def identity(x):
    return x

def always_return(x):
    def always_returns_value(*args, **kwargs):
        return x
    return always_returns_value

def value_equals(x):
    def check_value(y):
        return y == x
    return check_value

def not_implemented(*args, **kwargs):
    raise NotImplementedError()



class DotMatcher:
    def __init__(self, conditions):
        self.conditions = conditions

    def __call__(self, **args):
        pass


class rule:
    def __init__(self, condition = not_implemented, action = not_implemented):
        self.condition = condition
        self.action    = action


class Dispatcher:
    def __init__(self, otherwise = not_implemented):
        self.rules = []
        self.otherwise = not_implemented


    def __call__(self, *args, **kwargs):
        for r in self.rules:
            if r.condition(*args, **kwargs):
                return r.action(*args, **kwargs)

        return self.otherwise(*args, **kwargs)

    def given(self, condition, action):
        c = to_arg_matcher(condition)
        a = to_action(action)
        self.rules.append(rule(c, a))



to_arg_matcher = Dispatcher()
to_arg_matcher.rules.append(rule(lambda x: isinstance(x, types.ClassType), lambda x: type_checker(x)))
to_arg_matcher.rules.append(rule(lambda x: isinstance(x, types.TypeType), lambda x: type_checker(x)))

to_action    = Dispatcher()
to_action.rules.append(rule(lambda x: isinstance(x, collections.Callable), lambda x: x))

to_arg_matcher.given(just, lambda x: value_equals(x.value))
to_arg_matcher.given(int, value_equals)
to_arg_matcher.given(str, value_equals)
to_arg_matcher.given(float, value_equals)

to_action.given(just, lambda x: always_return(x.value))
to_action.given(int, always_return)
to_action.given(str, always_return)
to_action.given(float, always_return)



