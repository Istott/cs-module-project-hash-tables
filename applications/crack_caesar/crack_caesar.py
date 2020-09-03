# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# open and read contents of ciphertext.txt
with open("ciphertext.txt") as f:
    text = f.read()


key = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

# loop through characters
# for sentence in text:
count_chars = {}
for char in text:
    if char in count_chars:
        count_chars[char] += 1
    elif char.isalpha() and char not in count_chars:
        count_chars[char] = 1

ordered_count = [char[0] for char in sorted(count_chars.items(), key=lambda x: x[1], reverse=True)]

# convert text string into an array of chars
text_chars = list(text)

decoded_str = [None] * len(text_chars)

for i in range(len(ordered_count) - 1):
    for j in range(len(text_chars)):
        if text_chars[j] == ordered_count[i]:
            decoded_str[j] = key[i]
        elif decoded_str[j] is None:
            decoded_str[j] = text_chars[j]

print("".join(decoded_str))

# def encrypt(s):
#     result = ''

#     for c in s:
#         c = c.upper()

#         if c.isalpha():
#             result += encode_table[c]
#         else:
#             result += c

#     return result

# def decrypt(s):
#     result = ''

#     for c in s:
#         c = c.upper()

#         if c.isalpha():
#             result += decode_table[c]
#         else:
#             result += c

#     return result

# print(encrypt(words))
# print(decrypt(words))




# encode_table = {
#     'A': 'H',
#     'B': 'Z',
#     'C': 'Y',
#     'D': 'W',
#     'E': 'O',
#     'F': 'R',
#     'G': 'J',
#     'H': 'D',
#     'I': 'P',
#     'J': 'T',
#     'K': 'I',
#     'L': 'G',
#     'M': 'L',
#     'N': 'C',
#     'O': 'E',
#     'P': 'X',
#     'Q': 'K',
#     'R': 'U',
#     'S': 'N',
#     'T': 'F',
#     'U': 'A',
#     'V': 'M',
#     'W': 'B',
#     'X': 'Q',
#     'Y': 'V',
#     'Z': 'S'
# }

# decode_table = {value:key for key, value in encode_table.items()}