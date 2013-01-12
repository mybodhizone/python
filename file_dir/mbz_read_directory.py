#This script builds a list of all absolute path names of
#regular files in the current directory

import os, sys
import os, sys
from stat import *

#This list is global, since recursive call is made 
mylistoffiles = []
def getfilesinalist(currdir):
    """Returns a list of all filenames, recursively, starting from currdir."""
    #check if the currdir refers to a valid path
    rettrue = os.path.exists(currdir)
    if not rettrue:
        print '%s is not a valid search path' %currdir
        return
    for f in os.listdir(currdir):
        #portable way for using absolute pathname is to use join
        pathname = os.path.join(currdir, f)
        #stat call to know the type of file
        mode = os.stat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            getfilesinalist(pathname)
        elif S_ISREG(mode):
            # It's a file, add it to the list
            mylistoffiles.append(pathname)
        else:
            # Unknown file type, print a message
            print 'Skipping %s' % pathname
    #return the list to the caller, though this is not used 
    #by the recursive calls.
    return mylistoffiles

if __name__ == '__main__':
   
   #get the current directory
   currdir = os.getcwd()
   allfiles = getfilesinalist(currdir)
   #if the directory is empty, print a message
   #this case can come only if, this script gets some 
   #argument other than the current working directory.
   #Note the truth value testing
   if not allfiles:
        print "Seems the directory is empty"
        os._exit(0)
   for files in allfiles:
        print files

