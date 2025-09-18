/** @type {import('tailwindcss').Config} */
import * as tokens from "@esnet/esnet-tokens";

module.exports = {
  content: [
    "./mockups/**/*.html",
    "./app/**/*.html",
    "./pages/**/*.html",
    "./partials/**/*.html",
  ],
  theme: {
    fontFamily: {
      display: [tokens.ESNET_FONT_FAMILY_BODY_DISPLAY, "sans-serif"],
      sans: [tokens.ESNET_FONT_FAMILY_BODY_SANS, "sans-serif"],
      mono: [tokens.ESNET_FONT_FAMILY_BODY_MONO, "monospace"],
    },
    colors: {
      background: tokens.ESNET_COLOR_DARK_BACKGROUND,
      copy: tokens.ESNET_COLOR_DARK_COPY,
      copyAlt: tokens.ESNET_COLOR_DARK_COPY_ALT,
      surface_1: tokens.ESNET_COLOR_DARK_SURFACE_1,
      surface_2: tokens.ESNET_COLOR_DARK_SURFACE_2,
      error: tokens.ESNET_COLOR_DARK_ERROR,
      warning: tokens.ESNET_COLOR_DARK_ERROR,
      success: tokens.ESNET_COLOR_DARK_SUCCESS,
      shadow: tokens.ESNET_COLOR_DARK_SHADOW,
    },
    extend: {
      boxShadow: {
        none: tokens.ESNET_BOX_SHADOW_CORE_NONE,
        light: tokens.ESNET_BOX_SHADOW_CORE_LIGHT,
        medium: tokens.ESNET_BOX_SHADOW_CORE_MEDIUM,
        mediumInset: tokens.ESNET_BOX_SHADOW_CORE_MEDIUM_INSET,
      },
      spacing: {
        none: tokens.ESNET_SIZE_SPACING_NONE,
        xxsm: tokens.ESNET_SIZE_SPACING_XXSMALL,
        xsm: tokens.ESNET_SIZE_SPACING_XSMALL,
        md: tokens.ESNET_SIZE_SPACING_MEDIUM,
        lg: tokens.ESNET_SIZE_SPACING_LARGE,
        xlg: tokens.ESNET_SIZE_SPACING_XLARGE,
        xxlg: tokens.ESNET_SIZE_SPACING_XXLARGE,
        xxxlg: tokens.ESNET_SIZE_SPACING_XXXLARGE,
      },
      borderRadius: {
        none: tokens.ESNET_SIZE_RADIUS_NONE,
        sm: tokens.ESNET_SIZE_RADIUS_SMALL,
        md: tokens.ESNET_SIZE_RADIUS_MEDIUM,
        lg: tokens.ESNET_SIZE_RADIUS_LARGE,
        xl: tokens.ESNET_SIZE_RADIUS_XLARGE,
        xxl : tokens.ESNET_SIZE_RADIUS_XXLARGE,
        full: tokens.ESNET_SIZE_RADIUS_CIRCLE,
      },
      borderWidth: {
        none: tokens.ESNET_SIZE_BORDER_WIDTH_NONE,
        xs: tokens.ESNET_SIZE_BORDER_WIDTH_XSMALL,
        sm: tokens.ESNET_SIZE_BORDER_WIDTH_SMALL,
        md: tokens.ESNET_SIZE_BORDER_WIDTH_MEDIUM,
        lg: tokens.ESNET_SIZE_BORDER_WIDTH_LARGE,
        xl: tokens.ESNET_SIZE_BORDER_WIDTH_XLARGE,
      },
      fontSize: {
        // Headings - Sans
        h1_sans: [
          tokens.ESNET_TYPOGRAPHY_HEADER_1_SANS_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_HEADER_1_SANS_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_HEADER_1_SANS_FONT.fontWeight,
            letterSpacing: tokens.ESNET_TYPOGRAPHY_HEADER_1_SANS_LETTERSPACING,
          },
        ],
        h2_sans: [
          tokens.ESNET_TYPOGRAPHY_HEADER_2_SANS_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_HEADER_2_SANS_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_HEADER_2_SANS_FONT.fontWeight,
          },
        ],
        h3_sans: [
          tokens.ESNET_TYPOGRAPHY_HEADER_3_SANS_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_HEADER_3_SANS_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_HEADER_3_SANS_FONT.fontWeight,
          },
        ],
        h4_sans: [
          tokens.ESNET_TYPOGRAPHY_HEADER_4_SANS_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_HEADER_4_SANS_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_HEADER_4_SANS_FONT.fontWeight,
            letterSpacing: tokens.ESNET_TYPOGRAPHY_HEADER_4_SANS_LETTERSPACING,
          },
        ],
        h5_sans: [
          tokens.ESNET_TYPOGRAPHY_HEADER_5_SANS_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_HEADER_5_SANS_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_HEADER_5_SANS_FONT.fontWeight,
          },
        ],
        h6_sans: [
          tokens.ESNET_TYPOGRAPHY_HEADER_6_SANS_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_HEADER_6_SANS_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_HEADER_6_SANS_FONT.fontWeight,
          },
        ],

        // Headings - Mono
        h4_mono: [
          tokens.ESNET_TYPOGRAPHY_HEADER_4_MONO_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_HEADER_4_MONO_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_HEADER_4_MONO_FONT.fontWeight,
          },
        ],
        h5_mono: [
          tokens.ESNET_TYPOGRAPHY_HEADER_5_MONO_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_HEADER_5_MONO_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_HEADER_5_MONO_FONT.fontWeight,
          },
        ],
        h6_mono: [
          tokens.ESNET_TYPOGRAPHY_HEADER_6_MONO_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_HEADER_6_MONO_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_HEADER_6_MONO_FONT.fontWeight,
          },
        ],

        // Copy - Sans
        copy_1_sans: [
          tokens.ESNET_TYPOGRAPHY_COPY_1_SANS_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_COPY_1_SANS_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_COPY_1_SANS_FONT.fontWeight,
          },
        ],
        copy_2_sans: [
          tokens.ESNET_TYPOGRAPHY_COPY_2_SANS_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_COPY_2_SANS_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_COPY_2_SANS_FONT.fontWeight,
          },
        ],

        // Copy - Mono
        copy_1_mono: [
          tokens.ESNET_TYPOGRAPHY_COPY_1_MONO_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_COPY_1_MONO_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_COPY_1_MONO_FONT.fontWeight,
          },
        ],
        copy_2_mono: [
          tokens.ESNET_TYPOGRAPHY_COPY_2_MONO_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_COPY_2_MONO_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_COPY_2_MONO_FONT.fontWeight,
          },
        ],

        // Buttons - Display
        button_1_display: [
          tokens.ESNET_TYPOGRAPHY_BUTTON_1_DISPLAY_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_BUTTON_1_DISPLAY_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_BUTTON_1_DISPLAY_FONT.fontWeight,
            letterSpacing: tokens.ESNET_TYPOGRAPHY_BUTTON_1_DISPLAY_LETTERSPACING,
          },
        ],
        button_2_display: [
          tokens.ESNET_TYPOGRAPHY_BUTTON_2_DISPLAY_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_BUTTON_2_DISPLAY_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_BUTTON_2_DISPLAY_FONT.fontWeight,
            letterSpacing: tokens.ESNET_TYPOGRAPHY_BUTTON_2_DISPLAY_LETTERSPACING,
          },
        ],

        // Buttons - Sans
        button_1_sans: [
          tokens.ESNET_TYPOGRAPHY_BUTTON_1_SANS_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_BUTTON_1_SANS_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_BUTTON_1_SANS_FONT.fontWeight,
            letterSpacing: tokens.ESNET_TYPOGRAPHY_BUTTON_1_SANS_LETTERSPACING,
          },
        ],
        button_2_sans: [
          tokens.ESNET_TYPOGRAPHY_BUTTON_2_SANS_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_BUTTON_2_SANS_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_BUTTON_2_SANS_FONT.fontWeight,
            letterSpacing: tokens.ESNET_TYPOGRAPHY_BUTTON_2_SANS_LETTERSPACING,
          },
        ],

        // Labels - Sans
        label_1_sans: [
          tokens.ESNET_TYPOGRAPHY_LABEL_1_SANS_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_LABEL_1_SANS_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_LABEL_1_SANS_FONT.fontWeight,
            letterSpacing: tokens.ESNET_TYPOGRAPHY_LABEL_1_SANS_LETTERSPACING,
          },
        ],
        label_1_large: [
          tokens.ESNET_TYPOGRAPHY_LABEL_1_LARGE_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_LABEL_1_LARGE_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_LABEL_1_LARGE_FONT.fontWeight,
            letterSpacing: tokens.ESNET_TYPOGRAPHY_LABEL_1_LARGE_LETTERSPACING,
          },
        ],

        // Labels - Mono
        label_1_mono: [
          tokens.ESNET_TYPOGRAPHY_LABEL_1_MONO_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_LABEL_1_MONO_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_LABEL_1_MONO_FONT.fontWeight,
          },
        ],
        label_2_sans: [
          tokens.ESNET_TYPOGRAPHY_LABEL_2_SANS_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_LABEL_2_SANS_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_LABEL_2_SANS_FONT.fontWeight,
            letterSpacing: tokens.ESNET_TYPOGRAPHY_LABEL_2_SANS_LETTERSPACING,
          },
        ],
        label_2_large: [
          tokens.ESNET_TYPOGRAPHY_LABEL_2_LARGE_FONT.fontSize,
          {
            lineHeight: tokens.ESNET_TYPOGRAPHY_LABEL_2_LARGE_FONT.lineHeight,
            fontWeight: tokens.ESNET_TYPOGRAPHY_LABEL_2_LARGE_FONT.fontWeight,
            letterSpacing: tokens.ESNET_TYPOGRAPHY_LABEL_2_LARGE_LETTERSPACING,
          },
        ],
      },
    },
  },
  plugins: [],
};
