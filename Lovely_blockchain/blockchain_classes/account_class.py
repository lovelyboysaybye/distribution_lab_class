from datetime import datetime
from typing import List
from blockchain_classes.key_pair_class import KeyPair
from blockchain_classes.signature_class import Signature
from blockchain_classes.operation_class import Operation
from blockchain_classes.transaction_class import Transaction


class Account:
    def __init__(self, student_id: int, name: str, surname: str, start_date: datetime, private_key: int = 0) -> None:
        """
        Initializes the account objectю
        :param student_id: id of student card
        :param name: name of student
        :param surname: surname of student
        :param start_date: date of starting studying
        :param private_key: private key if user want to generate it by himself.
        """
        # Next parameters required for verifying that each student has only one account for voting.
        # Only administration will have the dictionary of account_id bounded with the student_id for anonymous voting.
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.start_date = start_date
        self.__nonce = 0

        # 'account_id' field is a public key of student.
        self.account_id = 0
        self.__private_key = private_key

    def get_nonce(self) -> int:
        return self.__nonce

    def gen_account(self, hex_code: int) -> None:
        """
        Generates the account by creating KeyPair of private and public keys.
        :param hex_code: code, provided by administration for registration unique account.
        """
        if self.verify_ability_to_register(hex_code):
            self.account_id, self.__private_key = KeyPair(private_key=self.__private_key).get_keys()
        else:
            raise Exception("API return False. Please, contact with administration center for more information.")

    def verify_ability_to_register(self, hex_code: int) -> bool:
        """
        Verifies that user can register.
        :param hex_code: hex code for registration
        :return: True if user with specified fields not exists yet and the server provides access.
        """

        # TODO: create an administration server with next function/API`s:
        #   - generate the hex_code: students asks the administration center for registration.
        #       They check whether the students is not registered yet and provide the generated hex_code for him.
        #       Generated hex code can be used only for limited time (hours/days).
        #       Generated hex code should be added to the database.
        #       Two types of codes:
        #           - generate new user - accept the registration only if user like that not exists.
        #           - delete previous and generate new user - accept the registration of new user and remove old user
        #               from database.
        #   - verify the registration: API checks for two types of codes and do operation, described above.
        #       If all parameters verified than API return True else False.
        return True

    def create_vote_transaction(self, voting_address: int, vote_number: int) -> Transaction:
        """
        Creates the vote transaction.
        :param voting_address: account_id for sending the vote message.
        :param vote_number: fnumber of candidate
        :return: str of transaction
        """

        operation = Operation(self.account_id, voting_address, vote_number, self.__private_key)
        transaction = Transaction(operation, self.__nonce)
        self.__nonce += 1
        return transaction

    def get_votes(self) -> List:
        """
        Gets all votes from this account.
        :return: list of transactions
        """
        # TODO: find all transactions created by current account.
        return ["Transaction class not implemented yet."]

    def sign_data(self, message: str) -> int:
        """
        Generates the signature for message by specific private_key.
        :param private_key: int value of private key
        :param message: message for signing
        :return: r and s
        """
        return Signature.generate_signature(self.__private_key, message)

    def __str__(self) -> str:
        return f"Name: {self.name}\nSurname: {self.surname}\nStudent_id: {self.student_id}\n" \
               f"Start date of studying: {self.start_date}\nAccount_id (public_key): {self.account_id}\n" \
               f"Private key: {self.__private_key}"
