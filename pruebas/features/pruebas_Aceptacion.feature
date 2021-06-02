Feature: App de estimacion

  Scenario Outline: Como usuario regular quiero crear un proyecto para manejar el proceso de estimación
    Given la <url> para la creacion
    When el usuario regular desee "crear" un proyecto con <nombre_proyecto> y <descripcion_proyecto>
    Then el sistema almacenara un nuevo proyecto

    Examples: proyectos
      | nombre_proyecto | descripcion_proyecto        |
      | proyecto1       | Este es el super proyecto 1 |
      | proyecto2       | Este es el super proyecto 2 |
      | proyecto3       | Este es el super proyecto 3 |
      | proyecto4       | Este es el super proyecto 4 |

  Scenario Outline: Como usuario regular quiero consultar un proyecto por id para ver sus módulos y funciones
    Given un <proyecto> existente
    When envio una peticion a la siguiente "url"
    Then el sistema retornara el proyecto con sus modulos y funciones

    Examples: proyectos
      | proyecto |
      | 1        |
      | 2        |
      | 3        |
      | 4        |

  Scenario Outline: Como usuario regular quiero actualizar el nombre y la descripción de un proyecto para manejar el proceso de estimación
    Given un <proyecto> existente
    When el usuario regular desee "actualizar" un proyecto con <nombre_proyecto> y <descripcion_proyecto>
    Then el sistema almacenara los cambios del proyecto

    Examples: actualizacion
      | proyecto | nombre_proyecto      | descripcion_proyecto                    |
      | 1        | proyecto1Actualizado | Este es el super proyecto 1 actualizado |
      | 2        | proyecto2Actualizado | Este es el super proyecto 2 actualizado |
      | 3        | proyecto3Actualizado | Este es el super proyecto 3 actualizado |
      | 4        | proyecto4Actualizado | Este es el super proyecto 4 actualizado |

  Scenario: Como usuario regular quiero ver el listado de proyectos para consultar su nombre y descripcion.
    Given esta la aplicacion arriba
    When envio una peticion a la siguiente url "get_all"
    Then el sistema retornara todos los proyectos con su nombre y descripcion

  Scenario Outline: Como usuario regular quiero crear un módulo para asociarlo a un proyecto
    Given un <proyecto> existente
    When envio una peticion a la siguiente url "dummy_url" para crear modulos del <proyecto> con los datos <nombre_modulo> y <descripcion_modulo>
    Then el sistema almacenara un nuevo modulo en el proyecto
    Examples: actualizacion
      | proyecto | nombre_modulo | descripcion_modulo               |
      | 1        | modulo1Prueba | Este es el super modulo 1 creado |
      | 2        | modulo2Prueba | Este es el super modulo 2 creado |
      | 3        | modulo3Prueba | Este es el super modulo 3 creado |
      | 4        | modulo4Prueba | Este es el super modulo 4 creado |

  Scenario: Como usuario regular quiero borrar el módulo asociado a un proyecto por Id para eliminar todas las funciones asociadas
    Given un <proyecto> existente
    And contiene modulos
    When envio una peticion a la siguiente url "dummy_url" <proyecto>
    Then el sistema eliminara el modulo del proyecto


  Scenario Outline: Como usuario regular quiero actualizar el nombre y descripción del módulo asociado a un proyecto
    Given un <proyecto> existente
    And contiene modulos
    When el usuario regular desee "actualizar" un modulo con <nombre_modulo> y <descripcion_modulo>
    Then el sistema almacenara los cambios del modulo

    Examples: actualizacion
      | proyecto | nombre_modulo            | descripcion_modulo                          |
      | 1        | modulo1PruebaActualizado | Este es el super modulo 1 creado Actualizado|
      | 2        | modulo2PruebaActualizado | Este es el super modulo 2 creado Actualizado|
      | 3        | modulo3PruebaActualizado | Este es el super modulo 3 creado Actualizado|
      | 4        | modulo4PruebaActualizado | Este es el super modulo 4 creado Actualizado|

Scenario: Como usuario regular quiero consultar el módulo asociado a un proyecto por su Id
    Given un <proyecto> existente
    And contiene modulos
    When envio una peticion a la siguiente url "dummy_url" <proyecto>
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


Scenario Outline: Como usuario regular quiero actualizar una función asociada a un módulo para almacenar el nombre de la función, número de campos, número de objetos y calcular la complejidad basado en la fórmula dada por el cliente
    Given un <nombre_modulo> existente
    And contiene funciones
    When el usuario regular desee "actualizar" una funcion con <nombre_funcion>, <numero_campos>, <numero_objetos> y <formula_cliente>
    Then el sistema almacenara los cambios de la funcion
    Examples: actualizacion
      | nombre_modulo | nombre_funcion            | numero_campos            | numero_objetos            | formula_cliente            |
      | modulo1       | funcion1PruebaActualizado | n_campos1Actualizado     | n_objetos1Actualizado     | formula1Actualizado        |
      | modulo2       | funcion2PruebaActualizado | n_campos2Actualizado     | n_objetos2Actualizado     | formula2Actualizado        |
      | modulo3       | funcion3PruebaActualizado | n_campos3Actualizado     | n_objetos3Actualizado     | formula3Actualizado        |
      | modulo4       | funcion4PruebaActualizado | n_campos4Actualizado     | n_objetos3Actualizado     | formula4Actualizado        |

