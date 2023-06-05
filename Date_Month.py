class Month_Days:
    def __init__(self, x=None, y=None):
        self.Month = x
        self.Days = y

    def __add__(self, x):
        temp = Month_Days()
        temp.Month = self.Month + x.Month
        temp.Days = self.Days + x.Days
        if temp.Days >= 30:
            temp.Month += 1
            temp.Days -= 30
            return temp

    def __str__(self):
        return 'Months:' + str(self.Month) + ' Days: ' + str(self.Days)


d1 = Month_Days(10, 24)
d2 = Month_Days(15, 15)
print("d1= {} d2={}".format(d1, d2))

d3 = d1 + d2
print(d3)