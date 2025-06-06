import json
import os

from user_stats import UserStats

user_message_count = {}

def jsonify(file_url):
    """
    Takes in a file URL, opens it and parses it to JSON and returns said JSON value.

    :param file_url: The string path of the file URL to fetch the JSON from.
    :return: A JSON representation of the data stored in the file.
    """

    raw_data_file = open(file_url)
    raw_data_string = raw_data_file.read()
    raw_data_file.close()
    return json.loads(raw_data_string)


def decode_username(encoded_username):
    """
    Instagram data returns double-encoded unicode strings, and genuine text may be presented as just \\u00xx, and looks
    even worse when printed to the console where it may just appear as spaces - this will convert it to latin1 and
    decode back from utf-8 to fix this.

    :param encoded_username: The username encoded with \\u00xx codes that needs converting.
    :return: A clean string showing what the user would've seen in the Instagram app.
    """
    return encoded_username.encode('latin1').decode('utf-8')


def extract_message_counts(raw_data_json, users):
    """
    Goes through the JSON data and counts the amount of messages sent per user, adding them to the users dictionary if
    they aren't already on there.

    :param raw_data_json: The JSON data about the message history.
    :param users: The users dictionary to store data in
    """

    for message in raw_data_json["messages"]:
        sender_name = message["sender_name"]
        if sender_name not in users:
            users[message["sender_name"]] = UserStats(sender_name, 1)
        else:
            users[message["sender_name"]].increase_message_count(1)


def fetch_all_data_files(directory):
    """
    Instagram splits data into different JSON files, this will get all the file names that need to be analysed for a
    complete analysis.

    :param directory: The directory to look through.
    :return: A list of file names in the given directory location.
    """

    return os.listdir(directory)


def display_entries(entries):
    """
    Loops through each entry and formats the username nicely with the number of messages the user has sent.

    :param entries: A dictionary list of {username: UserStats, ...}
    """

    for username in entries:
        print(decode_username(username[0]), ":", str(username[1].get_messages()), "messages sent.")


for data_file in fetch_all_data_files("data/"):
    json_data = jsonify("data/" + data_file)
    extract_message_counts(json_data, user_message_count)

sorted_user_message_count = sorted(user_message_count.items(), key=lambda x: x[1].get_messages(), reverse=True)
display_entries(sorted_user_message_count)