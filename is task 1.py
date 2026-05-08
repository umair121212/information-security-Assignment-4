# Choosing two prime numbers
p = 17
q = 19

# Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Public key exponent (must be coprime with phi)
e = 7

# Finding modular inverse (private key d)
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Private key
d = mod_inverse(e, phi)

# Encryption function
def encryption(message, e, n):
    encrypted = []

    for char in message:
        m = ord(char)      # Convert character to ASCII
        c = (m ** e) % n   # RSA encryption
        encrypted.append(c)

    return encrypted

# Decryption function
def decryption(cipher, d, n):
    decrypted = ""

    for c in cipher:
        m = (c ** d) % n   # RSA decryption
        decrypted += chr(m)  # Convert ASCII back to character

    return decrypted

# Original message
message = "Hello"

print("Original Message:", message)

# Encrypt
cipher_text = encryption(message, e, n)
print("Encrypted Message:", cipher_text)

# Decrypt
plain_text = decryption(cipher_text, d, n)
print("Decrypted Message:", plain_text)