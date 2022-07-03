from blockchain_classes.sha1_class import SHA1
from blockchain_classes.operation_class import Operation


class Transaction:
    """
    Transaction class that create transaction object with operations and nonce value.
    """
    def __init__(self, operation: Operation, nonce: int) -> None:
        """
        Initializes the Transaction object
        :param operation: operation used in transaction.
                          Due to the using only for voting process, decided to have only one operation.
        :param nonce: unique number for avoiding double voting.
        """
        self.operation = operation
        self.nonce = nonce
        self.transaction_id = SHA1().get_hash([*self.operation(), *self.nonce.to_bytes(1, byteorder='big')])

    def __str__(self) -> str:
        """
        :return: string representation of object.
        """
        return f"Transaction id: {self.transaction_id}\nNonce: {self.nonce}\nOperation: {self.operation}"
