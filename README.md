# py_dockerized_scrypt_hasher

 Docker version to expose a Python (Flask) API endpoint that hashes to scrypt (firebase)

```bash
docker pull ghcr.io/6degrees/py_dockerized_scrypt_hasher_service:latest
```

## Setup

1. First, you need some configuration variables from your firebase project, you can get them from firebase->authentication-> little three dots top right of users table

2. create an `docker_env_file` file in the project root directory, next to Dockerfile with the below content. (You can rename the `docker_env_file.example` and use it)

    ```bash
    base64_signer_key=__get_from_your_firebase_project__
    base64_salt_separator=__get_from_your_firebase_project__
    rounds=__get_from_your_firebase_project__
    mem_cost=__get_from_your_firebase_project__
    ```

3. Next, run the below commands in the project folder (next to Dockerfile)

    ```bash
    git clone this repo
    cd firebasescrypt
    docker build -t firebasescrypt
    docker run -p 5959 --env-file ./docker_env_file firebasescrypt
    ```

Now you have a flask endpoint running at your machine at `http://127.0.0.1:5959` (unless you changed the port or put on a server)

## Usage

Just make sure you have the native password ready and the `salt` used to encrypt it in firebase (not the `salt separator`)
Example:
    `http://127.0.0.1/scrypt?string=plain_password&salt=xe3yTfPUs-KyJw==`

## Credits

- https://stackoverflow.com/questions/12315398/check-if-a-string-is-encoded-in-base64-using-python
- https://github.com/JaakkoL/firebase-scrypt-python

## Licenses

No licenses, no nothing, just copy and paste all you want