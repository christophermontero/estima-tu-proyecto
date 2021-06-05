import random
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


def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))


@when('el usuario regular desee "crear" un proyecto con {id} {nombre_proyecto} y {descripcion_proyecto}')
def step_impl(context, id, nombre_proyecto, descripcion_proyecto):
    """
    :type context: behave.runner.Context
    :type nombre_proyecto: str
    :type descripcion_proyecto: str
    """
    url = context.api_url + context.resource

    body = {
        "idProyecto": id,
        "nombreProyecto": nombre_proyecto,
        "descProyecto": descripcion_proyecto
    }
    session = requests.Session()
    response = session.get(url=url)

    context.size = len(json.loads(response.text)["proyectos"])
    headers = {'Content-Type': 'application/json',
               'Accept': '*/*',
               'Connection': 'keep-alive',
               'Accept-Encoding': 'gzip, deflate, br'
               }
    req = requests.Request('POST', url, headers=headers, json=body)
    prepared = req.prepare()
    pretty_print_POST(prepared)
    response = session.send(prepared)


@then("el sistema retornara el proyecto con sus modulos y funciones")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.proyecto_info["proyecto"]["idProyecto"] == context.id_proyecto


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
    assert (context.proyectos is not None)


@then("el sistema almacenara un nuevo modulo en el proyecto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    obtener_modulos_proyecto = f"http://localhost:8080/modulos/{context.proyecto}"
    session = requests.Session()

    response = session.get(url=obtener_modulos_proyecto)
    tamano_actual = len(json.loads(response.text)["modulos"])
    assert tamano_actual - context.size is 1


@then("el sistema eliminara el modulo del proyecto")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    session = requests.Session()
    obtener_modulos_proyecto = f"http://localhost:8080/modulos/{context.id_proyecto}"

    response = session.get(url=obtener_modulos_proyecto)
    tamano_actual = len(json.loads(response.text)["modulos"])
    assert tamano_actual - context.size is -1


@when('envio una peticion get a la siguiente "{url}"')
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    """
    id_proyecto = random.choice(context.proyectos)['idProyecto']
    context.id_proyecto = id_proyecto
    url_get_all = f"http://localhost:8080/proyectos/{id_proyecto}"
    session = requests.Session()
    response = session.get(url=url_get_all)
    context.proyecto_info = json.loads(response.text)


@given("un {proyecto} existente")
def step_impl(context, proyecto):
    """
    :type context: behave.runner.Context
    :type proyecto: str
    """
    url = "http://localhost:8080/proyecto/1"
    context.api_url = url
    session = requests.Session()
    response = session.get(url=url)
    proyectos = json.loads(response.text)["proyectos"]


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
    context.proyectos = json.loads(response.text)["proyectos"]


@when('el usuario regular desee "actualizar" un proyecto con {nombre_proyecto} y {descripcion_proyecto}')
def step_impl(context, nombre_proyecto, descripcion_proyecto):
    """
    :type context: behave.runner.Context
    :type nombre_proyecto: str
    :type descripcion_proyecto: str
    """
    raise NotImplementedError(
        u'STEP: When el usuario regular desee "actualizar" un proyecto con <nombre_proyecto> y <descripcion_proyecto>')


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
    t = json.loads(context.response)
    assert t["modulos"] is not None


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


@given("un modulo existente dentro de un proyecto {id_proyecto}")
def step_impl(context, id_proyecto):
    """
    :type context: behave.runner.Context
    """
    url = f"http://localhost:8080/modulos/{id_proyecto}"
    context.url = url


@when("envio una peticion a la siguiente url de modulos")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    url = context.url
    session = requests.Session()
    response = session.get(url=url)
    context.response = response.text


@given("el link para crear modulos")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.url = "http://localhost:8080/modulos"


@when("envio una peticion crear modulos del {proyecto} con los datos {modulo} , {nombre_modulo} y {descripcion_modulo}")
def step_impl(context, proyecto, modulo, nombre_modulo, descripcion_modulo):
    """
    :type context: behave.runner.Context
    """
    context.proyecto = proyecto
    body = {
        "idModulo": modulo,
        "nombreModulo": nombre_modulo,
        "descModulo": descripcion_modulo,
        "proyecto_id": proyecto
    }
    obtener_modulos_proyecto = f"http://localhost:8080/modulos/{proyecto}"
    session = requests.Session()
    response = session.get(url=obtener_modulos_proyecto)
    print(response)
    context.size = len(json.loads(response.text)["modulos"])
    headers = {'Content-Type': 'application/json',
               'Accept': '*/*',
               'Connection': 'keep-alive',
               'Accept-Encoding': 'gzip, deflate, br'
               }
    req = requests.Request('POST', context.url, headers=headers, json=body)
    prepared = req.prepare()
    pretty_print_POST(prepared)
    response = session.send(prepared)


@given("un modulo {id_modulo} del proyecto {id_proyecto}")
def step_impl(context, id_modulo, id_proyecto):
    """
    :type context: behave.runner.Context
    """
    context.id_proyecto = id_proyecto
    context.id_modulo = id_modulo
    obtener_modulos_proyecto = f"http://localhost:8080/modulos/{id_proyecto}"
    session = requests.Session()
    response = session.get(url=obtener_modulos_proyecto)
    context.size = len(json.loads(response.text)["modulos"])


@when("llamo el metodo borrar modulo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    url = f"http://localhost:8080/modulos/{context.id_modulo}"
    session = requests.Session()
    response = session.delete(url=url)
