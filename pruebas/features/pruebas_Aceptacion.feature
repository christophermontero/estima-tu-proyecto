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
    Given un <proyecto> existente
    And contiene modulos
    When envio una peticion a la siguiente url "dummy_url" <proyecto>
    Then el sistema eliminara el modulo del proyecto

    #---------------------------------------------------------------------------------------------------
  Scenario: Como usuario regular quiero consultar el módulo asociado a un proyecto por su Id
    Given un modulo existente dentro de un proyecto 45
    When envio una peticion a la siguiente url de modulos
    Then el sistema retornara el modulo asociado

  Scenario Outline: Como usuario regular quiero crear una función asociada a un módulo para almacenar el nombre de la función, número de campos, número de objetos y calcular la complejidad basado en la fórmula dada por el cliente
    Given un <nombre_modulo> existente
    When envio una peticion a la siguiente url "dummy_url" para crear funciones del <nombre_modulo> con los datos <nombre_funcion>, <numero_campos>, <numero_objetos> y <formula_cliente>
    Then el sistema almacenara una funcion asociada a el modulo
    Examples: actualizacion
      | nombre_modulo | nombre_funcion | numero_campos | numero_objetos | formula_cliente |
      | modulo1       | funcion1Prueba | n_campos1     | n_objetos1     | formula1        |
      | modulo2       | funcion2Prueba | n_campos2     | n_objetos2     | formula2        |
      | modulo3       | funcion3Prueba | n_campos3     | n_objetos3     | formula3        |
      | modulo4       | funcion4Prueba | n_campos4     | n_objetos3     | formula4        |

  Scenario: Como usuario regular quiero eliminar una función asociada a un módulo para depurar o refactorizar funciones
    Given un <nombre_modulo> existente
    And contiene funciones
    When envio una peticion a la siguiente url "dummy_url" <nombre_modulo>
    Then el sistema eliminara la funcion del modulo