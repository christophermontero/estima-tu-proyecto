Feature: Como usuario regular quiero eliminar una función asociada a un módulo para depurar o refactorizar funciones

  Scenario: Crear un objeto
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!

  Scenario: Borrar un objeto
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!

  Scenario Outline: ajiaco un objeto
    Given we have behave installed <x>
    When we implement a test
    Then behave will test it for us!

    Examples: valores
      | x |
      | 1 |
      | 2 |
      | 3 |
      | 4 |