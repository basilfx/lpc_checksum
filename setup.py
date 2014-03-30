try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Setup definitions
setup(
    name="lpc_checksum",
    version="1.0",
    description="Python script to calculate LPC firmware checksums",
    author="Bas Stottelaar",
    author_email="basstottelaar@gmail.com",
    py_modules=["lpc_checksum"],
    license = "MIT",
    keywords = "lpc mcu cortex nxp",
    entry_points={
        "console_scripts": [
            "lpc_checksum = lpc_checksum:run",
        ]
    },
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Embedded Systems",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],
)