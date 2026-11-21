from batch_calculator import process_calculation

def test_process_addition():
    assert process_calculation("add", "6", "7") == ("OK", 13, "")