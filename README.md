# Estima tu Proyecto

![](https://img.shields.io/github/issues/christophermontero/estima-tu-proyecto)
![](https://img.shields.io/github/issues-pr-closed/christophermontero/estima-tu-proyecto)
![](https://img.shields.io/github/last-commit/christophermontero/estima-tu-proyecto)

## Tabla de contenidos:

- [Estima tu Proyecto](#estima-tu-proyecto)
  - [Tabla de contenidos:](#tabla-de-contenidos)
  - [Descripción del proyecto](#descripción-del-proyecto)
    - [Primera iteración](#primera-iteración)
    - [Rutas del API](#rutas-del-api)
    - [Modelos de datos](#modelos-de-datos)
  - [Guía de usuario](#guía-de-usuario)
  - [Guía de instalación](#guía-de-instalación)
    - [Requerimientos](#requerimientos)
  - [Cómo contribuir](#cómo-contribuir)
  - [Autores](#autores)
  - [Licencia](#licencia)

## Descripción del proyecto
Este es un proyecto académico, para la asignatura de ingeniería de software I de la Universidad Distrital Francisco José de Caldas

### Primera iteración
Calcular la complejidad de un proyecto basado en la cantidad de campos y objetos contenidos en cada módulo; es necesario persistir la información, sin embargo, no deberá tener autorización ni autenticación, por lo que sólo se usará un rol genérico.

### Rutas del API
```
* Proyecto: http://localhost:8080/proyectos
* Módulos: http://localhost:8080/modulos
* Funciones: http://localhost:8080/funciones
```

### Modelos de datos
* proyecto:
  * idProyecto INTEGER NOT NULL,
  * nombreProyecto VARCHAR(50),
  * descProyecto VARCHAR(150),
  * PRIMARY KEY (idProyecto)
* modulo:
  * idModulo INTEGER NOT NULL,
  * nombreModulo VARCHAR(50),
  * descModulo VARCHAR(150),
  * proyecto_id INTEGER,
  * RIMARY KEY (idModulo),
  * FOREIGN KEY(proyecto_id) REFERENCES proyecto (idProyecto)
* funcion:
  * idFuncion INTEGER NOT NULL,
  * nombreFuncion VARCHAR(50),
  * numCampos INTEGER,
  * numObjetos INTEGER,
  * complejidad VARCHAR(8),
  * modulo_id INTEGER,
  * PRIMARY KEY (idFuncion),
  * FOREIGN KEY(modulo_id) REFERENCES modulo (idModulo)

## Guía de usuario
Descripción de las carpetas y archivos del proyecto

```bash
├── funciones/                 # Servicio de funciones
│   ├── app.py                 # Punto de entrada del API
│   ├── db.py                  # Configuración de la base de datos
│   ├── model.py               # Definición del modelo de datos relacional
│   ├── requirements.txt       # Dependencias del proyecto
│   ├── Dockerfile             # Construcción de la imagen de docker
│   └── .dockerignore          # Archivos para ser ignorados en la compilación del contenedor
├── modulos/                   # Servicio de modulos
│   ├── app.py                 # Punto de entrada del API
│   ├── db.py                  # Configuración de la base de datos
│   ├── model.py               # Definición del modelo de datos relacional
│   ├── requirements.txt       # Dependencias del proyecto
│   ├── Dockerfile             # Construcción de la imagen de docker
│   └── .dockerignore          # Archivos para ser ignorados en la compilación del contenedor
├── proyectos/                 # Servicio de proyectos
│   ├── app.py                 # Punto de entrada del API
│   ├── db.py                  # Configuración de la base de datos
│   ├── model.py               # Definición del modelo de datos relacional
│   ├── requirements.txt       # Dependencias del proyecto
│   ├── Dockerfile             # Construcción de la imagen de docker
│   └── .dockerignore          # Archivos para ser ignorados en la compilación del contenedor
├── pruebas/                   # Pruebas de aceptación
│   ├── features/              # Definición de las características
│      ├── pruebas_aceptación  # Definición de las características
│   ├── steps/                 # Definición de los pasos
├── sqlite3/                   # Punto de montaje de la base de datos
│   ├── estima.db              # Definición de la base de datos
├── .gitignore                 # Carpetas y archivos para ingnorar en el repositorio
├── CONTRIBUTING.md            # Reglas para contribuir al proyecto
├── docker-compose.yml         # Instrucciones para construir todos los servicios
├── LICENSE                    # Definición del a licencia MIT
├── nginx.conf                 # Definición de los proxy_pass
└── README.md                  # Descripción del proyecto
```

Puede consultar la documentación del API [aquí](https://documenter.getpostman.com/view/7032390/TzY4gb3F)

## Guía de instalación
Clonar el repositorio y construir los contenedores.

```bash
git clone https://github.com/christophermontero/estima-tu-proyecto.git
cd estima-tu-proyecto
docker-compose up --build -d
```

### Requerimientos

    docker
    docker-compose

## Cómo contribuir
Los issues abiertos, los errores y las solicitudes de funciones se enumeran en la pestaña de _Issues_ y se etiquetan en consecuencia.

Vea el archivo [CONTRIBUTING.md](CONTRIBUTING.md) para conocer la guía de estilo y cómo contribuir.

## Autores
- [Christopher Ortiz Montero](https://github.com/christophermontero)
- [Alvaro Varón](https://github.com/alxvaron)
- [Carlos Andres Uriza](https://github.com/caurizaf)
- [Cristhian Camilo Lopez](https://github.com/cclopezp)
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
- [William Aguirre Carpeta](https://github.com/wakoagui)
- [Alejandro Daza](https://github.com/apdaza)
- [Luis Morales] (https://github.com/luisemo)
## Licencia
Este proyecto es de código abierto y está disponible bajo la [Licencia MIT](http://opensource.org/licenses/mit-license.php).
