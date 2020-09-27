def sum_of_list(digits_list,size):
    
    if (size == 0):
        return 0
    else:
        
        return digits_list[size- 1] + sum_of_list(digits_list,size-1)

digits_list = [4,7,0,6]
print(sum_of_list(digits_list,4))
