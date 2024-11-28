import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class slack:
    def __init__(self):
        self.web_token = "XXXXXXXXXX"
        self.channel_ID = ''
        self.username = 'Cerberus'

    def notify(self):
        message = 'test' # replace with message with relevant info
        client.chat_postMessage(channel = self.channel_id, text = message,
                                username = self.username)
