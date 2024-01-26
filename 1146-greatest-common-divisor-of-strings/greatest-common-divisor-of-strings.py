def compute_hcf(x, y):
        while(y):
            x, y = y, x % y
        return x
class Solution(object):
    
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        final_str = ""
        if len(str1) < len(str2):
            default = str1
            largest = str2
        else:
            default = str2
            largest = str1
        final_str+=default[0]
        needed_len = compute_hcf(len(default), len(largest))
        print(needed_len)
        if len(largest.replace(default, "")) == 0:  
            return default
        if len(default) > 1:
            for i in range(1, len(default)):
                if len(largest.replace(final_str, "")) != 0:
                    final_str+=default[i]                
                if len(largest.replace(final_str, "")) == 0 and len(default.replace(final_str, "")) == 0:  
                    if len(final_str) != needed_len:
                        final_str+=default[len(final_str):needed_len]
                    return final_str                                          
        else:
            if len(largest.replace(final_str, "")) == 0:                      
                    return final_str                          
        return ""



        