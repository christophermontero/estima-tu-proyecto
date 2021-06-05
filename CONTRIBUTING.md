# Cómo contribuir

Para crear un _pull request_, siga las instrucciones de GitHub en como [crear un _pull request_](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request). No olvidar siempre vincular tu _pull request_ a un _Issue_ existente.

## Tecnologías

Este proyecto es posible gracias a todos estos lenguajes, bibliotecas y _frameworks_ de código abierto.
| Tecnología                                                            | Descripción                                                                           |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| [Flask](https://flask.palletsprojects.com/en/2.0.x/)                  | Flask es un framework de aplicaciones web ligero                                      |
| [Flask-alchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) | Es una extensión para Flask que agrega soporte para SQLAlchemy                        |
| [Pytest](https://docs.pytest.org/en/6.2.x/)                           | Framework que facilita la escritura de pequeñas pruebas                               |
| [Behave](https://behave.readthedocs.io/en/stable/)                    | Es un desarrollo dirigido por el comportamiento                                       |
| [Docker](https://docs.docker.com/)                                    | Es una plataforma abierta para desarrollar y ejecutar aplicaciones                    |
| [Docker-compose](https://docs.docker.com/compose/)                    | Es una herramienta para definir y ejecutar aplicaciones Docker de varios contenedores |

## Guía de estilo
Las convenciones de codificación están sujetas a [PEP8](https://www.python.org/dev/peps/pep-0008/)

- Los nombres de los módulos y paquetes deberán usar minúsculas y los espacios entre palabras con guión bajo (_snake_case_).
- Los nombres de las clases deberán usar la primer letra de cada palabra en mayúscula (_PascalCase_).
- Las excepciones al ser clases deberán usar _PascalCase_ iniciado siempre con la palabra Error.
- Los nombres de las funciones y los métodos deberán usar minúsculas y los espacios entre palabras con guión bajo (_snake_case_).

## Nomenclatura para las ramas de desarrollo
- Rama principal: master
- Rama de desarrollo: develop
- Ramas para nuevas características: feature-#issue
- Rama para documentación: doc-#issue
- Rama para pruebas: test-#issue
- Rama para trabajo en curso: wip-#issue
