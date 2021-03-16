import re


class PalindromeChecker:

    def __init__(self, string):
        self.string = string
        self.palindromes = []
        self.cuts = 0

    @staticmethod
    def is_palindrome(string):
        string = re.sub("\\s+", "", string)
        return string == string[::-1]

    @staticmethod
    def clean_string(string):
        cleaned_string = re.sub("\\s+", "", string)
        return cleaned_string

    def get_palindromes(self):
        return self.palindromes

    def generate_palindromes(self):
        cleaned_string = PalindromeChecker.clean_string(self.string)
        string_length = len(cleaned_string)
        pointer = 0
        nextPointer = pointer + 1
        while (pointer < string_length and nextPointer < string_length):
            sub_string = cleaned_string[pointer:nextPointer + 1]
            if PalindromeChecker.is_palindrome(sub_string):
                self.palindromes.append(sub_string)
                pointer = nextPointer + 1
                nextPointer = pointer + 1
                self.cuts += 1
            else:
                nextPointer += 1
        return self.palindromes

    def get_longest_palindrome(self):
        longest_palindrome = ""
        for palindrome in self.palindromes:
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome
        return longest_palindrome

    def get_palindrome_cuts(self):
        return self.cuts
