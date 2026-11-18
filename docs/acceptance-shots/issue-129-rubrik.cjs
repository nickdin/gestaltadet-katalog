// Ärende #129: startsidans rubrik och sidan för Applikationsgränssnitt (C-139)
// ska rymmas i ett 390 px brett fönster, i ljust och mörkt läge.
//
// Körs från lagrets rot:   node docs/acceptance-shots/issue-129-rubrik.cjs [bas-url] [bildprefix]
// Utan bas mäter skriptet den publicerade sajten, https://gestaltadet.se/.
// En bas är en mapp-URL som slutar på "/" (för en sparad kopia: file:///sökväg/till/kopian/).
// Med ett bildprefix sparar skriptet en skärmbild per mätning som <prefix>-<sida>-<läge>.png.
//
// En sida godkänns när document.documentElement.scrollWidth inte är större än
// window.innerWidth. Skriptet skriver också ut rubrikens egna scrollWidth och clientWidth,
// men bedömer dem inte: en klippt rubrik fäller inte provet.
// Slutkod 0 när alla fyra mätningarna godkänns, 1 när någon faller.

const { chromium } = require('/home/nickdin/.npm/_npx/e41f203b7505f1fb/node_modules/playwright');

const base = process.argv[2] || 'https://gestaltadet.se/';
const shotPrefix = process.argv[3] || null;
const isFile = base.startsWith('file:');
const pages = [
  { name: 'startsida', path: isFile ? 'index.html' : '' },
  { name: 'C-139', path: 'katalog/file/C-139/index.html' },
];

(async () => {
  const browser = await chromium.launch({ executablePath: '/usr/bin/chromium' });
  let failures = 0;
  for (const page of pages) {
    for (const scheme of ['light', 'dark']) {
      const context = await browser.newContext({
        viewport: { width: 390, height: 844 },
        colorScheme: scheme,
      });
      const tab = await context.newPage();
      await tab.goto(base + page.path, { waitUntil: 'load' });
      const m = await tab.evaluate(() => {
        const h1 = document.querySelector('h1');
        return {
          page: document.documentElement.scrollWidth,
          window: window.innerWidth,
          heading: h1 ? h1.textContent.trim() : null,
          headingScroll: h1 ? h1.scrollWidth : null,
          headingClient: h1 ? h1.clientWidth : null,
          hyphens: h1 ? getComputedStyle(h1).hyphens : null,
          overflowWrap: h1 ? getComputedStyle(h1).overflowWrap : null,
        };
      });
      if (shotPrefix) await tab.screenshot({ path: `${shotPrefix}-${page.name}-${scheme}.png` });
      const ok = m.page <= m.window;
      if (!ok) failures += 1;
      console.log(
        `${page.name} ${scheme}: page scrollWidth ${m.page}, window ${m.window}, ` +
        `h1 scrollWidth ${m.headingScroll}, clientWidth ${m.headingClient}, ` +
        `hyphens ${m.hyphens}, overflow-wrap ${m.overflowWrap} -> ${ok ? 'PASS' : 'FAIL'}`
      );
      await context.close();
    }
  }
  await browser.close();
  console.log(failures === 0 ? 'all four measurements pass' : `${failures} of 4 measurements fail`);
  process.exit(failures === 0 ? 0 : 1);
})();
