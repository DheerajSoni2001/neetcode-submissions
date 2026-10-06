class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        common = Counter(words[0])

        for x in words[1:]:
            common &= Counter(x)
        return list(common.elements())