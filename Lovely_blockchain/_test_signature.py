from blockchain_classes.key_pair_class import KeyPair
from blockchain_classes.signature_class import Signature

TEST_PRIVATE_KEY = 0xA0DC65FFCA799873CBEA0AC274015B9526505DAAAED385155425F7337704883E


if __name__ == "__main__":
    public_key, private_key = KeyPair(private_key=TEST_PRIVATE_KEY).get_keys()
    wrong_private_key = 75263518707598184987916378021939673586055614731957507592904438851787542395619

    correct_message = "My messy message"
    wrong_message_lost_chars = correct_message[:-3]

    print("Check if all correct:")
    r, s = Signature.generate_signature(private_key, correct_message)
    print(Signature.verify_signature(r, s, public_key, correct_message))

    print("\nCheck if wrong private_key was used:")
    r, s = Signature.generate_signature(wrong_private_key, correct_message)
    print(Signature.verify_signature(r, s, public_key, correct_message))

    print("\nCheck if some characters in message are lost")
    r, s = Signature.generate_signature(private_key, correct_message)
    print(Signature.verify_signature(r, s, public_key, wrong_message_lost_chars))
