class Pattern16:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def hollow_pyramid(n):
        for i in range(n):
            for j in range(n - i - 1):
                print(" ", end="")
            for k in range(2 * i + 1):
                if i == n - 1 or k == 0 or k == 2 * i:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("")
            
    @staticmethod
    def inverted_hollow_pyramid(n):
        for i in range(n):
            for j in range(i):
                print(" ", end="")
            for k in range(2 * (n - i) - 1):
                if i == 0 or k == 0 or k == 2 * (n - i) - 2:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("")
            
if __name__ == "__main__":
    n = int(input("Enter Size: "))
    objt = Pattern16()
    objt.hollow_pyramid(n)
    objt.inverted_hollow_pyramid(n)