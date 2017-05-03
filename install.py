#!/usr/bin/env python
import os
import subprocess
import random, string

def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))

def run_command(cmd):
    return subprocess.check_output(cmd.split(' '))

def backup_dots(files):
    backup_folder = "/tmp/{}".format(randomword(10))
    home = os.getenv("HOME")
    run_command("mkdir -p {}".format(backup_folder))

    print("Creating a backup folder:{}".format(backup_folder))

    for file_name in files:
        run_command("cp {}/{} {}".format(home, file_name, backup_folder))

def is_link(file_name):
    return os.path.islink(file_name)

def main():
    backup_list = []
    for file_name in os.listdir('.'):
        if file_name[0] == '.':
            if not is_link(file_name):
                backup_list.append(file_name)

    backup_dots(backup_list)

if __name__ == '__main__':
    main()
      