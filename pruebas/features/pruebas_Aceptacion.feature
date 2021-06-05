Feature: App de estimacion

  Scenario Outline: Como usuario regular quiero crear un proyecto para manejar el proceso de estimación
    Given la "/proyectos" para la creacion
    When el usuario regular desee "crear" un proyecto con <id> <nombre_proyecto> y <descripcion_proyecto>
    Then el sistema almacenara un nuevo proyecto

    Examples: proyectos
      | id | nombre_proyecto | descripcion_proyecto        |
      | 10 | proyecto1       | Este es el super proyecto 1 |
      | 2  | proyecto2       | Este es el super proyecto 2 |
      | 3  | proyecto3       | Este es el super proyecto 3 |
      | 4  | proyecto4       | Este es el super proyecto 4 |

  Scenario: Como usuario regular quiero consultar un proyecto por id para ver sus módulos y funciones
    Given tengo la lista de proyectos
    When envio una peticion get a la siguiente "/proyectos"
    Then el sistema retornara el proyecto con sus modulos y funciones

  Scenario: Como usuario regular quiero ver el listado de proyectos para consultar su nombre y descripcion.
    Given esta la aplicacion arriba
    When envio una peticion a la siguiente url "/proyectos"
    Then el sistema retornara todos los proyectos con su nombre y descripcion

  Scenario Outline: Como usuario regular quiero crear un módulo para asociarlo a un proyecto
    Given el link para crear modulos
    When envio una peticion crear modulos del <proyecto> con los datos <modulo> , <nombre_modulo> y <descripcion_modulo>
    Then el sistema almacenara un nuevo modulo en el proyecto
    Examples: actualizacion
      | proyecto | modulo | nombre_modulo | descripcion_modulo               |
      | 10       | 1      | modulo1Prueba | Este es el super modulo 1 creado |
      | 2        | 2      | modulo2Prueba | Este es el super modulo 2 creado |
      | 3        | 3      | modulo3Prueba | Este es el super modulo 3 creado |
      | 4        | 4      | modulo4Prueba | Este es el super modulo 4 creado |

  Scenario: Como usuario regular quiero borrar el módulo asociado a un proyecto por Id para eliminar todas las funciones asociadas
    Given un modulo 1 del proyecto 10
    When llamo el metodo borrar modulo
    Then el sistema eliminara el modulo del proyecto

    #---------------------------------------------------------------------------------------------------
  Scenario: Como usuario regular quiero consultar el módulo asociado a un proyecto por su Id
    Given un modulo existente dentro de un proyecto 45
    When envio una peticion a la siguiente url de modulos
    Then el sistema retornara el modulo asociado

  Scenario Outline: Como usuario regular quiero crear una función asociada a un módulo para almacenar el nombre de la función, número de campos, número de objetos y calcular la complejidad basado en la fórmula dada por el cliente
    Given el link de crear funciones
    When envio una peticion para crear funciones con <idFuncion>,<nombreFuncion>,<numCampos>,<numObjetos>,<modulo_id>
    Then el sistema almacenara una funcion asociada a el modulo
    Examples: actualizacion
      | idFuncion | nombreFuncion  | numCampos | numObjetos | modulo_id |
      | 10        | funcion1Prueba | 15        | 5          | 2         |
      | 2         | funcion2Prueba | 16        | 6          | 2         |
      | 3         | funcion3Prueba | 1         | 2          | 2         |
      | 4         | funcion4Prueba | 2         | 3          | 2         |

  Scenario Outline: Como usuario regular quiero eliminar una función asociada a un módulo para depurar o refactorizar funciones
    Given el link de borrar funciones <idFuncion>
    When envio una peticion delete para la url
    Then el sistema eliminara la funcion del modulo
    Examples: actualizacion
      | idFuncion |
      | 10        |
      | 2         |
      | 3         |
      | 4         |