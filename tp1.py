# La classe block :
class Block:
    def __init__(self, index, timestamp, data, previous_hash='') :
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = ''

# ----------------------------- La liste de blocks : -------------------------------------

# --> Création du premier bloc (La genèse)
genesis_block = Block (0,"2025-10-12 00:00", "Bloc de genese", previous_hash="0")
blockchain = [genesis_block]
# --> L'affichage des informations du premier bloc (La genèse)
print(f"Index : {genesis_block.index}")
print(f"timestamp : {genesis_block.timestamp}")
print(f"Data : {genesis_block.data}")
print(f"Previous hash : {genesis_block.previous_hash}")
print(f"hash: {genesis_block.hash}")

# --> Création d'autres blocs
bloc1 = Block(1,"2025-10-12 00:05", "Alice envoie 5 BTC", previous_hash=genesis_block)
bloc2 = Block(2,"2025-10-12 00:10", "Houssam envoie 6 BTC", previous_hash=bloc1.previous_hash)

blockchain.append(bloc1)
blockchain.append(bloc2)
# --> L'affichage des informations des blocs
print("***** LES INFORMATIONS SUR BLOCS : *****")
for bloc in blockchain :
    print(f"Bloc {bloc.index} : data={bloc.data}, prev_hash={bloc.previous_hash}, hash={bloc.hash}")
