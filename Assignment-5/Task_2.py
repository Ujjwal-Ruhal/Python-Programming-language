'''
Task 2: Demonstrate List Slicing
-----> Creates a list of numbers from 1 to 10.
-----> Extracts the first five elements from the list.
-----> Reverses these extracted elements.
-----> Prints both the extracted list and the reversed list

'''

# create a list
numbers = [1,2,3,4,5,6,7,8,9,10]
#          | | | | | | | | | |
# index no.0 1 2 3 4 5 6 7 8 9
print('the list is: '+ str(numbers))

print('Extracts the first five elements: ' + str(numbers[0:5]))

print('Reversed extracted elements: ' + str(numbers[4::-1]))
print('Thank you')
