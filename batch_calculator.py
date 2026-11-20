"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""

from calculator import add, subtract, multiply, divide


def process_calculation(operation, a_text, b_text):
    """Return (status, result, error_code) for one calculation.

    Inputs are strings. Trim whitespace and use the four imported lab functions.
    Success: ("OK", numeric_result, "").
    The error_code is empty on success because there is no error to report.
    Error: ("ERROR", "", error_code).

    Check errors in order: UNKNOWN_OPERATION, INVALID_NUMBER, DIVISION_BY_ZERO.
    See the brief for the full contract. You may add small helper functions.
    """
    ops ={"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}

    if operation not in ops:
        return("ERROR", "", "UNKOWN_OPERATION")
    
    try:
            a = float(a_text)
            b = float(b_text)
    except ValueError:
         return("ERROR", "", "INVALID_NUMBER")

    if operation == "divide" and b == 0:
         return("ERROR", "", "DIVISION_BY_ZERO")

    return("OK", ops[operation](a,b), "")
    
