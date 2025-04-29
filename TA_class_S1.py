def count_even_numbers(numbers):
    even_counts = {}
    for num in numbers:
        if num % 2 == 0:
            even_counts[num] = even_counts.get(num, 0) + 1
    return even_counts


numbers = [1, 2, 3, 2, 4, 5, 4]
print(count_even_numbers(numbers))  


def sum_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    total = 0
    for num in even_numbers:
        total += num
    return even_numbers, total


numbers = [1, 2, 3, 4, 5, 6]
print(sum_even_numbers(numbers))  

def remove_duplicates(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique


numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))  


def find_common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common


list1 = [1, 2, 3, 4]
list2 = [2, 4, 6, 8]
print(find_common_elements(list1, list2))  


def filter_products(products, threshold):
    return [product for product, price in products.items() if price > threshold]


products = {"pen": 10, "book": 60, "laptop": 1000, "eraser": 5}
threshold = 50
print(filter_products(products, threshold))  


def calculate_averages(grades):
    avg_grades = {}
    for student, scores in grades.items():
        avg = sum(scores) / len(scores)
        avg_grades[student] = round(avg, 2)
    return avg_grades


grades = {"Ali": [18, 15, 20], "Sara": [12, 16, 14]}
print(calculate_averages(grades))  


def merge_duplicate_keys(input_list):
    result = {}
    for key, value in input_list:
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

input_list = [("a", 1), ("b", 2), ("a", 3)]
print(merge_duplicate_keys(input_list)) 


def merge_duplicate_keys(input_list):
    result = {}
    for key, value in input_list:
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


input_list = [("a", 1), ("b", 2), ("a", 3)]
print(merge_duplicate_keys(input_list))  

