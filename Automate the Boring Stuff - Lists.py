spam = ['cat', 'dog']
spam[0]
print(spam[0])

spam = [['cat','dog'],[10,20,30,40,50]]
print(spam[1][3])
print(spam[0][-1])

slicer = ['cat', 'bat', 'rat', 'elephant']
print(slicer[0:1]) # doesn't include the index on the right
print(slicer[1:])
print(slicer[:3])

# del spam[1][4]
print(len([1,2,3]))

print([1,2,3] + [4,5,6])
print("hello"*3)
print([1,2,3]*3)
int('42')
str(42)
list("Hello")

for i in range(4):
    print(i)

print(list(range(4)))
print(list(range(0, 100, 2)))

supplies = ['pens', 'staplers', 'bin']
for i in range(len(supplies)):
    print('Index' + str(i) + ' in supplies is ' + supplies[i])


supplies = ['pens' , 'pens','pens' , 'pens','pens' , 'pens','pens' , 'pens']
for i in range(len(supplies)):
    print('Index' + str(i) + ' in supplies is ' + supplies[i])

cat = ['fat','orange','loud']

size = cat[0]
color = cat[1]
disposition = cat[2]


size, color, disposition = cat
print(size)
print(color)
print(disposition)
size, color, disposition = 'skinny', 'black', 'quiet'
print(size)
print(color)
print(disposition)
a='AAA'
b='BBB'
a,b = b,a
print(a)
print(b)

spam = 42
spam = spam +1
spam +=1

spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('heyas')) # first value in a duplicate record in list

spam.append('new') # adds new record but we don't do spam = spam.append since the function's actual return value is None
print(spam)

spam.insert(2, 'second new')
print(spam)

spam.remove('second new') # only removes the first instance of the parameter
del spam[len(spam)-1]
print(spam)

sortedThisNumber = [9, 7, 5, 3 ,1]
sortedThisNumber.sort()
print(sortedThisNumber)
sortedThisAnimalNames = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
sortedThisAnimalNames.sort(reverse=True)
print(sortedThisAnimalNames)

# Ascii betical order; lower cases come after upper cases

sortedThisAnimalNames.sort(key=str.lower) # to sort on true alphabetical order regardless of the case

# relationships between lists and strings

# similarities between lists and strings: indexing, looping, assignment operators
print(list('Hello'))
name = 'Zophie'
print(name[0])
print(name[1:3])
print(name[-2])
print('Zo' in name)

for letter in name:
    print(letter)

# immutable and mutable data types
name = 'ZOphie the cat'
print(name[7])
try:
    name[7] = 'X' # this will result in an errow since strings are immutable
except:
    print('Error while changing immutable data')
    
# creating new strings from slices
name = 'Zophie a cat'
newName = name[0:7] + 'the ' + name[8:12]
print(newName)

# difference between immutable and mutable comes up with "references"
# lists uses references

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello'
print(cheese)
print(spam) # spam also changed since it is equal to cheese by reference since these are mutable values

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]    
eggs(spam) # lists are mutable
print(spam)

import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)

# line continuation
spam = ['apples',
        'oranges',
        'bananas',
        'cats']

print(spam)
print('four score and severn' + \
      'years ago')
