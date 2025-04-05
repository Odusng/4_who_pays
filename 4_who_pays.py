friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random
payer = random.randint (0, 4)
if payer < 1:
    print("Alice")
elif payer == 1 and payer < 2:
    print("Bob")
elif payer == 2 and payer < 3:
    print("Charlie")
elif payer == 3 and payer < 4:
    print("David")
else:
    print("Emanuel")