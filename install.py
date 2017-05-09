#!/usr/bin/env python
import os
import subprocess
import random
import string
import glob

IGNORE_LIST = [
    ".idea",
    ".git",
    "install.py",
    "README.md"
]


def install_dots(dotfiles):

    for dotfile in dotfiles:
        dotfile_path = dot_home(dotfile)

        if is_link(dotfile_path):
            print("Already a symbolic link: {}".format(dotfile_path))
        else:
            link_dotfile(dotfile)


def is_link(file_name):
    return os.path.islink(file_name)


def dot_home(dotfile):
    home = os.getenv("HOME")
    return os.path.join(home, ".{}".format(dotfile))


def dot_workstation(dotfile):
    """Return the full path of dotfile without the dot"""
    install_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(install_path, dotfile)


def link_dotfile(dotfile):
    source = dot_workstation(dotfile)
    target = dot_home(dotfile)

    print("Linking {} with {}".format(source, target))

    try:
        os.symlink(source, target)
    except OSError:
        print("Remove the file {} before linking".format(target))


def main():
    current_path = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(current_path)

    dotfiles = list(set(files) - set(IGNORE_LIST))
    install_dots(dotfiles)

if __name__ == '__main__':
    main()
