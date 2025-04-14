import numpy as np

temp = np.array([12,23,23,34,13,17,20])

#print average temp for week
ave_temp = np.mean(temp)
print(f"{ave_temp:.2f}")

#finding the maximun temp
max_temp = np.max(temp)
print(max_temp)

#finding the minimum temp
min_temp = np.min(temp)
print(min_temp)

#Convert Fahrenheit 
fah_temp = temp * 9/5 + 32
print(fah_temp)

#Above 20 temp
nrew_temp =  np.where(temp > 20)
print(nrew_temp)


