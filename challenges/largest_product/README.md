# Largest product of 2 adjacent values in a 2D array

## Challenge
Write a function called LargestProduct which takes in a 2D array. Without utilizing any of the built-in methods available to your language, return the largest product of 2 adjacent values within the 2D array.

##Solution
First we will declare a counter, an answer and an empty list. Next you will loop through the outside list while incrementing our counter as it itterates through each item and assign the product of each item to the index of the empty list. We will then loop through our new list and compare if our answer is less than our item. If true, it will reassign answer to that value.

![Whiteboarding](https://github.com/bhold6160/data-structures-and-algorithms/assets/largest_product.jpg)