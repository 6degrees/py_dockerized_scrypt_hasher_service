from flask import Flask, jsonify, request
from firebasescrypt import firebasescrypt
import os
import base64
import urllib.parse
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

base64_signer_key = ""
base64_salt_separator = ""

@app.route('/')
def index():
    return "Hello people"


@app.route('/scrypt', methods=["GET"])
def hash():
    password_native  = request.args.get('string', "")
    password_salt = urllib.parse.unquote(request.args.get('salt', ""))
    print(password_salt)
    

    # Sample Password hash parameters from Firebase Console.
    
    salt_separator = os.getenv('base64_salt_separator')
    signer_key = os.getenv('base64_signer_key')
    
    signer_key: bytes = base64.b64decode(signer_key)
    rounds= int(os.getenv('rounds'))
    mem_cost= int(os.getenv('mem_cost'))
    print('hello')
    derived_key = firebasescrypt.generate_derived_key(password_native, password_salt, salt_separator, rounds, mem_cost)
    print('hello')
    encrypted_hash = firebasescrypt.encrypt(signer_key, derived_key)
    password_hash = base64.b64encode(encrypted_hash).decode('utf-8')


    return 'I am hashing (' + password_native + ')' + ' and found ' + password_hash
















if __name__ == "__main__":
    app.run(debug=True)