A = {1,2,3,4,5}
B = {1,2,3}
C = {1,2,4}
D = {1,2,3,4,5}
E ={4,5,6}

#
#
# #A is strict_supeset of B and C
# #A is not strict_superset of D and E
#
# if len(A-B) > 0:
#     print("A is strict_supeset of B")
#
# if len(A - C) > 0:
#     print("A is strict_supeset of C")
#
# if len(A-D) == 0:
#     print("A is not strict_supeset of D")
#
# if len(E - A) > 0:
#     print("A is not strict_supeset of E")




def given_set(A,B):
    if len(A - B) > 0:
        print("A is strict_supeset of B")

    elif len(A - B) == 0:
        print("A is not strict_supeset of B")


    elif len(B - A) > 0:
        print("A is not strict_supeset of B")

given_set({1,2,3,4}, {1,2,3,4})
given_set({1,2,3}, {1,2,3,4})
given_set({1,2,3,4}, {1,2,3})
given_set({4,2,3}, {1,2,3,4})
given_set({1,2,3,4,5}, {4,2,1,3})