class Cipher:
    '''
    A cipher object is a shift / caeser cipher encryption and decryption
    object. It contains two methods, encode and decode. They take a plaintext
    string as a mandatory input, and shift_distance as an optional input. If
    shift_distance is not provided, it will default to 1.
    '''

    def encode(self, plaintext, shift_distance=None):
        ciphertext = []
        if shift_distance is None:
            shift_distance = 1
        for char in plaintext:
            if ord(char) >= 97 and ord(char) <= 122:
                ciphertext.append(chr((ord(char) + shift_distance - 97)
                                      % 26 + 97))
            elif ord(char) >= 65 and ord(char) <= 90:
                ciphertext.append(chr((ord(char) + shift_distance - 65)
                                      % 26 + 97))
            else:
                raise Exception('plaintext should include only lowercase or uppercase letters')
        return ''.join(ciphertext)

    def decode(self, plaintext, shift_distance=None):
        ciphertext = []
        if shift_distance is None:
            shift_distance = 1
        for char in plaintext:
            if ord(char) >= 97 and ord(char) <= 122:
                ciphertext.append(chr((ord(char) - shift_distance - 97)
                                      % 26 + 97))
            elif ord(char) >= 65 and ord(char) <= 90:
                ciphertext.append(chr((ord(char) - shift_distance + 65)
                                      % 26 + 97))
            else:
                raise Exception('plaintext should include only lowercase or uppercase letters')
        return ''.join(ciphertext)
