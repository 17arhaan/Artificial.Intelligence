class Pattern2:
    def inverted_pyramid(self, n):
        for i in range(n,0,-1):
            for j in range(1,i+1):
                print(j,end=" ")
            print("")

if __name__ == "__main__":
    n = int(input("Enter Array Length: "))
    objt = Pattern2()
    objt.inverted_pyramid(n)
    