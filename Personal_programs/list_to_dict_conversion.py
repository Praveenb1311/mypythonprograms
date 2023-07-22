def list_to_dic():
    list1 = ["Hello", "Praveen", "Message"]
    list2 = [122, 232,540]
    result = dict(zip(list1,list2))
    print(result)
list_to_dic()


def dic_to_tuple():
    val = {'Hello': 122, 'Praveen': 232, 'Message': 540}
    for i in val.items():
        print(i)

dic_to_tuple()


def dict_to_list():

    dict2 = {1: 'one', 2: 'two', 3: 'three'}
    list2 = []
    for i in dict2.items():
        list2.extend(list(i))
    print(list2)
dict_to_list()