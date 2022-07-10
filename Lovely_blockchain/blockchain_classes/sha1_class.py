class SHA1:
    LENGTH_IN_BYTES = 20

    def __init__(self):
        self.h0 = 0x67452301
        self.h1 = 0xEFCDAB89
        self.h2 = 0x98BADCFE
        self.h3 = 0x10325476
        self.h4 = 0xC3D2E1F0

    def get_hash(self, message):
        if type(message) is str:
            message = message.encode('ascii')
        h0 = self.h0
        h1 = self.h1
        h2 = self.h2
        h3 = self.h3
        h4 = self.h4

        pbits = bits = ''.join(format(byte, '08b') for byte in message) + '1'
        pbits = pbits + "0" * (448 - len(pbits) % 512) + '{0:064b}'.format(len(bits) - 1)

        for c in SHA1.make_chunks(pbits, 512):
            words = SHA1.make_chunks(c, 32)
            w = [0] * 80
            for n in range(0, 16):
                w[n] = int(words[n], 2)
            for i in range(16, 80):
                w[i] = SHA1.rol((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)

            a = h0
            b = h1
            c = h2
            d = h3
            e = h4

            # Main loop
            for i in range(0, 80):
                if 0 <= i <= 19:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= i <= 39:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= i <= 59:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                else:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6

                temp = SHA1.rol(a, 5) + f + e + k + w[i] & 0xffffffff
                e = d
                d = c
                c = SHA1.rol(b, 30)
                b = a
                a = temp

            h0 = h0 + a & 0xffffffff
            h1 = h1 + b & 0xffffffff
            h2 = h2 + c & 0xffffffff
            h3 = h3 + d & 0xffffffff
            h4 = h4 + e & 0xffffffff

        return int('%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4), base=16)

    @staticmethod
    def make_chunks(l, n):
        return [l[i:i + n] for i in range(0, len(l), n)]

    @staticmethod
    def rol(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff
