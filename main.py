import json
import os

senders = {}

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


def extract_message_counts(raw_data_json, users):
    """
    Goes through the JSON data and counts the amount of messages sent per user, adding them to the users dictionary if
    they aren't already on there.

    :param raw_data_json: The JSON data about the message history.
    :param users: The users dictionary to store data in
    """
    for message in raw_data_json["messages"]:
        if message["sender_name"] not in users:
            users[message["sender_name"]] = 1
        else:
            users[message["sender_name"]] = users[message["sender_name"]] + 1


def fetch_all_data_files(directory):
    """
    Instagram splits data into different JSON files, this will get all the file names that need to be analysed for a
    complete analysis.

    :param directory: The directory to look through.
    :return: A list of file names in the given directory location.
    """
    return os.listdir(directory)


for data_file in fetch_all_data_files("data/"):
    json_data = jsonify("data/" + data_file)
    extract_message_counts(json_data, senders)

print(senders)