S = "ababcbacadefegdehijhklij"

def get_partitions(S):
    interm_val = []
    ret_val = []
    iterate_partitions(S, interm_val)
    for i in reversed(interm_val):
        ret_val.append(i+1)
    return ret_val

def iterate_partitions(S, li):
    first_char = S[0]
    min_part = S.rfind(first_char)

    partitions = []
    i = min_part
    abort = False
    while (i < len(S) and abort == False):
        s1 = S[0:i]
        s2 = S[i+1:len(S)]
        if(check_valid_part([s1, s2])):
            abort = True
            #print(s1)
            if (len(s2)>0):
                iterate_partitions(s2, li)
        i += 1
    li.append(len(s1))

def check_valid_part(list_):
    ret_val = True
    if (len(list_)>1):
        for k in list_:
            for l in list_:
                for i in k:
                    if k != l:
                        if l.find(i) != -1:
                            ret_val = False
    return ret_val


print(get_partitions(S))
