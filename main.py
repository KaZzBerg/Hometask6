import random


def create_rand_list(list_length=10, start_value=1, end_value=50) -> list:
    rand_list = []
    for i in range(list_length):
        rand_list.append(random.randint(start_value, end_value))
    return rand_list


list1 = create_rand_list()
print(list1)

print('Task 2')


def count_nums():
    for numbers in list1:
        result = sum(list1)
        return result


print(count_nums())

print('Task 3')


def min_value():
    sorted_list = sorted(list1)
    min_num = sorted_list[0]
    return min_num


print(min_value())


def prime():
    x = [i for i in list1 if i % 2 != 0 and i % 3 != 0 and i % 5 != 0]
    if len(x) > 0:
        print(f'Prime number count: {len(x)}')
    else:
        print('No prime numbers')
    return x


print(prime())


delete_number = create_rand_list()
print(delete_number)
print('Numbers to delete: 5, 10')



def del_number():
    count = 0

    for i in delete_number:

        if i == 5 or i == 10:
            delete_number.remove(i)

            count += 1

    return count


print(f'Deleted numbers: {del_number()}')

print('Task 5')
nums_1 = create_rand_list()
nums_2 = create_rand_list()

print(nums_1)
print(nums_2)


def calc_eq_nums():
    result = (set(nums_1).intersection((set(nums_2))))
    return result


print(f'Common numbers are: {calc_eq_nums()}')

print('Task 6')


def count_degree():
    b = [i ** 2 for i in list1]
    return b


print(f'Result: {count_degree()}')
