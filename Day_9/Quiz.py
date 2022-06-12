#https://www.udemy.com/course/100-days-of-code/learn/quiz/4858578#overview

final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary = {
    "a": 9,
    "b": 8,
}

starting_dictionary.append({"c":7 })
print(starting_dictionary)
# 'dict' object has no attribute 'append'

final_dictionary = starting_dictionary["c"] = 7
# print(type(final_dictionary))
# makes final_dictionary of type int

starting_dictionary += {"c":7 }
# unsupported operand type(s) for +=: 'dict' and 'dict'

print(starting_dictionary)
# print(final_dictionary)
# print(type(final_dictionary))