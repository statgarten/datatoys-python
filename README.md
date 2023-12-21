# datatoys-python <img src="assets/logo.png" align="right" width="120" />

[![](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/) [![](https://img.shields.io/github/license/ResidentMario/missingno.svg)](https://github.com/statgarten/datatoys-python/blob/main/LICENSE.md) [![Downloads](https://static.pepy.tech/badge/datatoys)](https://pepy.tech/project/datatoys)

## Overview

`datatoys-python`는 통계, 데이터분석 입문하시는 분들이 쉽게 사용할 수 있는 공공데이터 패키지입니다. [`statgarten/datatoys`](https://github.com/statgarten/datatoys) R 패키지의 데이터를 파이썬에 `pandas.DataFrame` 형식으로 쉽게 불러올 수 있습니다. 데이터를 장난감처럼 가지고 놀아보세요 🧸.

`datatoys-python` is a Python library for loading the curated list of datasets from the [`statgarten/datatoys`](https://github.com/statgarten/datatoys) R library.

## Installation

![installation](https://github.com/statgarten/datatoys-python/blob/main/assets/install.gif)

```bash
# Install from pip
pip install datatoys
```

## Usage

![usage](https://github.com/statgarten/datatoys-python/blob/main/assets/demo.gif)

Checkout the [example notebook image](assets/notebook-example.png) for a quick start.

## A List of datasets

[statgarten/datatoys dataset list](https://github.com/statgarten/datatoys#a-list-of-datasets)

## Test

```python
pytest -s
```