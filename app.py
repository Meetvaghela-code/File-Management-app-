import os
import shutil
import zipfile
from cryptography.fernet import Fernet
import time

# Generate a key for encryption and decryption
# Save this key to a secure location
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename}: Created successfully")
    except FileExistsError:
        print(f"File name {filename} already exists!")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No file found")
    else:
        print("Files in directory:")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except Exception as e:
        print(f"An error occurred: {e}")

def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input("Enter data to be added = ")
            f.write(content + "\n")
            print(f"Content added to {filename} Successfully!")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except Exception as e:
        print(f"An error occurred: {e}")

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File renamed from {old_name} to {new_name} successfully!")
    except FileNotFoundError:
        print(f"File {old_name} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def move_file(filename, new_location):
    try:
        shutil.move(filename, new_location)
        print(f"File {filename} moved to {new_location} successfully!")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_file_size(filename):
    try:
        size = os.path.getsize(filename)
        print(f"Size of {filename}: {size} bytes")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def compress_file(filename, zip_filename):
    try:
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            zipf.write(filename)
        print(f"File {filename} compressed to {zip_filename} successfully!")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def decompress_file(zip_filename, extract_dir):
    try:
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            zipf.extractall(extract_dir)
        print(f"File {zip_filename} decompressed to {extract_dir} successfully!")
    except FileNotFoundError:
        print(f"Zip file {zip_filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def encrypt_file(filename):
    try:
        with open(filename, 'rb') as f:
            data = f.read()
        encrypted_data = cipher_suite.encrypt(data)
        with open(filename, 'wb') as f:
            f.write(encrypted_data)
        print(f"File {filename} encrypted successfully!")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_file(filename):
    try:
        with open(filename, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        with open(filename, 'wb') as f:
            f.write(decrypted_data)
        print(f"File {filename} decrypted successfully!")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_file_metadata(filename):
    try:
        stats = os.stat(filename)
        creation_time = time.ctime(stats.st_ctime)
        modification_time = time.ctime(stats.st_mtime)
        print(f"File: {filename}")
        print(f"Size: {stats.st_size} bytes")
        print(f"Creation time: {creation_time}")
        print(f"Modification time: {modification_time}")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def backup_directory(src, dest):
    try:
        shutil.copytree(src, dest)
        print(f"Directory {src} backed up to {dest} successfully!")
    except FileExistsError:
        print(f"Backup directory {dest} already exists!")
    except FileNotFoundError:
        print(f"Source directory {src} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def restore_directory(src, dest):
    try:
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(src, dest)
        print(f"Directory {src} restored to {dest} successfully!")
    except FileNotFoundError:
        print(f"Backup directory {src} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1: Create file')
        print('2: View all files')
        print('3: Delete file')
        print('4: Read file')
        print('5: Edit file')
        print('6: Rename file')
        print('7: Move file')
        print('8: Display file size')
        print('9: Compress file')
        print('10: Decompress file')
        print('11: Encrypt file')
        print('12: Decrypt file')
        print('13: Display file metadata')
        print('14: Backup directory')
        print('15: Restore directory')
        print('16: Exit')

        choice = input("Enter your choice (1-16) = ")

        if choice == '1':
            filename = input("Enter the file name to create = ")
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input("Enter the name of the file you want to delete = ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter the file name to read = ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter the file name you want to edit = ")
            edit_file(filename)
        elif choice == '6':
            old_name = input("Enter the current file name = ")
            new_name = input("Enter the new file name = ")
            rename_file(old_name, new_name)
        elif choice == '7':
            filename = input("Enter the file name to move = ")
            new_location = input("Enter the new location = ")
            move_file(filename, new_location)
        elif choice == '8':
            filename = input("Enter the file name to display its size = ")
            display_file_size(filename)
        elif choice == '9':
            filename = input("Enter the file name to compress = ")
            zip_filename = input("Enter the name of the zip file to create = ")
            compress_file(filename, zip_filename)
        elif choice == '10':
            zip_filename = input("Enter the name of the zip file to decompress = ")
            extract_dir = input("Enter the directory to extract files to = ")
            decompress_file(zip_filename, extract_dir)
        elif choice == '11':
            filename = input("Enter the file name to encrypt = ")
            encrypt_file(filename)
        elif choice == '12':
            filename = input("Enter the file name to decrypt = ")
            decrypt_file(filename)
        elif choice == '13':
            filename = input("Enter the file name to display metadata = ")
            display_file_metadata(filename)
        elif choice == '14':
            src = input("Enter the source directory to backup = ")
            dest = input("Enter the destination directory for the backup = ")
            backup_directory(src, dest)
        elif choice == '15':
            src = input("Enter the backup directory to restore from = ")
            dest = input("Enter the destination directory to restore to = ")
            restore_directory(src, dest)
        elif choice == '16':
            print("Closing the app......")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
