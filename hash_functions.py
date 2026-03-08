# Python One-Way Hash Functions Guide
# A one-way hash function maps arbitrary input to a fixed-size digest.
# "One-way" means you cannot reverse the digest back to the original input.

import hashlib
import hmac
import os

# ─────────────────────────────────────────────
# 1. Core properties of a cryptographic hash
# ─────────────────────────────────────────────
# • Deterministic   — same input always yields the same digest
# • Fixed-length    — output size is constant regardless of input size
# • Pre-image resistant — given digest d, finding m where hash(m)=d is infeasible
# • Collision resistant — finding two inputs with the same digest is infeasible
# • Avalanche effect — a 1-bit change in input flips ~50% of output bits

# ─────────────────────────────────────────────
# 2. hashlib — the standard library interface
# ─────────────────────────────────────────────
print("=== Available algorithms ===")
print(hashlib.algorithms_guaranteed)   # always available on every platform

# ─────────────────────────────────────────────
# 3. SHA-256 — the everyday workhorse
# ─────────────────────────────────────────────
print("\n=== SHA-256 ===")
data = b"Hello, world!"          # hashlib always works on bytes, not str

h = hashlib.sha256(data)
print(h.hexdigest())             # 64 hex chars = 256 bits
print(h.digest_size)             # 32 bytes
print(len(h.hexdigest()))        # 64 hex characters

# Feeding data incrementally (streaming large files)
h2 = hashlib.sha256()
h2.update(b"Hello, ")
h2.update(b"world!")             # same result — update() concatenates
print(h2.hexdigest())

# ─────────────────────────────────────────────
# 4. SHA-512 — larger digest, harder brute-force
# ─────────────────────────────────────────────
print("\n=== SHA-512 ===")
h = hashlib.sha512(data)
print(h.hexdigest())             # 128 hex chars = 512 bits
print(h.digest_size)             # 64 bytes

# ─────────────────────────────────────────────
# 5. SHA-3 family — different internal design (Keccak)
# ─────────────────────────────────────────────
print("\n=== SHA-3 ===")
print(hashlib.sha3_256(data).hexdigest())   # 256-bit SHA-3
print(hashlib.sha3_512(data).hexdigest())   # 512-bit SHA-3

# ─────────────────────────────────────────────
# 6. BLAKE2 — fast, secure, modern alternative
# ─────────────────────────────────────────────
print("\n=== BLAKE2 ===")
# BLAKE2b: optimised for 64-bit platforms; max digest 64 bytes
print(hashlib.blake2b(data).hexdigest())            # default 64-byte digest
print(hashlib.blake2b(data, digest_size=32).hexdigest())  # 32-byte digest

# BLAKE2s: optimised for 8–32-bit platforms; max digest 32 bytes
print(hashlib.blake2s(data).hexdigest())            # default 32-byte digest

# ─────────────────────────────────────────────
# 7. MD5 and SHA-1 — legacy only, NOT for security
# ─────────────────────────────────────────────
print("\n=== MD5 / SHA-1 (legacy — do NOT use for security) ===")
# Both are cryptographically broken (collisions can be engineered).
# Acceptable only for checksums / non-security deduplication.
print(hashlib.md5(data).hexdigest())        # 32 hex chars = 128 bits
print(hashlib.sha1(data).hexdigest())       # 40 hex chars = 160 bits

# ─────────────────────────────────────────────
# 8. Avalanche effect demonstration
# ─────────────────────────────────────────────
print("\n=== Avalanche effect ===")
msg_a = b"Hello, world!"
msg_b = b"Hello, World!"   # single uppercase 'W' — 1 bit difference

ha = hashlib.sha256(msg_a).hexdigest()
hb = hashlib.sha256(msg_b).hexdigest()

# Count differing bits
bits_a = bin(int(ha, 16))[2:].zfill(256)
bits_b = bin(int(hb, 16))[2:].zfill(256)
diff_bits = sum(a != b for a, b in zip(bits_a, bits_b))

print(f"msg_a hash : {ha}")
print(f"msg_b hash : {hb}")
print(f"Bits that differ: {diff_bits} / 256 ({diff_bits/256*100:.1f}%)")  # ~50%

# ─────────────────────────────────────────────
# 9. File integrity check
# ─────────────────────────────────────────────
print("\n=== File integrity check ===")

def sha256_file(path: str) -> str:
    """Return the SHA-256 hex digest of a file, reading it in chunks."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

# Demo: hash this script itself
digest = sha256_file(__file__)
print(f"SHA-256 of hash_functions.py: {digest}")

# ─────────────────────────────────────────────
# 10. Password hashing — hashlib.scrypt / pbkdf2_hmac
#     Never store plain passwords or use fast hashes (SHA-256 etc.) for passwords!
#     Use a slow, salted KDF (key derivation function) instead.
# ─────────────────────────────────────────────
print("\n=== Password hashing with PBKDF2 ===")
password = b"super_secret_password"
salt = os.urandom(16)           # random salt — store alongside the digest

dk = hashlib.pbkdf2_hmac(
    hash_name="sha256",
    password=password,
    salt=salt,
    iterations=600_000,         # NIST-recommended minimum (2023)
)
print(f"Salt (hex) : {salt.hex()}")
print(f"Digest     : {dk.hex()}")

# Verify: repeat derivation with the stored salt
dk_verify = hashlib.pbkdf2_hmac("sha256", password, salt, 600_000)
print(f"Password matches: {dk == dk_verify}")   # True

# ─────────────────────────────────────────────
# 11. HMAC — keyed hash for message authentication
#     Proves both integrity AND authenticity (sender knows the secret key).
# ─────────────────────────────────────────────
print("\n=== HMAC-SHA256 ===")
secret_key = b"shared_secret"
message    = b"Transfer $100 to Alice"

mac = hmac.new(secret_key, message, hashlib.sha256).hexdigest()
print(f"HMAC : {mac}")

# Constant-time comparison prevents timing attacks
received_mac = mac   # simulating a message received over the network
is_authentic = hmac.compare_digest(
    hmac.new(secret_key, message, hashlib.sha256).digest(),
    bytes.fromhex(received_mac),
)
print(f"Message authentic: {is_authentic}")   # True

# ─────────────────────────────────────────────
# 12. Quick-reference cheat sheet
# ─────────────────────────────────────────────
print("\n=== Cheat sheet ===")
cheat = [
    ("SHA-256",   "General purpose, widely trusted",              "✓ Use"),
    ("SHA-512",   "Larger margin; good on 64-bit CPUs",           "✓ Use"),
    ("SHA-3-256", "Different design (Keccak); standard compliant","✓ Use"),
    ("BLAKE2b",   "Fastest secure hash; built-in key/salt/len",   "✓ Use"),
    ("PBKDF2",    "Password hashing (slow KDF)",                  "✓ Use for passwords"),
    ("SHA-1",     "Broken — collision attacks demonstrated",      "✗ Avoid"),
    ("MD5",       "Broken — collision attacks trivial",           "✗ Avoid"),
]
col = "{:<12} {:<47} {}"
print(col.format("Algorithm", "Notes", "Verdict"))
print("-" * 72)
for row in cheat:
    print(col.format(*row))
