from unittest import TestCase, main
from datastructure.bracket_matching import main as match


class TestBracketMatches(TestCase):
    def test_unmatched_left_over(self):
        self.assertEqual(match("(){}name("),9)
    def test_closed_bracket_first(self):
        self.assertEqual(match("name)"),5)
        self.assertEqual(match("}"),1)
    def test_index(self):
        self.assertEqual(match("foo(bar[i);"),10)
        self.assertEqual(match("{[}"),3)
    def test_success(self):
        self.assertEqual(match("foo(bar);"),'Success')
        self.assertEqual(match("{[]}()"),'Success')
        self.assertEqual(match("(())()"),'Success')

if __name__ == '__main__':
    main()
