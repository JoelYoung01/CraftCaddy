// Vuetify
import "@/assets/styles/custom-vuetify.scss";
import "@mdi/font/css/materialdesignicons.css";
import { createVuetify, type ThemeDefinition } from "vuetify";

// To customize SASS variables, follow the guide here: https://vuetifyjs.com/en/features/sass-variables

const light = "#f2d8a8";
const lightGreen = "#cfb686";
const green = "#a19b5a";
const dark = "#3d2f1b";

const MainTheme: ThemeDefinition = {
  dark: true,
  colors: {
    // Add color overrides here
    background: lightGreen,
    surface: light,
    primary: dark
  },
  variables: {
    // Add CSS Variables here
    // https://github.com/vuetifyjs/vuetify/discussions/18883#discussioncomment-7868798
  }
};

export const vuetify = createVuetify({
  theme: {
    defaultTheme: "MainTheme",
    themes: {
      MainTheme
    }
  }
});
