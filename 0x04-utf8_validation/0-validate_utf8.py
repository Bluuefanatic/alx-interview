def validUTF8(data):
    # Helper function to check if a byte is a continuation byte
    def is_continuation(byte):
        return (byte & 0xC0) == 0x80

    # Number of bytes remaining in the current UTF-8 sequence
    num_bytes = 0

    for byte in data:
        # Determine the number of bytes in the UTF-8 sequence
        if num_bytes == 0:
            # Check the leading byte
            if (byte & 0x80) == 0x00:
                # 1-byte sequence (0xxxxxxx)
                num_bytes = 0
            elif (byte & 0xE0) == 0xC0:
                # 2-byte sequence (110xxxxx 10xxxxxx)
                num_bytes = 1
            elif (byte & 0xF0) == 0xE0:
                # 3-byte sequence (1110xxxx 10xxxxxx 10xxxxxx)
                num_bytes = 2
            elif (byte & 0xF8) == 0xF0:
                # 4-byte sequence (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
                num_bytes = 3
            else:
                # Invalid byte
                return False
        else:
            # Check continuation bytes
            if not is_continuation(byte):
                return False
            num_bytes -= 1

    # Check if all sequences were properly ended
    return num_bytes == 0

# Example usage
data = [197, 130, 1]  # Valid UTF-8 encoding
print(validUTF8(data))  # Should print True

data = [235, 140, 4]  # Invalid UTF-8 encoding
print(validUTF8(data))  # Should print False
