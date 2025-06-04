class UserStats:
    """
    This is a short class to store data on an instagram user member who has sent messages in the groupchat. This
    represents just one user through their username and the amount of messages they have sent to the groupchat, along
    with various methods to modify the data stored about them.
    """

    def __init__(self, username, messages=0):
        """
        Declares an instance of a user and their stats for messages sent.

        :param username: The username for the user
        :param messages: The number of messages seny by the user (defaults to 0)
        """
        self._username = username
        self._messages = messages


    def increase_message_count(self, quantity):
        """
        Increases the amount of messages sent by the user

        :param quantity: The amount to increase the stat by
        """

        self._messages += quantity


    def get_username(self):
        """
        Username is a string representing the display name of the user on Instagram.

        :return: The stored username.
        """

        return self._username


    def get_messages(self):
        """
        Messages is an integer representing the amount of messages sent by the user.

        :return: An integer amount of messages sent.
        """

        return self._messages
