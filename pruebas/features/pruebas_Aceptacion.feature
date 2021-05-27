Feature: Aplicacion

  Scenario: Como usuario regular quiero crear un proyecto para manejar el proceso de estimación
    Given esta la aplicacion arriba
    When envio una peticion a la siguiente url "dummy_url"
    Then el sistema almacenara un nuevo proyecto