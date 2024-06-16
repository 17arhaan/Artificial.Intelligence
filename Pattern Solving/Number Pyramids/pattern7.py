class Pattern7:
    def __init__(self):
        pass

    @staticmethod
    def inverse_reverse_pyramid_num(n): 
        for i in range(n,0,-1):
            for j in range(i,0,-1):
                print(j , end = " ")
            print("")
       
if __name__ == "__main__":
    n = int(input("Enter Array Length: "))
    objt = Pattern7()
    objt.inverse_reverse_pyramid_num(n)

