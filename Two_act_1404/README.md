import numpy as np

# ---- Act 1 ----
# Create a NumPy array of the first 10 positive integers.
## Create the array
arr = np.array([1,3,5,7,9,10,12,14,16,18])


print("---- Act one ----")
# 1.1 Print the array
print("Array: ",arr)

# 1.2 Print the shape and data type of the array.
print("Shape: ", arr.shape)
print("Data type: ", arr.dtype)

# 1.3 Multiply each element by 2 and print the result.
result = arr * 2
print("Multiply: ", result)


#---- Act 2 ----
# You are given the test scores of 5 students across 3 subjects in a 2D NumPy array.
# Each row represents a student, and each column a subject.

print("---- Act two ----")

scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# 2.1 Calculate and print the average score for each student.
ave_Student = np.mean(scores, axis=1)
print("Student's average score: ", ave_Student)

# 2.2 Calculate and print the average score for each subject.
ave_Subject = np.mean(scores, axis=0)
print("Average score of each subject: ", ave_Subject)

# 2.3 Identify the student (row index) with the highest total score.
row_sum = np.sum(scores, axis=1)
highest = np.max(row_sum)
highest_student = np.where(highest == row_sum)
print("index: ", highest_student)

# 2.4 Add 5 bonus points to the third subject for all students.

scores[:, 2] += 5
print("Add 5 bonus points to the third subject:  ", scores)
