# A Little about the project
 
  This is a project we (Shiloh and Ido) have done as part of our university course.
  It is a client-server application which is similar to a messagner (like Whatsapp or Telegram etc etc...);
  
  It communicates under a tcp connection with End-to-end encryption (E2EE). 
  
  Both the client-side and the server-side are written in Python.
  
  Each user needs to register or reconnect to the server and only then he can send (or read) messages to (from) other users that the server (upon request) sends to the users back.

  To achieve End-to-end encryption we utilised the Elliptic-curve Diffie–Hellman (ECDH) key agreement protocol and upon each new message we used it to choose a new AES-CBC key that we later     
  exchangd the message through [For a more in-detail explanation, keep scrolling].

  
  Essentially there are 4 major protocols or processes that operate with each other in the project:
  1) Registration protocol. 
  2) Connect/Connection protocol.
  3) Communication protocol. 
  4) Request for waiting messages protocol.

[Video for showcasing the project (in hebrew)]

#### Libraries used:
##### cryptography (.hazmat)
##### hashlib
##### Base64
##### Socket
##### json
##### threading
##### re (Secret Labs' Regular Expression Engine)

# Overview of Server and client actions

### Overview of the Server
The server works by default on port: 5000.

In it’s creation, it generates public and private ECC keys.

It waits for requests from clients (in the form of jsons') in an endless loop; when it receives a request, it deciphers the request and operates based on the request code it extracts from the request.

### Overview of the User
When created (after user input) it initializes a phone number, an email address and generates public and private ECC keys.

# Registration process:
 When server is online, and a client (lets name him Shiloh) wants to register.
 
#### The Steps of registration are:
1)	Shiloh asks the server for his public key.
2)	Shiloh sends the server his phone number and email address.
3)	Server validates phone number and email address.
4)	Server generates a random 6 figures code and sends it by secure channel to the user.
5)	Shiloh sends the server his public key.
6)	The server saves the new user (with all of his credentials) in the database.
7)	Server sends register success if no error has occurred.
 
# Connect protocol
when the server is online, and a client (lets name him Ido) wants to connect.

#### Presumptions:
User side - the user has already registered - he has the server’s public key and remembers the secret code the server gave him in the registration process.
Server side - the user has already registered, the server has the user’s public key, secret code, phone number and email address.

#### Steps of connecting to the server:
1)	Ido generates a shared secret with the server using ECDH (Elliptic-curve Diffie–Hellman) with his private key and the server’s public key.
2)	Ido generates a random salt and derives a secret key using KDF (key derivation function) on the shared secret with salt.
3)	Ido generates an AES key and a random iv encrypt the secret code (with CBC mode).
4)	Ido generates a random iv and wraps the AES key with the KDF derived key and the iv.
5)	Ido sends to the server a json with all the necessary parameters it needs:

```python
message_dict = {
          "code": ProtocolCodes.initConnectionAESExchange.value,
          "phone_number": phone_number,
          "wrapped_aes_key": base64.b64encode(wrapped_key_data).decode("utf-8"),
          "iv_for_wrapped_key": base64.b64encode(iv_for_wrapped_key).decode("utf-8"),
          "encrypted_secret_code": base64.b64encode(encrypted_secret_code).decode("utf-8"),
          "iv_for_secret": base64.b64encode(iv_for_secret).decode("utf-8"),
          "salt": base64.b64encode(salt).decode("utf-8"),
}
```
6) The	Server validates the phone number.
7) The	Server generates the same shared secret with his private key and Ido’s public key and derives the same derived key with the salt using KDF.
8)	The Server unwraps the wrapped AES key with derived key and iv.
9)	The Server decrypt the secret code using the AES key and the other iv, then validate the code from the database (where he saved Ido’s credentials).
10)	If all successful, the Server sends to Ido that the connection is established.


# Communication protocol - Communication between two users
when the server is online, and an online client (let's name him Ido) wants to send a message to another client (let's name him Shiloh).

