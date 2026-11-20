from batch_calculator import process_calculation

def test_procession_calculation():
    assert process_calculation("add", "6", "7") == ("OK", 13, "")