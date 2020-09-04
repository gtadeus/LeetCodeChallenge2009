S = "ababcbacadefegdehijhklij"

def partitionLabels(S):
    unique_chars = list(set(S))
    occurence_dic = {}
    
    for char in unique_chars:
        count = 0
        for i in range(0, len(S)): 
            
            # if match found increase count  
            if (char == S[i]): 
                count = count + 1
        occurence_dic[char] = count
    
    sort_orders = sorted(occurence_dic.items(), 
                        key=lambda x: x[1], 
                        reverse=True)
    candidates = []
    better_candidates = []
    i_ = 0
    for (i, j) in sort_orders:
        # part = S[S.rfind(i):S.find(i)]
        candidates.append((S.rfind(i), S.find(i)))
        if (i_ > 0):
            end, start = candidates[i_]
            if start == end_0 + 1:
                better_candidates.append((start_0, end))
                print(start, " ", end)
        else:
            (end_0, start_0) = candidates[i_]
            better_candidates.append((end_0, start_0) )
        i_ += 1
        
    return better_candidates

def partitionLabels2(S):
    candidates = []
    better_candidates = {}
    i_ = 0
    for i in S:
        candidates.append((S.rfind(i), S.find(i)))
        if (i_ > 0):
            end, start = candidates[i_]
            if start == end_0 + 1:
                better_candidates[i] = ((start, end))
                print(i, " ", start, " ", end)
        else:
            (end_0, start_0) = candidates[i_]
            better_candidates[i] = ((start_0, end_0) )
        i_ += 1
    
    last_hit = False
    max_end = 0
    for i in better_candidates.values():
        print(i)
        (start, end) = i
        if end > max_end:
            max_end = end
        if end == len(S):
            last_hit = True
    
    if last_hit == False:
        better_candidates['last_hit'] = (max_end+1, len(S))

    ret_val = []
    for i in better_candidates.values():
        (start, end) = i
        ret_val.append(end-start)

    return ret_val

def get_partitions(S):
    interm_val = []
    ret_val = []
    partition3(S, interm_val)
    for i in reversed(interm_val):
        ret_val.append(i+1)
    return ret_val

def partition3(S, li):
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
                partition3(s2, li)
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

li = ["abaccb", "deffed"]
S1 = "abaccbdeffed"
#print(check_valid_part(li))
#partition3(S)
print(get_partitions(S))
#print(partitionLabels2(S))