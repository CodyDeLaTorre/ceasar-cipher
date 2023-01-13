import string
class cipher:

  def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
      if char.isalpha():
        if char.isupper():
          shifted_char = chr((ord(char) + shift - 65) % 26 + 65)
        else:
          shifted_char = chr((ord(char) + shift - 97) % 26 + 97)
        encrypted_text += shifted_char
      else:
        encrypted_text += char

    return encrypted_text
  def decrypt(text , shift):
    original = cipher.encrypt(text, -shift)
    return original
    
  def crack(text):
    frequencies = {'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974, 'z': 0.00074}
    max_score = -1
    best_shift = -1
    for shift in range(1, 26):
        score = 0
        decrypted_text = cipher.encrypt(text, -shift)
        for char in decrypted_text:
            if char.lower() in string.ascii_lowercase:
                score += frequencies.get(char.lower(), 0)
        if score > max_score:
            max_score = score
            best_shift = shift
    decrypted_text = cipher.encrypt(text, -best_shift)
    return decrypted_text
