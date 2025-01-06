# numbers = [1,2,3]
# new_numbers = []
# for n in numbers:
#     nums = n + 1
#     new_numbers.append(nums)
# print(new_numbers)
#
# new_numbers2 = [n + 1 for n in numbers]
# print(new_numbers2)
#
#/////////////////////////////////////////////////////////////////

#
# new_range = [num * 2 for num in range(1,5)]
# print(new_range)

#/////////////////////////////////////////////////////////////////


# with open("file1.txt") as file1:
#     file1_list = [list.strip() for list in file1]
#     print(file1_list)
#
# with open("file2.txt") as file2:
#     file2_list = [list.strip() for list in file2]
#     print(file2_list)
#
#     merged_list = [num for num in file1_list if num in file2_list]
#     print("\n",merged_list)



#/////////////////////////////////////////////////////////////////


# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# new_names = [name.upper() for name in names if len(name) > 4]
# print(new_names)
#

#/////////////////////////////////////////////////////////////////

#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)
#
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)


#/////////////////////////////////////////////////////////////////


# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# import random
# students_score = {student:random.randint(1, 100) for student in names}
#
# print(students_score)
#
# passed_students = {student:score for (student, score) in students_score.items() if score >= 60}
#
# print(passed_students)


#/////////////////////////////////////////////////////////////////


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# sentence_list = sentence.split()
#
# sentence_and_words = {sentence_list:int(len(sentence_list)) for sentence_list in sentence_list}
#
# print(sentence_and_words)


#/////////////////////////////////////////////////////////////////


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
#
# weather_f = {day:(temp * 9/5 + 32) for (day, temp) in weather_c.items()}
# print(weather_f)


#/////////////////////////////////////////////////////////////////


import pandas

student_dics = {
    "students": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dics)

print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    if row.students == "Angela":
        print(row.score)