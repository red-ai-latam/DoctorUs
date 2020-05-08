#!/usr/bin/env python3
"""Entry point for example chatbot application using Infermedica API.

Example:
    To start the application simply type::

        $ python3 credentials.py APP_ID:APP_KEY

    where `APP_ID` and `APP_KEY` are Application Id and Application Key from
    your Infermedica account respectively.

Note:
    If you don't have an Infermedica account, please register at
    https://developer.infermedica.com.

"""
import argparse
import uuid


# Use when passing credentials from terminal

# def get_credentials():
#
#     args = parse_args()
#     auth_string = get_auth_string(args.auth)
#     case_id = new_case_id()


def get_auth_string(auth_or_path):
    """Retrieves authentication string from string or file.

    Args:
        auth_or_path (str): Authentication string or path to file containing it

    Returns:
        str: Authentication string.

    """
    if ":" in auth_or_path:
        return auth_or_path
    try:
        with open(auth_or_path) as stream:
            content = stream.read()
            content = content.strip()
            if ":" in content:
                return content
    except FileNotFoundError:
        pass
    raise ValueError(auth_or_path)


def new_case_id():
    """Generates an identifier unique to a new session.

    Returns:
        str: Unique identifier in hexadecimal form.

    Note:
        This is not user id but an identifier that is generated anew with each
        started "visit" to the bot.

    """
    return uuid.uuid4().hex


def parse_args():
    """Parses command line arguments.

    Returns:
        argparse.Namespace: Namespace containing three public attributes:
            1. auth (str) - authentication credentials.
            2. model (str) - chosen language model.
            3. verbose (bool) - flag indicating verbose output.

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("auth",
                        help="authentication string for Infermedica API: "
                             "APP_ID:APP_KEY or path to file containing it.")
    parser.add_argument("--model",
                        help="use non-standard Infermedica model/language, "
                             "e.g. infermedica-es")
    # TODO: Check if `verbose` actually does anything.
    parser.add_argument("-v", "--verbose",
                        dest="verbose", action="store_true", default=False,
                        help="dump internal state")
    args = parser.parse_args()
    return args
