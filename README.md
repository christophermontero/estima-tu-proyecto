# Estima tu Proyecto

![](https://img.shields.io/github/issues/christophermontero/estima-tu-proyecto)
![](https://img.shields.io/github/issues-pr-closed/christophermontero/estima-tu-proyecto)
![](https://img.shields.io/github/last-commit/christophermontero/estima-tu-proyecto)

## Tabla de contenidos:

- [Estima tu Proyecto](#estima-tu-proyecto)
  - [Tabla de contenidos:](#tabla-de-contenidos)
  - [Descripción del proyecto](#descripción-del-proyecto)
    - [Primera iteración](#primera-iteración)
    - [Endpoints del API](#endpoints-del-api)
    - [Modelos de datos](#modelos-de-datos)
  - [Guía de usuario](#guía-de-usuario)
  - [Guía de instalación](#guía-de-instalación)
    - [Dependencias](#dependencias)
  - [Requerimientos](#requerimientos)
  - [Cómo contribuir](#cómo-contribuir)
  - [Autores](#autores)
  - [Licencia](#licencia)


## Descripción del proyecto
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

## Guía de usuario
Explica los pasos básicos sobre cómo usar la herramienta digital. Es una buena sección para mostrar capturas de pantalla o gifs que ayuden a entender la herramienta digital.

## Guía de instalación
Paso a paso de cómo instalar la herramienta digital. En esta sección es recomendable explicar la arquitectura de carpetas y módulos que componen el sistema.

Según el tipo de herramienta digital, el nivel de complejidad puede variar. En algunas ocasiones puede ser necesario instalar componentes que tienen dependencia con la herramienta digital. Si este es el caso, añade también la siguiente sección.

La guía de instalación debe contener de manera específica:
- Los requisitos del sistema operativo para la compilación (versiones específicas de librerías, software de gestión de paquetes y dependencias, SDKs y compiladores, etc.).
- Las dependencias propias del proyecto, tanto externas como internas (orden de compilación de sub-módulos, configuración de ubicación de librerías dinámicas, etc.).
- Pasos específicos para la compilación del código fuente y ejecución de tests unitarios en caso de que el proyecto disponga de ellos.

### Dependencias
Descripción de los recursos externos que generan una dependencia para la reutilización de la herramienta digital (librerías, frameworks, acceso a bases de datos y licencias de cada recurso). Es una buena práctica describir las últimas versiones en las que ha sido probada la herramienta digital.

    Puedes usar este estilo de letra diferenciar los comandos de instalación.

## Requerimientos

Para instalar los requerimientos utilice el siguiente comando:

```
pip install -r requirements.txt
```


## Cómo contribuir
Los issues abiertos, los errores y las solicitudes de funciones se enumeran en la pestaña de _Issues_ y se etiquetan en consecuencia.

Vea el archivo [CONTRIBUTING.md](CONTRIBUTING.md) para conocer la guía de estilo y cómo contribuir.



## Autores
- [Christopher Ortiz Montero](https://github.com/christophermontero)
- [Alvaro Varón](https://github.com/alxvaron)
- [Carlos Andres Uriza](https://github.com/caurizaf)
- [Christian Camilo Lopez](https://github.com/cclopezp)
- [Carlos Andres Bautista](https://github.com/darkclassiccarlos)
- [David Guillermo Galvis](https://github.com/davidggalvises)
- [Edwar Arturo Rodriguez](https://github.com/edwarod)
- [Fabio Andres Bombiela](https://github.com/fbombi13)
- [Joaquin Caicedo Navarro](https://github.com/joaquincaicedonavarro)
- [Jonathan Steven Capera](https://github.com/JocoolQ)
- [José Sebastian Cañón](https://github.com/jscanon)
- [Daniel David Leal](https://github.com/lealdaniel00)
- [Sabrina Suarez Arrieta](https://github.com/sabrinasuarezarrieta)
- [Sebastian Camilo Vanegas](https://github.com/SCVA)
- [William Carpeta](https://github.com/wakoagui)
- [Alejandro Daza](https://github.com/apdaza)

## Licencia
Este proyecto es de código abierto y está disponible bajo la [Licencia MIT](http://opensource.org/licenses/mit-license.php).
