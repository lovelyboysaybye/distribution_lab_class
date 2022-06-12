from random import randbytes, seed
from AES import AES


if __name__ == "__main__":
    """
    Tests the AES library for encrypting and decrypting
    """
    text1 = b"Small text"   # less than one block size
    text2 = b"abcd" * 4     # 16 bytes block length
    text3 = b"My big text for more than 16 bytes."  # Text for more than 16 bytes

    # For the same results of generating the key
    seed(3)

    # randomly generated key
    key = randbytes(16)
    encrypted = AES(key).encrypt(text1)
    print(f"\n\tKey: {key}\n\t", end="")
    print(AES(key).decrypt(encrypted))

    # randomly generated key
    key = randbytes(16)
    encrypted = AES(key).encrypt(text2)
    print(f"\n\tKey: {key}\n\t", end="")
    print(AES(key).decrypt(encrypted))

    # randomly generated key
    key = randbytes(16)
    encrypted = AES(key).encrypt(text3)
    print(f"\n\tKey: {key}\n\t", end="")
    print(AES(key).decrypt(encrypted))
