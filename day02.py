def func_ch2_4(nums, k, t):
    sorted_ = [(b[0], b[1]) for b in sorted(enumerate(nums),key=lambda i:i[1], reverse=False)]
    #print(sorted_)
    i=0
    success = False
    counts = 0
    while i < len(nums) and success==False:
        j = i+1
        if i<len(nums)-1 and (abs(sorted_[i][1]-sorted_[i+1][1])) <= t:
            while j < len(nums) and success == False:
                t_ = abs(sorted_[i][1]-sorted_[j][1])
                k_ = abs(sorted_[i][0]-sorted_[j][0])
                #print(k_, t_)
                if (t_ <= t and k_ <= k):
                    success = True

                j += 1
                counts += 1
        i+=1
    print(counts)
    return success

nums = [1,3,6,2]
k=1
t=2
func_ch2_4(nums, k, t)