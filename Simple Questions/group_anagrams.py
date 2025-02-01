from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        iterated = []
        for i in range(0, len(strs)+1):
            try:
                if strs[i] in iterated:
                    continue
            except IndexError:
                continue
            current_op = [strs[i]]
            iterated.append(strs[i])
            for j in range(0, len(strs)+1):
                try:
                    if strs[j] in iterated:
                        continue
                except IndexError:
                    continue
                if sorted(list(strs[i])) == sorted(list(strs[j])):
                    current_op.append(strs[j])
                    iterated.append(strs[j])
            output.append(current_op)
        return output


if __name__ == '__main__':
    inputs = [["eat","tea","tan","ate","nat","bat"], ["",""]]
    outputs = [[["bat"],["nat","tan"],["ate","eat","tea"]], [["", ""]]]
    for i in range(0, len(inputs)):
        result = Solution().groupAnagrams(inputs[i])
        print('-'*50)
        print("Expected")
        print(outputs[i])
        print('-' * 50)
        print("Result")
        print(result)
        print('-' * 50)


