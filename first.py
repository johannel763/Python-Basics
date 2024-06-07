msg = "Hello World!"

print(msg[0:3])

print(msg[:])

print(msg[0:-1])

print(msg[-1:])

full_name = "Hendrik Johannes Nel"

middle_name = full_name[8:16]

first_name = full_name[0:7]

last_name = full_name[17:]

print(middle_name)

print(first_name)

print(last_name)

print(full_name[0: len(full_name)])

############### Slicing with step value

new_string = full_name[0: len(first_name):2]

print(new_string)

new_string = full_name[0: len(full_name):2]

print(new_string)

