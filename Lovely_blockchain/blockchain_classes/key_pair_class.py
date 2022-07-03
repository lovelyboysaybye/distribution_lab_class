import random
from blockchain_classes.constants import PRIVATE_KEY_LEN
from blockchain_classes.ecc_class import ECC


class KeyPair:
    """
    Class generates private and public keys.
    """
    def __init__(self, private_key: int = 0) -> None:
        """
        Initializes the object of KeyPair class.
        :param seed: seed for generating random value of private key.
        """
        if private_key:
            self.__private_key = private_key
        else:
            self.__private_key = random.getrandbits(PRIVATE_KEY_LEN)
        self.public_key = ECC.get_public_key(ECC.G_POINT, self.__private_key)

        # compressed public key used
        self.compressed_public_key = "03" if self.public_key[1] % 2 else "02" + hex(self.public_key[0])[2:].zfill(64)

        self.public_key = int.from_bytes([0x04,
                                          *self.public_key[0].to_bytes(32, byteorder='big'),
                                          *self.public_key[1].to_bytes(32, byteorder='big')], byteorder='big')

    def get_keys(self) -> (int, int):
        """
        Gets actual values of public and private keys.
        :return: int representations of public and private keys
        """
        return self.public_key, self.__private_key

    def __str__(self) -> str:
        return f"Private key: {self.__private_key}\n" \
               f"Compressed public key: {self.compressed_public_key}\n" \
               f"Full public key: 04{hex(self.public_key)}"
