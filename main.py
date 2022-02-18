from flask import Flask, jsonify, request
from firebasescrypt import firebasescrypt
import os
import base64
import urllib.parse
import binascii
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello people, use the scrypt endpoint with string and salt parameters"

@app.route('/scrypt', methods=["GET"])
def hash():
    password_native  = request.args.get('string', "")
    password_salt = urllib.parse.unquote(request.args.get('salt', ""))
    
    if not isBase64(password_salt):
        return "salt is not in correct syntax";

    # Sample Password hash parameters from Firebase Console.
    salt_separator = os.getenv('base64_salt_separator')
    signer_key = os.getenv('base64_signer_key')
    signer_key: bytes = base64.b64decode(signer_key)
    rounds= int(os.getenv('rounds'))
    mem_cost= int(os.getenv('mem_cost'))
    derived_key = firebasescrypt.generate_derived_key(password_native, password_salt, salt_separator, rounds, mem_cost)
    encrypted_hash = firebasescrypt.encrypt(signer_key, derived_key)
    password_hash = base64.b64encode(encrypted_hash).decode('utf-8')

    return password_hash

def isBase64(sb):
    try:
        base64.urlsafe_b64decode(sb)
        return True
    except binascii.Error:
        return False

if __name__ == "__main__":
    app.run(port=5959)