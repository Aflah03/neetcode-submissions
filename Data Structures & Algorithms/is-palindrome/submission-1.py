class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for letter in s:
            if letter.isalnum():
                arr.append(letter.lower())
        n = len(arr)
        for i in range(len(arr)//2):
            if arr[i] != arr[n-1-i]:
                return False
        return True