class Cipher:
    '''
    A cipher object is a shift / caeser cipher encryption and decryption
    object. It contains two methods, encode and decode. They take a plaintext
    string as a mandatory input, and shift_distance as an optional input. If
    shift_distance is not provided, it will default to 1.
    '''

    def encode(self, plaintext="", shift_distance=None):
        '''
        encode loops through the characters of plaintext. If plaintext is empty 
        or any characters are not letters, it raises an exception. Each letter 
        is converted to unicode, and the shift_distance is added to this value
        (default 1). It is normalized such that A or a is 0 (-97 and -65 
        respectively). This value modulo 26 added to 97 (lowercase a) results 
        in the shifted character. The shifted characters are added to a list, 
        and the join of the list is returned.
        '''
        if not plaintext:
            raise Exception('Cipher.encode() requires a non-empty string as input')
        ciphertext = []
        if shift_distance is None:
            shift_distance = 1 # Default
        for char in plaintext:
            if ord(char) >= 97 and ord(char) <= 122: # Lowercase
                ciphertext.append(chr((ord(char) + shift_distance - 97)
                                      % 26 + 97))
            elif ord(char) >= 65 and ord(char) <= 90: # Uppercase
                ciphertext.append(chr((ord(char) + shift_distance - 65)
                                      % 26 + 97))
            else:
                raise Exception('plaintext should include only lowercase or uppercase letters')
        return ''.join(ciphertext)

    def decode(self, plaintext="", shift_distance=None):
        '''
        decode loops through the characters of plaintext. If plaintext is empty 
        or any characters are not letters, it raises an exception. Each letter 
        is converted to unicode, and the shift_distance is subtracted from this 
        value (default 1). It is normalized such that A or a is 0 (-97 and -65 
        respectively). This value modulo 26 added to 97 (lowercase a) results 
        in the shifted character. The shifted characters are added to a list, 
        and the join of the list is returned.
        '''
        if not plaintext:
            raise Exception('Cipher.decode() requires a non-empty string as input')
        ciphertext = []
        if shift_distance is None:
            shift_distance = 1 # Default
        for char in plaintext:
            if ord(char) >= 97 and ord(char) <= 122: # Lowercase
                ciphertext.append(chr((ord(char) - shift_distance - 97)
                                      % 26 + 97))
            elif ord(char) >= 65 and ord(char) <= 90: # Uppercase
                ciphertext.append(chr((ord(char) - shift_distance - 65)
                                      % 26 + 97))
            else:
                raise Exception('plaintext should include only lowercase or uppercase letters')
        return ''.join(ciphertext)
