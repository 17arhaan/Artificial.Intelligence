class Pattern13:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def hollow_rect(l,b):
        for i in range(1,b+1):
            for j in range(1,l+1):
                if i == 1 or i == b or j == 1 or j == l:
                    print("*", end = " ")
                else:
                    print(" ",end = " ")
            print("")      
              
if __name__ == "__main__":
    l = int(input("Enter Length: "))
    b = int(input("Enter Breadth: "))
    objt = Pattern13()
    objt.hollow_rect(l,b)