import os
import subprocess
import sys
import shlex


def get_platform():
    if sys.platform == "win32":
        return "windows"
    elif sys.platform == "darwin":
        return "macosx"
    elif sys.platform.startswith("linux"):
        return "linux"
    else:
        return sys.platform


def run(command_line, working_directory=None, check_exit_code=False):
    environ = os.environ

    if working_directory is None:
        working_directory = os.getcwd()

    # out = ""
    print "Running \"{}\" in \"{}\"...".format(command_line, working_directory)
    parts = shlex.split(command_line)
    try:
        process = subprocess.Popen(parts,
                                   cwd=working_directory,
                                   env=environ,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   shell=False
                                   )
        for line in iter(process.stdout.readline, ''):
            # unmodified_line = line
            line = line.rstrip()
            print line
            sys.stdout.flush()
            # out += unmodified_line
        process.stdout.close()
        process.wait()
        if check_exit_code and process.returncode != 0:
            raise Exception("Error while running command:\n{}\nin:\n{}".format(command_line, working_directory))
        return process.returncode  # , out
    except IOError as (error, strerror):
        del error, strerror
        raise
    except:
        raise
