# lpc_checksum
Python script to calculate LPC firmware checksums, based on the C version by
Roel Verdult. It can be used as a standalone application, or as a Python module
that integrates directly in a build environment (e.g. SCons). It does not need
to be compiled.

[![Linting](https://github.com/basilfx/lpc_checksum/actions/workflows/lint.yml/badge.svg)](https://github.com/basilfx/lpc_checksum/actions/workflows/lint.yml)
[![Testing](https://github.com/basilfx/lpc_checksum/actions/workflows/test.yml/badge.svg)](https://github.com/basilfx/lpc_checksum/actions/workflows/test.yml)
[![PyPI version](https://badge.fury.io/py/lpc-checksum.svg)](https://badge.fury.io/py/lpc-checksum)

## Requirements
The only requirement is Python 3.9 or newer.

## Installation
This module can be installed from Pypi via `pip install lpc_checksum`.

Alternatively, you can install the latest version by cloning this repository
and run `python setup.py install`.

## Usage
There are two ways of using `lpc_checksum`.

### Standalone
When installed via Pip or from source, the command `lpc_checksum` should be
available on your PATH. By default, it assumes the input file is a binary file.

`lpc_checksum <firmware.bin|hex> [--format=bin] [--read-only]`

Program exits with a non-zero error code when it failed.

### As a module
```
import lpc_checksum

checksum = lpc_checksum.checksum(input_file, [read_only=True])
```

On error, an exception will be raised.

## Tests
To run the tests, please clone this repository and run `poetry run pytest`.

## Contributing
See the [`CONTRIBUTING.md`](CONTRIBUTING.md) file.

## License
See the [`LICENSE.md`](LICENSE.md) file (MIT license).
