from typing import List


class SolutionPureRecursion:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        if expression.isdigit():            # recursion base case , 如果表达式是数字，直接返回，记住是返回的是list，因为要遍历
            return [int(expression)]

        results = []
        for i, char in enumerate(expression):
            if char in "+-*":
                left_part = expression[:i]          # sub string
                right_part = expression[i+1:]

                left_results = self.diffWaysToCompute(left_part)
                right_results = self.diffWaysToCompute(right_part)

                # merge left and right results  (笛卡尔积)
                for l in left_results:
                    for r in right_results:
                        if char == "+":
                            results.append(l + r)
                        elif char == "-":
                            results.append(l - r)
                        else:
                            results.append(l * r)
        return results


































































