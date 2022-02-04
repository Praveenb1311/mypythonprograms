# with open("hello.txt", "w") as of:  #write mode, read mode, append mode----
#     of.write("this is my first file operation")
#     of.write("\n")
#     of.write("my  best friend huli")
#

# with open("hello.txt", "a") as of:  # write mode, read mode, append mode----
#     of.write("\n")
#     of.write("I am appending to the existing file")
#     of.write("\n")
#     of.write("I am done with appending")

#
# with open("hello.txt", "w") as of:  # write mode, read mode, append mode----
#     of.write("\n")
#     of.write("I am appending to the existing file")
#     of.write("\n")
#     of.write("I am done with appending")

#
# with open("hello.txt", "r") as fp:  # write mode, read mode, append mode----fp-file_pointer
#     data = fp.read()
#     print(data)

#
# with open("hello.txt", "r") as fp:  # write mode, read mode, append mode----fp-file_pointer
#     data = fp.readlines()
#
# print(data)

# with open("hello.txt", "r+") as fp: #read and write
#     data = fp.readlines()
#     for line in data:
#         fp.writelines(line)
#     fp.writelines("\n")
#     fp.writelines("I am done with r+ mode")


#to check the name
with open("hello.txt", "r") as fp:
    for data in fp.readlines()[7:]:
        if "Praveen" in data:
            print("yes found in : ", data)
    # data = fp.readlines()
    # for line in data:
    #     if "Praveen" in line:
    #         print("yes found in : ", line)
    #         break

