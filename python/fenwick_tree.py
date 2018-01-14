class Fenwick_tree(object):
    #Fenwick tree for range max query implementation
    def __init__(self,size):
        self.f_tree=[0]*(size+1)
        self.length=size+1

    def maximum(self,i):
        result=0
        i+=1
        while(i>=0):
            result=max(result,self.f_tree[i])
            i=(i&(i+1))-1
        return result

    def update(self,i,value):
        i+=1
        if (self.f_tree[i]>value):
            return
        while(i<self.length):
            self.f_tree[i]=max(self.f_tree[i],value)
            i|=i+1
        return

if __name__ == '__main__':
    ft=Fenwick_tree(5)
    ft.update(3,5)
    for i in range(0,5):
        print (ft.maximum(i))
    print ("Update")
    ft.update(2,4)
    for i in range(0,5):
        print (ft.maximum(i))
    print ("Update")
    ft.update(1,6)
    for i in range(0,5):
        print (ft.maximum(i))
