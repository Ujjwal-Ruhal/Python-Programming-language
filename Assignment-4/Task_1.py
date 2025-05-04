'''
Task 1: Read a File and Handle Errors 
-- Opens and reads a text file named sample.txt.
-- Prints its content line by line.
-- Handles errors gracefully if the file does not exist.

'''
try:
    file= open("sample.txt",'r')
    reading_file=file.read()
    print(reading_file)
    file.close()
except FileNotFoundError:
    print('file does not exit, make sure you created this file ')
