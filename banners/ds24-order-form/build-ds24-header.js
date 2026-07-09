const opentype = require('opentype.js');
const fs = require('fs');
const tmpdir = require('os').tmpdir();
const boldFont = opentype.parse(fs.readFileSync(tmpdir + '/inter-bold.ttf').buffer);
const orbitronFont = opentype.parse(fs.readFileSync(tmpdir + '/orbitron-black.ttf').buffer);

const W = 1200, H = 300;
const WHITE = '#ffffff';
const NAVY = '#013161';
const RED = '#f94238';
const GOLD = '#B29D60';
const BLACK = '#1a1a1a';

function tp(font, text, x, y, sz) {
  const scale = sz / font.unitsPerEm;
  let xPos = x, d = '';
  for (let i = 0; i < text.length; i++) {
    const g = font.charToGlyph(text[i]);
    const pathData = g.getPath(xPos, y, sz).toPathData(2);
    // Skip broken glyphs with NaN
    if (!pathData.includes('NaN')) {
      d += pathData;
    } else {
      // Fallback: try to get the glyph via charCodeAt
      const code = text.charCodeAt(i);
      const gIdx = font.charToGlyphIndex(text[i]);
      const glyph = font.glyphs.get(gIdx);
      if (glyph && glyph.path) {
        // Manually build the path with transform
        const commands = glyph.path.commands;
        for (const cmd of commands) {
          if (cmd.type === 'M') d += `M${(cmd.x * scale + xPos).toFixed(2)} ${(y - cmd.y * scale).toFixed(2)}`;
          else if (cmd.type === 'L') d += `L${(cmd.x * scale + xPos).toFixed(2)} ${(y - cmd.y * scale).toFixed(2)}`;
          else if (cmd.type === 'Q') d += `Q${(cmd.x1 * scale + xPos).toFixed(2)} ${(y - cmd.y1 * scale).toFixed(2)} ${(cmd.x * scale + xPos).toFixed(2)} ${(y - cmd.y * scale).toFixed(2)}`;
          else if (cmd.type === 'C') d += `C${(cmd.x1 * scale + xPos).toFixed(2)} ${(y - cmd.y1 * scale).toFixed(2)} ${(cmd.x2 * scale + xPos).toFixed(2)} ${(y - cmd.y2 * scale).toFixed(2)} ${(cmd.x * scale + xPos).toFixed(2)} ${(y - cmd.y * scale).toFixed(2)}`;
          else if (cmd.type === 'Z') d += 'Z';
        }
      }
    }
    xPos += g.advanceWidth * scale;
  }
  return d;
}

function tw(font, text, sz) {
  const scale = sz / font.unitsPerEm;
  let w = 0;
  for (let i = 0; i < text.length; i++) w += font.charToGlyph(text[i]).advanceWidth * scale;
  return w;
}

