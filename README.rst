lpc\_checksum
=============

Python script to calculate LPC firmware checksums, based on the C
version by Roel Verdult. It can be used as a stand alone application, or
as a Python module to integrate it directly in a build environment (e.g.
SCons). It does not require to be compiled.

Requirements
------------

The only requirement is Python 2.7.

Installation
------------

This module can be installed from Pypi via ``pip install lpc_checksum``.
Alternatively, you can install the latest version by cloning this
repository and run ``python setup.py install``.

Usage
-----

There are two ways of using ``lpc_checksum``.

Stand alone
~~~~~~~~~~~

When installed via Pip or from source, the command ``lpc_checksum``
should be available on your PATH.

``lpc_checksum <firmware.bin> [--readonly]``

Program exits with a non-zero error code when it failed.

As a module
~~~~~~~~~~~

::

    import lpc_checksum
    checksum = lpc_checksum.checksum(input_file, [readonly=True])

On error, an exception will be raised.

License
-------

See the ``LICENSE`` file (MIT license).
