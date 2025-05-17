
def square():
    numbers = [1,2,3,4,5]
    squares = {str(n):n**2 for n in numbers}
    print(squares)

def even():
    numbers = [1,2,3,4,5]
    even_squares = {n:n**2 for n in numbers if n % 2 == 0}
    print(even_squares)

def dictionary():
    keys = ['a','b','c']
    values = [1,2,3]
    dictionary = {k: v for k, v in zip(keys,values)}
    print(dictionary)

def multi_dictionary():
    
    dict1 = {'a': 1, 'b':2}
    dict2 = {'b':3, 'c':4}
    dict3 = {'d':5, 'e': 6}
    merge_dict = {**dict2, **dict1, **dict3}
    print(merge_dict)

def conmerging_dictionary():
    dict1 = {'a':1, 'b':2, 'c':3}
    dict2 = {'d':4, 'e':5, 'f':6}

                   # first line stores only 'a':1
                   # second line stores only 'e':5 and combine two keys and values into mered_dict 
    merged_dict = {**{k: v for k, v in dict1.items() if k in 'aeiou'},
                    **{k: v for k, v in dict2.items() if k in 'aeiou'}}
    
    print(merged_dict)

def looping():
    
    names = ["John", "Mike", "Sam", "Mark", "Ben"]
    for i in range (len(names)):
        print(i, names[i])
    
    for i, name in enumerate(names):
        print(i, name)
    for i, name in enumerate(names, start = 1):
        print(i, name)

def list_compare():

    print("***Zip***")    
    names = ['Alice', 'Bop', 'Cathy']
    ages = [25, 30, 35]

    paired = zip(names, ages)
    print(paired)

    print("***list***")
    names = ['Alice', 'Bop', 'Cathy']
    ages = [25, 30, 35]
    paired = list(zip(names,ages))
    print(paired)

    print("***Dictionary***")
    paired = dict(zip(names,ages))
    print(paired)

def combination_dict():
    ids = [1,2,3]
    names = ['Alice', 'Bop', 'Cathy', 'Mike']
    grades = ['A', 'B', 'A+', 'A']

    students = dict(zip(ids,zip(names, grades)))
    print(students)

def main():
    
    #square()
    #even()
    #dictionary()
    #multi_dictionary()
    #conmerging_dictionary()
    #looping()
    #list_compare()
    combination_dict()

if __name__ == "__main__":
    main()


