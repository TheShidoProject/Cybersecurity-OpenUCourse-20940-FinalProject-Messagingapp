# A Little about the project 📱🌐🖧
 
  This is a project we (Shiloh and Ido) have done as part of our university course.
  It is a client-server application which is similar to a messenger (like Whatsapp or Telegram etc etc...);
  
  It communicates under a tcp connection with End-to-end encryption (E2EE). 🔒
  
  Both the client-side and the server-side are written in Python.🐍
  
  Each user needs to register or reconnect to the server and only then he can send (or read) messages to (from) other users that the server (upon request) sends to the users back.

  To achieve End-to-end encryption we utilised the Elliptic-curve Diffie–Hellman (ECDH) key agreement protocol and upon each new message we used it to choose a new AES-CBC key that we later     
  exchangd the message through.🗝️🔐
  
  > [!NOTE]
  >  For a more in-detail explanation, keep scrolling and watch the following videos🗃️📂: 
  #### [What is the Diffie-Hellman algorithm?](https://youtu.be/85oMrKd8afY?si=-okZEN9M6x6zJxBk)
  #### [What is ECC (Elliptic Curve Cryptography)?](https://youtu.be/NF1pwjL9-DE?si=yOYptssAnffK5pZ8)
  #### [What is AES (Advanced Encryption Standard)?](https://youtu.be/O4xNJsjtN6E?si=UBw5hMDR66QG0dNL)
  #### [General good knowledge - Different AES modes](https://youtu.be/Rk0NIQfEXBA?si=TNnUPrqP4rYHjYPt)
  #### [Hashing Algorithms](https://youtu.be/b4b8ktEV4Bg?si=yWsUorino_4JtMYY)

  #### A gif illustrating how ECC works
  ![ECC_gif](https://github.com/TheShidoProject/Cybersecurity-OpenUCourse-20940-FinalProject-Messagingapp/blob/main/gifs/elliptic-curve-gif.gif)
  
> [!TIP]
> We recommend being familiar with the following videos above and of course the more knowledge you have the better🎯.


  #### Essentially there are 4 major protocols or processes that operate with each other in the project:
  ##### 1) Registration protocol. 
  ##### 2) Connect/Connection protocol.
  ##### 3) Communication protocol. 
  ##### 4) Request for waiting messages protocol.

  #### protocol codes in our uml
  ![protocol_codes_in_uml](https://github.com/TheShidoProject/Cybersecurity-OpenUCourse-20940-FinalProject-Messagingapp/blob/main/images/ProtocolCodes.png)
  


### Libraries used📚🎧☕:
#### cryptography (.hazmat)
#### hashlib
#### Base64
#### Socket
#### json
#### threading
#### re (Secret Labs' Regular Expression Engine)

### <ins>An inside look to the development process, our class UML's:</ins>
Here are some of our UML's we created before and during our work on the project - they contain some inaccuracies regarding the final design we went with but it contains some good points to what we thoguht of before and during our work on the project.
#### [server-side-uml_class_diagram](https://lucid.app/lucidchart/e60fc903-e641-4ff6-88d3-6dd8ac1bb5fd/edit?viewport_loc=-961%2C-279%2C3222%2C1799%2C0_0&invitationId=inv_81f414d9-cca6-4cd5-9e36-1ae5148da405)
#### [user-side-uml_class_diagram](https://lucid.app/lucidchart/cc9a3872-09da-4929-a7a3-ac6f06988815/edit?viewport_loc=-594%2C103%2C2061%2C1151%2C0_0&invitationId=inv_4f8fedab-117f-4bd2-a125-8facc4ec641d)
#### [Registration process](https://lucid.app/lucidchart/ef5d014f-755a-4853-8aa5-fa723d7300f9/edit?viewport_loc=-3171%2C-1122%2C4515%2C2120%2C0_0&invitationId=inv_0484b627-36d1-469e-9eb8-0d0644443883)
#### [Connection protocol and CheckWaitingMessagesProtocol](https://lucid.app/lucidchart/1c0befd0-05d0-4336-a706-4df23ce38326/edit?viewport_loc=-1060%2C-16%2C4177%2C2332%2C0_0&invitationId=inv_6b2772a5-4e2c-4f3f-af36-3ba3da01c8da)
#### [Communication protocol](https://lucid.app/lucidchart/e411f997-0c85-4016-a39f-16903ef4b05d/edit?viewport_loc=-374%2C-507%2C3045%2C1700%2C0_0&invitationId=inv_b38c84e0-deb4-4b11-a4d0-ac770831bbb3)
# Overview of Server and client actions

### Overview of the Server💻👾
The server works by default on port: 5000.

In it’s creation, it generates public and private ECC keys.

It waits for requests from clients (in the form of jsons') in an endless loop; when it receives a request, it deciphers the request and operates based on the request code it extracts from the request.

### Overview of the User📱👨‍💼
When created (after user input) it initializes a phone number, an email address and generates public and private ECC keys.

# Registration process:
### [Click here to view the UML we created for the Registration process](https://lucid.app/lucidchart/ef5d014f-755a-4853-8aa5-fa723d7300f9/edit?viewport_loc=-3171%2C-1122%2C4515%2C2120%2C0_0&invitationId=inv_0484b627-36d1-469e-9eb8-0d0644443883)
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
### [Click here to view the UML we created for the Connection protocol or check waiting messages protocol](https://lucid.app/lucidchart/1c0befd0-05d0-4336-a706-4df23ce38326/edit?viewport_loc=-1060%2C-16%2C4177%2C2332%2C0_0&invitationId=inv_6b2772a5-4e2c-4f3f-af36-3ba3da01c8da)
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
### [Click here to view the UML we created for the Communication protocol](https://lucid.app/lucidchart/e411f997-0c85-4016-a39f-16903ef4b05d/edit?viewport_loc=-374%2C-507%2C3045%2C1700%2C0_0&invitationId=inv_b38c84e0-deb4-4b11-a4d0-ac770831bbb3)
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
### [Click here to view the UML we created for the check waiting messages protocol or the Connection protocol](https://lucid.app/lucidchart/1c0befd0-05d0-4336-a706-4df23ce38326/edit?viewport_loc=-1060%2C-16%2C4177%2C2332%2C0_0&invitationId=inv_6b2772a5-4e2c-4f3f-af36-3ba3da01c8da)
when the server is online, and an online client (let's name him Shiloh) wants to see all of his messages.

#### The steps shiloh takes to view his messages:
1)	Shiloh asks the server for waiting messages according to his phone number.
2)	Server checks in database for Shiloh's waiting messages and sends the waiting messages to him (deleting them after viewing once).
3)	Each message contains the sender's information (along side the public key of the sender, the sender's phone number and more...) 
Shiloh generates the same shared secret with his private key and the sender’s public key (received from the server with the message) and derives the same derived key with the salt using KDF.
4)	Shiloh unwraps the wrapped AES key with derived key and iv.
5)	Shiloh decrypts the message using the AES key and the other iv.
6) Shiloh views the messages one by one.



