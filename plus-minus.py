test_case = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    res = [1 if x > 0 else -1 if x < 0 else 0 for x in arr]
    arr_len = len(arr)
    print("%.6f" % float(res.count(1)/arr_len))
    print("%.6f" % float(res.count(-1)/arr_len))
    print("%.6f" % float(res.count(0)/arr_len))
    

plusMinus(test_case)
