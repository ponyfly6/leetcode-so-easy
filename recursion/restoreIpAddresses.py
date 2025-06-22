from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        path = []       # 路径list ，用于存储当前正在构建的ip地址的各个段
        self._backtrack(s, 0, path, results)
        return results
    
    def _backtrack(self, s: str, start_index: int, path: List[str], results: List[str]):
        """
        回溯函数
        :param s: 原始字符串
        :param start_index: 当前准备从原始字符串的哪个索引开始截取
        :param path: 已经找到的IP段列表，例如 ["255", "255"]
        :param results: 最终的结果列表
        """
        if len(path) == 4 and start_index == len(s):
            results.append(".".join(path))
            return
        
        if len(path) == 4 and start_index == len(s):
            return 
        
        for i in range(1, 4):
            if start_index + i > len(s):
                break
            segment = s[start_index:start_index + i]
            if self._is_valid_segment(segment):
                path.append(segment)
                self._backtrack(s, start_index + i, path, results)
                path.pop()
            
        

    def _is_valid_segment(self, segment: str) -> bool:
        if len(segment) > 3:
            return False
        
        if len(segment) > 1 and segment[0] == "0":
            return False
        
        if int(segment) > 255 or int(segment) < 0:
            return False
        return True
    

solver = Solution()
s = "25525511135"
solutions = solver.restoreIpAddresses(s)
print(f"对于 s='{s}', 所有可能的IP地址是:")
print(solutions)
# 输出:
# 对于 s='25525511135', 所有可能的IP地址是:
# ['255.255.11.135', '255.255.111.35']


solver2 = Solution()
s2 = "101023"
solutions2 = solver2.restoreIpAddresses(s2)
print(f"\n对于 s='{s2}', 所有可能的IP地址是:")
print(solutions2)
# 输出:
# 对于 s='101023', 所有可能的IP地址是:
# ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']