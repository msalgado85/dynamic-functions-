# def check_3_digits(number):
#     return number in range(100, 1000)

# result = check_3_digits(68)
# print(result)


# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100, 1000):
#             return True
#         else: 
#             return False

# result = check_3_digits([555, 999, 600])
# print((result))


# def check_3_digits(list):

#     three_digits_list = []

#     for n in range(100, 1000):
#         three_digits_list.append(n)
#     else:
#         pass

#     return False

# result = check_3_digits([555, 99, 600])


# coffee_prices = [('cappuccino', 1.5),
#                  ('espresso', 1.2),
#                  ('mocha', 1.9)]

# def most_expensive_coffee(list_of_prices):

#     highest_price = 0
#     my_most_expensive_coffee = ''

#     for coffee, price in list_of_prices:
#         if price > highest_price:
#             highest_price = price
#             my_most_expensive_coffee = coffee
#         else:
#             pass

#     return(my_most_expensive_coffee, highest_price)

# print(most_expensive_coffee(coffee_prices))



# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

# values = [-3,-1, 2, 4, 6]
# def all_positives(num):
#     for value in values:
#         if value > 0:
#             return True
#         else: return False

# print(all_positives(values))




# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

# values = [300, 500, 100]
# def sum_less(num):
#     for value in values:
#         if sum(values) > 0 and sum(values) < 1000:
#             sum_nums = sum(values)
#         return sum_nums
# print(sum_less(values))



# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.

values = [4, 8, 11, 14, 21]
def count_even(num):
    count = 0
    for value in values:
        if value % 2 == 0:
           count += 1
        else: pass
    return count
print(count_even(values))
