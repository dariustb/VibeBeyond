/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/templates/**/*.html",
    "./src/static/**/*.js"
  ],
  theme: {
    extend: {},
    fontFamily: {
      neirizi: ["Neirizi", "serif"],
      glacial: ["Glacial Indifference", "sans-serif"],
    },
  },
  plugins: [],
  purge: {
    enabled: true,
    content: [
        './**/*.html'
    ]
  }
}

