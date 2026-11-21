from batch_calculator import process_calculation

def test_process_addition():
    assert process_calculation("add", "6", "7") == ("OK", 13, "")

def test_process_calculation_subtract():
    assert process_calculation("subtract", "5", "4") == ("OK", 1, "")

def test_process_calculation_multiply():
    assert process_calculation("multiply", "8", "9") == ("OK", 72, "")

def test_process_calculation_divide():
    assert process_calculation("divide", "20", "5") == ("OK", 4, "")

def test_process_calculation_unknown_op():
    assert process_calculation("mod", "13", "2") == ("ERROR", "", "UNKNOWN_OPERATION")

def test_process_calculation_invalid_num():
    assert process_calculation("add", "", "2") == ("ERROR", "", "INVALID_NUMBER")

def test_process_calculation_div_by_zero():
    assert process_calculation("divide", "12", "0") == ("ERROR", "", "DIVISION_BY_ZERO")

def test_process_calculation_error_priority():
    assert process_calculation("mod", "", "0") == ("ERROR", "", "UNKNOWN_OPERATION")

def test_process_calculation_negative_sub():
    assert process_calculation("subtract", "2", "12") == ("OK", -10, "")

def test_process_calculation_decimal_add():
    assert process_calculation("add", "4.6", "8.08") == ("OK", 12.68, "")

def test_process_calculation_whitespace_add():
    assert process_calculation(" add", "8 ", "4") == ("OK", 12, "")