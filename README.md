# A Little about the project
 
  This is a project we (Shiloh and Ido) have done as part of our university course.
  It is a client-server application which is similar to a messagner (like Whatsapp or Telegram etc etc...);
  It communicates under a tcp connection with End-to-end encryption (E2EE). 
  
  Both the client-side and the server-side are written in Python.
  
  Each user needs to register or reconnect to the server and only then he can send (or read) messages to (from) other users that the server (upon request) sends to the users back.
  To achieve End-to-end encryption we utilised the Elliptic-curve Diffie–Hellman (ECDH) key agreement protocol and upon each new message we used it to choose a new AES-CBC key that we later     
  exchangd the message through [For a more in-detail explanation, keep scrolling].

  
  Essentially there are 4 major "protocols" that operate with each other in the project, the Registration protocol, the Connect/Connection protocol the Communication protocol and the Request for 
  waiting messages protocol.

[Video for showcasing the project (in hebrew)]

#### Libraries used:
##### cryptography (.hazmat)
##### hashlib
##### Base64
##### Socket
##### json
##### threading
##### re (Secret Labs' Regular Expression Engine)
##### random
##### os
##### enum
##### abc

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

