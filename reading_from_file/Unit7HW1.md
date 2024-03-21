# Unit 7 Homework 1

This homework is from Python Crash Course, 3rd Edition, by Eric Matthes. To submit this homework, you will need to attach a link to your GitHub repo in Google Classroom

## Problem 1
Open a blank file in your text editor called my_learning.txt and write a few lines summarizing what you’ve learned about Python so far. Start each line with the phrase "In Python you can. . . ."
Save the file my_learning.txt in the same directory as your exercises from this chapter. Write a program that reads the file
and prints what you wrote two times: print the contents once by reading in the entire file, and once by storing the lines in a list and then looping over each line.

## Problem 2
You can use the replace() method to replace any word in a string with a different word. Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:
```
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
```
Read in each line from the file you just created, my_learning.txt, and replace the word Python with the name of another language, such as C. Print each modified line to the screen.

## Problem 3
The program file_reader.py in this section uses a temporary variable, lines, to show how splitlines() works. You can skip the temporary variable and loop directly over the list that splitlines() returns:

```for line in contents.splitlines():```

Remove the temporary variable from each of the programs in this section, to make them more concise.
