from palindrome_checker import PalindromeChecker

if __name__ == "__main__":
    string = input("Enter string: ")
    checker = PalindromeChecker()
    print("Is a palindrome: {}".format(checker.is_palindrome(string)))
    print("Longest palindrome from the string: {}".format(checker.get_longest_palindrome(string)))
