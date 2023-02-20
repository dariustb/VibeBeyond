<!-- Status Badges -->
[![Lint][lint-status]][lint-url] [![Unit Test][unit-status]][unit-url] [![Github Pages][gh-page-status]][gh-page-url]

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
[lint-status]: https://github.com/dariustb/VibeBeyond/actions/workflows/lint.yml/badge.svg
[lint-url]: https://github.com/dariustb/VibeBeyond/actions/workflows/lint.yml
[unit-status]: https://github.com/dariustb/VibeBeyond/actions/workflows/unitttest.yml/badge.svg
[unit-url]: https://github.com/dariustb/VibeBeyond/actions/workflows/unitttest.yml
[gh-page-status]: https://github.com/dariustb/VibeBeyond/actions/workflows/pages/pages-build-deployment/badge.svg
[gh-page-url]: https://github.com/dariustb/VibeBeyond/actions/workflows/pages/pages-build-deployment
