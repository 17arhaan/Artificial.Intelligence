class Pattern8:
    def __init__(self):
        pass

    @staticmethod
    def triangle_num(n): 
        for i in range(1,n+1):
            for j in range(n,0,-1):
                if j > i:
                    print(" ", end = ' ')
                else:
                    print(i, end = ' ')
            print("")
       
if __name__ == "__main__":
    n = int(input("Enter Array Length: "))
    objt = Pattern8()
    objt.triangle_num(n)
