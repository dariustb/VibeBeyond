---
layout: default
title: Getting Started
parent: Development
nav_order: 2
---

# Getting started

![getting started gif](https://media.tenor.com/HgjpIg9fxH0AAAAC/excited-lets-get-this-party-started.gif)

## Setting up your coding environment

### Prerequisites

* [VS Code](https://code.visualstudio.com/) + extensions:
    * [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar)  (v0.3.1361 or greater)
    * [Tauri](https://marketplace.visualstudio.com/items?itemName=tauri-apps.tauri-vscode) (v0.2.1 or greater)
    * [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer) (v0.3.1361 or greater)
* [Node](https://nodejs.org/en/) (v18.12.1 or greater)
    * Installing node through their [official site](https://nodejs.org/en/) is the best way to get npm/npx installed. 
* [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) (9.2.0 or greater)
* [Rustlang][Rust-url] (1.66.0 or greater)
    * Rust is necessary to build the desktop version of the app and may cause issues if not installed

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
  * Running on web will not allow the app to fully function (using Vue on web without Rust backend).
* Run as web and desktop
  ```sh
  npm run tauri dev
  ```
  **Note**: the tauri app will open on its own once it finishes loading. The web app will be served with a http://localhost:1420/ address to follow and view on your browser. Use `ctrl+C` to end the server. 

---
[Rust-url]: https://www.rust-lang.org/
