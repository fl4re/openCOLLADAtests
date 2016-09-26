import errno
import os
import subprocess
import sys

def get_platform():
    if sys.platform == "win32":
        return "windows"
    elif sys.platform == "darwin":
        return "macosx"
    elif sys.platform.startswith("linux"):
        return "linux"
    else:
        return sys.platform
            
def run(commandLine, workingDirectory, checkExitCode=True):
    out = ""
    print "Running \"{}\" in \"{}\"...".format(commandLine, workingDirectory)
    
    if isinstance(commandLine, list):
        parts = commandLine
    else:
        parts = commandLine.split()
        
    try:
        process = subprocess.Popen(parts, 
                                   cwd=workingDirectory,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   shell=(get_platform()=="windows")
                                   )
        for line in iter(process.stdout.readline, ''):
            unmodifiedLine = line
            line = line.rstrip()
            print line
            sys.stdout.flush()
            out += unmodifiedLine
        process.stdout.close()
        process.wait()
        if checkExitCode and process.returncode != 0:
            raise Exception("Error while running command:\n{}\nin:\n{}".format(commandLine, workingDirectory))
        return (process.returncode, out)
    except IOError, (errno, strerror):
        raise
    except:
        raise
    return (1, out)