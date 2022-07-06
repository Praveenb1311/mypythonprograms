import os
size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')
else:
    print("file is not empty")
    # with open("test.txt") as f:
    #     print(f.read())
    # with open("test.txt", "w") as f:
    #     print(f.write("huli is adding"))
    with open("test.txt", "a") as f:
        print(f.write("\nhuli and praveen are appending"))
num = 8
print('%o' % num)
print('%.2f' % num)
print('%d' % num)
print(bin(num))
