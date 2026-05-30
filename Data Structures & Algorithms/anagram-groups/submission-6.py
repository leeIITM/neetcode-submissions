class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = {}
        for i in strs:
            sorted_strs = "".join(sorted(i))

            if sorted_strs not in ana_map:
                ana_map[sorted_strs] = [i]
            else:
                ana_map[sorted_strs].append(i)
        return list(ana_map.values())