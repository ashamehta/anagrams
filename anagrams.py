"""
Script: Asha Thomas
Purpose: Illumina interview by Vivek Krishnakumar
Date: 3/29/2022

Instructions:
Given a list of strings, return all the anagram groups.
For example "pot", "turn", "opt", "top", should return
[{"pot", "opt", "top"}, {"turn"}]

Usage: python3 anagrams.py
Run unit tests: python3 -m unittest anagrams.py
"""

from typing import Dict, List, Tuple
import unittest


def get_anagram_groups(words:List) -> Dict[str, Tuple]:
    """
    :param words: input list of words
    :return: hash table that maps alphabetically sorted word to
        all associated anagrams from input list

    This function iterates through each word in the input list. For each word,
    the word is:
    1. Sorted alphabetically
    2. Checked if already present in hash table
        a) If yes, add unsorted word to list corresponding to associated
            sorted string.
        b) If no, add new entry to dictionary with the sorted string as key
            and a list containing the unsorted string as the value.
    """
    anagram_groups = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    print("The input list contains the following anagram groups: ")
    for value in anagram_groups.values():
        print(value)
    return anagram_groups


def main():
    # words = ["top", "pot", "angel", "glean", "elbow", "below", "lobe"]
    words = ["pot", "turn", "opt", "top"]
    anagram_groups = get_anagram_groups(words)


# Example unit tests
class TestAnagram(unittest.TestCase):
    def test_anagram_group_1(self):
        words1 = ["pot", "turn", "opt", "top"]
        anagram_groups1 = get_anagram_groups(words1)
        self.assertIn(
            ("opt", ["pot", "opt", "top"]),
            anagram_groups1.items()
        )
        self.assertIn(
            ("nrtu", ["turn"]),
            anagram_groups1.items()
        )

    def test_anagram_group_2(self):
        words2 = ["top", "pot", "angel", "glean", "elbow", "below", "lobe"]
        anagram_groups2 = get_anagram_groups(words2)
        self.assertIn(
            ("opt", ["top", "pot"]),
            anagram_groups2.items()
        )
        self.assertIn(
            ("aegln", ["angel", "glean"]),
            anagram_groups2.items()
        )
        self.assertIn(
            ("belo", ["lobe"]),
            anagram_groups2.items()
        )


if __name__ == "__main__":
    main()
