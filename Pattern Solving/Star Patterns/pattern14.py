class Pattern14:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def parallelogram(n):
        for i in range(1,n+1):
            for j in range(i):
                print(" ", end=" ")
            for k in range(n):
                print("*", end=" ")
            print("")
              
if __name__ == "__main__":
    n = int(input("Enter Size: "))
    objt = Pattern14()
    objt.parallelogram(n)