
from functools import wraps
import logging

logger = logging.getLogger(__name__)



class ArgumentMismatch(TypeError):
    pass






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




