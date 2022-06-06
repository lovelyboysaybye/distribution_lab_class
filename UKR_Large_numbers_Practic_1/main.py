import time
import random

BITS_LENGTH_ARRAY = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]


def brute_force_timers(bits_length: int, find_key: int) -> int:
    """
    Runs Brute-force attack for finding specified key from all possible combinations of keyspace of specified bit length
    :param bits_length: Length of bits
    :param find_key: random generated value of bits_length, that should be found
    :return: Time in milliseconds for key search
    """
    start_time_milliseconds = int(round(time.time() * 1000))
    found_key = brute_force(bits_length, find_key)
    end_time_milliseconds = int(round(time.time() * 1000))

    return end_time_milliseconds - start_time_milliseconds


def brute_force(bits_length: int, find_key: int) -> int:
    """
    Finds searched key by Brute-force method.
    :param bits_length: Length of bits
    :param find_key: random generated value of bits_length, that should be found
    :return: return found key
    """
    tmp_key = 0
    while tmp_key != find_key:
        tmp_key += 1
    return tmp_key


if __name__ == "__main__":
    # Specified random seed for the same results for each run of code
    random.seed(3)

    # Prints number of possible combinations for specified number of bits
    print("Number of possible options for specified number of bits:")
    for bit_length in BITS_LENGTH_ARRAY:
        print(f"\tFor {bit_length} key length exists keyspace of elements: {2**bit_length}")

    # Generates random keys of specified bits length
    print("\nGenerated random keys of specified bits length:")
    random_keys_array = {bit_length: random.getrandbits(bit_length) for bit_length in BITS_LENGTH_ARRAY}
    for bit_length, random_key in random_keys_array.items():
        print(f"{bit_length}-bits random key: {hex(random_key)}")

    # How much time for Brute-force attack required
    print("\nHow much time for Brute-force attack required for generated random value:")
    for bit_length, random_key in random_keys_array.items():
        print(f"{bit_length}-bits random key found by Brute-force attack "
              f"for {brute_force_timers(bit_length, random_key)} milliseconds.")
