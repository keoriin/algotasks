'''
#############################################TASK1###################################
def find_max_multiplication(string):
    if not isinstance(string, str):
        return
    max_prod = 0
    max_com = None

    for i in range(len(string) - 3):
        if string[i:i + 4].isdigit():
            digits = [int(digit) for digit in string[i:i + 4]]
            prod = 1
            for digit in digits:
                prod *= digit
            if prod > max_prod:
                max_prod = prod
                max_com = digits

    return max_prod if max_com else None

# How to Test?:
print(find_max_multiplication('abc123456def'))
print(find_max_multiplication('a1b2c3d4e'))
'''
'''
###############################Task 2##########################################################

class BinarySorter:
    def count_ones_in_binary(self, num):
        return bin(num).count('1')

    def custom_sort(self, arr):
        return sorted(arr, key=lambda x: (self.count_ones_in_binary(x), x))

'''

