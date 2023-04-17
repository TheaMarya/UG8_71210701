class Kasir:
    def __init__(self):
        self.pejual = []
    
    def __len__(self):
        return len(self.pejual)
    
    def is_empty(self):
        return len(self.pejual) == 0
    
    def dequeue(self):
        if not self.is_empty():
            return self.pejual.pop(0)
    
    def enqueue(self, pelanggan):
        self.pejual.append(pelanggan)
        
    def printAll(self):
        print("=== Kasir ===")
        for i in range(len(self.pejual)):
            print(f"{i+1}. {self.pejual[i]}")

pejual = Kasir()

pejual.enqueue("Haniif")
pejual.enqueue("Sindu")
pejual.enqueue("Dedi")
pejual.printAll()

print("Pelanggan Haniif Selesai Membayar")
pejual.dequeue()
print("* Melakukan Resize *")
pejual.enqueue("Beatrix")
pejual.enqueue("Kosong")
pejual.enqueue("Kosong")
pejual.printAll()

print("Pelanggan Sindu Selesai Membayar")
pejual.dequeue()
pejual.printAll()

pejual.enqueue("Shalon")
pejual.printAll()