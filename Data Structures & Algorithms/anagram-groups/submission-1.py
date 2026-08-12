class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for word in strs:
            arr = [0]* 26
            for ch in word:
                arr[ord(ch)- ord('a')] +=1
            mp[tuple(arr)].append(word)
        res = []
        for key, value in mp.items():
            # print("key is : ", key)
            # print("value is : ", value)
            res.append(value)
        return res
