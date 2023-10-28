import '@/styles/global.css';
import type { AppProps } from 'next/app';
import React from "react";
import axios from "axios";
import { inputAnatomy } from "@chakra-ui/anatomy";
import {
  ChakraProvider,
  createMultiStyleConfigHelpers,
  extendTheme,
} from "@chakra-ui/react";
// import { AuthProvider } from '@/common/contexts/AuthContext';
// import { DatasetProvider } from '@/common/contexts/DatasetContext';


const { definePartsStyle, defineMultiStyleConfig } =
  createMultiStyleConfigHelpers(inputAnatomy.keys);

const baseStyle = definePartsStyle({
  field: {
    fontFamily: "body",
    color: "dark.500",
    focusBorderColor: "pink.500",
  },
});

const inputTheme = defineMultiStyleConfig({ baseStyle });

// Chakra UI Theme
const theme = extendTheme({
  components: { Input: inputTheme },
  colors: {
    prussianblue: "#062337",
    // Solid buttons
    dodgerblue: {
      600: "#47B3FF", // lighter
      500: "#0496FF", // darker
    },
    // Outline buttons
    dodgerbluedark: {
      50: "#EBF7FF",
      500: "#0496FF",
      600: "#0083E0",
    },
    // Ghost buttons
    dodgerbluelight: {
      50: "#D6EDFF",
      500: "#0496FF",
      600: "#0083E0",
    },
    bluejeans: {
      600: "#72C3FE", // lighter
      500: "#4BB3FD", // darker
    },
    dark: {
      500: "#131515",
      600: "#1A1C1D",
      700: "#000000",
    },
    cultured: {
      400: "#FFFFFF",
      500: "#F5F5F5",
      600: "#EBEBEB",
    },
    // Ghost buttons gray (edit/delete)
    graycultured: {
      50: "#EBEBEB",
      600: "#999999",
    },
    hints: {
      100: "#D6EDFF", // lighter
      500: "#0496FF", // darker
    },
  },
  fonts: {
    display:
      'Montserrat, "Proxima Nova", Armitage, -apple-system, ui-sans-serif',
    body: '"Open Sans", ui-sans-serif, -apple-system, system-ui',
    mono: '"Fira Code", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace',
  },
});

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

export default function App({ Component, pageProps }: AppProps) {
  return (
    // <AuthProvider>
    //   <DatasetProvider>
        <ChakraProvider theme={theme}>
          <Component {...pageProps} />
        </ChakraProvider>
    //   </DatasetProvider>
    // </AuthProvider>
  );
}
