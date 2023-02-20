<!-- Status Badges -->
[![Unit Test](https://github.com/dariustb/VibeBeyond/actions/workflows/vitest.yml/badge.svg)](https://github.com/dariustb/VibeBeyond/actions/workflows/vitest.yml) [![Lint](https://github.com/dariustb/VibeBeyond/actions/workflows/eslint.yml/badge.svg)](https://github.com/dariustb/VibeBeyond/actions/workflows/eslint.yml)
[![Unit Test](https://github.com/dariustb/VibeBeyond/actions/workflows/pytest.yml/badge.svg)](https://github.com/dariustb/VibeBeyond/actions/workflows/pytest.yml) [![Lint](https://github.com/dariustb/VibeBeyond/actions/workflows/pylint.yml/badge.svg)](https://github.com/dariustb/VibeBeyond/actions/workflows/pylint.yml)
[![Github Pages][gh-page-status]][gh-page-url]

# Vibe Beyond

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup - Vue

```sh
cd frontend/
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Run Unit Tests with [Vitest](https://vitest.dev/)

```sh
npm run test
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

## Project Setup - Flask
*from outside the backend folder*
```sh
python -m venv venv
source venv/Scripts/activate
pip install -r backend/requirements.txt
```

### Compile and Hot-Reload for Development
```sh
python backend/app.py
```

### Run Unit Tests with [Pytest](https://docs.pytest.org/en/latest/)

```sh
pytest backend/
```

### Lint with [Pylint](https://pylint.readthedocs.io/en/latest/)
```sh
pylint backend/
```

<!-- Markdown links -->
[gh-page-status]: https://github.com/dariustb/VibeBeyond/actions/workflows/pages/pages-build-deployment/badge.svg
[gh-page-url]: https://github.com/dariustb/VibeBeyond/actions/workflows/pages/pages-build-deployment
