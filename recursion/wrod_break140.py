from typing import List, Dict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        main function
        """
        self.wordDict = set(wordDict)
        self.memo: Dict[str, List[str]] = {}        # 记忆化（备忘录）。用于存储已经计算过的子问题的解，避免重复计算
        return self._solve(s)
    
    def _solve(self, s: str) -> List[str]:

        if s in self.memo:
            return self.memo[s]
        
        if not s:
            return []

        results = []

        # 遍历所有可能的前缀
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix in self.wordDict:

                if i == len(s):
                    results.append(prefix)      # 不能break，因为要遍历所有可能的句子
                else:
                    suffix = s[i:]
                    suffix_sentences = self._solve(suffix)
                    for sub_sentence in suffix_sentences:
                        results.append(prefix + " " + sub_sentence)
        
        self.memo[s] = results

        return results


# --- 使用 ---
solver = Solution()
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
solutions = solver.wordBreak(s, wordDict)
print(f"对于 s='{s}', 所有可能的句子是:")
# 为了输出顺序一致，可以排序后打印
print(sorted(solutions)) 
# 输出:
# 对于 s='catsanddog', 所有可能的句子是:
# ['cat sand dog', 'cats and dog']


# 再来一个例子
solver2 = Solution()
s2 = "pineapplepenapple"
wordDict2 = ["apple", "pen", "applepen", "pine", "pineapple"]
solutions2 = solver2.wordBreak(s2, wordDict2)
print(f"\n对于 s='{s2}', 所有可能的句子是:")
print(sorted(solutions2))
# 输出:
# 对于 s='pineapplepenapple', 所有可能的句子是:
# ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']


"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def dfs(index: int) -> list[str]:
            if index in memo:
                return memo[index]

            if index == len(s):
                return [""]

            results = []
            for endIndex in range(index + 1, len(s) + 1):
                word = s[index: endIndex]

                if word in wordSet:
                    listOfSuffixSentences = dfs(endIndex)

                    for suffixSentence in listOfSuffixSentences:
                        if suffixSentence == "":
                            results.append(word)
                        else:
                            results.append(word + " " + suffixSentence)

            memo[index] = results
            return results

        return dfs(0)



"""