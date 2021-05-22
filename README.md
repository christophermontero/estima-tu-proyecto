# Estima tu Proyecto

![](https://img.shields.io/github/issues/christophermontero/estima-tu-proyecto)
![](https://img.shields.io/github/issues-pr-closed/christophermontero/estima-tu-proyecto)
![](https://img.shields.io/github/last-commit/christophermontero/estima-tu-proyecto)

## Descripción de proyecto
Este es un proyecto académico, para la asignatura de ingeniería de software I de la Universidad Distrital Francisco José de Caldas

### Primera iteración
Calcular la complejidad de un proyecto basado en la cantidad de campos y objetos contenidos en cada módulo; es necesario persistir la información, sin embargo, no deberá tener autorización ni autenticación, por lo que sólo se usará un rol genérico.

### Endpoints del API
* Proyecto
* Módulos
* Funciones
* Campos
* Parámetros

### Modelos de datos
* Proyecto:
  * Id proyecto
  * Nombre proyecto
  * Descripción del proyecto
* Módulo:
  * Id proyecto
  * Id módulo
  * Nombre módulo
  * Descripción del módulo
* Función:
  * Id módulo
  * Id función
  * Nombre función
  * Número de campos
  * Número de objetos
  * Complejidad

