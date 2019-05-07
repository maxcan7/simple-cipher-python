Shift Cipher Challenge
======================

## Goal

My challenge was to complete a shift cipher challenge that can encode and
decode simple phrases. My code passes their test script, as well as some other
important cases not included in their test script.

## What is a shift cipher?
# (This is from the challenge README)

Shift ciphers are also called Caesar ciphers as they were used by Julius Caesar
to scramble his messages to military personnel, so that they were purposefully
unintelligible to any unintended reader.

Using a shift cipher is a simple and well-known (albeit usually insecure!)
encryption technique, and a suitable topic for the focus of our challenge. In a
simple shift cipher, a given input phrase is shifted by a certain number of
characters so that it is no longer legible.

For example, when using a shift of 1, the letter _a_ would be shifted to _b_.

### Examples
# (This is from the challenge README)

When using a shift of _1_ (default):

```python
cipher = Cipher()

# Encode:
cipher.encode('foobar') # ---> 'gppcbs'

# Decode:
# We can simply reverse the shift
cipher.decode('gppcbs') # ---> 'foobar'
```

When using a shift of _10_:

```python
cipher = Cipher()

# Encode:
cipher.encode('foobar', 10) # ---> 'pyylkb'

# Decode:
cipher.decode('pyylkb', 10) # ---> 'foobar'
```

Our implementation of the shift cipher is a simple one:

- For encoding, the input text should be shifted by _n_ characters, with a
  default shift of 1
- For decoding, encoded text should be shifted back and return the original
  input text.
- When a shift causes a letter to pass the end of the alphabet, it should wrap
  to the beginning.

Example: _z_ shifted by 1 should become _a_.

## Explanation of my code

The `simple_cipher.py` script is what calculates the shift cipher.

At a high level, the script loops through the `plaintext`, and based on the 
character `char` on that iteration, whether it is `encoding` or `decoding`, and 
the `shift_distance`, performs a calculation to do the shift, and then appends 
the shifted character to a list. At the end of the loop, the join of the list 
is returned.

- Because it stores the characters in a list before returning the join, the 
  space complexity of the algorithm is O(N)

- Because it loops through each `char`  in `plaintext`, the time complexity
  of the algorithm is also O(N). The join() operation is also O(N), but since
  it is outside the loop, this makes the pipeline effectively still O(N).
  
The algorithm leverages the relationship between letter characters in unicode, 
and the circulatory of the shift rule through the use of modulo.

- Lowercase letters (`a` through `z`) convert to 97 through 122 in unicode. For
  encoding, the algorithm `chr((ord(char) + shift_distance - 97) % 26 + 97)` 
  takes the unicode value `ord()` of a given lowercase letter character `char`, 
  adds the `shift_distance`, and subtracts 97, such that with a 
  `shift_distance` of 0, the minimum value of lowercase letters would be 0, 
  corresponding to `a`. The modulo 26 `%` gives us the division remainder, such 
  that for `char = a` and `shift_distance = 1`, we would have: 
    - `97 + 1 - 97 = 1` 
    - `1 % 26 = 1`
    - `1 + 97 = 98`
  Which is then converted back to character `chr()` as `chr(98) = b`.

- With a `shift_distance` of 0, this calculation is still performed, but this
  will only return the original character.

- Because of this use of modulo, if the `shift_distance` would exceed the 
  alphabet (e.g. `z` with `shift_distance = 1`), it will instead give us a 
  remainder value less than or equal to 26, which in this example would be
    - `122 + 1 - 97 = 26`
    - `26 % 26 = 0`
    - `0 + 97 = 97`
    - `chr(97) = a`

- For uppercase letters (`A` through `Z`), the values range from 65 through 90,
  and the value prior to modulo is normalized by subtracting 65. However, after
  the modulo, 97 is added, returning a lowercase letter. In this case, even
  with a `shift_distance` of 0, a lowercase version of the letter will be 
  returned.
  
- `encode` and `decode` are effectively the inverse of each other. In encoding,
  the `shift_distance` is added, and in decoding, the `shift_distance` is
  subtracted, such that encoding with a negative `shift_distance` is the same
  as decoding with the absolute value of that `shift_distance`, and the reverse
  is also true.
  
In regards to running the code, the script can be read as follows:

- `Cipher` is a class with the methods `encode` and `decode`, making it 
  compatible with the provided test script `simple_cipher_test.py`. 

The methods take two inputs, `plaintext` and `shift_distance`. 

- The first input is `plaintext`, the string to be encoded/decoded. If no 
  inputs are provided, an exception will be raised. If `plaintext` is empty, 
  contains any spaces, or any characters besides letters, this will also raise 
  an exception. 

- `shift_distance` is the number of times to shift each character. It is an 
  optional input, and defaults to 1. A shift_distance of 0 will run the
  calculation, but this will only change uppercase characters to lowercase, 
  lowercase characters will not be changed.

## Download
# (This is from the challenge README)

Fork this repository to your account and clone it, or download it as a zip and
extract the files.

## Run
# (This is from the challenge README)

1. Open a terminal window and navigate to the challenge directory.
2. Run `pip install pytest`.
3. Run `pytest simple_cipher_test.py` to test the challenge.

## Troubleshooting
# (This is from the challenge README)

- Ensure you have python installed (`python -v`)
- Ensure you have pytest installed (`pip install pytest`)
- Ensure you are in the challenge directory

## About Us
# (This is from the challenge README)

The Cyndx platform harnesses the power of semantic search which is driven by
our proprietary predictive analytics engine. We make data smarter, so that it
can work harder and more effective for you, which ultimately allow you to find
the right investments or investors to satisfy your needs, every time.

Learn more: https://www.cyndx.com

## Attribution
# (This is from the challenge README)

Simplified and adapted from the Exercism (https://exercism.io/) cipher exercise.
