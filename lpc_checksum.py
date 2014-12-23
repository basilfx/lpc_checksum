#!/usr/bin/env python

import sys
import os
import struct
import argparse

__version__ = "1.0.1"

"""
Calculate checksum image for LPC firmware images and write. Code is a Python
port of the C version written by Roel Verdult named `lpcrc'.
"""

BLOCK_COUNT = 7
BLOCK_LENGTH = 4
BLOCK_TOTAL = (BLOCK_COUNT * BLOCK_LENGTH)

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

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input firmware for checksumming")
    parser.add_argument("-r", "--readonly", action="store_true",
                        help="read only mode (do not write checksum to file)")
    options = parser.parse_args()

    # Calculate checksum
    try:
        result = checksum(options.filename, options.readonly)
    except Exception as e:
        sys.stdout.write("Error: %s\n" % (e.strerror or e.message))
        return 1

    # Done
    sys.stdout.write("Succesfully updated CRC to 0x%08x\n" % result)

def checksum(filename, read_only=False):
    """
    Calculate the checksum of a given binary image. The checksum is written back
    to the file and is returned. When read_only is set to True, the file will
    not be changed

    filename  -- firmware file to checksum
    read_only -- whether to write checksum back to filename or not
    """

    with open(filename, "rb+") as handle:
        block = handle.read(BLOCK_TOTAL)

        # Read out the data blocks used for crc calculation
        if len(block) != BLOCK_TOTAL:
            raise Exception("Could not read required bytes")

        # Compute the CRC value
        crc = 0

        for i in range(BLOCK_COUNT):
            value, = struct.unpack_from("I4", block, i * BLOCK_LENGTH)
            crc += value

        crc = ((~crc) + 1) & 0xFFFFFFFF

        # Write CRC bakc to the file
        if not read_only:
            handle.seek(0, os.SEEK_CUR)
            handle.write(struct.pack("I4", crc))

        # Done
        return crc

# Invoke main when started from command line
if __name__ == "__main__":
    run()