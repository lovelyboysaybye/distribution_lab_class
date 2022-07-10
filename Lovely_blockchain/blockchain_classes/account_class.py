from datetime import datetime
from typing import List
from blockchain_classes.key_pair_class import KeyPair
from blockchain_classes.signature_class import Signature
from blockchain_classes.operation_class import Operation
from blockchain_classes.transaction_class import Transaction
from blockchain_classes.blockchain_class import Blockchain


class Account:
    """
    Account of student. This type of account can only spent voting tickets on votes.
    """
    def __init__(self, student_id: int, name: str, surname: str, start_date: datetime, private_key: int = 0) -> None:
        """
        Initializes the account object.
        :param student_id: id of student card
        :param name: name of student
        :param surname: surname of student
        :param start_date: date of starting studying
        :param private_key: private key if user want to generate it by himself.
        """
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.start_date = start_date
        self.__nonce = 0

        # 'account_id' field is a public key of student.
        self.account_id = 0
        self.__private_key = private_key
        self.gen_account()

    def get_nonce(self) -> int:
        """
        Gets the nonce value for transaction. Used for checking duplicates of txs.
        :return: int value of nonce
        """
        return self.__nonce

    def gen_account(self) -> None:
        """
        Generates the account by creating KeyPair of private and public keys.
        """
        self.account_id, self.__private_key = KeyPair(private_key=self.__private_key).get_keys()

    def create_vote_transaction(self, voting_ticket: int, voting_address: int, vote_number: int) -> Transaction:
        """
        Creates the vote transaction.
        :param voting_ticket: the hash of transaction, that provide ability for account for voting.
            Rule: voting ticket transaction should point on the transaction, that sent by the voting address account.
                  That rule used for participating in parallel votes.
                  Also, the voting_ticket transaction should be sent for the current user. It prevent for spending the
                    voting ticket by another user.
        :param voting_address: account_id for sending the vote message.
        :param vote_number: number of candidate
        :return: str of transaction
        """
        operation = Operation(self.account_id, voting_ticket, voting_address, vote_number, self.__private_key)
        transaction = Transaction(operation, self.__nonce)
        self.__nonce += 1
        return transaction

    def get_voting_tickets(self, blockchain: Blockchain) -> List[Transaction]:
        """
        Gets all voting tickets for this account.
        :return: list of transactions
        """
        voting_tickets = []
        for tmp_voting_ticket in blockchain.voting_tickets:
            tx = blockchain.get_tx_by_id(tmp_voting_ticket)
            if tx.operation.receiver_id == self.account_id:
                voting_tickets.append(tx)
        return voting_tickets

    def sign_data(self, message: str) -> int:
        """
        Generates the signature for message by specific private_key.
        :param message: message for signing
        :return: r and s
        """
        return Signature.generate_signature(self.__private_key, message)

    def __str__(self) -> str:
        """
        :return: string representation of account
        """
        return f"Name: {self.name}\nSurname: {self.surname}\nStudent_id: {self.student_id}\n" \
               f"Start date of studying: {self.start_date}\nAccount_id (public_key): {self.account_id}\n" \
               f"Private key: {self.__private_key}"
