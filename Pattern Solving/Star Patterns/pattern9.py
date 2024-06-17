class Pattern9:
    def __init__(self):
        pass

    @staticmethod
    def downward_star_pyramid(n): 
        for i in range(1,n+1):
            for j in range(n,0,-1):
                if j > i:
                    print(" ", end = ' ')
                else:
                    print("*", end = ' ')
            print("")
       
if __name__ == "__main__":
    n = int(input("Enter Array Length: "))
    objt = Pattern9()
    objt.downward_star_pyramid(n)
