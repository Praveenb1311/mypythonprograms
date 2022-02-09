def crop_sentense(sentense,k):
    if k >= len(sentense):
        return sentense
    split_sentense = sentense.split()
    croped_sentense = sentense[:k+1]
    split_cropped_sentense = croped_sentense.split()
    print(split_cropped_sentense, split_sentense)
    print(croped_sentense)
    zip_sentense = list(zip(split_cropped_sentense,split_sentense))
    print(zip_sentense)

    if zip_sentense[-1][0] == zip_sentense[-1][1]:
        return "".join(croped_sentense)
    else:
        joined_sentense = "".join(croped_sentense)
        stripped_sentense = joined_sentense.rstrip(zip_sentense[-1][0])
        return stripped_sentense.rstrip()
sentense_1 = "Hello Huli, How are you?"
print(crop_sentense(sentense_1,10))
sentense_1 = "I am fine Thank you for asking"
print(crop_sentense(sentense_1,17))

sentense_1 = "Hello world you are so great"
print(crop_sentense(sentense_1,29))