# Security Compliance Summary ✨</>✨

## Confidentiality

### Key Exchange and Encryption:
•	The server and client utilize Elliptic Curve Diffie-Hellman (ECDH) to establish a shared secret, ensuring that sensitive information (like keys and messages) is exchanged securely over an encrypted channel.
•	Messages between clients and the server, as well as inter-client communication, are encrypted using AES in CBC mode. This ensures that even if intercepted, the information is unintelligible without the correct decryption key.
### Secure Storage with Hashing:
•	User credentials and sensitive identifiers (e.g., secret code) are hashed using a secure cryptographic hashing algorithm (e.g., SHA-256) before being stored in the database.
•	Hashing ensures that even if the database is compromised, attackers cannot reverse the hashed data to obtain the original values. Additionally, salt values are used to prevent precomputed attacks like rainbow table attacks.
•	This practice aligns with the principle of defense in depth, further safeguarding sensitive information.

## Integrity

### Message Encryption
•	By using AES encryption, the integrity of messages is inherently protected since tampering with the ciphertext results in decryption failure or nonsensical plaintext.

### Validation Mechanisms
•	The server validates incoming data such as phone numbers, email addresses, and secret codes during both registration and connection, ensuring the legitimacy and accuracy of the data being processed.

### <ins>Authentication:</ins>
#### Client-Server Authentication
•	During registration and connection, the client sends its public key and a securely derived secret code to the server, which cross-verifies it with its stored data to authenticate the user.
#### Inter-Client Authentication
•	Before sending messages, users request the recipient's public key from the server. This ensures that encryption is directed toward the intended recipient, authenticated by their phone number.

