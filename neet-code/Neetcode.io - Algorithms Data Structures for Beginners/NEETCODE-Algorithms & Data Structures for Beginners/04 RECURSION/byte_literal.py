my_bytes = b"hello"
for byte in my_bytes:
    print(byte)
print(
        my_bytes.decode(),
        type(my_bytes.decode()),
        type(my_bytes.__str__())
    )
print(my_bytes.__str__() is my_bytes, my_bytes.__str__() == my_bytes.decode("utf-8"))
