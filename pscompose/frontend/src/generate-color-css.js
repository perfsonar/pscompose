// This script generates a css/color.css defining themed color variables
const fs = require("fs");
const tokens = require("@esnet/esnet-tokens");

const css = `
/* AUTO-GENERATED — DO NOT EDIT */

:root {
  --background: 210 211 215;
  --copy: ${hexToRgbChannels(tokens.ESNET_COLOR_CORE_BLACK_800)};
  --copyAlt: ${hexToRgbChannels(tokens.ESNET_COLOR_LIGHT_COPY_ALT)};
  --surface_1: ${hexToRgbChannels(tokens.ESNET_COLOR_LIGHT_SURFACE_1)};
  --surface_2: ${hexToRgbChannels(tokens.ESNET_COLOR_LIGHT_SURFACE_2)};
  --error: ${hexToRgbChannels(tokens.ESNET_COLOR_LIGHT_ERROR)};
  --warning: ${hexToRgbChannels(tokens.ESNET_COLOR_LIGHT_WARNING)};
  --success: ${hexToRgbChannels(tokens.ESNET_COLOR_LIGHT_SUCCESS)};
  --shadow: ${hexToRgbChannels(tokens.ESNET_COLOR_CORE_SLATE_400)};
}

[data-theme="dark"] {
  --background: ${hexToRgbChannels(tokens.ESNET_COLOR_DARK_BACKGROUND)};
  --copy: ${hexToRgbChannels(tokens.ESNET_COLOR_DARK_COPY)};
  --copyAlt: ${hexToRgbChannels(tokens.ESNET_COLOR_DARK_COPY_ALT)};
  --surface_1: ${hexToRgbChannels(tokens.ESNET_COLOR_DARK_SURFACE_1)};
  --surface_2: ${hexToRgbChannels(tokens.ESNET_COLOR_DARK_SURFACE_2)};
  --error: ${hexToRgbChannels(tokens.ESNET_COLOR_DARK_ERROR)};
  --warning: ${hexToRgbChannels(tokens.ESNET_COLOR_DARK_WARNING)};
  --success: ${hexToRgbChannels(tokens.ESNET_COLOR_DARK_SUCCESS)};
  --shadow: ${hexToRgbChannels(tokens.ESNET_COLOR_DARK_SHADOW)};
}
`;

function hexToRgbChannels(hex) {
  const normalized = hex.replace("#", "");
  const bigint = parseInt(normalized, 16);

  const r = (bigint >> 16) & 255;
  const g = (bigint >> 8) & 255;
  const b = bigint & 255;

  return `${r} ${g} ${b}`;
}


fs.writeFileSync("./css/color.css", css);
