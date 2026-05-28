'use strict';

// pa11y-ci configuration for the built HTML documentation.
//
// Discovers every page under build/html and checks it against WCAG 2.1 AA.
// Build the site first so build/html exists.

const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');

const htmlRoot = path.resolve(__dirname, 'build', 'html');

const urls = fs
  .readdirSync(htmlRoot, { recursive: true })
  .filter((entry) => entry.endsWith('.html'))
  // Skip theme assets (e.g. _static/webpack-macros.html is a Jinja template,
  // not a rendered page); only audit real documentation pages.
  .filter((entry) => !entry.split(path.sep).includes('_static'))
  .sort()
  .map((entry) => pathToFileURL(path.join(htmlRoot, entry)).href);

module.exports = {
  defaults: {
    standard: 'WCAG2AA',
    runners: ['htmlcs'],
    timeout: 120000,
    chromeLaunchConfig: {
      // Use a system Chrome when PUPPETEER_EXECUTABLE_PATH is set (CI),
      // otherwise fall back to Puppeteer's bundled Chromium (local).
      executablePath: process.env.PUPPETEER_EXECUTABLE_PATH || undefined,
      args: ['--no-sandbox', '--disable-setuid-sandbox'],
    },
  },
  urls,
};
