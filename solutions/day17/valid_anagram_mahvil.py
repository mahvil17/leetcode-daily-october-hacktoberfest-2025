"""
🔠 Day 17 - Valid Anagram (LeetCode #242)
----------------------------------------
Author: Mahvil
GitHub: https://github.com/Mahvil
Hacktoberfest 2025 Contribution

Description:
Given two strings s and t, return True if t is an anagram of s, and False otherwise.

Example:
Input: s = "listen", t = "silent"
Output: True
"""

def isAnagram(s: str, t: str) -> bool:
    # Sorting-based approach
    return sorted(s) == sorted(t)


# Driver code
if __name__ == "__main__":
    s = input("Enter first string: ").strip()
    t = input("Enter second string: ").strip()

    if isAnagram(s, t):
        print("✅ Both strings are anagrams.")
    else:
        print("❌ Not anagrams.")
