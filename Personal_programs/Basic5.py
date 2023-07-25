

import numpy as np

def calculate_inverse(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] =1.0/values[i]
    return output


# large_array = np.random.randint(1,10, size=1000000)

result = np.random.randint(1, 10, size=100000)
print(calculate_inverse(result))

large_array = np.random.randint(1, 100, size=10000)

L = np.random.random(100)
print(np.sum(L))
