

from pytrpatr.dispatcher import Dispatcher
import unittest


class Test_Dispatcher(unittest.TestCase):
    def test_empty_dispatcher_raises_exception_when_invoked(self):
        d = Dispatcher()
        with self.assertRaises(NotImplementedError):
            d("Hello")

    def test_action_occurs_when_corresponding_condition_is_satisfied(self):
        d = Dispatcher()
        d.when(lambda x : isinstance(x, int), lambda x : 1)
        d.when(lambda x : isinstance(x, str), lambda x : 2)
        
        self.assertEqual(d(5), 1)
        self.assertEqual(d("hello"), 2)


    def test_most_recent_rule_takes_precendence(self):
        d = Dispatcher()
        d.when(lambda x : x > 0, lambda x : 1)
        d.when(lambda x : x > 8, lambda x : 2)
        d.when(lambda x : x > 4 and x < 12, lambda x : 3)
        
        msg1 = "Rule 1 applies over the interval (1, 4]"
        msg2 = "Rule 2 applies over the interval [12, infinity)"
        msg3 = "Rule 3 applies over the interval (4, 12)"
        
        self.assertEqual(d(2), 1, msg1)
        self.assertEqual(d(2), 1, msg1)
        self.assertEqual(d(5), 3, msg3)
        self.assertEqual(d(11), 3, msg3)
        self.assertEqual(d(12), 2, msg2)
        self.assertEqual(d(500), 2, msg2)


    def test_handles_arg_count_mismatches_gracefully(self):
        d = Dispatcher()
        d.when(lambda x : True, lambda x : 1)
        d.when(lambda x, y : True, lambda x, y : 2)

        try:
            self.assertEqual(d(1), 1, "Rule 1 should fire whenever the dispatcher is called with 1 argument")
        except TypeError:
            self.fail("The Dispatcher attempted to invoke rule 2 with 1 argument")

        try:
            self.assertEqual(d(1, 2), 2, "Rule 2 should fire whenever the dispatcher is called with 2 arguments")
        except TypeError:
            self.fail("The Dispatcher attempted to invoke rule 1 with 2 arguments")



    def test_otherwise_handles_anything_that_does_not_satisfy_any_rules(self):
        d = Dispatcher()
        d.when(lambda x : x > 0, lambda x : 1)
        d.otherwise(lambda *x : 2)
        
        self.assertEqual(d(10), 1, "The rule catches any value greater than 0")
        self.assertEqual(d(10, "Bob Saget"), 2, "No rule accepts 2 arguments, so the action described by self.on_match_failure is invoked")
