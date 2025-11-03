import hashlib
from datetime import datetime

class Block:
    def __init__ (self,index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.create_hash()

    
    def create_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}".encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.create_hash()
        print(f" Essai nonce {self.nonce} : hash = {self.hash}")
        print(f"Bloc miné ! Nonce final : {self.nonce}, Hash : {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    # Niveau de la difficulté : nombre de zéros requis
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "2025-10-12", "Block de genèse", "0")
    
    def get_last_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        # Miner le bloc avant de l'ajouter
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
    
    def is_chain_valid(self):
        for i in range (1,len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i-1]
            # Vérifier l'intégrité du hash
            if current.hash != current.create_hash():
                return False
            # Vérifier le lien avec le bloc précédent
            if current.previous_hash != prev.hash:
                return False
        return True

# Instantiation de le classe Blockchain:
blockchain1 = Blockchain()
blockchain1.add_block(Block(1, str(datetime.now()), "bloc 1 de la blockchain"))
blockchain1.add_block(Block(2,str(datetime.now()),"bloc 2 de la blockchain"))
blockchain1.add_block(Block(3, str(datetime.now()), "bloc 3 de la blockchain"))
blockchain1.add_block(Block(4,str(datetime.now()),"bloc 4 de la blockchain"))

# test de falsification du bloc 4:
blockchain1.chain[3].data = "HACK"

# Vérification de la validité:
if blockchain1.is_chain_valid():
    print(" aucun bloc n a ete falsifie.")
else:
    print("Une flasification a ete faite !")

