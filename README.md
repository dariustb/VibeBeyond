<!-- PROJECT SHIELDS -->
[![PyTest][pytest]][pytest-url]
[![PyLint][pylint]][pylint-url]
[![GPages][gpages]][gpages-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/dariustb/vibebeyond">
    <img src="https://i1.sndcdn.com/artworks-nXTBoQMnJHSoNPbn-yX34xA-t500x500.jpg" alt="Logo" width="100" height="100">
  </a>

  <h1 align="center">Vibe Beyond</h1>

  <p align="center">
    Flask AI-generated lofi hip-hop radio
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
Vibe beyond is an app that'll probably make the anti-creative-AI crowd upset. The application is used to emulate the function of those 24-hour "Lofi Hip-Hop Beats to Study/Chill to" while working with the component of a desktop app to use the user's storage to build (and remove) new songs to stream.

_Please [refer to the documentation][docs] for the full breakdown and logic explanation of the app._

### Built With
* ![Python][python.io]
* ![Flask][flask.io]
* ![Tailwind][tailwind.css]
* ![NPM][npm.io]


### Prerequisites

* [VS Code][vscode] (1.76.2 or greater)
* [npm][npm] (9.2.0 or greater)
* [Python 3][python] (3.11.0 or greater)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Setup
#### Install Dependencies
```sh
# python libraries
pip install -r requirements.txt

# npm packages
npm install

# tailwindCSS
npm run tailwind
```

#### Run App
`python src/app.py`

## Testing
#### Unit Test
`pytest src/`

#### Linting Test
`pylint src/`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[app]:  #
[docs]: https://dariustb.github.io/VibeBeyond/

<!-- Technologies -->
[vscode]:   https://code.visualstudio.com/
[volar]:    https://marketplace.visualstudio.com/items?itemName=Vue.volar
[node]:     https://nodejs.org/en/
[npm]:      https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
[python]:   https://www.python.org/

<!-- Featured images -->
[product-screenshot]:   /docs/assets/images/wf_start.png

<!-- CI Test badges -->
[pytest]:   https://github.com/dariustb/VibeBeyond/actions/workflows/pytest.yml/badge.svg
[pylint]:   https://github.com/dariustb/VibeBeyond/actions/workflows/pylint.yml/badge.svg
[gpages]:   https://github.com/dariustb/VibeBeyond/actions/workflows/pages/pages-build-deployment/badge.svg 
[pytest-url]:   https://github.com/dariustb/VibeBeyond/actions/workflows/pytest.yml
[pylint-url]:   https://github.com/dariustb/VibeBeyond/actions/workflows/pylint.yml
[gpages-url]:   https://github.com/dariustb/VibeBeyond/actions/workflows/pages/pages-build-deployment

<!-- Markdown Badges -->
[node.js]:      https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white
[npm.io]:       https://img.shields.io/badge/NPM-%23CB3837.svg?style=for-the-badge&logo=npm&logoColor=white
[vue.js]:       https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[tailwind.css]: https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white
[python.io]:    https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[flask.io]:     https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
