import socket
import time

from CommunicationConstants import SERVER_IP, SERVER_DEFUALT_PORT
from GlobalCryptoUtils import generate_ecc_keys
from GlobalValidations import is_valid_phone_number, is_valid_email
from user_side import User
from user_side.Requests import RegisterRequest, ConnectReqeust, CommunicationRequest, CheckWaitingMessagesRequest
from user_side.User import get_email_validated, get_validated_phone_number, connect_to_user
from user_side.user_utils import load_public_key, load_private_key


def get_secret_code() -> str:
    """
    Prompt the user to enter a 6-digit secret code and validate it.

    Returns:
        str: The validated 6-digit secret code.
    """
    while True:
        # Prompt the user for input
        code = input("Enter a 6-digit secret code: ").strip()

        # Check if the code is 6 digits long and numeric
        if code.isdigit() and len(code) == 6:
            return code
        else:
            print("Invalid code. Please enter a 6-digit numeric code.")


def display_options():
    """Display available user options (CLI-based implementation)."""
    print("1. Register to server")
    print("2. Connect to server")


def display_options_after_connection():
    print("Now that you are connected what do you want to do?")
    print("1. Send message")
    print("2. Show waiting messages")
    print("3. Exit program")


def get_validated_option_number(lowest, highest):
    """
        After the options were displayed, returns the number the user chose,
        :raises error if the option number is illegal
    """
    while True:
        try:
            # Prompt the user for input
            number = int(input(f"Enter a number between {lowest} and {highest}: "))

            # Validate the range
            if lowest <= number <= highest:
                return number
            else:
                print("\nInvalid input. Please enter a number between 1 and 3.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def decide_which_process_to_perform(chosen_number):
    connected = False
    user = None
    server_ip = SERVER_IP
    server_port = SERVER_DEFUALT_PORT
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((server_ip, server_port))

    if chosen_number == 1:
        user = User.create_user()
        register_request = RegisterRequest(conn=conn, user=user)
        connected = register_request.run()
        print("Write the secret code that you got from the server (That's for future connections)")
        user_secret_code = get_secret_code()
        user.set_secret_code(user_secret_code)
    elif chosen_number == 2:
        user = connect_to_user()
        user_secret_code = get_secret_code()
        user.set_secret_code(user_secret_code)
        connect_request = ConnectReqeust(conn=conn, user=user)
        connected = connect_request.run()

    while connected:
        display_options_after_connection()
        chosen_number = get_validated_option_number(1, 3)
        if chosen_number == 1:
            print("Entering send message request")
            print("Enter The phone number you want to send a message to:")
            target_phone_number = get_validated_phone_number()
            message = input("Write what message you want to send him")
            send_message_request = CommunicationRequest(conn=conn, user=user, target_phone_number=target_phone_number,
                                                        message_to_user=message)
            send_message_request.run()

        elif chosen_number == 2:
            print("Entering check waiting messages protocol")
            check_waiting_messages_request = CheckWaitingMessagesRequest(conn=conn, user=user)
            check_waiting_messages_request.run()
        elif chosen_number == 3:
            print("OK exiting")
            connected = False
            conn.close()
        time.sleep(10) # SLEEPING FOR 10 SECONDS TO SEE MESSAGE
        connect_request = ConnectReqeust(conn=conn, user=user)
        connected = connect_request.run()
