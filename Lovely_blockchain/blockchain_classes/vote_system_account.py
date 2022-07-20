from typing import List, Set
from blockchain_classes.key_pair_class import KeyPair
from blockchain_classes.signature_class import Signature
from blockchain_classes.operation_class import Operation
from blockchain_classes.transaction_class import Transaction
from blockchain_classes.blockchain_class import Blockchain


class VotingSystemAccount:
    """
    Account of voting system. This type of account can create voting tickets for votes.
    """
    def __init__(self, vote_id: int, name_of_vote: str, private_key: int = 0) -> None:
        """
        Initializes the voting system account object.
        :param vote_id: id of voting process system
        :param name_of_vote: name of voting process
        :param private_key: private key if user want to generate it by himself.
        """
        self.vote_id = vote_id
        self.name_of_vote = name_of_vote

        # 'account_id' field is a public key of votingSystemAccount
        self.account_id = 0
        self.__private_key = private_key
        self.gen_account()

    def gen_account(self) -> None:
        """
        Generates the account by creating KeyPair of private and public keys.
        """
        self.account_id, self.__private_key = KeyPair(private_key=self.__private_key).get_keys()

    def create_transaction_for_voting(self, students_voting_addresses: List[int], blockchain: Blockchain) -> Set[Transaction]:
        """
        Creates the voting tickets for voting.
        :param students_voting_addresses: List of students that will take a part in voting process of current vote.
        :param blockchain: blockchain object required for calculation nonce value from txDatabase
        :return: List of transaction
        """
        list_of_transactions = []
        nonce_list = [tx.nonce for tx in blockchain.txDatabase if tx.operation.sender_id == self.account_id]
        if len(nonce_list):
            nonce = max(nonce_list) + 1
        else:
            nonce = 0

        for student_id in students_voting_addresses:
            operation = Operation(self.account_id, 0, student_id, 0, self.__private_key)
            transaction = Transaction(operation, nonce)
            nonce += 1
            list_of_transactions.append(transaction)
        return set(list_of_transactions)

    def get_results_of_voting(self, blockchain: Blockchain) -> List[Transaction]:
        """
        Gets the list of spent voting tickets.
        :param blockchain: blockchain of tx blocks.
        :return: List of transactions, that spent their voting tickets.
        """
        results_of_votes = []
        for tx in blockchain.txDatabase:
            if tx.operation.receiver_id == self.account_id and tx.transaction_id not in blockchain.voting_tickets:
                results_of_votes.append(tx)
        return results_of_votes

    def sign_data(self, message: str) -> int:
        """
        Generates the signature for message by specific private_key.
        :param private_key: int value of private key
        :param message: message for signing
        :return: r and s
        """
        return Signature.generate_signature(self.__private_key, message)

    def __str__(self) -> str:
        return f"Name of voting system: {self.name_of_vote}\nVote id: {self.vote_id}\n" \
               f"Private key: {self.__private_key}"
