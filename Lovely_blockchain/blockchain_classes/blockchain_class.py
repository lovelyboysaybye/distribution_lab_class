from typing import Set, List
from blockchain_classes.sha1_class import SHA1
from blockchain_classes.block_class import Block
from blockchain_classes.transaction_class import Transaction
from blockchain_classes.operation_class import Operation


class Blockchain:
    """
    Blockchain class operates with the block history and transaction database.
    """
    def __init__(self, message="Voting process should be opened for public!!!") -> None:
        """
        Initializes the blockchain object. Create a genesis block
        :param message: message, that will be hashed for genesis block.
        """
        self.message = message
        genesis_block = Block(set(), SHA1().get_hash(self.message))
        self.__blockHistory = [genesis_block]
        self.txDatabase: Set[Transaction] = set()
        self.voting_tickets = []

    def print(self) -> None:
        """
        Prints validated blocks of blockchain.
        """
        for index, block in enumerate(self.get_blockHistory()):
            print(f"Block {index}:")
            print(str(block))

    def get_blockHistory(self) -> List[Block]:
        """
        Gets block history
        :return: list of blocks
        """
        return self.__blockHistory

    def __append_blockHistory(self, block: Block) -> None:
        """
        Appends new block to blockHistory
        :param block: block for appending
        """
        self.__blockHistory.append(block)

    def validate_block(self, block: Block) -> bool:
        """
        Validates proposed block and add it to the history, if it is correct.
        Also, update the txDatabase with new transactions and voting_tickets db.
        :param block: Block for adding
        """
        new_tx_list = list()
        tickets_copy = list(self.voting_tickets)

        # Verifies whether block non-empty on transactions
        if len(block.transaction_arr) == 0:
            raise Exception("Block does not have any transaction.")

        # Verifies, that proposed block point on the last block in history
        if block.previous_hash != self.get_blockHistory()[-1].block_id:
            raise Exception("Block does not point on the last block in history.")

        # Verifies, that all transaction from block have not been added to a txDatabase
        if not self.__validate_tx_list_unique(block.transaction_arr):
            raise Exception("Block contains transactions that was added in previous blocks.")

        # Verifies transactions by voting tickets rules
        for transaction in block.transaction_arr:
            # Verifies nonce value. Should not exist value bigger or equal than current value. Also should exist value -1
            txs_nonce_by_sender = [tx.nonce for tx in [*new_tx_list, *self.txDatabase] if tx.operation.sender_id == transaction.operation.sender_id]

            # Nonce verifications
            if transaction.nonce == 0 and transaction.nonce in txs_nonce_by_sender:
                raise Exception(f"Zero nonce transaction already exists by user.\n{transaction}")

            if transaction.nonce != 0:
                if transaction.nonce in txs_nonce_by_sender:
                    raise Exception(f"Transaction with that nonce value already exists.\n{transaction}")

                if transaction.nonce - 1 not in txs_nonce_by_sender:
                    raise Exception(f"Nonce - 1 not found. Please, create nonce - 1 transaction.\n{transaction}")

            # Transaction, that create voting tickets.
            if transaction.operation.voting_ticket == 0:
                # This rule help for preventing duplicates voting tickets. If voting_ticket number equals to 0 and
                #   vote number equal to zero, than it is possible to verifies duplicates only compare
                #   the hex of operations.
                # Without this rule of vote_number equal zero, the operation hex will be different
                #   for different vote_number.
                if transaction.operation.vote_number != 0:
                    raise Exception(f"Voting ticket transaction vote_number field should be equal to 0.\n{transaction}")

                if not Operation.verify_operation(transaction.operation, transaction.operation.sender_id):
                    raise Exception(f"Wrong singature.\n{transaction}")

                # Prevent duplicates voting tickets for students.
                if not self.__verify_voting_ticket_not_exist(transaction, tickets_copy, new_tx_list):
                    raise Exception(f"Duplicate transaction.\n{transaction}")

                tickets_copy.append(transaction.transaction_id)
            # Else transaction spent voting ticket
            else:
                # Verifies, that voting_ticket not spent already
                if transaction.operation.voting_ticket not in tickets_copy:
                    raise Exception(f"voting ticket already spent.\n{transaction}")

                # Verifies voting ticket spending
                vote_ticket = self.get_tx_by_id(transaction.operation.voting_ticket)
                if vote_ticket.operation.sender_id != transaction.operation.receiver_id:
                    raise Exception(f"Voting ticket is tried to be spent for another voting system.\n{transaction}")
                if vote_ticket.operation.receiver_id != transaction.operation.sender_id:
                    raise Exception(f"Voting ticket is tried to be spent by another user.\n{transaction}")

                if not Operation.verify_operation(transaction.operation, transaction.operation.sender_id):
                    raise Exception(f"Wrong signature.\n{transaction}")
                tickets_copy.remove(transaction.operation.voting_ticket)

            new_tx_list.append(transaction)

        self.txDatabase.update(new_tx_list)
        self.voting_tickets = tickets_copy
        self.__append_blockHistory(block)
        return True

    def __verify_voting_ticket_not_exist(self, voting_ticket_tx: Transaction, tickets_copy: List[int], new_tx_list: List[Transaction]) -> bool:
        """
        Verifies if voting ticket does not exists yet. Used for verifying duplicates of voting tickets for one user.
        :param voting_ticket_tx:
        :return: True if proposed ticket is new.
        """
        tx_ticket_not_exist = True
        for voting_ticket_id in tickets_copy:
            tmp_voting_ticket = self.get_tx_by_id(voting_ticket_id, new_tx_list)
            if tmp_voting_ticket.operation.operation_hex == voting_ticket_tx.operation.operation_hex:
                tx_ticket_not_exist = False
                break

        return tx_ticket_not_exist

    def get_tx_by_id(self, tx_id: int, new_tx_list: List[Transaction] = None) -> Transaction:
        """
        Gets the transaction from txDatabase by id.
        :param tx_id: id of transaction for finding
        :param new_tx_list: list of transaction
        :return: Found transaction else None
        """
        new_tx_list = new_tx_list if new_tx_list is not None else []

        found_tx = None
        for tx in [*self.txDatabase, *new_tx_list]:
            if tx.transaction_id == tx_id:
                found_tx = tx
                break
        return found_tx

    def __validate_tx_list_unique(self, transaction_arr: Set[Transaction]) -> bool:
        """
        Validates whether all transaction from block have not been added to a txDatabase
        :param transaction_arr: list of transaction
        :return: if all transaction does not exist in txDatabase yet return True, otherwise False.
        """
        return len(set(self.txDatabase) & set(transaction_arr)) == 0
