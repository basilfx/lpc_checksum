from setuptools import setup

# Setup definitions
setup(
    name="lpc_checksum",
    version="2.0.0",
    description="Python script to calculate LPC firmware checksums",
    long_description=open("README.rst").read(),
    author="Bas Stottelaar",
    author_email="basstottelaar@gmail.com",
    py_modules=["lpc_checksum"],
    install_requires=["intelhex"],
    platforms=["any"],
    license="MIT",
    url="https://github.com/basilfx/lpc_checksum",
    keywords="lpc mcu cortex nxp flashing",
    test_suite="tests",
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "lpc_checksum = lpc_checksum:run",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Embedded Systems",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5"
    ]
)
