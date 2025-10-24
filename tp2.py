import hashlib
import json

class Block:
    def __init__(self, index, timsetamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timsetamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.create_hash()

    def create_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}".encode()
        return hashlib.sha256(block_string).hexdigest()


def Verify_block(blockchain):
    for i in range(1,len(blockchain)):
        block_actuel = blockchain[i]
        previous_block = blockchain[i-1]
        if block_actuel.previous_hash != previous_block.hash :
            return False
    return True
    
#  Création de la genèse :

# genesis = Block(0,"2025-10-12 00:05", "Alice envoie 7 BTC", previous_hash="0")
# --> L'affichage des informations du premier bloc (La genèse)
# print(f"Index : {genesis.index}")
# print(f"timestamp : {genesis.timestamp}")
# print(f"Data : {genesis.data}")
# print(f"Previous hash : {genesis.previous_hash}")
# print(f"hash: {genesis.hash}")

# --> Création de la liste de blocks
BlockChain_List = []
genesis = Block(0,"2025-10-12", "Bloc de genèse","0")
BlockChain_List.append(genesis)
Block1 = Block(1,"2025-10-12", "Alice envoie 5 BTC", BlockChain_List[-1].hash)
BlockChain_List.append(Block1)
Block2 = Block(2,"2025-10-12", "Bob envoie 3 BTC", BlockChain_List[-1].hash)
BlockChain_List.append(Block2)

# Affichage de tous les blocks :
print(json.dumps([b.__dict__ for b in BlockChain_List], indent=4))
BlockChain_test = [genesis, Block1]
if Verify_block(BlockChain_test):
    print(" Compatibe !!")
else : 
    print(" Incompatibe !!")

