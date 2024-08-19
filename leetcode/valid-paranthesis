class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        dict1={')':'(','}':'{',']':'['}
        for c in s:
            if c in dict1.values():
                stack.append(c)
            elif c in dict1.keys():
                if stack and stack[-1] in dict1[c]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack)==0

