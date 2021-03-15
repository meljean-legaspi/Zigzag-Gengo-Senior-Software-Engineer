class PalindromeChecker:

    def is_palindrome(self, string):
        return string == string[::-1]

    def get_palindromes(self, string):
        string_length = len(string)
        palindromes = []
        for index in range(string_length):
            counter = 1
            while counter < string_length:
                sub_string = string[index:counter + 1]
                if self.is_palindrome(sub_string):
                    palindromes.append(sub_string)
                counter += 1
        return palindromes

    def get_longest_palindrome(self, string):
        palindromes = self.get_palindromes(string)
        longest_palindrome = ""
        for palindrome in palindromes:
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome
        return longest_palindrome
