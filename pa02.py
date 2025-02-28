"""
I Daniel Ramirez (da582727) affirm that
this program is entirely my own work and that I have neither developed my code with any
another person, nor copied any code from any other person, nor permitted my code to be copied
or otherwise used by any other person, nor have I copied, modified, or otherwise used programs
created by others. I acknowledge that any violation of the above terms will be treated as
academic dishonesty.
"""


import sys

# Reads the input file and returns its content
def read_file(filename):

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        sys.stderr.write(f"Error: File '{filename}' not found.\n")
        sys.exit(1)


# Pads content with 'X' if needed to match checksum size alignment
def pad_content(content, checksum_size):
    
    pad_length = checksum_size // 8  # convert bits to bytes
    padding_needed = (pad_length - (len(content) % pad_length)) % pad_length
    return content + ("X" * padding_needed)


# Prints content with exactly 80 characters per line
def print_formatted_text(content):

    for i in range(0, len(content), 80):
        print(content[i:i+80])


# Calculates 8-bit, 16-bit, or 32-bit checksum
def calculate_checksum(content, checksum_size):

    checksum = 0
    if checksum_size == 8:
        for char in content:
            checksum += ord(char)
        checksum &= 0xFF  # mask to 8 bits
    elif checksum_size == 16:
        for i in range(0, len(content), 2):
            part = (ord(content[i]) << 8) + (ord(content[i+1]) if i+1 < len(content) else 0)
            checksum += part
        checksum &= 0xFFFF  # mask to 16 bits
    elif checksum_size == 32:
        for i in range(0, len(content), 4):
            part = (
                (ord(content[i]) << 24) +
                ((ord(content[i+1]) << 16) if i+1 < len(content) else 0) +
                ((ord(content[i+2]) << 8) if i+2 < len(content) else 0) +
                (ord(content[i+3]) if i+3 < len(content) else 0)
            )
            checksum += part
        checksum &= 0xFFFFFFFF  # mask to 32 bits
    return checksum


def main():
    
    print()
    
    # Some error handling
    if len(sys.argv) != 3:
        print("error")
        sys.exit(1)

    try:
        filename = sys.argv[1]
        checksum_size = int(sys.argv[2])
        if checksum_size not in [8, 16, 32]:
            raise ValueError
    except:
        print("error")
        sys.exit(1)

    content = read_file(filename)
    content = pad_content(content, checksum_size)

    print_formatted_text(content)
    checksum = calculate_checksum(content, checksum_size)

    # Formatting with specific spacing for each checksum size
    if checksum_size == 8:
        print(f"{checksum_size:2d} bit checksum is {checksum:8x} for all {len(content):4d} chars")
    elif checksum_size == 16:
        print(f"{checksum_size:2d} bit checksum is {checksum:8x} for all {len(content):4d} chars")
    elif checksum_size == 32:
        print(f"{checksum_size:2d} bit checksum is {checksum:8x} for all {len(content):4d} chars")

if __name__ == "__main__":
    main()
