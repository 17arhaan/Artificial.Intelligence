class Pattern15:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def inverted_pyramid(n):
        for i in range(n):
            for j in range(i):
                print(" ", end="")
            for k in range(2 * (n - i) - 1):
                print("*", end="")
            print("")
            
if __name__ == "__main__":
    n = int(input("Enter Size: "))
    objt = Pattern15()
    objt.inverted_pyramid(n)