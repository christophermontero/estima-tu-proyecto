import requests
import json
from behave import *


@then('el sistema almacenara un nuevo proyecto')
def step_impl(context):
    url = context.api_url + context.resource
    session = requests.Session()

    response = session.get(url=url)
    tamano_actual = len(json.loads(response.text)["proyectos"])
    assert tamano_actual - context.size is 1


@given('la "{url}" para la creacion')
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    :type url: str
    """
    context.api_url = 'http://localhost:8080'
    context.resource = url


@when('el usuario regular desee "crear" un proyecto con {nombre_proyecto} y {descripcion_proyecto}')
def step_impl(context, nombre_proyecto, descripcion_proyecto):
    """
    :type context: behave.runner.Context
    :type nombre_proyecto: str
    :type descripcion_proyecto: str
    """
    url = context.api_url + context.resource
    body = {"nombreProyecto": nombre_proyecto,
            "descProyecto": descripcion_proyecto}

    session = requests.Session()

    response = session.get(url=url)
    context.size = len(json.loads(response.text)["proyectos"])
    session.post(url=url, data=body)


@then("el sistema retornara el proyecto con sus modulos y funciones")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Se verifica que contenga nombre y descripcion


@then("el sistema almacenara los cambios del proyecto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then el sistema almacenara los cambios del proyecto')


@then("el sistema retornara todos los proyectos con su nombre y descripcion")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    respuesta = "nombre"

    assert (respuesta in context.response)


@then("el sistema almacenara un nuevo modulo en el proyecto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then el sistema almacenara un nuevo modulo en el proyecto')


@step("contiene modulos")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And contiene modulos')


@then("el sistema eliminara el modulo del proyecto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then el sistema eliminara el modulo del proyecto')


@when('envio una peticion get a la siguiente "{url}"')
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    """
    session = requests.Session()
    response = session.get(url=context.api_url + url)
    context.proyecto = json.loads(response.text)


@given("un {proyecto} existente")
def step_impl(context, proyecto):
    """
    :type context: behave.runner.Context
    :type proyecto: str
    """
    raise NotImplementedError(u'STEP: Given un <proyecto> existente')


@given("esta la aplicacion arriba")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.api_url = 'http://localhost:8080'


@when('envio una peticion a la siguiente url "{recurso}"')
def step_impl(context, recurso):
    """
    :type context: behave.runner.Context
    :type recurso: string
    """
    url = context.api_url + recurso
    session = requests.Session()
    response = session.get(url=url)
    context.response = response.text


@when('el usuario regular desee "actualizar" un proyecto con {nombre_proyecto} y {descripcion_proyecto}')
def step_impl(context, nombre_proyecto, descripcion_proyecto):
    """
    :type context: behave.runner.Context
    :type nombre_proyecto: str
    :type descripcion_proyecto: str
    """
    raise NotImplementedError(
        u'STEP: When el usuario regular desee "actualizar" un proyecto con <nombre_proyecto> y <descripcion_proyecto>')


@when(
    'envio una peticion a la siguiente url "dummy_url" para crear modulos del {proyecto} con los datos {nombre_modulo} y {descripcion_modulo}')
def step_impl(context, proyecto, nombre_modulo, descripcion_modulo):
    """
    :type context: behave.runner.Context
    :type proyecto: str
    :type nombre_modulo: str
    :type descripcion_modulo: str
    """
    raise NotImplementedError(
        u'STEP: When envio una peticion a la siguiente url "dummy_url" para crear modulos del <proyecto> con los datos <nombre_modulo> y <descripcion_modulo>')


@when('envio una peticion a la siguiente url "dummy_url" <proyecto>')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When envio una peticion a la siguiente url "dummy_url" <proyecto>')


@when('el usuario regular desee "actualizar" un modulo con {nombre_modulo} y {descripcion_modulo}')
def step_impl(context, nombre_modulo, descripcion_modulo):
    """
    :type context: behave.runner.Context
    :type nombre_modulo: str
    :type descripcion_modulo: str
    """
    raise NotImplementedError(
        u'STEP: When el usuario regular desee "actualizar" un modulo con <nombre_modulo> y <descripcion_modulo>')


@then("el sistema almacenara los cambios del modulo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then el sistema almacenara los cambios del modulo')


@then("el sistema retornara el modulo asociado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: el sistema retornara el modulo asociado')


@when(
    'envio una peticion a la siguiente url "dummy_url" para crear funciones del {nombre_modulo} con los datos {nombre_funcion}, {numero_campos}, {numero_objetos} y {formula_cliente}')
def step_impl(context, nombre_modulo, nombre_funcion, numero_campos, numero_objetos, formula_cliente):
    """
    :type context: behave.runner.Context
    :type nombre_modulo: str
    :type nombre_funcion: str
    :type numero_campos: int
    :type numero_objetos: int
    :type formula_cliente: str
    """
    raise NotImplementedError(
        u'STEP: When envio una peticion a la siguiente url "dummy_url" para crear funciones del <nombre_modulo> con los datos <nombre_funcion>, <numero_campos>, <numero_objetos> y <formula_cliente>')


@then("el sistema almacenara una funcion asociada a el modulo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then el sistema almacenara una funcion asociada a el modulo')


@step("contiene funciones")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And contiene funciones')


@when(
    'el usuario regular desee "actualizar" una funcion con {nombre_funcion}, {numero_campos}, {numero_objetos} y {formula_cliente}')
def step_impl(context, nombre_funcion, numero_campos, numero_objetos, formula_cliente):
    """
    :type context: behave.runner.Context
    :type nombre_funcion: str
    :type numero_campos: int
    :type numero_objetos: int
    :type formula_cliente: str
    """
    raise NotImplementedError(
        u'STEP: When el usuario regular desee "actualizar" una funcion con <nombre_funcion>, <numero_campos>, <numero_objetos> y <formula_cliente>')


@then("el sistema almacenara los cambios de la funcion")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then el sistema almacenara los cambios de la funcion')


@when('envio una peticion a la siguiente url "dummy_url" <nombre_modulo>')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When envio una peticion a la siguiente url "dummy_url" <nombre_modulo>')


@then("el sistema eliminara la funcion del modulo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then el sistema eliminara la funcion del modulo')


@given("tengo la lista de proyectos")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    url = "http://localhost:8080/proyectos"
    context.api_url = url
    session = requests.Session()
    response = session.get(url=url)
    context.proyectos = json.loads(response.text)["proyectos"]
