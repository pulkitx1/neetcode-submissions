class Solution:
    def groupAnagrams(self, strs):
        mp = {}  # normal dictionary

        for word in strs:
            key = ''.join(sorted(word))  # sorted key

            if key not in mp:
                mp[key] = []

            mp[key].append(word)

        return list(mp.values())