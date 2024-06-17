class Pattern10:
    def __init__(self):
        pass

    @staticmethod
    def forward_star_pyramid(n): 
        for i in range(1,n+1):
            for j in range(i,n+1):
                print("*", end = ' ')
            print("")
       
if __name__ == "__main__":
    n = int(input("Enter Array Length: "))
    objt = Pattern10()
    objt.forward_star_pyramid(n)
