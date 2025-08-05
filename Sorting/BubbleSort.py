ll=[5,4,2,1,3]

def bubblesort(ll:list):
    for i in range(len(ll)-1,0,-1):
        for j in range(0,i):
            if ll[j] > ll[j+1]:
                ll[j],ll[j+1]=ll[j+1],ll[j]


ll = [5,4,2,1,3]
bubblesort(ll)
print(ll)


