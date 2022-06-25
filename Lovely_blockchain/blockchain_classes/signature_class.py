import random
from blockchain_classes.constants import PRIVATE_KEY_LEN
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
        return r, s

    @staticmethod
    def verify_signature(signature_r: int, signature_s: int, public_key: int, message: str) -> bool:
        """
        Verifies whether the signature are correct or not.
        :param signature_r: r of signing
        :param signature_s: s of signing
        :param public_key: public key for verifying the signing by private key of this public key.
        :param message: message that signing
        :return: true if signature are correct otherwise false
        """
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
