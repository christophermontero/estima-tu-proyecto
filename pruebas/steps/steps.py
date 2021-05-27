from behave import *

@given('esta la aplicacion arriba')
def step_impl(context):
    pass

@given('voy vender bonice')
def step_impl(context):
    pass

@when('envio una peticion a la siguiente url {url}')
def step_impl(context, url):
    print(url)

@then('el sistema almacenara un nuevo proyecto')
def step_impl(context):
    assert context.failed is False