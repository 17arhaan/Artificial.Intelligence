class Pattern1:
    def pyramid_num(self,n):
        for i in range (n):
            for j in range(i+1):
                print(j+1 , end =' . ')
            print('')                 
        
if __name__ == "__main__":
    n = int(input("Enter Array Length: "))
    objt = Pattern1()
    objt.pyramid_num(n)
    