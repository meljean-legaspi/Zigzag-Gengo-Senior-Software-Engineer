from palindrome_checker import PalindromeChecker


def test_when_string_is_not_a_palindrome_return_false():
    string = "test"
    assert PalindromeChecker.is_palindrome(string) is False


def test_when_string_is_a_simple_palindrome_return_true():
    string = "abcdcba"
    assert PalindromeChecker.is_palindrome(string) is True


def test_when_string_has_more_than_one_palindrome_return_count_not_zero():
    string = "abaxyzzyxfccf"
    checker = PalindromeChecker(string)
    checker.generate_palindromes()
    assert len(checker.get_palindromes()) > 0


def test_when_string_has_no_palindrome_return_count_zero():
    string = "today"
    checker = PalindromeChecker(string)
    checker.generate_palindromes()
    assert len(checker.get_palindromes()) == 0


def test_when_string_has_multiple_palindromes_return_longest():
    string = "abaxyzzyxfccf"
    checker = PalindromeChecker(string)
    checker.generate_palindromes()
    assert checker.get_longest_palindrome() == "xyzzyx"


def test_when_string_has_no_palindromes_cuts_should_be_zero():
    string = "today"
    checker = PalindromeChecker(string)
    checker.generate_palindromes()
    cuts = checker.get_palindrome_cuts()
    assert cuts == 0


def test_when_string_has_palindromes_return_number_of_cuts_to_get_substrings():
    string = "noonabbadc"
    checker = PalindromeChecker(string)
    checker.generate_palindromes()
    cuts = checker.get_palindrome_cuts()
    assert cuts == 2
