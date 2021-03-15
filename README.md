# Technical Notes
## Solution Explanation
### Level 1
Used Python's slicing function to reverse the input string. If the input string is the same with the reversed, the **is_palindrome** function returns **True**.

### Level 2
An array of all possible palindromes for the input string are fetched first using the **get_palindromes** function. Then, the output from the previous function is used by the **get_longest_palindrome** function.

Two loops are used in the **get_palindromes** function.

- The outer for loop iterates through all the string's indices from the start to the end of string. Let index from for loop be **x**.
- The inner while loop starts with the index from the outer loop plus one. Let index used in while loop be **y** where its starting value is x + 1. This loop gets the substring in each iteration (string[x : y]) and checks if it is a palindrome. If it is a palindrome, that substring is added to an array. Then the loop continues until the end of the string.
- When the inner loop ends, the outer loop shifts to the next index and continues the substring checks.

In **get_longest_palindrome**, we iterate through the palindromes array. We used a variable called **longest_palindrome** which holds the longest palindrome. The length of the **longest_palindrome** is checked against the next string in the loop. If that next string is longer, we use that instead. The output we got when we reach the end of the loop is then returned by the function.

### Level 3
The solution for level 3 is not yet available.