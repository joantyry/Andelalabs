def find_max_min(input_array):
    max_num = max(input_array)
    min_num = min(input_array)
    for n in input_array:
      if (min_num != max_num):
        return [min_num,max_num]
      else:
        return [n]