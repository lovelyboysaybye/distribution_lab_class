Classes of Lovely blockchain placed in 'blockchain_classes' directory. The structure is:
    
    - key_pair_class.py contains KeyPair class for generating private and public keys.
        Private key can passed as the keyword argument (used for testing here, but can be used for generating by the
        user pseudo-random generator).
    - signature_class.py contains Signature class for generatinh signature of message by private key and verify existing
        signed message by the public key.
    - sha1_class.py contains SHA1 class for generating hash of message in Signature class.
    - ecc_class.py contains ECC class for calculating the public key of private key by the Elliptic Curve Cryptography.
        Used in Signature and KeyPair classes.
    - account_class.py contains Account class for creating account, sending voting transactions and finding
        all previous votes.

Tests:

    - *_test_key_pair.py* verifies the KeyPair class.
    - *_test_signature.py* verifies the Signature class.
    - *_test_account.py* verifies the Account class.