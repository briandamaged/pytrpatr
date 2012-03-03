
import unittest

from pytrpatr.typechecking import typechecker
from pytrpatr.typechecking import accepts, ArgumentMismatch

class baseclass(object):
    pass

class subclass(baseclass):
    pass



class Test_typechecker(unittest.TestCase):
    
    def test_exact_type(self):
        tc = typechecker(str)
        
        value = "hello"
        self.assertTrue(tc(value), 'The string %s satisfies the string typechecker' % value)

    def test_type_mismatch(self):
        tc = typechecker(str)
        
        value = 5
        self.assertFalse(tc(value), 'The integer %i does not satisfy the string typechecker' % value)


    def test_subclass_match(self):
        tc = typechecker(baseclass)
        
        value = subclass()
        self.assertTrue(tc(value), 'A baseclass typechecker is satisfied by instances of the baseclass')

    def test_baseclass_not_match_subclass(self):
        tc = typechecker(subclass)
        
        value = baseclass()
        self.assertFalse(tc(value), 'A subclass typechecker is not satisfied by instances of the baseclass')


class TestAccepts(unittest.TestCase):

    def test_basic_usage(self):
        @accepts(int)
        def foo(x):
            return x + 1
        
        foo(5)

    def test_invalid_argument(self):
        @accepts(int)
        def foo(x):
            return x + 1
        
        with self.assertRaises(ArgumentMismatch):
            foo("Hello")
