import hashlib
import time
class Transaction:
    def __init__(self, from_adress, to_adress, amount):
        self.from_adress = from_adress
        self.to_adress = to_adress
        self.amount = amount

class Block:
    def __init__(self, timestamp, transactions, previous_hash=''):
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.create_hash()
    
    def create_hash(self):
        block_string = (str(self.previous_hash) + str(self.timestamp) 
                        + str([t.__dict__ for t in self.transactions])
                        + str(self.nonce)).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target :
            self.nonce += 1
            self.hash = self.create_hash()
        print(f"Bloc mine ! Nonce = {self.nonce} , Hash = {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]   
        self.difficulty = 2
        self.pending_transactions = []
        self.mining_rewards = 10

    def create_genesis_block(self):
        return Block("01/01/2020", [], "0")
    
    def get_last_block(self):
        return self.chain[-1]
    
    def create_trasanction(self, transaction):
        # Ajoute une transaction à la liste des transactions en attente 
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner_address):
        # Créer un bloc avec toutes les transactions en attente
        block = Block(time.time(), self.pending_transactions, self.get_last_block().hash)
        block.mine_block(self.difficulty)
        print("Bloc valide et ajoute a la chaine !")
        self.chain.append(block)
        # Après minage, on crée une transaction de récompense pour le mineur
        self.pending_transactions = [
            Transaction(None, miner_address, self.mining_rewards)
        ]

    def get_balance_of_address(self, address):
        balance = 0
        for block in self.chain:
            for trans in block.transactions:
                if trans.from_adress == address:
                    balance -= trans.amount
                if trans.to_adress == address:
                    balance += trans.amount
        return balance
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i-1]
            if current.hash != current.create_hash() or current.previous_hash != prev.hash:
                return False
        return True

# ---------------- test et vérification:
OurBlockchain = Blockchain()
# Création des transactions
# Transaction N°1 :
OurBlockchain.create_trasanction(Transaction("Alice","Bob",50))
# Transaction N°2 :
OurBlockchain.create_trasanction(Transaction("Bob","Charlie",25))
# Transaction N°3 :
OurBlockchain.create_trasanction(Transaction("Salama","Meriam",60))

# Miner la 1ère transaction en attente -- appel N°1
OurBlockchain.mine_pending_transactions('Alice')

# Affichage du solde du mineur:
print(f"Le solde du mineur (Alice) = {OurBlockchain.get_balance_of_address('Alice')}")

# Miner la 1ère transaction en attente -- Appel N°2
OurBlockchain.mine_pending_transactions('Alice')

# Affichage du solde :
print(f"Aprs le 2eme minage : Le solde du mineur (Alice) = {OurBlockchain.get_balance_of_address('Alice')}")

# Miner la 3ème transaction en attente -- appel N°1
OurBlockchain.mine_pending_transactions('Salama')

#Affichage du solde:
print(f"Aprs le 1er minage : Le solde du mineur (Salama)= {OurBlockchain.get_balance_of_address('Salama')}")

# Miner la 3ème transaction en attente -- appel N°2
OurBlockchain.mine_pending_transactions('Salama')

#Affichage du solde:
print(f"Aprs le 2eme minage : Le solde du mineur (Salama)= {OurBlockchain.get_balance_of_address('Salama')}")

# Vérification de la validité:
print(" \n\t\t------------------------------ TEST DE VALIDITE ------------------------------")
if OurBlockchain.is_chain_valid():
    print("Les blocs de votre blockchain sont encore valides !")
else:
    print("Oups! Un problème est servenu")



