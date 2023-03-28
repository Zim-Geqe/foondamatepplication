import re

def parse_equation(equation):
    # This function parses the equation string and returns a tuple of the form (a, b, c, d, is_first_type)
    # where is_first_type is True if the equation is of the form ax + b = c and False if the equation is of the form a(x + b) + c = d.
    # If the equation is not of either form, the function raises a ValueError.
    first_type_regex = r'^\s*(\d+)\s*x\s*([-+])\s*(\d+)\s*=\s*(\d+)\s*$'
    second_type_regex = r'^\s*(\d+)\s*\(\s*x\s*([-+])\s*(\d+)\s*\)\s*([-+])\s*(\d+)\s*=\s*(\d+)\s*$'

    first_type_match = re.match(first_type_regex, equation)
    if first_type_match:
        a = int(first_type_match.group(1))
        b = int(first_type_match.group(3)) * (-1 if first_type_match.group(2) == '-' else 1)
        c = int(first_type_match.group(4))
        return a, b, c, None, True

    second_type_match = re.match(second_type_regex, equation)
    if second_type_match:
        a = int(second_type_match.group(1))
        b = int(second_type_match.group(3)) * (-1 if second_type_match.group(2) == '-' else 1)
        c = int(second_type_match.group(5))
        d = int(second_type_match.group(6))
        return a, b, c, d, False

    raise ValueError("Invalid equation")

def solve_equation(equation):
    a, b, c, d, is_first_type = parse_equation(equation)

    if is_first_type:
        # Solve equation of the form ax + b = c
        x = (c - b) / a
        steps = [
            "Isolate x terms to one side of the equation.",
            f"{a}x {b:+} {c} = 0",
            f"{a}x {b:+} {c} {b:+} {-b} = {-b}",
            f"{a}x {b:+} {c-b} = {-b}",
            f"{a}x = {c-b}",
            f"x = {x}"
        ]
    else:
        # Solve equation of the form a(x + b) + c = d
        x = (d - c) / a - b
        steps = [
            "Distribute a to remove parentheses",
            f"{a}(x {b:+} {b}) {c:+} {-d} = 0",
            f"{a}x {a*b:+} {c} {d:+} {-a*b} = 0",
            "Combine like terms",
            f"{a}x {b:+} {d - c} = 0",
            "Isolate x terms to one side of the equation",
            f"{a}x {b:+} {d - c} {b:+} {-b} = {-b}",
            f"{a}x {b:+} {d - c - b} = {-b}",
            f"{a}x = {d - c - b}",
            f"x = {x}"
        ]

    return x, steps
    
if __name__ == '__main__':
    equation = input("Enter equation: ")
    x, steps = solve_equation(equation)
    print(f"Solution: x = {x}")
    print("Steps:")
    print(steps)
