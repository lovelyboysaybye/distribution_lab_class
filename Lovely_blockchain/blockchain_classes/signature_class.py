import random
from blockchain_classes.constants import PRIVATE_KEY_LEN
from blockchain_classes.constants import PUBLIC_KEY_BYTES
from blockchain_classes.ecc_class import ECC
from blockchain_classes.sha1_class import SHA1


class Signature:
    """
    Class for generating and verifying signature of message.
    """
    @staticmethod
    def generate_signature(private_key: int, message: str) -> (int, int):
        """
        Generates the signature for message by specific private_key.
        :param private_key: int value of private key
        :param message: message for signing
        :return: r and s
        """
        random_val = random.getrandbits(PRIVATE_KEY_LEN)

        x_rand, y_rand = ECC.get_public_key(ECC.G_POINT, random_val)
        r = x_rand % ECC.N
        s = ((Signature.hash(message) + r * private_key) * ECC.modinv(random_val, ECC.N)) % ECC.N
        return int.from_bytes([*r.to_bytes(32, byteorder='big'),
                               *s.to_bytes(32, byteorder='big')], byteorder='big')

    @staticmethod
    def verify_signature(signature: int, public_key: int, message: str) -> bool:
        """
        Verifies whether the signature are correct or not.
        :param signature: r and s of signing as one variable
        :param public_key: public key for verifying the signing by private key of this public key.
        :param message: message that signing
        :return: true if signature are correct otherwise false
        """
        signature_bytes = signature.to_bytes(32 * 2, byteorder='big')
        signature_r, signature_s = int.from_bytes(signature_bytes[:32], byteorder='big'), \
                                   int.from_bytes(signature_bytes[32:], byteorder='big')
        public_key_bytes = public_key.to_bytes(PUBLIC_KEY_BYTES, byteorder='big')
        public_key = [int.from_bytes(public_key_bytes[1:(PUBLIC_KEY_BYTES - 1) // 2 + 1], byteorder='big'),
                      int.from_bytes(public_key_bytes[(PUBLIC_KEY_BYTES - 1) // 2 + 1:], byteorder='big')]
        w = ECC.modinv(signature_s, ECC.N)
        p1 = ECC.get_public_key(ECC.G_POINT, (Signature.hash(message) * w) % ECC.N)
        p2 = ECC.get_public_key(public_key,  (signature_r * w) % ECC.N)
        x, y = ECC.ECadd(p1, p2)
        return signature_r == x

    @staticmethod
    def hash(message: str) -> int:
        """
        Gets hash of message
        :param message: str of message
        :return: hash of message
        """
        return SHA1().get_hash(message)
