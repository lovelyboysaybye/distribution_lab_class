from random import seed
from blockchain_classes.key_pair_class import KeyPair

TEST_PRIVATE_KEY = 0xA0DC65FFCA799873CBEA0AC274015B9526505DAAAED385155425F7337704883E


if __name__ == "__main__":
    my_keys = KeyPair(private_key=TEST_PRIVATE_KEY)
    print(my_keys)
    print()

    seed(3)
    my_keys = KeyPair()
    print(my_keys)
