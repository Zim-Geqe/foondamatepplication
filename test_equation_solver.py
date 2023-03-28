import unittest

from equation_solver import parse_equation, solve_equation


class TestEquationSolver(unittest.TestCase):
    def test_parse_equation(self):
        self.assertEqual(parse_equation("2x + 3 = 7"), (2, 3, 7, None, True))
        self.assertEqual(parse_equation("3(x - 4) + 5 = 8"), (3, -4, 5, 8, False))
        with self.assertRaises(ValueError):
            parse_equation("2y + 3 = 7")
    
    
    
    def test_solve_equation(self):
        self.assertEqual(solve_equation("2x + 3 = 7"), (2.0,
        ['Isolate x terms to one side of the equation.', '2x +3 7 = 0', '2x +3 7 +3 -3 = -3', '2x +3 4 = -3', '2x = 4', 'x = 2.0']))
        self.assertEqual(solve_equation("3(x - 4) + 5 = 8"),(5.0, 
        ['Distribute a to remove parentheses', '3(x -4 -4) +5 -8 = 0', '3x -12 5 +8 12 = 0', 'Combine like terms', '3x -4 3 = 0', 'Isolate x terms to one side of the equation', '3x -4 3 -4 4 = 4', '3x -4 7 = 4', '3x = 7', 'x = 5.0']
        ) )



if __name__=="__main__":
    unittest.TestCase        