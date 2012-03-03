
import unittest

from pytrpatr.typechecking import accepts, ArgumentMismatch


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
