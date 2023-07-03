<!-- PROJECT SHIELDS -->
[![PyTest][pytest]][pytest-url]
[![PyLint][pylint]][pylint-url]
[![GPages][gpages]][gpages-url]

<!-- PROJECT LOGO -->
<br />
<div align="center" id="readme-top">
  <a href="https://github.com/dariustb/vibebeyond">
    <img src="https://i1.sndcdn.com/artworks-nXTBoQMnJHSoNPbn-yX34xA-t500x500.jpg" alt="Logo" width="100" height="100">
  </a>

  <h1 align="center">Vibe Beyond</h1>

  <p align="center">
    AI-generated lofi hip-hop radio
    <br />
    <a href="https://dariustb.github.io/VibeBeyond/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dariustb/vibebeyond/issues">Report Bug</a>
    ·
    <a href="https://github.com/dariustb/vibebeyond/issues">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
Welcome to the world of lofi hip hop! Our radio station is unique in that it generates its music in real-time using Python through Pygame. Linh and myself have built a custom algorithm that creates a relaxing, soothing soundscape that's perfect for studying, working, or simply unwinding.

Our code generates a continuous stream of music that's never the same twice, ensuring that our listeners always have a fresh and unique experience. We've designed our platform to be accessible and easy to use, with a sleek and intuitive interface that lets you customize your listening experience to suit your preferences.

At our core, we're passionate about music and technology, and we're committed to pushing the boundaries of what's possible with code. Whether you're a fan of lofi hip hop or simply curious about the intersection of music and programming, we invite you to join us on this journey of exploration and discovery!

_Please [refer to the documentation][docs] for the full breakdown and logic explanation of the app._

### Built With
* ![Python][python.io]

### Prerequisites

* [VS Code][vscode] (1.76.2 or greater)
* [Python 3][python] (3.11.0 or greater)
  * [pip 3][python] (versions 22.3 - 23.0.1)

### Install Dependencies
```sh
pip install -r requirements.txt
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Usage
```sh
python src/app.py
```
### Local Development
#### Unit Test
```sh
python -m pytest
```
#### Linting Test
```sh
pylint src/ tests/
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[app]:  #
[docs]: https://dariustb.github.io/VibeBeyond/

<!-- Technologies -->
[vscode]:   https://code.visualstudio.com/
[python]:   https://www.python.org/

<!-- Featured images -->
[product-screenshot]:   #

<!-- CI Test badges -->
[pytest]:   https://github.com/dariustb/VibeBeyond/actions/workflows/pytest.yml/badge.svg
[pylint]:   https://github.com/dariustb/VibeBeyond/actions/workflows/pylint.yml/badge.svg
[gpages]:   https://github.com/dariustb/VibeBeyond/actions/workflows/pages/pages-build-deployment/badge.svg 
[pytest-url]:   https://github.com/dariustb/VibeBeyond/actions/workflows/pytest.yml
[pylint-url]:   https://github.com/dariustb/VibeBeyond/actions/workflows/pylint.yml
[gpages-url]:   https://github.com/dariustb/VibeBeyond/actions/workflows/pages/pages-build-deployment

<!-- Markdown Badges -->
[python.io]:    https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
