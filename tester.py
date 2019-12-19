def inter(a_list):
    for i in range(0, len(a_list) - 1):   
        for j in range(0, len(a_list) - 1):
            if a_list[j + 1] < a_list[j]:
                a_list[j+1], a_list[j] = a_list[j], a_list[j+1]
    return a_list
