def count_frequency():
    str1 = input("Please enter the sentance: ").upper() # this prints in {} and class will consider as string
    li = str1.split() # split prints the list
    print(li)
    d ={}

    for i in li:
        if i not in d.keys():  # insted of this we can simply fy by putting get method d[i] = d.get(i,0)+1
            d[i] = 0
        d[i] = d[i]+1
    print("Frequency of words are as shown ", d)

count_frequency()
