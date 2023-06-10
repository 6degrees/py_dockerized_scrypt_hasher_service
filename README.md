# py_dockerized_scrypt_hasher

Docker version to expose a Python (Flask) API endpoint that hashes to scrypt (firebase)

## Setup

1. Get config variables from your firestore project
   1. firebase->authentication-> little three dots top right of users table
2. Create an `.env` file with the below content

   ```bash
    base64_signer_key=__get_from_your_firebase_project__
    base64_salt_separator=__get_from_your_firebase_project__
    rounds=__get_from_your_firebase_project__
    mem_cost=__get_from_your_firebase_project__
    ```

3. Pull the image
   `docker pull ghcr.io/6degrees/docker_py_scrypt_hasher:latest`
4. Run

    ```bash
    docker run -d -p 5959 --name docker_py_scrypt_hasher ghcr.io/6degrees/docker_py_scrypt_hasher:latest
    ```

Now you have a flask endpoint running at your machine at `http://127.0.0.1:5959` (unless you changed the port)

## Usage

Just make sure you have the native password ready and the `salt` used to encrypt it in firebase (not the `salt separator`)
Example:
    `http://127.0.0.1/scrypt?string=plain_password&salt=xe3yTfPUs-KyJw==`

## Credits

- <https://stackoverflow.com/questions/12315398/check-if-a-string-is-encoded-in-base64-using-python>
- <https://github.com/JaakkoL/firebase-scrypt-python>

## Licenses

No licenses, no nothing, just copy and paste all you want
