"""
evidence_id​1 w​eight​1 c​ollection_time​1 ​ evidence_value​1
"""
def recursive_base_2(num = 0, res=""):
    if num < 2:
        return str(num%2)
    else:
        res += recursive_base_2(num//2)
        res += str(num%2)
        return res

def recursive_find_sublists(lst=[], result_list=[], i=0):
    if i == 2**len(lst):
        return
    else:
        base2 = recursive_base_2(i)
        padded_str = f"{int(base2):0{len(evidences)}}"
        sub=[]
        recursive_get_list_from_base2_str(lst,sub, padded_str)
        result_list.append(sub)
        i+=1
        recursive_find_sublists(lst, result_list, i)

def recursive_get_list_from_base2_str(lst=[], result=[], string = "", i=0):
    if i == len(lst):
        return
    else:
        if string[i] == "1":
            result.append(lst[i])
        i+=1
        recursive_get_list_from_base2_str(lst, result, string, i)

def recursive_insertion_sort(lst,i=0,j=0):
    if i==len(lst):
        return
    else:
        if j==0:
            i+=1
            j=i+1
        elif lst[j-1]>lst[j]:
            lst[j-1], lst[j] = lst[j], lst[j-1]
        recursive_insertion_sort(lst,i,j-1)

def recursive_insertion_sort_by_subval(lst, subIndex=0,i=0,j=0):
    if i==len(lst):
        return
    else:
        if j==0:
            i+=1
            j=i+1
        elif lst[j-1][subIndex]>lst[j][subIndex]:
            lst[j-1], lst[j] = lst[j], lst[j-1]
        recursive_insertion_sort_by_subval(lst,subIndex,i,j-1)

def recursive_sum_of_2d_list(lst, subIndexForSum=0, sum=0):
        if len(lst) == 0:
            return sum
        else:
            sum+=lst.pop()[subIndexForSum]
            sum = recursive_sum_of_2d_list(lst, subIndexForSum, sum)
            return sum

def recursive_only_weights_solution(sublists, max_value = -1, max_list = []):
    if len(sublists) == 0:
        return max_value, max_list
    else:
        list_to_check = sublists.pop()
        weight_sum = recursive_sum_of_2d_list(list_to_check.copy(),1)
        value_sum = recursive_sum_of_2d_list(list_to_check.copy(), 3)
        if weight_sum <= weight_limit and value_sum > max_value:
            max_value = value_sum
            max_list = list_to_check
        return recursive_only_weights_solution(sublists, max_value, max_list)

def recursive_only_time_solution(sublists, max_value = -1, max_list = []):
    if len(sublists) == 0:
        return max_value, max_list
    else:
        list_to_check = sublists.pop()
        time_sum = recursive_sum_of_2d_list(list_to_check.copy(),2)
        value_sum = recursive_sum_of_2d_list(list_to_check.copy(), 3)
        if time_sum <= time_limit and value_sum > max_value:
            max_value = value_sum
            max_list = list_to_check
        return recursive_only_time_solution(sublists, max_value, max_list)

def recursive_weight_and_time_solution(sublists, max_value = -1, max_list = []):
    if len(sublists) == 0:
        return max_value, max_list
    else:
        list_to_check = sublists.pop()
        weight_sum = recursive_sum_of_2d_list(list_to_check.copy(),1)
        time_sum = recursive_sum_of_2d_list(list_to_check.copy(),2)
        value_sum = recursive_sum_of_2d_list(list_to_check.copy(), 3)
        if weight_sum <= weight_limit and time_sum <= time_limit and value_sum > max_value:
            max_value = value_sum
            max_list = list_to_check
        return recursive_weight_and_time_solution(sublists, max_value, max_list)


crime_scene = open("crime_scene.txt", "r")
weight_limit, time_limit = [int(x) for x in crime_scene.readline().split()]
num_of_evidences = int(crime_scene.readline())

evidences = []

for _ in range(num_of_evidences):
    evidences.append([int(x) for x in crime_scene.readline().split()])

sublists = []
recursive_find_sublists(evidences, sublists)

max_val, max_list = recursive_only_weights_solution(sublists.copy())

# print(max_val)
recursive_insertion_sort_by_subval(max_list,0)
# print(max_list)

with open("solution_part1.txt", "w") as f:
    f.write(str(max_val) + "\n")
    ids = []
    for sub in max_list:
        ids.append(sub[0])
    ids = " ".join(str(x) for x in ids)
    f.write(ids)

max_val, max_list = recursive_only_time_solution(sublists.copy())

# print(max_val)
recursive_insertion_sort_by_subval(max_list,0)
# print(max_list)

with open("solution_part2.txt", "w") as f:
    f.write(str(max_val) + "\n")
    ids = []
    for sub in max_list:
        ids.append(sub[0])
    ids = " ".join(str(x) for x in ids)
    f.write(ids)

max_val, max_list = recursive_weight_and_time_solution(sublists.copy())

# print(max_val)
recursive_insertion_sort_by_subval(max_list,0)
# print(max_list)

with open("solution_part3.txt", "w") as f:
    f.write(str(max_val) + "\n")
    ids = []
    for sub in max_list:
        ids.append(sub[0])
    ids = " ".join(str(x) for x in ids)
    f.write(ids)