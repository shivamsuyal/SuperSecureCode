import pyAesCrypt

def encrypt_file(input_file, output_file, password):
    bufferSize = 64 * 1024  # Set the buffer size (64 KB in this example)
    
    try:
        with open(input_file, "rb") as f_in, open(output_file, "wb") as f_out:
            pyAesCrypt.encryptStream(f_in, f_out, password, bufferSize)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    input_file = "plain_text.txt"
    output_file = "encrypted_text.aes"
    password = "your_password_here"
    
    encrypt_file(input_file, output_file, password)
