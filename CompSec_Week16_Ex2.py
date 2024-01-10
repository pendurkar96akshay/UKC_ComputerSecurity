import hashlib
import sys
import requests
import hashlib

requests.packages.urllib3.disable_warnings()                    # Disable HTTP Warnings


hash = '3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b'
print("Leaked Hash : " + hash)

# Making a list of hash functions to iterate 
all_hash_functions = [hashlib.md5, hashlib.sha1, hashlib.sha224, hashlib.sha256, hashlib.sha384, hashlib.sha512, hashlib.blake2b, hashlib.blake2s, hashlib.sha3_224, hashlib.sha3_256, hashlib.sha3_384, hashlib.sha3_512]

# Fetching the list of common passwords and storing it in a object
file_contents = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/phpbb.txt')

# Iterating through each hash function
for each_hash_functions in all_hash_functions:

    # Iterating through each line of the common passwords file and hashing the contents of that line
    for i in file_contents.text.split('\n'):
        i_hashed = each_hash_functions(i.encode()).hexdigest()

        # Comparing the computed hashed value with the pre-defined (leaked) hash value
        if i_hashed == hash:
            print("Hash Matched! \n" + "Plain text - "+ i + "\nIts Hash : " + i_hashed)
            break