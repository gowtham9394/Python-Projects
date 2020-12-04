# using the addition operator without variables [String Concatenation]

name = "Gowtham" + " " + "Kumar"
print(name)

# using the addition operator with variables

first_name = "Gowtham"
last_name = "Kumar"
full_name = first_name + " " + last_name
print(full_name)

# using the new f strings [after python 3.6]
print( f"Hello {full_name}")

# using indexes to print each element

word = "Computer"
print( word [0])
print( word [1])
print( word [2])
print( word [3])
print( word [4])
print( word [5])
print( word [6])
print( word [7])
print( word [-0])
print( word [-1])
print( word [-2])
print( word [-3])
print( word [-4])
print( word [-5])
print( word [-6])
print( word [-7])

# using string slicing to print each element

print(word [0:1])
print(word [0:8])

print( word[ 0 : 5 : 3 ] )