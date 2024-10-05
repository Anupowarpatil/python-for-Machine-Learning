class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        random_values = []
        for i in range(0,len(s1)):
            random_values.append(i)
        for i in range(0,len(s2)):
            for j in range(0,len(random_values)):
                index=random_values[j]
                if s2[i]==s1[index]:
                    del random_values[j]
                    if len(random_values)==0:
                        return True
        
