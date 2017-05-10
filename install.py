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
HOME = os.getenv("HOME")

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

def install_custom_zsh():
    """Install custom zsh plugins"""

    source = dot_workstation("zsh/custom")
    target = os.path.join(HOME, ".oh-my-zsh/custom")

    if is_link(target):
            print("Already a symbolic link: {}".format(target))
            return

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
    install_custom_zsh()

if __name__ == '__main__':
    main()
