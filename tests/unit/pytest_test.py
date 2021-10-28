# Pytest will fail if it finds no tests;
#  having this in here ensures that there
#  is always a basic test for it to find
#  that must pass.
def test_pytest_finds_unit_tests():
    assert True