#### Steps of sending a message:
1)	Ido sends the server Shiloh’s phone number and asks for Shiloh’s public key.
2)	The Server validates the phone number and sends Ido as requested Shiloh’s public key.
3)	Ido repeats steps 1-4 from the last chapter, but instead of using the server’s public key, he uses Shiloh’s public key (and encrypt his message with the AES key).
4)	Ido sends the server:
   
```python
message_dict = {
          "code": UserSideRequestCodes.SEND_MESSAGE.value,
          "sender_public_key": base64.b64encode(user_public_key_pem).decode('utf-8'),
          "wrapped_aes_key": base64.b64encode(wrapped_key_data).decode('utf-8'),
          "iv_for_wrapped_key": base64.b64encode(iv_for_wrapped_key).decode('utf-8'),
          "encrypted_message": base64.b64encode(encrypted_message).decode('utf-8'),
          "iv_for_message": base64.b64encode(iv_for_secret).decode('utf-8'),
          "salt": base64.b64encode(salt).decode('utf-8'),
}
```
5)	The Server saves the message in database under waiting messages for Shiloh. 

In order to see the message Shiloh needs to initiate the next chapter, request for waiting messages.

# Request for waiting messages protocol / CheckWaitingMessagesProtocol
when the server is online, and an online client (let's name him Shiloh) wants to see all of his messages.

#### The steps shiloh takes to view his messages:
1)	Shiloh asks the server for waiting messages according to his phone number.
2)	Server checks in database for Shiloh's waiting messages and sends the waiting messages to him (deleting them after viewing once).
3)	Each message contains the sender's information (along side the public key of the sender, the sender's phone number and more...) 
Shiloh generates the same shared secret with his private key and the sender’s public key (received from the server with the message) and derives the same derived key with the salt using KDF.
4)	Shiloh unwraps the wrapped AES key with derived key and iv.
5)	Shiloh decrypts the message using the AES key and the other iv.
6) Shiloh views the messages one by one.

# Questions, you might be having:
  #### ***Why use ECC-based asymmetric encryption algorithm (Elliptic Curve Cryptography) instead of the known RSA asymmetric encryption algorithm?***
  For those wondering why did we use ECC-based encryption instead of RSA-based encryption here are some of our considerations: 

  1) Smaller Key Sizes for Equivalent Security:
      ECC provides the same level of security as RSA but with much smaller key sizes. For example, a 256-bit key in ECC offers roughly the same security as a 3072-bit key in RSA. Smaller key           sizes mean less computational power is required, leading to faster encryption/decryption and less memory usage.

  2) Efficiency and Lower Power Consumption:
      Since ECC uses smaller keys for the same level of security, it results in faster computation and reduced bandwidth consumption. This makes ECC especially useful in environments with              limited resources, like mobile devices or IoT (Internet of Things) devices. ECC's efficiency in terms of smaller key sizes means that it consumes less power, which is particularly valuable       in battery-powered devices

  3) Better Scalability:
    With the increasing need for stronger encryption over time, ECC's efficiency and scalability make it more viable for future cryptographic needs. As computational power grows, RSA requires        increasingly larger key sizes, which eventually becomes impractical. ECC, on the other hand, can maintain strong security while using relatively small key sizes.

  4) Security:
    The underlying mathematical problem behind ECC (the elliptic curve discrete logarithm problem) is considered more difficult to solve compared to RSA's integer factorization problem,              especially as key sizes increase. Therefore, ECC is generally seen as more secure for a given key size.

  5) Expanding our Skill Set:
     We wanted to use this project to learn new technologies, after both of us already have done a project using RSA-based encryption; we used this project as a way to experiment with                 integrating new technologies.

  ##### A chart the represents the Efficiency of RSA vs ECC in terms of key size for similar security
  ![RSA_vs_ECC](https://github.com/TheShidoProject/Cybersecurity-OpenUCourse-20940-FinalProject-Messagingapp/blob/main/images/rsa_vs_ecc_performance.png)

