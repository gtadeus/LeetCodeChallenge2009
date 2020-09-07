class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words=str.split(' ')
        if len(pattern) != len(words):
            return False
        check_dic = {}
        check_dic2={}
        i = 0
        for p in pattern:
            w=words[i]
            check_dic2[w]=p
            if (p in check_dic.keys()):
                if check_dic[p]!=w:
                    return False
            check_dic[p]=w
            i += 1
        
        if len(check_dic) != len(check_dic2):
            return False
        return True