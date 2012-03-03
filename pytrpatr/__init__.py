import types
import collections
from functools import wraps




'''

def identity(x):
    return x



def value_equals(x):
    def check_value(y):
        return y == x
    return check_value

def not_implemented(*args, **kwargs):
    raise NotImplementedError()



class ListMatcher:
    def __init__(self, conditions):
        self.conditions = conditions

    def __call__(self, *args):
        if len(self.conditions) != len(args):
            return False

        for (c, a) in zip(self.conditions, args):
            if not c(a):
                return False

        return True


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
        c = to_arglist_matcher(condition)
        a = to_action(action)
        self.rules.append(rule(c, a))


# The Dispatcher's given method constructs a dispatcher rule by invoking
# other dispatchers.  To make this work, we need to bootstrap 3 instances:
to_arg_matcher     = Dispatcher()
to_arglist_matcher = Dispatcher()
to_action          = Dispatcher()


to_arg_matcher.rules.append(rule(type_checker(types.TypeType), type_checker))
to_arglist_matcher.otherwise = to_arg_matcher
to_action.rules.append(rule(type_checker(types.FunctionType), identity))


to_arg_matcher.given(types.ClassType, type_checker)
to_arg_matcher.given(just, lambda x: value_equals(x.value))
to_arg_matcher.given(int, value_equals)
to_arg_matcher.given(str, value_equals)
to_arg_matcher.given(float, value_equals)
to_arg_matcher.given(types.FunctionType, identity)


def __optimize_bounded_list_matcher(x):
    if len(x) == 0:
        return lambda *aray: len(aray) == 0
    elif len(x) == 1:
        return to_arg_matcher(x[0])
    else:
        return ListMatcher(map(to_arg_matcher, x))


to_arglist_matcher.given(list, __optimize_bounded_list_matcher)
to_arglist_matcher.given(tuple, __optimize_bounded_list_matcher)
to_arglist_matcher.given(types.FunctionType, identity)

to_action.given(just, lambda x: always_return(x.value))
to_action.given(int, always_return)
to_action.given(str, always_return)
to_action.given(float, always_return)


'''
