# qGrover

[![License: Apache][license-shield]][license-url]

*Read this in other languages: [English](README.md), [Spanish](README.es.md).*

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Contributors](#contributors)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)
* [Credits](#credits)



<!-- ABOUT THE PROJECT -->
## About The Project

Development and testing project on the performance of Grover's algorithm compared to other search algorithms, this project was developed during the [Qiskit Hackathon Bilbao 2019](https://github.com/qiskit-community/qiskit-hackathon-bilbao-19).

There is a brief explanation in this Elevator Pitch in [PowerPoint](presentacion/pGrover-ElevatorPitch.pptx) 
or [pdf](presentacion/pGrover-ElevatorPitch.pdf).

**Update:** we won [second place](https://www.ilb.eus/es/bilbao-quantum-computing-hackathon-2019/) in our category :D
### Built With
* [Qiskit](https://qiskit.org/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)

<!-- CONTRIBUTORS -->
## Contributors

Thanks to the [support staff](#acknowledgements) that helped with the theoretical content and with Qiskit language:

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
## Getting Started

To get a local copy up and running follow these simple example steps:

### Prerequisites
* python3
* python3-dev
#### Windows
Download and install Python from this [link](https://www.python.org/downloads/windows/)
#### Linux
```sh
sudo apt install python3 python3-dev
```

### Installation

1. Clone the repository
```sh
git clone https://github.com/oierajenjo/q-Grover-Algorithm
```

2. Install Python packages
#### Windows
```sh
pip install -r requirements.txt
```
#### Linux
```sh
sudo pip3 install -r requirements.txt
```

3. You may need to configure additional settings in the settings.py file like db or localizations.


<!-- USAGE EXAMPLES -->
## Usage
### Demo

You can run an interactive Demo from the [qGrover](qGrover) folder as a normal Django application.

Note: _For more information, please refer to the [Offical Documentation](https://www.djangoproject.com/start/)._

### Performance
The performance graphs have been made with the tools in the [algorithm_comparison](algorithm_comparison) folder.

To make a test, run the file [comparisons.py](algorithm_comparison/comparisons.py).

<!-- CONTRIBUTING -->
## Contributing

Feel free to open pull requests with new features or bug fixes. Any contributions you make are **greatly appreciated**.

As the license states, you can fork and even redistribute this as long as it remains as a GPL project. 


<!-- LICENSE -->
## License

Distributed under the Apache License. See [`LICENSE`](LICENSE) for more information.


<!-- CONTACT -->
## Contact

If you are not that tech savvy feel free to ask us any questions via email, just keep in mind we might not know 
the answer to your questions as we did this in a Hackathon and we are not experts in this area.


## Acknowledgements

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


## Credits

- Bootstrap Template based on [Gentelella](https://github.com/ColorlibHQ/gentelella) by Colorlib



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/badge/License-Apache%202.0-orange.svg
[license-url]: https://github.com/oierajenjo/q-Grover-Algorithm/blob/master/LICENSE



