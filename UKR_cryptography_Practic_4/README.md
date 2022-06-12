1. Was implemented the AES library for 10 rounds for 128 bits key. The library in AES.py file.
2. Implemented AES library can encrypt and decrypt the messages of different length. If length not aligned to 16 bytes,
it will be padded with bytes of length of padding. Also, the padded message will be unpadded after decryption.
3. main.py run several test cases for encrypting text of bytes and decrypt them.

Example of output of code:

	Key: b'\xfd?\xeb<\x92P\xb7\x97J\x9bR\x8bicc!'
	b'Small text'

	Key: b'\xa4a\xb5^\xf5[{\xea\xfd\x80\x9a\x9a\x9e\x92[y'
	b'abcdabcdabcdabcd'

	Key: b'\xa64/\xa0\xfd\xb8\xb2\x94\xd9\x7f\xc6\x10=\x92\x08\x9b'
	b'My big text for more than 16 bytes.'