#!/usr/bin/env python

import sys
import struct
import argparse
import intelhex

__version__ = "2.2.0"

"""
Calculate checksum image for LPC firmware images and write. Code is a Python
port of the C version written by Roel Verdult named `lpcrc'.

The checksum is the two's-complement of the sum of the first seven 4-byte
blocks (w.r.t the start address). This value is placed in the eight block.
"""

BLOCK_COUNT = 7
BLOCK_SIZE = 4
BLOCK_TOTAL = (BLOCK_COUNT * BLOCK_SIZE)


def run():
    """
    Entry point for console script.
    """
    sys.exit(main())


def main():
    """
    Command line wrapper for the checsum() method. Requires the first parameter
    to be the filename. If no filename is given, the syntax will be printed.
    Output is written to stdout and errors to stderr.
    """

    # Parse arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename", type=str, help="input file for checksumming")
    parser.add_argument(
        "-f", "--format", action="store", type=str, default="bin",
        choices=["bin", "hex"], help="input file format (defaults to bin)")
    parser.add_argument(
        "-r", "--readonly", action="store_true",
        help="read only mode (do not write checksum to file)")
    options = parser.parse_args()

    # Calculate checksum.
    try:
        result = checksum(
            options.filename, options.format, options.readonly)
    except Exception as e:
        sys.stdout.write("Error: %s\n" % e)
        return 1

    # Done.
    sys.stdout.write("Succesfully updated checksum to 0x%08x\n" % result)


def checksum(filename, format="bin", read_only=False):
    """
    Calculate the checksum of a given binary image. The checksum is written
    back to the file and is returned. When read_only is set to True, the file
    will not be changed.

    filename  -- firmware file to checksum
    format    -- input file format (bin or hex, default bin)
    read_only -- whether to write checksum back to the file (default False)
    """

    # Open the firmware file.
    handle = intelhex.IntelHex()
    handle.loadfile(filename, format=format)

    block_start = handle.minaddr()

    # Read the data blocks used for checksum calculation.
    block = bytearray(handle.gets(block_start, BLOCK_TOTAL))

    if len(block) != BLOCK_TOTAL:
        raise Exception("Could not read the required number of bytes.")

    # Compute the checksum value.
    result = 0

    for i in range(BLOCK_COUNT):
        value, = struct.unpack_from("I", block, i * BLOCK_SIZE)
        result = (result + value) & 0xFFFFFFFF

    result = ((~result) + 1) & 0xFFFFFFFF

    # Write checksum back to the file.
    if not read_only:
        handle.puts(block_start + BLOCK_TOTAL, struct.pack("I", result))
        handle.tofile(filename, format=format)

    # Done
    return result


# E.g. `python lpc_checksum.py --format bin firmware.bin`.
if __name__ == "__main__":
    run()
