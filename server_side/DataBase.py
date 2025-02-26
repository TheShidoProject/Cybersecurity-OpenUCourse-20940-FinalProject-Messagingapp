from GlobalCryptoUtils import hash_secret_code
from GlobalValidations import is_valid_phone_number
from Message import Message
from User import User
import hashlib

class DataBase:
    def __init__(self):
        self.users = {}  # Dictionary to store users, keyed by phone_number

    def register_user(self, phone_number, public_key:bytes, secret_code):
        """
        Register a user with the given phone number.
        """
        self.users[phone_number] = User(phone_number, public_key, hash_secret_code(secret_code))
        return True

    def is_user_registered(self, phone_number):
        """
        Check if a user with the given phone number is registered.
        """
        return phone_number in self.users

    def get_user_by_phone_number(self, phone_number):
        if not is_valid_phone_number(phone_number=phone_number):
            raise ValueError("phone_number is invalid")
        if not self.is_user_registered(phone_number):
            raise ValueError("User is not registered for this phone number")
        return self.users[phone_number]

    def get_public_key_by_phone_number(self, phone_number):
        """
        Get the public key of a user by their phone number.
        """
        if phone_number in self.users:
            return self.users[phone_number].get_public_key()
        print(f"No user found with phone number {phone_number}.")
        return None

    def is_secret_code_correct_for_user(self, user, code):
        """
        Check if the given secret code matches the user's stored secret code.
        """
        if user in self.users.values():
            salt = user.get_secret_code_hash()[:16]  # Extract the salt from the stored hash
            stored_password_hash = user.get_secret_code_hash()[16:]  # Extract the hash part
            salted_password = salt + code.encode('utf-8')
            new_hash = hashlib.sha256(salted_password).hexdigest().encode('utf-8')
            return new_hash == stored_password_hash
        print("User not found in the database.")
        return False

    def add_message_to_user(self, phone_number, message: Message):
        """
        Add a message to the user's waiting messages.

        Args:
            phone_number (str): The phone number of the user.
            message (Message): The message to add.

        Raises:
            ValueError: If the phone number is invalid or the user is not registered.
        """
        if not is_valid_phone_number(phone_number):
            raise ValueError("Invalid phone number.")

        if phone_number not in self.users:
            raise ValueError(f"No user registered with phone number {phone_number}.")

        user = self.users[phone_number]
        user.add_message(message)

    def get_waiting_messages_for_user(self, phone_number):
        """
        Returns the waiting messages for the user with the given phone number. And clears the waiting messages dict

        Args:
            phone_number (str): The phone number of the user.

        Returns:
            list: A list of waiting messages for the user.

        Raises:
            ValueError: If the phone number is invalid or the user is not registered.
        """
        if not is_valid_phone_number(phone_number):
            raise ValueError("Invalid phone number.")

        if phone_number not in self.users:
            raise ValueError(f"No user registered with phone number {phone_number}.")

        user = self.users[phone_number]
        return user.get_waiting_messages()

    def clear_messages_for_user(self, phone_number):
        """
        Clears all messages for the specified user by phone number.

        Args:
            phone_number (str): The phone number of the user whose messages are to be cleared.

        Raises:
            ValueError: If the phone number is invalid or if no user is registered with the provided phone number.
        """
        if not is_valid_phone_number(phone_number):
            raise ValueError("Invalid phone number.")

        if phone_number not in self.users:
            raise ValueError(f"No user registered with phone number {phone_number}.")

        user = self.users[phone_number]
        user.clear_messages()
