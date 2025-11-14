from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Génération d'une paire de clés RSA 2048 bits
private_key = rsa.generate_private_key(public_exponent = 65537, key_size = 2048)
public_key = private_key.public_key()
print("Cles RSA generees avec succes !")

# ---- Chiffrement et déchiffrement d'un message:
message = b"Blockchain et cryptographie asymetrique"
# Chifrement:
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
    )
)
# Déchiffrement:
plaintext = private_key.decrypt(
    ciphertext, 
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
    )
)
print("Message initial :", message)
print("Message dechifree : ",plaintext.decode())

# ---- Création d'une signature:
message = b"Transaction : ALice -> Bob : 3 BTC"
# Signature avec la clé privée
signature = private_key.sign(
    message,
    padding.PSS(
        mgf = padding.MGF1(hashes.SHA256()),
        salt_length = padding.PSS.MAX_LENGTH 
    ),
    hashes.SHA256()
)
print("Signature (hex):", signature.hex()[:80], "...")

# Vérification de la signature
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf = padding.MGF1(hashes.SHA256()),
            salt_length = padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature valide - Le message est authentique")
except Exception:
    print("Signature invalide !")


