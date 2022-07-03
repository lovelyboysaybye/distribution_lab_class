import random
from datetime import datetime
from blockchain_classes.account_class import Account
from blockchain_classes.operation_class import Operation
from blockchain_classes.constants import PUBLIC_KEY_BYTES

STUDENT_ID = 12345678
STUDENT_ID_2 = 12345679
NAME = "ANDRII"
SURNAME = "TSEMKO"
START_DATE = datetime(2021, 9, 1)
TEST_PRIVATE_KEY = 0xA0DC65FFCA799873CBEA0AC274015B9526505DAAAED385155425F7337704883E
VOTING_ACCOUNT_ID = random.getrandbits(PUBLIC_KEY_BYTES * 8)

if __name__ == "__main__":
    # Random keys account
    random_account = Account(STUDENT_ID, NAME, SURNAME, START_DATE)
    random_account.gen_account(0)
    print(random_account)
    print()

    # Private key specified account
    private_key_account = Account(STUDENT_ID_2, NAME, SURNAME, START_DATE, private_key=TEST_PRIVATE_KEY)
    private_key_account.gen_account(0)
    print(private_key_account)

    # Create transaction on voting address with candidate number 3
    print("\nCreated transaction:")
    my_transaction = private_key_account.create_vote_transaction(VOTING_ACCOUNT_ID, 3)
    print(my_transaction)
    print("Verify transaction signature:")
    print(Operation.verify_operation(my_transaction.operation, private_key_account.account_id))

    # Create transaction on voting address with candidate number 3
    print("\nCreated transaction 2:")
    my_transaction2 = private_key_account.create_vote_transaction(VOTING_ACCOUNT_ID, 5)
    print(my_transaction2)
    print("Verify transaction signature:")
    print(Operation.verify_operation(my_transaction2.operation, private_key_account.account_id))
