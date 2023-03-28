# foondamatepplication
Equation Solver
This is a simple Python module that can solve linear equations of the form ax + b = c or a(x + b) + c = d, and provide a list of steps for how the solution was obtained.

Running the App 
run : python equation_solver.py
enter the quation you want to solve

Limitations
This module only supports linear equations of the form ax + b = c or a(x + b) + c = d. If the input equation is not of either form, the solve_equation function will raise a ValueError.

Testing
Unit and integration tests are included in the tests.py file. To run the tests, simply run python test_equation_solver.py from the command line.
run : python -m unittest