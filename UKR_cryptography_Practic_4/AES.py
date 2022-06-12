from typing import List


class AES:
    """
    AES class for encrypting and decrypting messages.
    """
    s_box = (
        0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
        0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
        0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
        0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
        0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
        0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
        0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
        0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
        0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
        0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
        0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
        0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
        0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
    )

    inv_s_box = (
        0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
        0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
        0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
        0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
        0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
        0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
        0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
        0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
        0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
        0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
        0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
        0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
        0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
        0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
        0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
    )

    r_con = (
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
    )

    def __init__(self, master_key: bytes) -> None:
        """
        Initializes the AES class object.
        :param master_key: key for encrypting and decrypting.
        """
        self.n_rounds = 10
        self._key_matrices = self._expand_key(master_key)

    def _expand_key(self, master_key: bytes) -> List[List]:
        """
        Expands and returns a list of key matrices for the given master_key.
        :param master_key: bytes of key
        :return: List of keys for encrypting blocks.
        """
        # Initialize round keys with raw key material.
        key_columns = AES.bytes2matrix(master_key)
        iteration_size = len(master_key) // 4

        i = 1
        while len(key_columns) < (self.n_rounds + 1) * 4:
            word = list(key_columns[-1])

            if len(key_columns) % iteration_size == 0:
                word.append(word.pop(0))
                word = [AES.s_box[b] for b in word]
                word[0] ^= AES.r_con[i]
                i += 1
            elif len(master_key) == 32 and len(key_columns) % iteration_size == 4:
                word = [AES.s_box[b] for b in word]

            word = AES.xor_bytes(word, key_columns[-iteration_size])
            key_columns.append(word)

        return [key_columns[4 * i: 4 * (i+1)] for i in range(len(key_columns) // 4)]

    @staticmethod
    def xor_bytes(a: List, b: List) -> bytes:
        """
        XORs a and b lists.
        :param a: list
        :param b: list
        :return: xored bytes.
        """
        return bytes(i ^ j for i, j in zip(a, b))

    @staticmethod
    def bytes2matrix(text: bytes) -> List[List]:
        """
        Converts a 16-byte array into a state matrix.
        :param text: bytes array
        :return state matrix
        """
        return [list(text[i:i + 4]) for i in range(0, len(text), 4)]

    @staticmethod
    def matrix2bytes(matrix: List[List]) -> bytes:
        """
        Converts a state matrix into a 16-byte array.
        :param matrix: state matrix
        :return bytes array.
        """
        return bytes(sum(matrix, []))

    @staticmethod
    def pad(text: bytes) -> bytes:
        """
        Pads the padded bytes. Padded bytes contain repeated value of size of padding elements.
        If text aligned to 16 bytes, padding will add the new 16 bytes block.
        :param text: text for padding.
        :return: bytes of padded text.
        """
        padding_len = 16 - (len(text) % 16)
        padding = bytes([padding_len] * padding_len)
        return text + padding

    @staticmethod
    def unpad(text: bytes) -> bytes:
        """
        Unpads the padded bytes. Padded bytes contain repeated value of size of padding elements.
        :param text: text for unpadding.
        :return: bytes of unpadded text.
        """
        padding_len = text[-1]
        message, padding = text[:-padding_len], text[-padding_len:]
        return message

    @staticmethod
    def _split_blocks(message: bytes, block_size: int = 16) -> List[bytes]:
        """
        Splits message on blocks.
        :param message: byte vector for splitting on block_size
        :param block_size: size of block for splitting
        :return: List of bytes of blocks.
        """
        return [message[i:i + block_size] for i in range(0, len(message), block_size)]

    @staticmethod
    def _sub_bytes(state: List[List]) -> None:
        """
        Changes bytes by another values from table.
        :param state: state bytes for operation.
        """
        for i in range(4):
            for j in range(4):
                state[i][j] = AES.s_box[state[i][j]]

    @staticmethod
    def _inv_sub_bytes(state: List[List]) -> None:
        """
        Changes bytes by another values from table for inverse syb bytes.
        :param state: state bytes for operation.
        """
        for i in range(4):
            for j in range(4):
                state[i][j] = AES.inv_s_box[state[i][j]]

    @staticmethod
    def _shift_rows(state: List[List]) -> None:
        """
        Shifts rows of state.
        :param state: state bytes for operation.
        """
        state[0][1], state[1][1], state[2][1], state[3][1] = state[1][1], state[2][1], state[3][1], state[0][1]
        state[0][2], state[1][2], state[2][2], state[3][2] = state[2][2], state[3][2], state[0][2], state[1][2]
        state[0][3], state[1][3], state[2][3], state[3][3] = state[3][3], state[0][3], state[1][3], state[2][3]

    @staticmethod
    def _inv_shift_rows(state: List[List]) -> None:
        """
        Inverses shift rows of state.
        :param state: state bytes for operation.
        """
        state[0][1], state[1][1], state[2][1], state[3][1] = state[3][1], state[0][1], state[1][1], state[2][1]
        state[0][2], state[1][2], state[2][2], state[3][2] = state[2][2], state[3][2], state[0][2], state[1][2]
        state[0][3], state[1][3], state[2][3], state[3][3] = state[1][3], state[2][3], state[3][3], state[0][3]

    @staticmethod
    def _add_round_key(state: List[List], round_key: List[List]) -> None:
        """
        Adds by xor operation round key.
        :param  state: state block for operation.
        :param round_key: round key matrix for XOR.
        """
        for i in range(4):
            for j in range(4):
                state[i][j] ^= round_key[i][j]

    @staticmethod
    def _xtime(a):
        return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

    @staticmethod
    def _mix_single_column(column: List) -> None:
        """
        Mixes only one column.
        :param column: column of bytes/
        """
        t = column[0] ^ column[1] ^ column[2] ^ column[3]
        u = column[0]
        column[0] ^= t ^ AES._xtime(column[0] ^ column[1])
        column[1] ^= t ^ AES._xtime(column[1] ^ column[2])
        column[2] ^= t ^ AES._xtime(column[2] ^ column[3])
        column[3] ^= t ^ AES._xtime(column[3] ^ u)

    @staticmethod
    def _mix_columns(state: List[List]) -> None:
        """
        Mixes columns operation.
        :param state: bytes state for operation.
        """
        for i in range(4):
            AES._mix_single_column(state[i])

    @staticmethod
    def _inv_mix_columns(state: List[List]) -> None:
        """
        Inverses the mixing columns operation.
        :param state: bytes state for operation.
        """
        for i in range(4):
            u = AES._xtime(AES._xtime(state[i][0] ^ state[i][2]))
            v = AES._xtime(AES._xtime(state[i][1] ^ state[i][3]))
            state[i][0] ^= u
            state[i][1] ^= v
            state[i][2] ^= u
            state[i][3] ^= v

        AES._mix_columns(state)

    def __encrypt_block(self, text: bytes) -> bytes:
        """
        Encrypt 16 bytes single block of text.
        :param text: 16 bytes of data to encryption.
        :return: bytes of encrypted block
        """
        plain_state = AES.bytes2matrix(text)

        AES._add_round_key(plain_state, self._key_matrices[0])

        for i in range(1, self.n_rounds):
            AES._sub_bytes(plain_state)
            AES._shift_rows(plain_state)
            AES._mix_columns(plain_state)
            AES._add_round_key(plain_state, self._key_matrices[i])

        AES._sub_bytes(plain_state)
        AES._shift_rows(plain_state)
        AES._add_round_key(plain_state, self._key_matrices[-1])

        return AES.matrix2bytes(plain_state)

    def __decrypt_block(self, ciphertext: bytes) -> bytes:
        """
        Decrypts 16 bytes single block of ciphertext.
        :param ciphertext: 16 bytes of encrypted data.
        :return: bytes of decrypted block
        """
        cipher_state = AES.bytes2matrix(ciphertext)

        AES._add_round_key(cipher_state, self._key_matrices[-1])
        AES._inv_shift_rows(cipher_state)
        AES._inv_sub_bytes(cipher_state)

        for i in range(self.n_rounds - 1, 0, -1):
            AES._add_round_key(cipher_state, self._key_matrices[i])
            AES._inv_mix_columns(cipher_state)
            AES._inv_shift_rows(cipher_state)
            AES._inv_sub_bytes(cipher_state)

        AES._add_round_key(cipher_state, self._key_matrices[0])

        return AES.matrix2bytes(cipher_state)

    def encrypt(self, text: bytes) -> bytes:
        """
        Encrypts bytes of text. The encryption text padded for aligning 16 bytes length and splitted on state blocks.
        :param text: text bytes for encryption.
        :return: bytes of encrypted text
        """
        padded_text = AES.pad(text)
        text_matrix = AES._split_blocks(padded_text)
        return b''.join([self.__encrypt_block(block) for block in text_matrix])

    def decrypt(self, ciphertext: bytes) -> bytes:
        """
        Decrypts bytes of encrypted text. The decrypted text unpadded.
        :param ciphertext: text bytes for decryption.
        :return: bytes of decrypted text
        """
        text_matrix = AES._split_blocks(ciphertext)
        return AES.unpad(b''.join([self.__decrypt_block(block) for block in text_matrix]))
