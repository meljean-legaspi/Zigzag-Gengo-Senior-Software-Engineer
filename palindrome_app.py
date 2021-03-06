from palindrome_checker import PalindromeChecker

if __name__ == "__main__":
    string = input("Enter string: ")
    checker = PalindromeChecker(string)
    print("Is a palindrome: {}"
          .format(PalindromeChecker.is_palindrome(string)))
    checker.generate_palindromes()
    print("Longest palindrome from the string: {}"
          .format(checker.get_longest_palindrome()))
    print("Number of cuts: {}"
          .format(checker.get_palindrome_cuts()))
