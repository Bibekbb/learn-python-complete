import time
import hmac
import hashlib
import struct
import base64

def generate_totp(secret, digits=10, timestep=30, t0=0):
    # Convert secret to bytes
    key = secret.encode()

    # Calculate time counter
    counter = int((int(time.time()) - t0) / timestep)

    # Pack counter in big-endian format
    counter_bytes = struct.pack(">Q", counter)

    # Create HMAC-SHA512
    hmac_hash = hmac.new(key, counter_bytes, hashlib.sha512).digest()

    # Dynamic truncation to get a 4-byte string
    offset = hmac_hash[-1] & 0x0F
    code = (struct.unpack(">I", hmac_hash[offset:offset+4])[0] & 0x7FFFFFFF) % (10 ** digits)

    return str(code).zfill(digits)

if __name__ == "__main__":
    email = "iambibekbb@gmail.com"
    secret = email + "HENNGECHALLENGE004"
    print(generate_totp(secret))
