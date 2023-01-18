<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/dariustb/vibebeyond">
    <img src="https://i1.sndcdn.com/artworks-nXTBoQMnJHSoNPbn-yX34xA-t500x500.jpg" alt="Logo" width="100" height="100">
  </a>

  <h1 align="center">Vibe Beyond</h1>

  <p align="center">
    Tauri AI-generated lofi hip-hop radio
    <br />
    <a href="https://dariustb.github.io/VibeBeyond/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://vibe-beyond.vercel.app/">View Demo</a>
    ·
    <a href="https://github.com/dariustb/vibebeyond/issues">Report Bug</a>
    ·
    <a href="https://github.com/dariustb/vibebeyond/issues">Request Feature</a>
  </p>
</div>
 


<!-- ABOUT THE PROJECT -->
## About The Project

[![Vibe Beyond Screen Shot][product-screenshot]](https://github.com/dariustb/vibebeyond/)

Vibe beyond is an app that'll probably make the anti-creative-AI crowd upset. The application is used to emulate the function of those 24-hour "Lofi Hip-Hop Beats to Study/Chill to" while working with the component of a desktop app to use the user's storage to build (and remove) new songs to stream.

_Please [refer to the documentation][docs] for the full breakdown and logic explanation of the app._

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Tauri][Tauri.io]][Tauri-url]
* [![Vue][Vue.js]][Vue-url]
* [![Rust][Rust.io]][Rust-url]
* [![Tailwind][Tailwind.css]][Tailwind-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

_This is the TL;DR version of the dev's "Getting Started" section. More details are included [in the documentation][docs]._

### Prerequisites

* [VS Code](https://code.visualstudio.com/) + extensions:
    * [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar)  (v0.3.1361 or greater)
    * [Tauri](https://marketplace.visualstudio.com/items?itemName=tauri-apps.tauri-vscode) (v0.2.1 or greater)
    * [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer) (v0.3.1361 or greater)
* [Node](https://nodejs.org/en/) (v18.12.1 or greater)
* [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) (9.2.0 or greater)
* [Rustlang][Rust-url] (1.66.0 or greater)

### Installation

1. Clone the repo
   ```sh
   git clone git@github.com:dariustb/VibeBeyond.git
   ```
2. Install NPM packages
   ```sh
   cd VibeBeyond
   npm install
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Run locally

* Run as web only
  ```sh
  npm run dev
  ```
* Run as web and desktop
  ```sh
  npm run tauri dev
  ```
  **Note**: the tauri app will open on its own once it finishes loading. The web app will be served with a http://localhost:1420/ address to follow and view on your browser. Use `ctrl+C` to end the server. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[app]: https://vibe-beyond.vercel.app/
[docs]: https://dariustb.github.io/VibeBeyond/
[forks-url]: https://github.com/dariustb/vibebeyond/network/members
[stars-url]: https://github.com/dariustb/vibebeyond/stargazers
[issues-url]: https://github.com/dariustb/vibebeyond/issues
[license-url]: https://github.com/dariustb/vibebeyond/blob/master/LICENSE.txt

[contributors-shield]: https://img.shields.io/github/contributors/dariustb/vibebeyond.svg?style=for-the-badge
[contributors-url]: https://github.com/dariustb/vibebeyond/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dariustb/vibebeyond.svg?style=for-the-badge
[stars-shield]: https://img.shields.io/github/stars/dariustb/vibebeyond.svg?style=for-the-badge
[issues-shield]: https://img.shields.io/github/issues/dariustb/vibebeyond.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/dariustb/vibebeyond.svg?style=for-the-badge
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/dariustb

[product-screenshot]: /docs/media/Wireframe%20-%20Start.png
[web-app-snapshot]: https://vercel.com/ddfabdf2-b143-4a33-abe7-9e1856543739

[Tauri.io]:https://img.shields.io/badge/tauri-%2324C8DB.svg?style=for-the-badge&logo=tauri&logoColor=%23FFFFFF
[Tauri-url]:https://tauri.app/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Rust.io]: https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white
[Rust-url]: https://www.rust-lang.org/
[Tailwind.css]: https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white
[Tailwind-url]: https://tailwindcss.com/
