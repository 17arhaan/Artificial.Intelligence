class Pattern12:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def hollow_square(n):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i == 1 or i == n or j == 1 or j == n:
                    print("*",end = " ")
                else:
                    print(" ",end = " ")
            print("")
        
if __name__ == "__main__":
    n = int(input("Enter Array Length: "))
    objt = Pattern12()
    objt.hollow_square(n)