#!/usr/bin/env python
"""
Script to apply regex substitutions to a text files.
Usage: the source file named as in string "sourefilename" is in the same
folder of the present python script
"""
import os, sys, re, shutil



thePath = os.path.dirname(os.path.abspath(__file__)) 
#we assume the file is in the same directory as this script


sourcefilename = "source.tex"  
#this is the name of the file to be converted, with extension


fullpath_in = os.path.join(thePath, sourcefilename)
#this creates the correct path for the source


outputfilename = "converted.wiki"  
#this is the name of the output file, with extension


fullpath_out = os.path.join(thePath, outputfilename)
#this creates the correct path for the output
     
 
def find(filepath_in, pattern):
	"""
	searches for a regex in a file and copies its first occurrence in a string
	"""
	# Read contents from file as a single string
	file_handle = open(filepath_in, 'r')
	file_string = file_handle.read()
	file_handle.close()

	# here the search and transfer in the string occurs
	match_obj = re.match(pattern, file_string)
	
	return match_obj.group(0)
	
	
def replace(filepath_in, filepath_out, pattern, replacement):
	"""
	apply regex substitutions to the content of a file, and writes it in a 
	new file
	"""
	# Read contents from file as a single string
	file_handle = open(filepath_in, 'r')
	file_string = file_handle.read()
	file_handle.close()

	
	# here the substitution occurs. The final flags mean: 
	# re.M = take care of the multiple lines
	# re.S = the "." regex includes the "newline" caracter
	# re.U = assumes the encoding is unicode
	file_string = re.sub(pattern, replacement, file_string, re.M|re.S|re.U)
	
	# Write contents to output file.
	# Using mode 'w' creates or overwrites the file.
	file_handle = open(filepath_out, 'w')
	file_handle.write(file_string)
	file_handle.close()
    
	return
	



# copies the header in a string for future use
# compiling the regex is crucial!
regexpress = re.compile(r"(.+?)\\begin{document}", re.M|re.S|re.U)  
header_string = find(fullpath_in, regexpress) 




# deletes the header
# compiling the regex is crucial!
regexpress = re.compile(r"(.+?)\\begin{document}", re.M|re.S|re.U)  
replacement = r"" 
replace(fullpath_in, fullpath_out, regexpress, replacement) 




# changes the inline math, from  $foo$    to  <math>foo</math>
# compiling the regex is crucial!
regexpress = re.compile(r"\$(.+?)\$", re.M|re.S|re.U)  
replacement = r"<math>\1</math>" 
replace(fullpath_out, fullpath_out, regexpress, replacement)    
     
