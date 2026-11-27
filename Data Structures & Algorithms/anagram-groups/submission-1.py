class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}
        
        for s in strs:
            key =''.join(sorted(s))
            if key in dicts:
                dicts[key].append(s)
            else:
                dicts[key] = [s]
        return list(dicts.values())


            

        