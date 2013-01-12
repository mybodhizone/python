#This script finds all files having some specific extension names

import os, sys, re
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

def builddictoffiles(mylistoffiles):
    """Returns a dictionary of {absolute pathname, filename}"""
    #making an empty dictionary
    mydictoffiles = {}
    for f in mylistoffiles:
        #basename returns the last component of the absolute path
        filename  = os.path.basename(f)
        #key = absolute pathname, value = filename
        mydictoffiles[f] = filename
    return mydictoffiles


def makeregex(mylistofextnames ):
    """Returns a regular expression object for matching extension names"""

    #Note the use of map, re.escape,join
    myregexstring = '|'.join(map(appenddollar, map(re.escape, mylistofextnames)))
    #print myregexstring

    #getting regexobject 
    myregexobj = re.compile(myregexstring) 

    return myregexobj

def appenddollar(mystr):
    return mystr + '$'

if __name__ == '__main__':
   
   #Have a string of file extensions, separated by spaces
   myfileextnames = '.doc .exe .c .o .obj .h'

   #get the current directory
   currdir = os.getcwd()
   allfiles = getfilesinalist(currdir)
   #if the directory is empty, print a message and exit
   #this case can come only if, this script gets some 
   #argument other than the current working directory.
   #Note the truth value testing
   if not allfiles:
        print "Seems the directory is empty exiting !!"
        os._exit(0)
   #Now create the dictionary of absolute pathnames + filenames
   mydictoffiles = builddictoffiles(allfiles)

   #Now use the split function to make a list from the space separated string
   mylistofextnames = myfileextnames.split()
   myregexobject = makeregex(mylistofextnames)

   #Now iterate the dictionary 
   for key, value in mydictoffiles.items():
        #Search for matching extnames
        searchstat = myregexobject.search(value)
        if searchstat:
            print key, value



