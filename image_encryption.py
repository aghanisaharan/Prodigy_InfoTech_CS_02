from PIL import Image
import random
import os
import sys


# ===============================
# Encryption Function
# ===============================
def encrypt_image(input_path, output_path, key):

    img = Image.open(input_path).convert("RGB")

    width, height = img.size
    pixels = list(img.getdata())

    random.seed(key)
    indices = list(range(len(pixels)))
    random.shuffle(indices)

    encrypted_pixels = [pixels[i] for i in indices]

    encrypted_img = Image.new("RGB", (width, height))
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save(output_path)


# ===============================
# Decryption Function
# ===============================
def decrypt_image(input_path, output_path, key):

    img = Image.open(input_path).convert("RGB")

    width, height = img.size
    encrypted_pixels = list(img.getdata())

    random.seed(key)
    indices = list(range(len(encrypted_pixels)))
    random.shuffle(indices)

    decrypted_pixels = [None] * len(encrypted_pixels)

    for i, shuffled_index in enumerate(indices):
        decrypted_pixels[shuffled_index] = encrypted_pixels[i]

    decrypted_img = Image.new("RGB", (width, height))
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save(output_path)


# ===============================
# Utility Functions
# ===============================
def print_header():
    print("\n" + "="*50)
    print("      IMAGE ENCRYPTION TOOL (Pixel Swapping)")
    print("="*50)


def get_mode():
    print("\nSelect Mode:")
    print("1. Encrypt Image 🔐")
    print("2. Decrypt Image 🔓")

    while True:
        choice = input("\nEnter choice (1 or 2): ").strip()

        if choice == "1":
            return "encrypt"
        elif choice == "2":
            return "decrypt"
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")


def get_file_path():

    while True:
        path = input("\nEnter image file path: ").strip()

        if os.path.exists(path):
            return path
        else:
            print("❌ File not found. Try again.")


def get_key():

    while True:
        key_input = input("\nEnter numeric key (example: 12345): ").strip()

        if key_input.isdigit():
            return int(key_input)
        else:
            print("❌ Key must be a number.")


def generate_output_path(input_path, mode):

    filename, ext = os.path.splitext(input_path)

    if mode == "encrypt":
        return filename + "_encrypted.png"
    else:
        return filename + "_decrypted.png"


# ===============================
# Main Program
# ===============================
def main():

    print_header()

    mode = get_mode()

    input_path = get_file_path()

    key = get_key()

    output_path = generate_output_path(input_path, mode)

    print("\nProcessing... ⏳")

    try:

        if mode == "encrypt":
            encrypt_image(input_path, output_path, key)
            print("✅ Encryption successful!")

        else:
            decrypt_image(input_path, output_path, key)
            print("✅ Decryption successful!")

        print(f"📁 Output file: {output_path}")

    except Exception as e:
        print("❌ Error:", e)

    print("\nDone ✔")


# Run program
if __name__ == "__main__":
    main()
