from behave import *


@given('we are on the home page')
def step_impl(context):
    context.execute_steps('')


@when('I add a new resource')
def click_link_text(text):
    text = "Add new resource"


@when('I see "Name:"')
def should_see(text):
    text = "Name:"


@when('I enter "test" in "box"')
def click_element(element):
    element = "id_name"


@when('I fill in "Description Name" with "BDD TEST" ')
def should_see(context, text):
    context.execute_steps()


@when('I fill in "Url" with "BDD TEST" ')
def should_see(context, text):
    context.execute_steps('')


@when('I press "Submit"" ')
def step_impl(context):
    context.execute_steps('')


