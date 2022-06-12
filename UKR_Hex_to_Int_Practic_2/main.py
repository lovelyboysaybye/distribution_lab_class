from enum import Enum


class EndianType(Enum):
    """
    Static class with types of endians.
    """
    LITTLE_ENDIAN_TYPE = 1
    BIG_ENDIAN_TYPE = 2


class HEXConverter:
    """
    Class of HEX converter.
    Works with Little endian and Big endian for converting string HEX value to actual value
    (due to specified endian) and vice verse.
    """
    @staticmethod
    def convert_hex_to_value(hex_repr: str, endian_type: EndianType = None) -> [int, int]:
        """
        Converts string hex representation to actual int value based on specified endian type.
        :param hex_repr: string hex representation.
        :param endian_type: EndianType value for specified type of endian.
        :return: int value of hex, number of bytes
        """
        # Get correct hex representation for specifeid endiant type
        if endian_type == EndianType.LITTLE_ENDIAN_TYPE:
            hex_repr = HEXConverter.hex_to_little_endian(hex_repr)

        return int(hex_repr, base=16), len(hex_repr) // 2

    @staticmethod
    def convert_value_to_hex(value: int, number_of_bytes: int, endian_type: EndianType = None) -> str:
        """
        Converts int value to its hex representation based on specified endian type.
        :param value: int value for conversion.
        :param number_of_bytes: int number of bytes
        :param endian_type: EndianType value for specified type of endian.
        :return: hex value
        """
        # Get hex representation without '0x'
        hex_repr = hex(value)[2:]
        hex_repr += "00" * (number_of_bytes - len(hex_repr) // 2)
        if endian_type == EndianType.LITTLE_ENDIAN_TYPE:
            hex_repr = HEXConverter.hex_to_little_endian(hex_repr)
        return hex_repr

    @staticmethod
    def hex_to_little_endian(hex_repr: str) -> str:
        """
        Converts hex_representation from BIG ENDIAN to LITTLE ENDIAN.
        :param hex_repr: str hex representation
        :return: little endian hex representation
        """
        return "".join([hex_repr[x:x+2] for x in range(0,len(hex_repr),2)][::-1])


def test_func(test_index: int, hex_value: str) -> None:
    """
    Test function, that print conversion result of input hex str representation to int value in both endians.
    Also, compares the hex values of already converted values with input hex str representation.
    :param test_index: index of test for printing
    :param hex_value: str hex value representation
    """
    # Calculate Big and Little endian int values for specified hex
    big_endian_val, number_of_bytes = HEXConverter.convert_hex_to_value(hex_value, EndianType.BIG_ENDIAN_TYPE)
    little_endian_val, number_of_bytes = HEXConverter.convert_hex_to_value(hex_value, EndianType.LITTLE_ENDIAN_TYPE)

    print(f"\nVector {test_index}:\n\tValue: {hex_value}\n\tNumber of bytes: {number_of_bytes}\n\t"
          f"Little-endian: {little_endian_val}\n\tBig-endian: {big_endian_val}")

    # Get HEX representation for big and little endians and compare with input string
    big_endian_hex = HEXConverter.convert_value_to_hex(big_endian_val, number_of_bytes, EndianType.BIG_ENDIAN_TYPE)
    if big_endian_hex == hex_value.lower():
        print("Input HEX and converted hex value from convertor equals for BIG ENDIAN.")
    else:
        print("Input HEX and converted hex value from convertor ARE NOT equal for BIG ENDIAN.")

    little_endian_val_endian_hex = HEXConverter.convert_value_to_hex(little_endian_val,
                                                                     number_of_bytes,
                                                                     EndianType.LITTLE_ENDIAN_TYPE)
    if HEXConverter.hex_to_little_endian(little_endian_val_endian_hex) == hex_value.lower():
        print("Input HEX and converted hex value from convertor equals for LITTLE ENDIAN.")
    else:
        print("Input HEX and converted hex value from convertor ARE NOT equal for LITTLE ENDIAN.")


if __name__ == "__main__":
    test_index = 1

    hex_val1 = "ff00000000000000000000000000000000000000000000000000000000000000"
    test_func(test_index, hex_val1)
    test_index += 1

    hex_val2 = "aaaa000000000000000000000000000000000000000000000000000000000000"
    test_func(test_index, hex_val2)
    test_index += 1

    hex_val3 = "FFFFFFFF"
    test_func(test_index, hex_val3)
    test_index += 1

    hex_val4 = "F000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    test_func(test_index, hex_val4)
    test_index += 1
