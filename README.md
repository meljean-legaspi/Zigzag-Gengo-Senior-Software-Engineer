# Technical Notes
## Running the Application
Run the following from the console:

     py palindrome_app.py

After that, the application asks for a string and prints the following:
- whether the whole string is a palindrome
- the longest palindrome substring we can get from the string

## Solution Explanation
### Level 1
Used Python's slicing function to reverse the input string. If the input string is the same with the reversed, the **is_palindrome** function returns **True**.

### Level 2
An array of all possible palindromes for the input string are fetched first using the **get_palindromes** function. Then, the output from the previous function is used by the **get_longest_palindrome** function.

A single while loop is used to get the palindromes. We iterate through the string. Using the slice function, we get the substring from index 0 (pointer) to the next character (nextPointer).

If the substring is the same with its reversed form:
- We add that substring to the palindromes array.
- Then, we shift the pointer variable to the index of the character next to the end of the substring.

If the substring is not the same, we just move the nextPointer variable to the next character and use the slice function again to get the substring from the pointer variable.

With this implementation, we don't get all the possible palindromes (i.e. palindromes within the palindromes).

In **get_longest_palindrome**, we iterate through the palindromes array. We used a variable called **longest_palindrome** which holds the longest palindrome. The length of the **longest_palindrome** is checked against the next string in the loop. If that next string is longer, we use that instead. The output we got when we reach the end of the loop is then returned by the function.

### Level 3
The solution for level 3 is not yet available.