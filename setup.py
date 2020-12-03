# -*- coding: utf-8 -*-
from setuptools import setup

# TODO: if py gets upgrade to >=1.6,
#       remove _width_of_current_line in terminal.py

def main():
    setup(
        package_dir={"": "src"},
    )


if __name__ == "__main__":
    main()
