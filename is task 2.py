import hashlib

# Key generation
p = 5
q = 11
n = p * q
phi = (p - 1) * (q - 1)

# Public key (must be coprime with phi)
e = 3

def mod_inverse(e, phi):   # Find private key d
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

d = mod_inverse(e, phi)

def get_hash(message):
    return int(hashlib.sha256(message.encode()).hexdigest(), 16) % n

# SIGN MESSAGE
def sign(message, d, n):
    msg_hash = get_hash(message)
    signature = pow(msg_hash, d, n)
    return signature

# VERIFICATION
def verify(message, signature, e, n):
    msg_hash = get_hash(message)
    decrypted_hash = pow(signature, e, n)
    return msg_hash == decrypted_hash

message = "Umair"

print("Message:", message)

signature = sign(message, d, n)
print("Digital signature:", signature)

# Let's verify
is_valid = verify(message, signature, e, n)
print("Verification (original message):", is_valid)

# Modification in message
fake_message = "Umair Ahmed"   # Message changed/modified

validation_check = verify(fake_message, signature, e, n)
print("Verification (modified message):", validation_check)