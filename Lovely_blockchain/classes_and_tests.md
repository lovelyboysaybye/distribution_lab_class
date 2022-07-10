Classes of Lovely blockchain placed in 'blockchain_classes' directory. The structure is:
    
    - key_pair_class.py contains KeyPair class for generating private and public keys.
        Private key can passed as the keyword argument (used for testing here, but can be used for generating by the
        user pseudo-random generator).
    - signature_class.py contains Signature class for generatinh signature of message by private key and verify existing
        signed message by the public key.
    - sha1_class.py contains SHA1 class for generating hash of message in Signature class.
    - ecc_class.py contains ECC class for calculating the public key of private key by the Elliptic Curve Cryptography.
        Used in Signature and KeyPair classes.
    - account_class.py contains Account class for creating student account, sending voting transactions and finding
        all voting tickets.
    - vote_system_account.py contains VotingSystemAccount for creating Vote System account, sending voting tickets for
        list of specified students and get results of votes from blockchain txDatabase.
    - operation_class.py contains Operation class for creating and verifiyng operation by signature.
    - transaction_class.py contains Transaction class for creating transaction.
    - block_class.py contains Block class that keeps transaction lists, point on previous block and calculates
        current block id.
    - blockchain_class.py contains Blockchain class that create chain of block by creating genesis block, add new blocks,
        that were validated by list of rules. Contains txDatabase for all transactions. Contains voting_tickets db of
        voting tickets, that not used yet.

Tests:

    - *_test_key_pair.py* verifies the KeyPair class.
    - *_test_signature.py* verifies the Signature class.
    - *_test_account.py* verifies the student Account class.
    - *_main.py* verifies the all blockchain system with spending of voting tickets tests, creating and validate blocks
        and verifying results of votes.
