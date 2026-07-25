class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for i in strs:
            sortedS= "".join(sorted(i))
            dic[sortedS].append(i)

        return list(dic.values())
        

        