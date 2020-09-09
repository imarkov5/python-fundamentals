# I. Update Values in Dictionaries and Lists
# 1.Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# 2.Change the last_name of the first student from 'Jordan' to 'Bryant'
# 3.In the sports_directory, change 'Messi' to 'Andres'
# 4.Change the value 20 in z to 30

def val_dict(x = [ [5,2,3], [10,8,9] ], students = [{'first_name':'Michael','last_name': 'Jordan'},{'first_name':'John', 'last_name':'Rosales'}],sports_directory = {'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'], 'soccer':['Messi', 'Ronaldo', 'Rooney']},z = [{'x': 10, 'y': 20}]):
    x[1][0]=15
    print(x)
    students[0]['last_name'] = 'Bryant'
    print(students)
    sports_directory['soccer'][0] = 'Andres'
    print(sports_directory)
    z[0]['y']= 30
    print(z)
val_dict()
    
# II. Iterate Through a List of Dictionaries
#Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function #loops through each dictionary in the list and prints each key and the associated value. For #example, given the following list:

def iterateDictionary(some_list):
    for idx in range(len(some_list)):
        for key in some_list[idx]:
           print(key, '-', some_list[idx][key])
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}]
iterateDictionary(students) 

#code where first name and last name on the line

def iterateDictionary(some_list):
    for x in range(len(some_list)):
        for y in some_list[x]:
            if (y == 'first_name'):
                print(y + " - " + some_list[x][y], end=", ")
            else:
                print(y + " - " + some_list[x][y])

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}]
iterateDictionary(students) 

#drew's version: the best one

def iterateDictionary(some_list):
    for student in some_list:
        temp = ''
        for key, value in student.items():
            if(key == 'first_name'):
                temp += f'{key} - {value}, '
            else:
                temp +=f'{key} - {value}'
        print(temp)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}]
iterateDictionary(students) 

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# III. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
def iterateDictionary2(key_name, some_list):
    for k in range(len(some_list)):
        print(some_list[k][key_name])
iterateDictionary2('first_name', students)

# IV. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key, value in some_dict.items():
            print(len(value),key.upper())
            for val in some_dict[key]:
                print(val)
            print('\n')
printInfo(dojo)
