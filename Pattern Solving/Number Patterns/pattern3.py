class Pattern3:
    def inverted_pyramid_same_num(self, n):
        for i in range(n,0,-1):
            for j in range(1,i+1):
                print("7",end=" ")
            print("")

if __name__ == "__main__":
    n = int(input("Enter Array Length: "))
    objt = Pattern3()
    objt.inverted_pyramid_same_num(n)
    