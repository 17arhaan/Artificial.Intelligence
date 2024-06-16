class Pattern4:
    def inverted_pyramid_extra_alpha(self,n) -> int:
        for i in range(n,0,-1):
            for j in range(0,i+1):
                print(j,end = " ")
            print("")
    
if __name__ == "__main__":
    n = int(input("Enter Array Length: "))
    objt = Pattern4()
    objt.inverted_pyramid_extra_alpha(n)