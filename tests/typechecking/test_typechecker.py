
import unittest

from pytrpatr.typechecking import TypeChecker


class baseclass(object):
    pass

class subclass(baseclass):
    pass



class Test_typechecker(unittest.TestCase):
    
    def test_exact_match(self):
        tc = TypeChecker(str)
        
        value = "hello"
        self.assertTrue(tc(value), 'The string %s satisfies the string typechecker' % value)

    def test_type_mismatch(self):
        tc = TypeChecker(str)
        
        value = 5
        self.assertFalse(tc(value), 'The integer %i does not satisfy the string typechecker' % value)


    def test_subclass_is_a_baseclass(self):
        tc = TypeChecker(baseclass)
        
        value = subclass()
        self.assertTrue(tc(value), 'A baseclass typechecker is satisfied by instances of the baseclass')

    def test_baseclass_is_not_a_subclass(self):
        tc = TypeChecker(subclass)
        
        value = baseclass()
        self.assertFalse(tc(value), 'A subclass typechecker is not satisfied by instances of the baseclass')


    def test_typechecker_equality(self):
        tc1 = TypeChecker(baseclass)
        tc2 = TypeChecker(baseclass)
        
        self.assertEqual(tc1, tc2, 'tc1 and tc2 check for the same type')
        self.assertFalse(tc1 != tc2, 'tc1 != tc2 returns False')

    def test_typechecker_inequality(self):
        tc1 = TypeChecker(baseclass)
        tc2 = TypeChecker(subclass)
        
        self.assertNotEqual(tc1, tc2, 'tc1 and tc2 check for different types')
        self.assertFalse(tc1 == tc2, 'tc1 == tc2 returns False')
