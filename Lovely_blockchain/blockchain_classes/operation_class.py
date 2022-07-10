from __future__ import annotations
from blockchain_classes.signature_class import Signature
from blockchain_classes.constants import PUBLIC_KEY_BYTES


class Operation:
    """
    Operation class for creating data for future transaction.
    """
    def __init__(self, sender_id: int, voting_ticket: int, receiver_id: int, vote_number: int, private_key) -> None:
        """
        Initializes Operation object.
        :param sender_id: id of account who send vote.
        :param voting_ticket: the hash of transaction, that provide ability for account for voting.
            Rule: voting ticket transaction should point on the transaction, that sent by the voting address account.
                  That rule used for participating in parallel votes.
            Note: voting_ticket == 0 can be used by vote system account only.
        :param receiver_id: id of account who collect votes.
        :param vote_number: number of candidate, for whom user voted.
        :param private_key: private key for signed data of vote.
        """
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.voting_ticket = voting_ticket
        self.vote_number = vote_number
        self.operation_bytes_list = self.generate_bytes_of_operation()
        self.operation_hex = hex(int.from_bytes(self.operation_bytes_list, byteorder='big'))[2:]
        self.signature = Signature.generate_signature(private_key, self.operation_hex)

    def generate_bytes_of_operation(self):
        """
        Generates the bytes of operation.
        :return:  array of bytes of operation
        """
        return [*self.voting_ticket.to_bytes(PUBLIC_KEY_BYTES, byteorder='big'),
                *self.sender_id.to_bytes(PUBLIC_KEY_BYTES, byteorder='big'),
                *self.receiver_id.to_bytes(PUBLIC_KEY_BYTES, byteorder='big'),
                *self.vote_number.to_bytes(1, byteorder='big')]

    @staticmethod
    def verify_operation(operation: 'Operation', public_key) -> bool:
        """
        Verifies signature of operation by public key.
        :param operation: signed operation
        :param public_key: public key of signature
        :return: True if verified successfully.
        """
        return Signature.verify_signature(operation.signature, public_key, operation.operation_hex)

    def __call__(self):
        return self.operation_bytes_list

    def __str__(self) -> str:
        return f"Sender id: {self.sender_id}\nReceiver id: {self.receiver_id}\n" \
               f"Vote number: {self.vote_number}\nSignature: {self.signature}\n" \
               f"Voting ticket: {self.voting_ticket}\n"
