import hmac, hashlib, base64, time, struct

def generate_totp(secret, time_step=30, digits=10, t0=0):
    counter = int((int(time.time()) - t0) / time_step)
    key = secret.encode()
    msg = struct.pack(">Q", counter)
    hmac_hash = hmac.new(key, msg, hashlib.sha512).digest()
    offset = hmac_hash[-1] & 0x0F
    code = (struct.unpack(">I", hmac_hash[offset:offset + 4])[0] & 0x7FFFFFFF) % (10 ** digits)
    return str(code).zfill(digits)

email = "iambibekbb@gmail.com"
secret = email + "HENNGECHALLENGE004"

print(generate_totp(secret))
