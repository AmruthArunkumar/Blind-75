class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            occ = [0] * 26
            for l in s:
                occ[ord(l)-ord('a')] += 1
            groups[str(occ)].append(s)
        return list(groups.values())