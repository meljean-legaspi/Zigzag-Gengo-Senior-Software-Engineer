from palindrome_checker import PalindromeChecker

def test_when_string_is_not_a_palindrome_return_false():
    checker = PalindromeChecker()
    string = "test"
    assert checker.is_palindrome(string) == False

def test_when_string_is_a_simple_palindrome_return_true():
    checker = PalindromeChecker()
    string = "abcdcba"
    assert checker.is_palindrome(string) == True

def test_when_string_has_more_than_one_palindrome_return_count_not_zero():
    checker = PalindromeChecker()
    string = "abaxyzzyxfccf"
    assert len(checker.get_palindromes(string)) > 0

def test_when_string_has_multiple_palindromes_return_longest():
    checker = PalindromeChecker()
    string = "abaxyzzyxfccf"
    assert checker.get_longest_palindrome(string) == "xyzzyx"