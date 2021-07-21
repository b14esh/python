import sys
print(sys.getdefaultencoding()) # показать кодировку по умолчанию
print(ord("a")) # показать код буквы а
print(chr(97)) # показать чему равен код 97 (буква a)
print(chr(1823)) # показать чему равен код 1823

s = 'hello'
# Перевод кодировок
enc_ascii = s.encode('ascii')
enc_utf8 = s.encode('utf8')
enc_utf16 = s.encode('utf16')
print(type(enc_ascii))

print(enc_ascii)
print(enc_utf8)
print(enc_utf16)

#Посчитаем количество байт в каждой кодировке слова hello
print(len(enc_ascii)) # мы увидем количество байт на символ
print(len(enc_utf8)) # мы увидем количество байт на символ
print(len(enc_utf16)) # мы увидем количество байт на символ

#
str_in_bytes_0 = b'hello'
str_in_bytes_1 = s.encode("utf8")

str_in_text = 'hello'

print(type(str_in_bytes_0))
print(type(str_in_bytes_1))
print(type(str_in_text))

print('bytes'.encode('utf8'))
print('байты'.encode("utf8"))

print(str_in_bytes_0[0])
print(str_in_text[0])

# Перевод из байтов в строку
# При переводе нужно обезательно указать кодировку
result = str(str_in_bytes_0) # !!!!!! НЕ ПРАВИЛЬНО, ПОЛУЧИМ БРЕД
print(result)

result = str(str_in_bytes_0, 'utf8') # Правильно.
print(result)

result = str_in_bytes_1.decode('utf8')
print(result)