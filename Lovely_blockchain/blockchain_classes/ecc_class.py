from blockchain_classes.constants import PRIVATE_KEY_LEN


class ECC:
    """
    Elliptic Curve Cryptography based on the secp256k1.
        Link: https://www.secg.org/SEC2-Ver-1.0.pdf (Page 15)
    """
    P_VAL = 2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1  # From the secp256k1 recommendation.
    N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141  # Number of points in the field
    A_VAL = 0   # For: y^2 = x^3 + A_VAL * x + B_VAL - A_VAL only used in current implementation.
                # Due to the addition operation in ECdouble func not affect the code.
    Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
    Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
    G_POINT = (Gx, Gy)  # Generator point for ECC multiplication

    @staticmethod
    def modinv(a: int, n=P_VAL) -> int:
        """
        Calculates inverse division for EEC with P_VAL
        :param a: value for operation
        :return: calculated value
        """
        lm, hm = 1, 0
        low, high = a % n, n
        while low > 1:
            ratio = high // low
            nm, new = hm - lm * ratio, high - low * ratio
            lm, low, hm, high = nm, new, lm, low

        return lm % n

    @staticmethod
    def ECadd(a: (int, int), b: (int, int)) -> (int, int):
        """
        Calculates the ECC addition of points.
        :param a: first point for operation
        :param b: second point for operation
        :return: calculated point
        """
        lam_add = ((b[1] - a[1]) * ECC.modinv(b[0] - a[0])) % ECC.P_VAL
        x = (lam_add ** 2 - a[0] - b[0]) % ECC.P_VAL
        y = (lam_add * (a[0] - x) - a[1]) % ECC.P_VAL
        return x, y

    @staticmethod
    def ECdouble(a: (int, int)) -> (int, int):
        """
        Calculates the ECC multiplication of operated point and P_VAL.
        :param a: point for operation
        :return: calculated point
        """
        lam = ((3 * a[0] ** 2 + ECC.A_VAL) * ECC.modinv(2 * a[1])) % ECC.P_VAL
        x = (lam ** 2 - 2 * a[0]) % ECC.P_VAL
        y = (lam * (a[0] - x) - a[1]) % ECC.P_VAL
        return x, y

    @staticmethod
    def get_public_key(point, value) -> (int, int):
        """
        Calculates the public key value from the private key on elliptic curve based on the ECC multiplication.
        :raise: Exception for any values of private key that not in range(0; ECC.N)
        :return: X and Y of public key.
        """
        if value == 0 or value >= ECC.N:
            raise Exception("Invalid Scalar/Private Key")

        scalar_bin = bin(value)[2:]

        q_point = point
        for i in range(1, len(scalar_bin)):
            q_point = ECC.ECdouble(q_point)
            if scalar_bin[i] == "1":
                q_point = ECC.ECadd(q_point, point)

        return q_point
