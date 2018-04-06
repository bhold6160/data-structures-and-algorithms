# Multi-bracket Validation.
<!-- Short summary or background information -->

## Challenge
 Create a function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced.

## Solution
I first created two lists, one with the opening bracket variations and one with closing bracket variations. I then stored those values into a dictionary assigning the keys to the opening brackets and the values to the closing brackets. I then itterate through the string passed in when the function is called and check it against the items in opening. If a match is found its added appended to my 