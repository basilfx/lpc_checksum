import os
import unittest
import lpc_checksum


class LpcChecksumTest(unittest.TestCase):
    """
    Test cases for `lpc_checksum`.
    """

    def test_checksum__binary(self):
        """
        Test the `checksum` method using a binary file.
        """

        path = os.path.join(
            os.path.dirname(__file__), "data", "hello-world.bin")
        checksum = lpc_checksum.checksum(path, format="bin", read_only=True)

        self.assertEqual(checksum, 0xefffe722)

    def test_checksum__hex(self):
        """
        Test the `checksum` method using a HEX file.
        """

        path = os.path.join(
            os.path.dirname(__file__), "data", "hello-world.hex")
        checksum = lpc_checksum.checksum(path, format="hex", read_only=True)

        self.assertEqual(checksum, 0xefffe722)

    def test_checksum__hex_high_start(self):
        """
        Test the `checksum` method using a HEX file where the start address is
        not zero.
        """

        path = os.path.join(
            os.path.dirname(__file__), "data", "high-start-address.hex")
        checksum = lpc_checksum.checksum(path, format="hex", read_only=True)

        self.assertEqual(checksum, 0x53e48792)

    def test_checksum__overflow(self):
        """
        Test the `checksum` method given a binary value that generates an
        overflow.

        See https://github.com/basilfx/lpc_checksum/issues/2.
        """

        path = os.path.join(
            os.path.dirname(__file__), "data", "overflow.bin")
        checksum = lpc_checksum.checksum(path, format="bin", read_only=True)

        self.assertEqual(checksum, 0x02b6aa66)
