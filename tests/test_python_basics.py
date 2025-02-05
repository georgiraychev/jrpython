import pytest
from interview.python_basics import StringManipulator, DataStructures

def test_string_manipulator():
    sm = StringManipulator()
    
    # Test reverse_words
    assert sm.reverse_words("hello world") == "world hello"
    assert sm.reverse_words("Python is awesome") == "awesome is Python"
    
    # Test count_vowels
    assert sm.count_vowels("hello") == 2
    assert sm.count_vowels("AEIOU") == 5
    
    # Test palindrome
    assert sm.is_palindrome("radar") == True
    assert sm.is_palindrome("hello") == False
    assert sm.is_palindrome("A man a plan a canal Panama") == True

def test_data_structures():
    ds = DataStructures()
    
    # Test find_duplicates
    assert set(ds.find_duplicates([1, 2, 2, 3, 3, 4])) == {2, 3}
    assert ds.find_duplicates([1, 2, 3, 4]) == []
    
    # Test merge_sorted_lists
    assert ds.merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert ds.merge_sorted_lists([1], [2]) == [1, 2] 