## Resistance to MITM Attacks (Man-in-the-middle)
### Use of ECC (Elliptic Curve Cryptography)
•	ECDH key exchange ensures that even if an attacker intercepts the data, they cannot derive the shared secret without access to the private keys.
### Public Key Validation
•	 The server plays a critical role in verifying and distributing public keys, reducing the risk of an attacker inserting a malicious key.
### Randomness and Salts
•	Random IVs and salts in key derivation and encryption prevent replay attacks and make it computationally infeasible to predict or replicate keys.
### AES Encryption
•	The use of AES encryption ensures that even if ciphertext is intercepted, it cannot be decrypted without the correct AES key. 
#### A picture that represents a MITM attack
![MITM_attack](https://github.com/TheShidoProject/Cybersecurity-OpenUCourse-20940-FinalProject-Messagingapp/blob/main/images/man_in_the_middle.png)



# Questions, you might be having
  ### ***Why use ECC-based cryptography (Elliptic Curve Cryptography) instead of the known RSA-based cryptography?***
  For those wondering why did we use ECC-based encryption instead of RSA-based encryption here are some of our considerations: 

#### 1) Smaller Key Sizes for Equivalent Security
ECC provides the same level of security as RSA but with much smaller key sizes. For example, a 256-bit key in ECC offers roughly the same security as a 3072-bit key in RSA. Smaller key sizes mean less computational power is   
required, leading to faster encryption/decryption and less memory usage.

#### 2) Efficiency and Lower Power Consumption
Since ECC uses smaller keys for the same level of security, it results in faster computation and reduced bandwidth consumption. This makes ECC especially useful in environments with limited resources, like mobile devices or IoT (Internet of Things) devices. ECC's efficiency in terms of smaller key sizes means that it consumes less power, which is particularly valuable in battery-powered devices

#### 3) Better Scalability
With the increasing need for stronger encryption over time, ECC's efficiency and scalability make it more viable for future cryptographic needs. As computational power grows, RSA requires increasingly larger key sizes, which eventually becomes impractical. ECC, on the other hand, can maintain strong security while using relatively small key sizes.

 #### 4) Security
The underlying mathematical problem behind ECC (the elliptic curve discrete logarithm problem) is considered more difficult to solve compared to RSA's integer factorization problem, especially as key sizes increase. Therefore, ECC is generally seen as more secure for a given key size.

#### 5) Expanding our Skill Set
We wanted to use this project to learn new technologies, after both of us already have done a project using RSA-based encryption; we used this project as a way to experiment with integrating new technologies.
 
  #### A chart the represents the Efficiency of RSA vs ECC in terms of key size for similar security
  ![RSA_vs_ECC](https://github.com/TheShidoProject/Cybersecurity-OpenUCourse-20940-FinalProject-Messagingapp/blob/main/images/rsa_vs_ecc_performance.png)

  ### ***Why switch from ECC-based asymmetric encryption algorithm to the AES (Advanced Encryption Standard)?***
  For those wondering why do we change from the ECC-based asymmetric encryption algorithm to the AES symmetric encryption algorithm upon each new message, we do it because AES is much faster and more efficient for encrypting large   
  amounts of data. Asymmetric encryption is generally more computationally intensive than symmetric based; In our case we switch from ECC which is an asymmetric encryption algorithm to the AES which is symmetric based.

