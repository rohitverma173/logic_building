user_list = [4,3,2,10,12,1,5,6]

i = 1
while(i < len(user_list)):
    curr_val = user_list[i]
    j = i
    while(j>0):
        if user_list[j] < user_list[j-1]:
            j = j-1
            tmp_val = user_list[j]
            user_list[j] = curr_val
            user_list[j+1] = tmp_val
        else:
            user_list[j] = curr_val
            break
    print(user_list)
    i = i + 1

print(user_list)




