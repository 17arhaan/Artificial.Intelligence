class Pattern5:
    def pyramid_odd_num(self,n):
        i = 1
        while i <= n:  
            j = 1
            while j <= i:
                print((i * 2 - 1) , end = " ")
                j += 1
            i += 1
            print ('')
                      
if __name__ == "__main__":
    n = int(input("Enter Array Length: "))
    objt = Pattern5()
    objt.pyramid_odd_num(n)
    