// Bonfire circle path data (reused)
const bonfireCirclePath = "M0 0 C1.15 0 2.3 0 3.48 0 C21.57 0.04 39.03 0.79 56.81 4.38 C57.89 4.59 58.96 4.8 60.07 5.02 C103.44 13.97 143.68 32.77 176.81 62.38 C177.27 62.77 177.27 62.77 179.58 64.78 C184.05 68.7 188.17 72.7 191.99 77.25 C193.29 78.77 194.63 80.24 196.01 81.69 C207.83 94.15 217.35 108.4 225.7 123.37 C226.76 125.28 227.84 127.18 228.93 129.07 C241.85 152.05 249.22 177.55 253.81 203.38 C253.94 204.02 254.07 204.67 254.2 205.34 C257.12 220.5 257.34 235.63 257.31 251.01 C257.31 253.82 257.32 256.63 257.35 259.44 C257.85 303.73 248.29 347.34 226.81 386.38 C226.44 387.06 226.06 387.74 225.67 388.45 C204.93 425.79 174.51 456.66 137.81 478.38 C137.07 478.83 136.33 479.29 135.56 479.77 C111.56 494.5 84.29 503 56.81 508.38 C55.79 508.59 54.76 508.8 53.71 509.02 C16.72 516.39 -26.64 516.06 -63.19 506.38 C-62.63 502.7 -61.7 500.2 -59.63 497.12 C-59.1 496.31 -58.56 495.5 -58.01 494.66 C-57.43 493.8 -56.84 492.93 -56.24 492.04 C-55.63 491.12 -55.02 490.2 -54.39 489.26 C-52.44 486.31 -50.47 483.37 -48.5 480.44 C-45.95 476.62 -43.41 472.8 -40.86 468.97 C-40.55 468.5 -40.55 468.5 -38.94 466.09 C-24.76 444.74 -11.22 422.97 1.48 400.7 C2.35 399.19 3.22 397.67 4.09 396.16 C23.91 361.7 40.46 323.61 47.81 284.38 C47.9 283.92 47.9 283.92 48.34 281.6 C61.56 209.71 42.74 143.92 2.05 84.39 C-1.92 78.64 -1.92 78.64 -4.19 76.38 C-3.97 76.89 -3.76 77.4 -3.53 77.93 C4.11 96.14 9.29 113.77 11.81 133.38 C11.91 134.1 12.01 134.83 12.1 135.58 C17.66 180.72 1.32 225.47 -20.19 264.38 C-20.68 265.27 -21.18 266.17 -21.69 267.1 C-33.14 287.84 -45.77 307.78 -58.5 327.73 C-63.09 334.93 -67.66 342.14 -72.19 349.38 C-72.64 350.1 -73.1 350.83 -73.56 351.57 C-99.41 393.01 -119.41 434.3 -124.19 483.38 C-151.67 479.6 -185.13 443.7 -201 423.3 C-201.72 422.34 -202.44 421.37 -203.19 420.38 C-203.42 420.07 -203.42 420.07 -204.62 418.5 C-239.66 372.55 -256.09 317.63 -255.71 260.13 C-255.69 256.64 -255.7 253.15 -255.72 249.67 C-256.11 180.48 -231.05 118.5 -182.87 69.07 C-166.14 52.19 -146.05 39.48 -125.19 28.38 C-124.53 28.02 -123.87 27.66 -123.19 27.29 C-98.16 13.77 -70.22 6.36 -42.19 2.38 C-41 2.2 -39.81 2.02 -38.59 1.84 C-25.76 0.04 -12.94 -0.02 0 0 Z";

