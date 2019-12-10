# qGrover

[![License: Apache][license-shield]][license-url]

*Lea esto en otros idiomas: [Inglés](README.md), [Castellano](README.es.md).*

<!-- TABLE OF CONTENTS -->
## Tabla de Contenidos

* [Sobre el proyecto](#sobre-el-proyecto)
  * [Construido con](#construido-con)
* [Colaboradores](#colaboradores)
* [Cómo empezar](#cmo-empezar)
  * [Prerrequisitos](#prerrequisitos)
  * [Instalación](#instalacin)
* [Uso](#uso)
* [Contribuyendo](#contribuyendo)
* [Licencia](#licencia)
* [Contacto](#contacto)
* [Agradecimientos](#agradecimientos)
* [Créditos](#crditos)



<!-- ABOUT THE PROJECT -->
## Sobre el proyecto

Proyecto de desarrollo y pruebas sobre el rendimiento del algoritmo de Grover
en comparación con otros algoritmos de búsqueda.

Hay una breve explicación en este "Elevator Pitch" en [PowerPoint](presentacion/pGrover-ElevatorPitch.pptx) 
o [pdf](presentacion/pGrover-ElevatorPitch.pdf).

### Construido con
* [Qiskit](https://qiskit.org/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)

<!-- CONTRIBUTORS -->
## Colaboradores

Gracias al [personal de apoyo](#agradecimientos) que ayudó con el contenido teórico y con el lenguaje de Qiskit:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/oierajenjo">
        <img src="https://avatars1.githubusercontent.com/u/25632727?s=400&v=4"
        width="150px;" alt="Oier Ajenjo"/><br/><sub><b>Oier Ajenjo</b></sub></a><br/></td>
    <td align="center"><a href="https://github.com/carloslago">
        <img src="https://avatars2.githubusercontent.com/u/15263623?s=400&v=4" 
        width="150px;" alt="Carlos Lago"/><br/><sub><b>Carlos Lago</b></sub></a><br/></td>
    <td align="center"><a href="https://github.com/AlbertoMGV">
        <img src="https://avatars2.githubusercontent.com/u/31722793?s=400&v=4"
        width="150px;" alt="Alberto Miranda"/><br/><sub><b>Alberto Miranda</b></sub></a><br/></td>
    <td align="center"><a href="https://github.com/aitormorais">
        <img src="https://avatars3.githubusercontent.com/u/43671531?s=400&v=4"
         width="150px;" alt="Aitor Morais"/><br/><sub><b>Aitor Morais</b></sub></a><br/></td>
    <td align="center"><a href="https://github.com/rafaelromon">
        <img src="https://avatars0.githubusercontent.com/u/15263554?s=400&v=4" 
        width="150px;" alt="Rafael Romón"/><br /><sub><b>Rafael Romón</b></sub></a><br/></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

<!-- GETTING STARTED -->
## Cómo empezar

Para obtener una copia local en funcionamiento, siga estos sencillos pasos de ejemplo:

### Prerrequisitos
* python3
* python3-dev
#### Windows
Descargue e instale Python desde este [enlace](https://www.python.org/downloads/windows/)
#### Linux
```sh
sudo apt install python3 python3-dev
```

### Instalación

1. Clonar el repositorio
```sh
git clone https://github.com/oierajenjo/q-Grover-Algorithm
```

2. Instalar paquetes de Python
#### Windows
```sh
pip install -r requirements.txt
```
#### Linux
```sh
sudo pip3 install -r requirements.txt
```

3. Es posible que necesite configurar ajustes adicionales en el archivo settings.py como db o localizaciones.


<!-- USAGE EXAMPLES -->
##Uso
### Demo

Puedes ejecutar una Demo interactiva desde la carpeta de [qGrover](qGrover) como una aplicación normal de Django.

_Para más información, consulte la [Documentación Oficial](https://www.djangoproject.com/start/)_

###Rendimiento
Las gráficas de rendimiento se han conseguido con las herramientas de la carpeta [algorithm_comparison](algorithm_comparison).

Para hacer una prueba, ejecutar el fichero [comparisons.py](algorithm_comparison/comparisons.py).


<!-- CONTRIBUTING -->
## Contribuyendo

Siéntase libre de abrir solicitudes pull con nuevas características o correcciones de errores. 
Cualquier contribución que usted haga será muy apreciada.

Como dice la licencia, puedes hacer un fork e incluso redistribuirse mientras siga siendo un proyecto GPL. 


<!-- LICENSE -->
## Licencia

Distribuido bajo la licencia Apache. Vea [`LICENCIA`](LICENSE) para más información.

<!-- CONTACT -->
## Contacto

Si usted no es tan experto en tecnología, siéntase libre de hacernos cualquier pregunta por correo electrónico, 
sólo tenga en cuenta que es posible que no sepamos la respuesta a sus preguntas, ya que lo hicimos en un Hackathon 
y no somos expertos en este área.


## Agradecimientos

<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/VicPinaCanelles">
        <img src="https://avatars0.githubusercontent.com/u/55274463?s=400&v=4"
        width="100px;" alt="Vic Pina"/><br/><sub><b>Vic Pina</b></sub></a><br/></td>
    <td align="center"><a href="https://github.com/amartinfer">
        <img src="https://avatars1.githubusercontent.com/u/7209496?s=400&v=4" 
        width="100px;" alt="Ana Martín"/><br/><sub><b>Ana Martín</b></sub></a><br/></td>
    <td align="center"><a href="https://www.researchgate.net/profile/Giancarlo_Gatti">
        <img src="https://i1.rgstatic.net/ii/profile.image/784553258012674-1564063481856_Q512/Giancarlo_Gatti.jpg"
        width="100px;" alt="Giancarlo Gatti"/><br/><sub><b>Giancarlo Gatti</b></sub></a><br/></td>
  </tr>
</table>


## Créditos

- Plantilla de Bootstrap basada en [Gentelella](https://github.com/ColorlibHQ/gentelella) de Colorlib



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/badge/License-Apache%202.0-orange.svg
[license-url]: https://github.com/oierajenjo/q-Grover-Algorithm/blob/master/LICENSE