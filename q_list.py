q_size = 5
front = -1
q = [None] * q_size
print(q)
def insert_front(front, item):
    if front == q_size-1:
        print("Que is overflow")
        return front
    else:
        front += 1
        q[front] = item
        return front


def remove_rear(front):
    if -1 == front:
        print("Que is underflow")
        return front
    else:
        q.pop(0)
        front -= 1
        q.append(None)
        return front

front = insert_front(front,10)
front = insert_front(front,8)
front = insert_front(front,5)
front = insert_front(front,6)
front = insert_front(front,7)
front = insert_front(front,2)

print(q)
front = remove_rear(front)
front  = remove_rear(front)
front  = remove_rear(front)
front  = remove_rear(front)
front  = remove_rear(front)
front  = remove_rear(front)

# rear = remove_rear(rear, front)
# rear = remove_rear(rear, front)
# rear = remove_rear(rear, front)
# rear = remove_rear(rear)
print(q)

front = insert_front(front,6)
front = insert_front(front,7)

print(q)



# circular- automatically circulate, single ended que, double ended



