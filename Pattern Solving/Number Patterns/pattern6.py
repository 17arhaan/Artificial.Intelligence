class Pattern6:
    def __init__(self):
        pass

    @staticmethod
    def reverse_pyramid_num(n): 
        for i in range(1,n+1):
            for j in range(i,0,-1):
                print(j , end = " ")
            print("")
       
if __name__ == "__main__":
    n = int(input("Enter Array Length: "))
    objt = Pattern6()
    objt.reverse_pyramid_num(n)