const flamePath = "M0 0 C3.93 1.79 5.66 3.82 8.25 7.31 C9.14 8.49 10.02 9.67 10.91 10.86 C11.39 11.51 11.88 12.17 12.39 12.85 C14.15 15.2 15.93 17.53 17.72 19.86 C29.75 35.56 41.56 51.4 52.9 67.59 C54.84 70.35 56.78 73.1 58.74 75.85 C66.42 86.63 73.81 97.59 81.12 108.62 C82.24 110.3 83.35 111.97 84.46 113.65 C86.63 116.91 88.8 120.17 90.96 123.43 C92.89 126.33 94.82 129.23 96.76 132.13 C101.82 139.68 106.77 147.28 111.56 155 C112.21 156.04 112.85 157.07 113.52 158.14 C118.02 165.38 122.47 172.65 126.8 179.98 C128.18 182.3 129.56 184.61 130.94 186.92 C139.22 200.81 147.18 214.85 155 229 C155.52 229.95 156.05 230.9 156.59 231.88 C176.6 268.13 195.32 305.09 212 343 C212.31 343.7 212.62 344.4 212.93 345.12 C222.65 367.17 231.69 389.44 240.23 411.97 C240.95 413.87 241.68 415.76 242.4 417.66 C257.58 457.3 270.19 497.96 281 539 C281.41 540.53 281.81 542.06 282.22 543.58 C303.73 625.07 315.87 708.87 320 793 C320.06 794.08 320.12 795.17 320.18 796.28 C325.48 898.12 316.09 1001.04 294 1117 C293.84 1117.83 293.67 1118.66 293.5 1119.52 C283.83 1168.23 271.43 1216.49 257 1264 C256.88 1264.39 256.88 1264.39 256.28 1266.38 C242.31 1312.5 226.54 1358.11 209 1403 C208.72 1403.72 208.44 1404.44 208.15 1405.18 C204.52 1414.49 200.79 1423.75 197 1433 C196.86 1433.33 196.86 1433.33 196.18 1435.01 C176.57 1482.92 155.34 1530.1 132.64 1576.62 C130.66 1580.7 128.71 1584.8 126.76 1588.9 C117.76 1607.86 108.4 1626.65 98.55 1645.18 C96.1 1649.8 93.69 1654.45 91.29 1659.1 C85.19 1670.88 78.93 1682.56 72.54 1694.19 C70.36 1698.17 68.2 1702.17 66.04 1706.16 C56 1724.75 45.67 1743.15 35.16 1761.48 C32.74 1765.71 30.32 1769.94 27.91 1774.18 C8.43 1808.35 -11.56 1842.2 -32.03 1875.77 C-33.93 1878.88 -35.82 1882 -37.71 1885.12 C-49.68 1904.82 -61.85 1924.39 -74.08 1943.93 C-76.01 1947.01 -77.94 1950.1 -79.86 1953.19 C-91.56 1971.92 -103.36 1990.59 -115.23 2009.21 C-116.96 2011.94 -118.7 2014.68 -120.44 2017.41 C-128.58 2030.22 -136.76 2043.01 -144.95 2055.79 C-147.03 2059.04 -149.11 2062.29 -151.18 2065.54 C-157.36 2075.2 -163.54 2084.85 -169.78 2094.47 C-173.88 2100.8 -177.94 2107.15 -182 2113.5 C-186.48 2120.51 -190.97 2127.52 -195.5 2134.5 C-202.02 2144.55 -208.46 2154.64 -214.91 2164.73 C-216.97 2167.95 -219.03 2171.17 -221.09 2174.39 C-238.88 2202.16 -256.56 2230 -274 2258 C-274.55 2258.88 -275.1 2259.76 -275.66 2260.66 C-296.68 2294.43 -317.09 2328.57 -337 2363 C-337.63 2364.09 -338.26 2365.17 -338.91 2366.29 C-348.97 2383.68 -358.62 2401.24 -368 2419 C-368.24 2419.45 -368.24 2419.45 -369.43 2421.7 C-371.48 2425.58 -373.53 2429.47 -375.57 2433.37 C-377.26 2436.59 -378.96 2439.8 -380.68 2443.01 C-400.6 2480.4 -417.35 2519.28 -432 2559 C-432.74 2561.01 -433.49 2563.02 -434.23 2565.03 C-435.83 2569.35 -437.42 2573.67 -439 2578 C-442.52 2574.85 -444.65 2571.37 -446.8 2567.23 C-447.15 2566.56 -447.51 2565.89 -447.87 2565.21 C-449.03 2563.02 -450.17 2560.82 -451.31 2558.62 C-452.12 2557.09 -452.93 2555.55 -453.73 2554.01 C-456.17 2549.35 -458.59 2544.68 -461 2540 C-461.35 2539.32 -461.7 2538.64 -462.07 2537.93 C-483.36 2496.59 -501.76 2453.84 -516.71 2409.79 C-517.88 2406.33 -519.1 2402.88 -520.32 2399.43 C-531.73 2366.76 -540.17 2332.91 -547 2299 C-547.14 2298.31 -547.28 2297.62 -547.42 2296.92 C-556.33 2252.44 -562.07 2206.81 -562.2 2161.41 C-562.21 2159.87 -562.22 2158.32 -562.22 2156.78 C-562.24 2151.88 -562.25 2146.97 -562.25 2142.06 C-562.25 2141.23 -562.25 2140.39 -562.25 2139.53 C-562.26 2113.23 -561.8 2087.16 -559 2061 C-558.83 2059.33 -558.65 2057.65 -558.48 2055.98 C-548.89 1964.62 -524.69 1875.65 -456 1707 C-455.44 1705.78 -454.88 1704.55 -454.32 1703.33 C-445.36 1683.77 -435.85 1664.5 -426.25 1645.25 C-425.68 1644.11 -425.12 1642.97 -424.53 1641.8 C-417.41 1627.51 -410.04 1613.4 -402.33 1599.42 C-400.37 1595.85 -398.46 1592.26 -396.57 1588.66 C-396.4 1588.34 -396.4 1588.34 -395.56 1586.75 C-394.9 1585.49 -394.23 1584.24 -393.57 1582.98 C-386.83 1570.18 -379.9 1557.51 -372.7 1544.96 C-370.84 1541.71 -368.98 1538.46 -367.13 1535.21 C-354.92 1513.74 -342.47 1492.42 -329.88 1471.17 C-328.53 1468.9 -327.18 1466.62 -325.84 1464.34 C-316.35 1448.28 -306.78 1432.29 -296.96 1416.43 C-293.11 1410.2 -289.31 1403.93 -285.52 1397.66 C-279.29 1387.37 -272.99 1377.12 -266.59 1366.93 C-260 1356.43 -253.52 1345.87 -247.03 1335.3 C-243.63 1329.76 -240.22 1324.23 -236.81 1318.69 C-236.14 1317.6 -235.48 1316.52 -234.79 1315.4 C-230.18 1307.92 -225.56 1300.44 -220.93 1292.97 C-215.92 1284.87 -210.93 1276.76 -205.94 1268.65 C-202.34 1262.8 -198.74 1256.96 -195.12 1251.13 C-187.76 1239.27 -180.51 1227.35 -173.28 1215.41 C-170.8 1211.31 -168.3 1207.21 -165.8 1203.11 C-139.06 1159.23 -112.95 1114.93 -88 1070 C-87.36 1068.86 -86.73 1067.71 -86.07 1066.54 C-58.22 1016.39 -31.13 965.53 -7.47 913.26 C-5.98 909.95 -4.47 906.66 -2.96 903.36 C38.07 813.37 71.63 718.72 93 607 C93.15 606.15 93.3 605.3 93.46 604.42 C100.31 565.57 104.99 526.4 107 487 C107.06 486.03 107.11 485.05 107.17 484.05 C112.28 395.9 102.4 306.64 59 144 C58.78 143.33 58.57 142.67 58.34 141.98 C46.65 106.18 32.64 71.25 17 37 C16.71 36.37 16.42 35.74 16.13 35.09 C12.88 27.98 9.6 20.88 6.3 13.8 C4.17 9.21 2.08 4.61 0 0 Z";

