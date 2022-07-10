from blockchain_classes.sha1_class import SHA1
from blockchain_classes.transaction_class import Transaction
from typing import Set


class Block:
    """
    Class that represents the block of transactions.
    """
    def __init__(self, transaction_arr: Set[Transaction], previous_hash: int) -> None:
        """
        Initializes the Block object
        :param transaction_arr: set of transaction, that should be used in block
        :param previous_hash: hash value of previous block
        """
        self.transaction_arr = transaction_arr
        self.previous_hash = previous_hash
        self.block_id = self.hash_of_block()

    def hash_of_block(self) -> int:
        """
        Calculates the hash of current block
        :return: return hash value of block
        """
        tmp_hash_value = SHA1().get_hash(self.previous_hash.to_bytes(SHA1.LENGTH_IN_BYTES, 'big'))
        for transaction in self.transaction_arr:
            tmp_hash_value = SHA1().get_hash([*tmp_hash_value.to_bytes(SHA1.LENGTH_IN_BYTES, 'big'), *transaction.transaction_id.to_bytes(SHA1.LENGTH_IN_BYTES, 'big')])

        return tmp_hash_value

    def __str__(self) -> str:
        """
        :return: string representation of object.
        """
        return "Block_id: {0}\nTransactions:{1}\nPrevious_hash: {2}"\
            .format(self.block_id,
                    ', '.join([str(tran.transaction_id) for tran in self.transaction_arr]),
                    self.previous_hash)
