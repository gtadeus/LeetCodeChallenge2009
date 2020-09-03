def calc_time(arr):
    ret_list = sorted(list(itertools.permutations(arr)))
    ret_val = ""
    ret_tuple = []

    for i in ret_list:
        if i[0] <= 2 and i[2] <= 5:
            
            a = str(i[0]) + str(i[1])
            b = str(i[2]) + str(i[3])
            a_i = int(a)
            b_i = int(b)
            if a_i <=23 and b_i <= 59:
                ret_tuple.append(i)
    
    if (len(ret_tuple)>0):
        i_final = ret_tuple[-1]
        ret_val = str(i_final[0])+str(i_final[1]) +":"+str(i_final[2])+str(i_final[3])
    
    return ret_val

ret = calc_time([9,9,3,2])
print(ret)