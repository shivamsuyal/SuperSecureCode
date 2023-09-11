import pyAesCrypt

def decrypt_file(input_file, output_file, password):
    bufferSize = 64 * 1024  # Set the buffer size (64 KB in this example)

    try:
        with open(input_file, "rb") as f_in, open(output_file, "wb") as f_out:
            pyAesCrypt.decryptStream(f_in, f_out, password, bufferSize)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    input_file = "encrypted_text.aes"
    output_file = "decrypted_text.txt"
    password = "your_password_here"
    
    decrypt_file(input_file, output_file, password)
