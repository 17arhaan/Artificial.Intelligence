class Pattern11:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def filled_square(n):
        for i in range(1,n+1):
            for j in range(n):
                print("*",end = " ")
            print("")
        
if __name__ == "__main__":
    n = int(input("Enter Array Length: "))
    objt = Pattern11()
    objt.filled_square(n)