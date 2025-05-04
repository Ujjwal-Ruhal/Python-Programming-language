'''
Task 2: Write and Append Data to a File
-- Takes user input and writes it to a file named output.txt.
-- Appends additional data to the same file.
-- Reads and displays the final content of the file.

'''


with open('output.txt','w') as file:
    writing_data = file.write(input('Enter Text to write to the file: ') + '\n')
    print('Data successfully added to output.txt file ')

with open('output.txt','a') as file:
    appending_file = file.write(input('Enter additional text to append : ') + '\n')
    print('Data successfully added to output.txt file ')

with open('output.txt','r') as file:
    reading_file = file.read()
    print('the final content of output.txt file is: ')
    print(reading_file)

print('thank you')