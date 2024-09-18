# The list data type
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

# For loops with lists, multiple assignment, and augmented operators

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

