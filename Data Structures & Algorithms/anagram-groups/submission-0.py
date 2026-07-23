class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in hash_dict:
                hash_dict[key].append(s)
            else:
                hash_dict[key] = [s]
        return list(hash_dict.values())
        

        