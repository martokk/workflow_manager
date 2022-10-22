# workflow_manager

---

---

## Very first steps (DELETE THIS AFTER COMPLETING!)

### Initialize your code

1. Initialize `git` inside your repo:

```bash
cd workflow_manager && git init
```

2. If you don't have `Poetry` installed run:

```bash
make poetry-download
```

3. Initialize poetry and install `pre-commit` hooks:

```bash
make install
make pre-commit-install
```

4. Run the codestyle:

```bash
make codestyle
```

5. Upload initial code to GitHub:

```bash
git add .
git commit -m ":tada: Initial commit"
git branch -M main
git remote add origin https://github.com/martokk/workflow_manager.git
git push -u origin main
```

Read more on the DEV_README.md file.

---

---

<div align="center">

[![Build status](https://github.com/martokk/workflow_manager/workflows/build/badge.svg?branch=master&event=push)](https://github.com/martokk/workflow_manager/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/workflow_manager.svg)](https://pypi.org/project/workflow_manager/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/martokk/workflow_manager/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/martokk/workflow_manager/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/martokk/workflow_manager/releases)
[![License](https://img.shields.io/github/license/martokk/workflow_manager)](https://github.com/martokk/workflow_manager/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

A python library for the vApp's 'workflow_manager' applications.

</div>

---

## Features

## Installation

```bash
pip install -U workflow_manager
```

or install with `Poetry`

```bash
poetry add workflow_manager
```



## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/martokk/workflow_manager/releases) page.

## 🛡 License

[![License](https://img.shields.io/github/license/martokk/workflow_manager)](https://github.com/martokk/workflow_manager/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/martokk/workflow_manager/blob/master/LICENSE) for more details.

## What's next

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)
