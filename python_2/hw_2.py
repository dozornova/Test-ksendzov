import math

item_1 = 2
item_2 = 9

result_sum = item_1 + item_2
print('sum =', result_sum)

result_subtr = item_2 - item_1
print('subtraction =', result_subtr)

result_multi = item_1 * item_2
print('multiplication =', result_multi)

result_exp = item_1 ** item_2
print('exp =', result_exp)

result_m_exp = math.pow(item_1, item_2)
print('exp math =', result_m_exp)

result_s_root = (item_2 ** 0.5)
print('square root =', result_s_root)

result_m_s_root = math.sqrt(item_2)
print('square root math =', result_m_s_root)

result_mp_s_root = math.pow(item_2, 0.5)
print('square root math pow =', result_m_s_root)

item_1 = 3      #odd
item_2 = 2      #even

result_division = item_1 / item_2
print('division =', result_division)

result_m_floor = math.floor(result_division)
print('floor =', result_m_floor)

result_m_ceil = math.ceil(result_division)
print('ceil =', result_m_ceil)

result_int = int(result_division)
print('int division =', result_int)

result_no_division_loss = int(item_1 / item_2)
print('no division int loss', result_no_division_loss)

result_division_loss = item_1 % item_2
print('division loss remainder', result_division_loss)

##########

item_3 = 5

item_3 = item_3 + 10
print('5 + 10 =', item_3)

item_3 = item_3 - 5
print('15 - 5 =', item_3)

item_3 = item_3 * 3
print('10 * 3 =', item_3)

item_3 = item_3 / 2
print('30 / 2 =', item_3)

item_3 = item_3 ** 2
print('15.0 ** 2 =', item_3)

item_3 = item_3 * 0.5
print('225.0 * 0.5 =', item_3)

item_3 = item_3 % item_3
print('item_3 %', item_3)


##########

b_item_t = True
b_item_f = False

b_item_result_sum = (b_item_t + b_item_f)
print('sum', b_item_result_sum)

b_item_relult_subtr = b_item_t - b_item_f
print('subtr', b_item_relult_subtr)

b_item_relult_multi = b_item_t * b_item_f
print('multi', b_item_relult_multi)

# 57. Вывести b_item_relult_division в консоль. (Получить ошибку)
# b_item_relult_division = b_item_t / b_item_f
# print('division error 1 / 0', b_item_relult_division)

b_item_1_int = int(b_item_t)
print('int for b_item_t =', b_item_1_int)

b_item_2_int = int(b_item_f)
print('int for b_item_f =', b_item_2_int)