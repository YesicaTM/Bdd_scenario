from pytest_bdd import scenario, scenarios, parser, parsers, given, when, then
from full_retirement_age_calculator_app import main
import mock

EXTRA_TYPES = {
    'Date': int
}

scenarios('../features/calc_retire.feature', example_converters=EXTRA_TYPES)


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


@scenario('../features/calc_retire.feature', 'Entering a valid birth year')
def test_1():
    pass


@given("The prompt “Enter the year of birth or <enter> to exit”")
def prompt():
    pass


@when(parsers.cfparse('The user enters {Year:Date}', extra_types=EXTRA_TYPES))
@when('The user enters <Year>')
def year_entry(Date):
#     ??
    pass
