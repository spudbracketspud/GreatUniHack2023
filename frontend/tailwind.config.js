/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    fontFamily: {
      'display': 'Montserrat, "Proxima Nova", Armitage, -apple-system, ui-sans-serif',
      'body': '"Open Sans", ui-sans-serif, -apple-system, system-ui',
      'mono': '"Fira Code", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace',
    },
    extend: {
      colors: {
        seasalt: '#F4F7F5',
        jade: '#3E794D',
        jadelight: '#4C945E',
        emerald: '#76D082',
        rosybrown: '#B08285',
        eerieblack: '#172121',
      },
    },
  },
  plugins: [],
}
