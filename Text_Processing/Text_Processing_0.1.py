#!/usr/bin/env python
import re
import sys

#Regular expression to serch the word string from beginning of the line
MY_REG_EXPR1 = '^mystring'

#Input File and Output File
MY_INPUT_FILE_NAME = 'mbz_config.txt'
MY_OUTPUT_FILE_NAME = 'mbz_script.txt'
MY_NEW_OUTPUT_FILE ='mbz_newscript.txt'

#Function definitions follow
   
##########################################################################
def open_file(filename, file_opening_mode):
    try:
        myfilehandle = open(filename, file_opening_mode)
    except IOError:
        print "Cannot open file - " , filename, "exiting!\n"
        sys.exit(1)
    #print "Opened successfully - " + filename + "\n"
    return myfilehandle
###########################################################################

##########################################################################
#Function to read all lines, from a file and return the list of all lines.

###########################################################################

def read_all_lines_from_file(myfilehandle):
    #read all the lines
    all_lines = myfilehandle.readlines()
    if not all_lines:
        print "Seems your  file is empty!!! \n"
    #close file handle, already all data have been read
    myfilehandle.close()
    return all_lines
############################################################################

###########################################################################
#Function to accept the lines from the input and output files
#and do the processing 
############################################################################

def compare_lines(lines_from_input_file, lines_from_output_file):
  
    #If suppose the config file was empty, then return all the lines
    #of the hit script
    if not lines_from_input_file:
        print "Your first file was empty!!!\n"
        return lines_from_output_file

    #Now do the normal case.
    
    #The regular expression below -finds  the word string at the beginning
    myregexobj = re.compile(MY_REG_EXPR1)
    for ip_line in lines_from_input_file: #Iterate over lines, from config file
        my_new_list_of_lines = [] #This is the list of lines, that will be finally returned
        #Split lines from config file into two parts (with = as the delimiter)
        ip_broken_line = ip_line.split('=')
        for op_line in lines_from_output_file: #lines from script file
        #for those lines, which have the word string from beginning
            searchstat = myregexobj.search(op_line)
            #Successful means I have got a declaration line
            #Now search for the variable Name, which ip_broken_line[0]
            if searchstat:
                ret = op_line.find(ip_broken_line[0])
                if (ret > -1): #When not found find method returns -1
                    #Here Need to make the new ouptput line
                    op_broken_line = op_line.split('=')
                    #The 2nd part of the line in the script is discarded.
                    #modified_line = op_broken_line[0] + '=' + ip_broken_line[1]
                    #Removing spaces from left hand side of the string
                    modified_line = op_broken_line[0] + '=' + ip_broken_line[1].lstrip()
                    my_new_list_of_lines.append(modified_line)
                    
                else:
                    my_new_list_of_lines.append(op_line)
                    
            else:
                my_new_list_of_lines.append(op_line)
        #Now need to update the list of lines in the output file's list
        del lines_from_output_file #clear the earlier list of lines
        lines_from_output_file = list(my_new_list_of_lines) #deep copy a list
    return my_new_list_of_lines
                    
##############################################################################
                
##############################################################################      
#Function to write modified lines to the file.
#line_to_be_written is a list containing all the lines, including the
#modified lines.
##############################################################################

def update_file_with_line(filename, lines_to_be_written):
    try:
        file_handle = open(filename, 'w')
    except IOError:
        print "Cannot open  file - " , filename , "for writing\n"
        return
    try:
        for my_line in lines_to_be_written:
            file_handle.write(my_line)
    except IOError:
        print "Error - while writing  to file  " , filename , "\n"
        print "Exiting - Usuccessfully\n"
        #file_handle.close()
        sys.exit(1)
    file_handle.close()
    return
##############################################################################

##############################################################################
#Function to print contents of a line
##############################################################################
def my_display_file(filename):
    my_file_handle = open_file(filename, 'r')
    lines_from_file = read_all_lines_from_file(my_file_handle)
    for single_line in lines_from_file:
        print single_line
    return
##############################################################################    
                          
       
#Start the actual script here
  
myinfilehandle = open_file(MY_INPUT_FILE_NAME, 'r')

myoutputfilehandle = open_file(MY_OUTPUT_FILE_NAME, 'r')

lines_from_inputfile = read_all_lines_from_file(myinfilehandle)

lines_from_outputfile = read_all_lines_from_file(myoutputfilehandle)

all_lines_including_new = compare_lines(lines_from_inputfile, lines_from_outputfile)

#Now update the file
update_file_with_line(MY_NEW_OUTPUT_FILE, all_lines_including_new)

#displaing the updated file
print "\nDisplaying the Modified File\n"

my_display_file(MY_NEW_OUTPUT_FILE)

print "\nExiting Successfully\n"




