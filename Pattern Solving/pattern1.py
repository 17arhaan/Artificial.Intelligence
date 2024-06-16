class Pattern1:
    def pyramid_num(self,n,array):
        self.array = []
        n = len(array)
        for i in range (n):
           print(array[i])                 

if __name__ == "__main__":
    m = int(input("Enter Array Length: "))
    pyramid_nun(m)