test_cases = ["a", "abab", "aba", "abcabcabcabc", "aac", "aaccaacc", "babbabbabbabbab"]

def func_01(s):
    ret_val = False
    length = len(s)
    
    if length > 1 and s == len(s) * s[0]:
        return True
    
    max_len = int(length / 2)
    for i in range(0, max_len+1):
        sub_str = s[0:i]
        len_sub_str = len(sub_str)
        if (len_sub_str != 0):
            factor = int(length / len_sub_str)
            if factor != length:
                if s == factor * sub_str:
                    return True
    return ret_val

for t in test_cases:
    print(t, func_01(t))
