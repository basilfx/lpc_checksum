# lpc_checksum v1.0
Python script to calculate LPC firmware checksums, based on the C version by Roel Verdult. Can be used as a stand alone application, or as a Python module to integrate directly in a build environment (e.g. SCons).

## Requirements
* Python 2.7

## Usage
There are two ways of using `lpc_checksum`.

### Stand alone
`lpc_checksum.py <firmware.bin> [--readonly]`

Program exits with a non-zero error code when it failed.

### As a module
```
import lpc_checksum
checksum = lpc_checksum.checksum(input_file, [readonly=True])
```

On error, an exception is thrown.

## License
See the `LICENSE` file (MIT license).