function buildSVG(variant) {
  const isGlow = variant === 'glow';
  const trustBarH = 60;
  const mainH = H - trustBarH;

  let svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">\n`;

  // Defs for glow filter
  if (isGlow) {
    svg += `<defs>
  <filter id="gold-glow" x="-15%" y="-15%" width="130%" height="130%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="5" result="blur1"/>
    <feFlood flood-color="${GOLD}" flood-opacity="0.8" result="color1"/>
    <feComposite in="color1" in2="blur1" operator="in" result="glow1"/>
    <feGaussianBlur in="SourceAlpha" stdDeviation="10" result="blur2"/>
    <feFlood flood-color="${GOLD}" flood-opacity="0.4" result="color2"/>
    <feComposite in="color2" in2="blur2" operator="in" result="glow2"/>
    <feMerge><feMergeNode in="glow2"/><feMergeNode in="glow1"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>\n`;
  }

  // White main background
  svg += `<rect width="${W}" height="${mainH}" fill="${WHITE}"/>\n`;
  // Navy trust bar
  svg += `<rect y="${mainH}" width="${W}" height="${trustBarH}" fill="${NAVY}"/>\n`;

  // ===== TITLE: AI MARKETERS CLUB in Orbitron Black (stacked) =====
  const titleSize = 56;
  const titleX = 40;
  const line1Y = 80;
  const line2Y = 130;
  const aiText = 'AI MARKETERS';
  const clubText = 'CLUB';
  const aiD = tp(orbitronFont, aiText, titleX, line1Y, titleSize);
  const clubD = tp(orbitronFont, clubText, titleX, line2Y, titleSize);

  if (isGlow) {
    // Glow variant: gold glow filter on batman black fill
    svg += `<g filter="url(#gold-glow)">\n`;
    svg += `  <path d="${aiD}" fill="${BLACK}"/>\n`;
    svg += `  <path d="${clubD}" fill="${BLACK}"/>\n`;
    svg += `</g>\n`;
  } else {
    // Stroke variant: gold stroke behind batman black fill (paint-order: stroke)
    svg += `<path d="${aiD}" fill="${BLACK}" stroke="${GOLD}" stroke-width="2.5" paint-order="stroke"/>\n`;
    svg += `<path d="${clubD}" fill="${BLACK}" stroke="${GOLD}" stroke-width="2.5" paint-order="stroke"/>\n`;
  }

  // ===== TAGLINE (larger) =====
  const tagSize = 20;
  const tagText = 'OVER $10M IN COMMISSIONS PAID';
  const tagY = 172;
  svg += `<path d="${tp(boldFont, tagText, titleX + 2, tagY, tagSize)}" fill="${GOLD}"/>\n`;
  // Gold accent line
  svg += `<rect x="${titleX + 2}" y="${tagY + 10}" width="70" height="3" fill="${GOLD}"/>\n`;

  // ===== iMAC (drawn first = behind) =====
  const imacScale = 0.85;
  const imacX = 730, imacY = 2;
  svg += `<g transform="translate(${imacX}, ${imacY}) scale(${imacScale})">\n`;
  svg += `  <g fill="none" fill-rule="evenodd">
    <g fill="#343434">
      <path d="M335,7.92343253 C335,3.55033805 331.446533,0 327.069584,0 L7.93041607,0 C3.55346724,0 0,3.55033805 0,7.92343253 L0,199.53284 L335,199.53284 L335,7.92343253 Z"/>
      <path d="M321.662482,13.20364 C321.662482,13.0711826 321.554821,12.963536 321.422166,12.963536 L13.5778336,12.963536 C13.4451793,12.963536 13.3375179,13.0711826 13.3375179,13.20364 L13.3375179,186.318636 C13.3375179,186.451173 13.4451793,186.55874 13.5778336,186.55874 L321.422166,186.55874 C321.554821,186.55874 321.662482,186.451173 321.662482,186.318636 L321.662482,13.20364 Z"/>
      <rect width="307.604" height="172.875" transform="translate(13.698 13.326)"/>
    </g>
    <ellipse cx="167.5" cy="5.508" fill="#3E3E3E" rx="1.417" ry="1.416"/>
    <g transform="translate(0 199.206)">
      <path fill="#D5D2CF" d="M126.377188,77.7472811 C120.623231,77.7472811 116.945841,77.3335819 116.627502,76.4884158 L116.627502,75.3868986 L218.371536,75.3868986 L218.371536,76.4884158 C218.053198,77.3335819 214.375808,77.7472811 208.621851,77.7472811 L126.377028,77.7472811 Z"/>
      <path fill="#C3C3C3" d="M116.627983,75.3874588 C117.482626,73.6527073 128.384224,68.0045004 129.803288,65.4508342 C131.908373,62.6935597 133.335447,43.6684377 134.267792,31.1692629 L134.267792,30.0542199 L200.732368,30.0542199 L200.732368,31.1692629 C201.664713,43.6684377 203.091787,62.6935597 205.196872,65.4508342 C206.615936,68.0045004 217.517535,73.6527073 218.372177,75.3874588 C218.291111,76.5446802 213.446187,76.8036723 208.764758,76.8036723 L126.235562,76.8036723 C121.553973,76.8036723 116.709049,76.5446802 116.627983,75.3874588 Z"/>
      <path fill="#D5D2CF" d="M335,0.0112048541 L0,0.0112048541 L0,23.2451101 C0,27.6181245 3.55346724,31.1685426 7.93041607,31.1685426 L327.069584,31.1685426 C331.446533,31.1685426 335,27.6181245 335,23.2451101 L335,0.0112048541 Z"/>
    </g>
  </g>\n`;
  svg += `</g>\n`;

  // iMac screen: mocked video course UI
  const sX = imacX + 13.698 * imacScale;
  const sY = imacY + 13.326 * imacScale;
  const sW = 307.604 * imacScale;
  const sH = 172.875 * imacScale;
  svg += `<clipPath id="imac-screen"><rect x="${sX}" y="${sY}" width="${sW}" height="${sH}"/></clipPath>\n`;
  svg += `<g clip-path="url(#imac-screen)">\n`;
  svg += `  <rect x="${sX}" y="${sY}" width="${sW}" height="${sH}" fill="#f5f5f5"/>\n`;
  svg += `  <rect x="${sX}" y="${sY}" width="${sW}" height="12" fill="${NAVY}"/>\n`;
  const sideW = sW * 0.28;
  svg += `  <rect x="${sX}" y="${sY + 12}" width="${sideW}" height="${sH - 12}" fill="#e8e8e8"/>\n`;
  for (let i = 0; i < 6; i++) {
    svg += `  <rect x="${sX + 4}" y="${sY + 18 + i * 12}" width="${sideW - 8}" height="7" rx="1" fill="${i === 0 ? RED : '#ccc'}"/>\n`;
  }
  const vidX = sX + sideW + 4, vidY2 = sY + 16;
  const vidW = sW - sideW - 8, vidH = (sH - 24) * 0.6;
  svg += `  <rect x="${vidX}" y="${vidY2}" width="${vidW}" height="${vidH}" rx="2" fill="#1a1a1a"/>\n`;
  const playX = vidX + vidW / 2 - 5, playY = vidY2 + vidH / 2 - 6;
  svg += `  <polygon points="${playX},${playY} ${playX},${playY + 12} ${playX + 10},${playY + 6}" fill="${WHITE}" opacity="0.8"/>\n`;
  svg += `  <rect x="${vidX}" y="${vidY2 + vidH + 2}" width="${vidW}" height="3" rx="1" fill="#ddd"/>\n`;
  svg += `  <rect x="${vidX}" y="${vidY2 + vidH + 2}" width="${vidW * 0.35}" height="3" rx="1" fill="${RED}"/>\n`;
  for (let i = 0; i < 2; i++) {
    svg += `  <rect x="${vidX}" y="${vidY2 + vidH + 10 + i * 8}" width="${vidW * (i === 0 ? 0.7 : 0.5)}" height="4" rx="1" fill="#bbb"/>\n`;
  }
  svg += `</g>\n`;

  // ===== MACBOOK (drawn second = on top, overlapping iMac on the left) =====
  const mbScale = 216 / 3310;
  // Align MacBook bottom with iMac bottom
  const imacBottom = imacY + 277 * imacScale;
  const mbH = 1899 * mbScale;
  const mbX = 660, mbY = imacBottom - mbH;
  svg += `<g transform="translate(${mbX}, ${mbY}) scale(${mbScale})">\n`;
  svg += `  <g fill="none" fill-rule="evenodd">
    <g transform="translate(302)">
      <rect width="2706" height="1899" fill="#D5D2CF" rx="94"/>
      <rect width="2686" height="1879" x="10" y="10" fill="#4D4D4D" rx="84"/>
      <rect width="2666" height="1859" x="20" y="20" fill="#343434" rx="74"/>
      <path fill="#3E3E3E" d="M20,1763 L2686,1763 L2686,1805 C2686,1845.86907 2652.86907,1879 2612,1879 L94,1879 C53.1309285,1879 20,1845.86907 20,1805 L20,1763 Z"/>
      <rect width="2560" height="1600" fill="#343434" transform="translate(73 124)"/>
      <circle cx="1352" cy="71" r="10" fill="#3E3E3E"/>
    </g>
    <g transform="translate(0 1826)">
      <path fill="#A9A9A9" d="M350,73 C202.970972,73 86.3043049,55.6666667 0,21 L3310,21 C3224.55874,55.32 3109.35933,72.6516 2964.40176,72.9948 L350,73 Z"/>
      <rect width="3310" height="21" fill="#D5D2CF"/>
      <rect width="568" height="21" x="1372" fill="#9D9A97"/>
    </g>
  </g>\n`;
  svg += `</g>\n`;

  // MacBook screen: white bg + bonfire terminal logo + "21-day software trial"
  const mbScrX = mbX + (302 + 73) * mbScale;
  const mbScrY = mbY + 124 * mbScale;
  const mbScrW = 2560 * mbScale;
  const mbScrH = 1600 * mbScale;
  svg += `<clipPath id="mb-screen"><rect x="${mbScrX}" y="${mbScrY}" width="${mbScrW}" height="${mbScrH}"/></clipPath>\n`;
  svg += `<g clip-path="url(#mb-screen)">\n`;
  svg += `  <rect x="${mbScrX}" y="${mbScrY}" width="${mbScrW}" height="${mbScrH}" fill="#ffffff"/>\n`;

  // Bonfire Terminal full-color logo centered on screen
  // Logo is 600x195. Scale to ~78% of screen width, shift right for centering
  const logoTargetW = mbScrW * 0.78;
  const logoScale2 = logoTargetW / 600;
  const logoH = 195 * logoScale2;
  const logoX2 = mbScrX + (mbScrW - 600 * logoScale2) / 2 + 2; // +2 nudge right
  const logoY2 = mbScrY + (mbScrH - logoH) / 2 - 5; // slightly above center for trial text below

  svg += `  <g transform="translate(${logoX2}, ${logoY2}) scale(${logoScale2})">\n`;
  // Red bonfire circle
  svg += `    <g transform="translate(8, 25) scale(0.254)"><path d="${bonfireCirclePath}" fill="${RED}" transform="translate(255.1875,-0.375)"/></g>\n`;
  // BONFIRE text (gold) - using Orbitron outlined paths
  svg += `    <path d="${tp(orbitronFont, 'BONFIRE', 148, 78, 48)}" fill="${GOLD}"/>\n`;
  // TERMINAL text (navy)
  svg += `    <path d="${tp(orbitronFont, 'TERMINAL', 148, 140, 48)}" fill="${NAVY}"/>\n`;
  svg += `  </g>\n`;

  // "21-day software trial" text centered below logo
  const trialText = '21-DAY SOFTWARE TRIAL';
  const trialSize = 7;
  const trialW = tw(boldFont, trialText, trialSize);
  const trialX = mbScrX + (mbScrW - trialW) / 2 + 2;
  const trialY = logoY2 + logoH + 4;
  svg += `  <path d="${tp(boldFont, trialText, trialX, trialY, trialSize)}" fill="${NAVY}"/>\n`;

  svg += `</g>\n`;

  // ===== TRUST BAR =====
  const badges = ['MONEY-BACK GUARANTEE', 'SECURE CHECKOUT', 'ONE-TIME PAYMENT'];
  const badgeSize = 24;
  const badgeSpacing = W / 3;
  const badgeY = mainH + trustBarH / 2 + 5;
  const checkR = 17;

  for (let i = 0; i < badges.length; i++) {
    const cx = badgeSpacing * i + badgeSpacing / 2;
    const badgeTextW = tw(boldFont, badges[i], badgeSize);
    const totalW = checkR * 2 + 12 + badgeTextW;
    const startX = cx - totalW / 2;
    const circCX = startX + checkR;
    const circCY = badgeY - 4;

    // Gold circle
    svg += `<circle cx="${circCX}" cy="${circCY}" r="${checkR}" fill="${GOLD}"/>\n`;
    // White checkmark - shifted right +2 for better centering
    const ckX = circCX - 3;
    const ckY = circCY;
    svg += `<path d="M${ckX - 1} ${ckY} L${ckX + 3} ${ckY + 5} L${ckX + 9} ${ckY - 5}" fill="none" stroke="${WHITE}" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>\n`;
    // Badge text (larger)
    svg += `<path d="${tp(boldFont, badges[i], startX + checkR * 2 + 12, badgeY, badgeSize)}" fill="${WHITE}"/>\n`;
  }

  svg += `</svg>`;
  return svg;
}

// Generate both variants
const strokeSVG = buildSVG('stroke');
const glowSVG = buildSVG('glow');

fs.writeFileSync('D:/marketing/ds24-order-form-header-stroke.svg', strokeSVG);
fs.writeFileSync('D:/marketing/ds24-order-form-header-glow.svg', glowSVG);
console.log('Stroke: ' + Math.round(strokeSVG.length / 1024) + 'kb');
console.log('Glow: ' + Math.round(glowSVG.length / 1024) + 'kb');
