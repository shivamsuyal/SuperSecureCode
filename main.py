from encrypt import encrypt_file
from decrypt import decrypt_file

if __name__ == "__main__":
    # Encrypt a file
    input_file = "plain_text.txt"
    output_file = "encrypted_text.aes"
    password = "your_password_here"
    
    encrypt_file(input_file, output_file, password)
    print("File encrypted successfully!")

    # Decrypt a file
    input_file = "encrypted_text.aes"
    output_file = "decrypted_text.txt"
    
    decrypt_file(input_file, output_file, password)
    print("File decrypted successfully!")
