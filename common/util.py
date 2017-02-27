import os
import subprocess
import sys
import shlex


#
# Utility functions.
#

# Returns current platform as a string.
def get_platform():
    if sys.platform == "win32":
        return "windows"
    elif sys.platform == "darwin":
        return "macosx"
    elif sys.platform.startswith("linux"):
        return "linux"
    else:
        return sys.platform


# Runs a subprocess.
def run(command_line, working_directory=None):
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
        stdout, stderr = process.communicate(None)
        if stdout is not None:
            print stdout
        if stderr is not None:
            print stderr
        return process.returncode
    except IOError as (error, strerror):
        del error, strerror
        raise
    except:
        raise


# Finds a file in root_dir and returns found file's full path.
def find_file(root_dir, filename, parent_dir_partial_name=''):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if parent_dir_partial_name == '' or dirpath.endswith(parent_dir_partial_name):
            for f in filenames:
                if f == filename:
                    return os.path.join(dirpath, f)
    return ''


# Returns true if str ends with one of the strings in strs.
def ends_with(str, strs):
    for s in strs:
        if str.endswith(s):
            return True
    return False


# Lists files in root_dir, recursively or not.
def list_files(root_dir, exts, recursive):
    file_list = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if ends_with(filename, exts):
                file_list.append(os.path.join(dirpath, filename))
        if not recursive:
            break
    return file_list
