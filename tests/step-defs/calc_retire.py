from pytest_bdd import scenario, given, when, then
from full_retirement_age_calculator_app import main
import mock


@scenario('../features/calc_retire.feature', 'Exiting the program')
def test_exit():
    pass


@given("The prompt “Enter the year of birth or <enter> to exit”")
def year_prompt():
    pass
    # assert calculator.birth_year_str == "Enter the year of birth or <enter> to exit "


@when("The user presses the <Enter> key")
def enter():
    # mock.patch('builtins.input', return_value="")
    pass

@then("the program will end")
def end():
    pass