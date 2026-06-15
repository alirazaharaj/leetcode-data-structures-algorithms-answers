class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str=""
        for char in s:
            if char.isalnum():
                cleaned_str= cleaned_str + char.lower()
        print(cleaned_str)
        if cleaned_str[::-1] == cleaned_str:
            return True
        else:
            return False
