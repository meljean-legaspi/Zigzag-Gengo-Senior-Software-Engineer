class PalindromeChecker:

    def is_palindrome(self, string):
        return string == string[::-1]

    def get_palindromes(self, string):
        string_length = len(string)
        palindromes = []
        pointer = 0
        nextPointer = pointer + 1
        while (pointer < string_length and nextPointer < string_length):
            sub_string = string[pointer:nextPointer + 1]
            if self.is_palindrome(sub_string):
                palindromes.append(sub_string)
                pointer = nextPointer + 1
                nextPointer = pointer + 1
            else:
                nextPointer += 1
        return palindromes

    def get_longest_palindrome(self, string):
        palindromes = self.get_palindromes(string)
        longest_palindrome = ""
        for palindrome in palindromes:
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome
        return longest_palindrome
