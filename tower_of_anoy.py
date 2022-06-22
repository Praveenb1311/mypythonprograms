def hanoi(disks, source, auxiliary, target):
    if disks == 1:
        print('Move disk 1 from peg {} to peg {}.'.format(source, target))
        return

    hanoi(disks - 1, source, target, auxiliary)
    print('Move disk {} from peg {} to peg {}.'.format(disks, source, target))
    hanoi(disks - 1, auxiliary, source, target)


disks = int(input('Enter number of disks: '))
hanoi(disks, 'A', 'B', 'C')
print(2**disks-1)


# Recursive function to solve Tower
# of Hanoi puzzle
def towerOfHanoi(n, from_rod, to_rod, aux_rod1,
aux_rod2):

if (n == 0):
return
if (n == 1):
print(“Move disk”, n, “from rod”,
from_rod, “c to rod”, to_rod)
return

towerOfHanoi(n – 2, from_rod, aux_rod1,
aux_rod2, to_rod)
print(“Move disk”, n-1, “from rod”, from_rod,
“c to rod”, aux_rod2)


print(“Move disk”, n, “from rod”, from_rod,
“c to rod”, to_rod)

print(“Move disk”, n-1, “from rod”, aux_rod2,
“c to rod”, to_rod)

towerOfHanoi(n – 2, aux_rod1, to_rod,
from_rod, aux_rod2)

# driver program
n = 4 # Number of disks

# A, B, C and D are names of rods
towerOfHanoi(n, ‘A’, ‘D’, ‘B’, ‘C’)

# This code is contributed by Smitha.
