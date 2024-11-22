/** @type {import('tailwindcss').Config} */
import * as tokens from "@esnet/esnet-tokens";

module.exports = {
  content: ["./mockups/**/*.html"],
  theme: {
    fontFamily: {
      sans: ["Source Sans 3", "Open Sans", "sans-serif"],
      mono: ["Source Code Pro", "monospace"],
      display: ["Signika", "Open Sans", "sans-serif"],
    },
    colors: {
      black: {
        100: tokens.ESNET_COLOR_CORE_BLACK_100,
        200: tokens.ESNET_COLOR_CORE_BLACK_200,
        300: tokens.ESNET_COLOR_CORE_BLACK_300,
        400: tokens.ESNET_COLOR_CORE_BLACK_400,
        500: tokens.ESNET_COLOR_CORE_BLACK_500,
        600: tokens.ESNET_COLOR_CORE_BLACK_600,
        700: tokens.ESNET_COLOR_CORE_BLACK_700,
        800: tokens.ESNET_COLOR_CORE_BLACK_800,
        900: tokens.ESNET_COLOR_CORE_BLACK_900,
        1000: tokens.ESNET_COLOR_CORE_BLACK_1000,
      },
      white: {
        100: tokens.ESNET_COLOR_CORE_WHITE_100,
        200: tokens.ESNET_COLOR_CORE_WHITE_200,
        300: tokens.ESNET_COLOR_CORE_WHITE_300,
        400: tokens.ESNET_COLOR_CORE_WHITE_400,
        500: tokens.ESNET_COLOR_CORE_WHITE_500,
        600: tokens.ESNET_COLOR_CORE_WHITE_600,
        700: tokens.ESNET_COLOR_CORE_WHITE_700,
        800: tokens.ESNET_COLOR_CORE_WHITE_800,
        900: tokens.ESNET_COLOR_CORE_WHITE_900,
        1000: tokens.ESNET_COLOR_CORE_WHITE_1000,
      },
      slate: {
        50: tokens.ESNET_COLOR_CORE_WHITE_50,
        100: tokens.ESNET_COLOR_CORE_WHITE_100,
        200: tokens.ESNET_COLOR_CORE_WHITE_200,
        300: tokens.ESNET_COLOR_CORE_WHITE_300,
        400: tokens.ESNET_COLOR_CORE_WHITE_400,
        500: tokens.ESNET_COLOR_CORE_WHITE_500,
        600: tokens.ESNET_COLOR_CORE_WHITE_600,
        700: tokens.ESNET_COLOR_CORE_WHITE_700,
        800: tokens.ESNET_COLOR_CORE_WHITE_800,
        900: tokens.ESNET_COLOR_CORE_WHITE_900,
        1000: tokens.ESNET_COLOR_CORE_WHITE_1000,
      },
      blue: {
        100: tokens.ESNET_COLOR_CORE_BLUE_100,
        200: tokens.ESNET_COLOR_CORE_BLUE_200,
        300: tokens.ESNET_COLOR_CORE_BLUE_300,
        400: tokens.ESNET_COLOR_CORE_BLUE_400,
        500: tokens.ESNET_COLOR_CORE_BLUE_500,
        600: tokens.ESNET_COLOR_CORE_BLUE_600,
        700: tokens.ESNET_COLOR_CORE_BLUE_700,
        800: tokens.ESNET_COLOR_CORE_BLUE_800,
        900: tokens.ESNET_COLOR_CORE_BLUE_900,
        1000: tokens.ESNET_COLOR_CORE_BLUE_1000,
      },
    },
    extend: {
      colors: {
        surface: {
          1: tokens.ESNET_COLOR_DARK_SURFACE_1,
          2: tokens.ESNET_COLOR_DARK_SURFACE_2,
          bg: tokens.ESNET_COLOR_DARK_BACKGROUND,
        },
      },
    },
  },
  plugins: [],
};

