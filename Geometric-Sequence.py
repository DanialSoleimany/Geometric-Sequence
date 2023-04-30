# Geometric sequence
# Ex. 3, 9, 27, 81, 243, ... 

def sequence(start, step, number):
    sequence = []
    multi = start
    for number in range(1, number+1):
        sequence.append(multi)
        multi *= step
    return sequence

start = int(input("Start:\n"))
step = int(input("Step:\n"))
number = int(input("Number:\n"))

print(sequence(start, step, number))