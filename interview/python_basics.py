class StringManipulator:
    """
    Fix the string manipulation methods to make all tests pass.
    """
    def reverse_words(self, sentence):
        # Bug: This only reverses characters, not words
        return sentence[::-1]
    
    def count_vowels(self, text):
        # Bug: This counts all characters
        return len(text)
    
    def is_palindrome(self, text):
        # Bug: Incorrect palindrome check
        return True

class DataStructures:
    """
    Fix the data structure implementations.
    """
    def find_duplicates(self, numbers):
        # Bug: Should return list of numbers that appear more than once
        return []
    
    def merge_sorted_lists(self, list1, list2):
        # Bug: Should merge two sorted lists while maintaining order
        return list1 + list2 