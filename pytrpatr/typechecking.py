
from functools import wraps
import logging

logger = logging.getLogger(__name__)


class ArgumentMismatch(TypeError):
    pass


class TypeChecker(object):
    '''
    This is essentially a function that checks whether or not
    a value is of a given type.
    '''
    
    def __init__(self, t):
        self.type = t

    def __call__(self, instance):
        return isinstance(instance, self.type)

    def __eq__(self, other):
        return isinstance(other, TypeChecker) and (self.type == other.type)

    def __ne__(self, other):
        return not(self == other)





class accepts(object):
    def __init__(self, *arg_specs):
        self.arg_specs = arg_specs

    def __call__(self, f):
        @wraps(f)
        def check_args(*args, **kwargs):
            for (spec, arg) in zip(self.arg_specs, args):
                if not isinstance(arg, spec):
                    raise ArgumentMismatch()
            return f(*args, **kwargs)

        return check_args



class returns(object):
    def __init__(self, return_spec):
        self.return_spec = return_spec

    def __call__(self, f):
        @wraps(f)
        def check_return_value(*args, **kwargs):
            return f(*args, **kwargs)
        
        return check_return_value


class raises(object):
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __call__(self, f):
        @wraps(f)
        def check_exceptions(*args, **kwargs):
            return f(*args, **kwargs)
        return check_exceptions




