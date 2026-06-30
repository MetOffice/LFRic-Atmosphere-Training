# Vendored Sphinx Extensions

This directory contains local Sphinx extensions used to build the training
materials without fetching extension code from unmaintained external Git
repositories at build time.

## Quizdown Provenance

| Component | Local file | Upstream source | Upstream license | Local license |
| --- | --- | --- | --- | --- |
| `sphinxcontrib-quizdown` extension | `source/_extensions/quizdown.py` | [`sphinxcontrib/quizdown/__init__.py` at `d9f24a7a2305ad5b196e06597b1779c9414d1d85`](https://github.com/bonartm/sphinxcontrib-quizdown/blob/d9f24a7a2305ad5b196e06597b1779c9414d1d85/sphinxcontrib/quizdown/__init__.py) | [`LICENSE` at `d9f24a7a2305ad5b196e06597b1779c9414d1d85`](https://github.com/bonartm/sphinxcontrib-quizdown/blob/d9f24a7a2305ad5b196e06597b1779c9414d1d85/LICENSE) | `source/_extensions/licenses/sphinxcontrib-quizdown-LICENSE.txt` |
| `quizdown-js` browser asset | `source/_static/vendor/quizdown/quizdown.js` | [`public/build/quizdown.js` at `v0.6.0`](https://github.com/bonartm/quizdown-js/blob/v0.6.0/public/build/quizdown.js) | [`LICENSE` at `v0.6.0`](https://github.com/bonartm/quizdown-js/blob/v0.6.0/LICENSE) | `source/_static/vendor/quizdown/LICENSE.txt` |

The vendored `quizdown-js` file was downloaded from:

<https://cdn.jsdelivr.net/gh/bonartm/quizdown-js@0.6.0/public/build/quizdown.js>

Its SHA256 is:

`e48994e393ebbd939e6f6c50eb1d0e130d1a43e9b08c8386bcf4e42f4b0cba8c`
