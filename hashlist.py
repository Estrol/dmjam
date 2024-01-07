import os
import hashlib

# Define the directory
dir_path = './lists'

# check if ojnlist_hash.dat exist
if os.path.exists('./ojnlist_hash.dat'):
    os.remove('./ojnlist_hash.dat')

# Create a file to store the hash
file = open('./ojnlist_hash.dat', 'w')
file.write('hash=sha256,')

for idx, filename in enumerate(os.listdir(dir_path)):
    file_path = os.path.join(dir_path, filename)
    
    with open(file_path, 'rb') as file2:
        bytes = file2.read()
        readable_hash = hashlib.sha256(bytes).hexdigest()
        print(f'File {idx}: {filename}, sha256 Hash: {readable_hash}')
        file.write(f'{filename}={readable_hash},')

file.close()