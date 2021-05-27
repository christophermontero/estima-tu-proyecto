from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@given('we have behave installed {x}')
def step_impl(context, x):
    print(x)

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False