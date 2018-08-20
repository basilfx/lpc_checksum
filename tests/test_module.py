import os
import unittest
import lpc_checksum


class LpcChecksumTest(unittest.TestCase):
    """
    Test cases for `lpc_checksum`.
    """

    def test_checksum__binary(self):
        """
        Test checksum from a binary file.
        """

        path = os.path.join(
            os.path.dirname(__file__), "data", "hello-world.bin")
        checksum = lpc_checksum.checksum(path, format="bin", read_only=True)

        self.assertEqual(checksum, 0xefffe722)

    def test_checksum__hex(self):
        """
        Test checksum from a HEX file.
        """

        path = os.path.join(
            os.path.dirname(__file__), "data", "hello-world.hex")
        checksum = lpc_checksum.checksum(path, format="hex", read_only=True)

        self.assertEqual(checksum, 0xefffe722)
