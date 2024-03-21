# Unit 7 Homework 2

This homework is from Python Crash Course, 3rd Edition, by Eric Matthes. To submit this homework, you will need to attach a link to your GitHub repo in Google Classroom

## Problem 1
Guest Book: Write a while loop that prompts users for their name. Collect all the names that are entered, and then write these names to a file called guest_book.txt. Make sure each entry appears on a new line in the file. Make the loop stop when someone types 'exit'.

## Problem 2

Suppose you have the following dictionary:
```
class_test_data={
        "Billy Bot":{"Test 1":95,"Test 2":90,"Test 3":87},
        "Samantha Smith":{"Test 1":85,"Test 2":88,"Test 3":91},
        "John Doe":{"Test 1":78,"Test 2":82,"Test 3":79},
        "Emily Jones":{"Test 1":92,"Test 2":95,"Test 3":96},
        "Michael Brown":{"Test 1":88,"Test 2":84,"Test 3":90}
}
```
Write a function called grade_book_creator that will take in the dictionary file and make a text file for each person with their grades in it. The filename should be their name.txt and the contents would look like the following:
```
Name: Billy Bot
Test 1: 95
Test 2: 90
Test 3: 87
```
