import os
import random
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def get_and_delete_first_row(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Read all lines into a list

    if not lines:
        return None  # If the file is empty, return None

    first_row = lines.pop(0).strip()  # Remove the first line and strip newline characters

    # Write the remaining lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
    
    return first_row

# Replace my_file.txt with path to your file
file_path = 'my_file.txt'

client = WebClient(token=os.environ["SLACK_TOKEN"])
print(os.environ['SLACK_TOKEN'])

# Select the correct slack channel to post to
try:
    response = client.chat_postMessage(
        channel="learning-python",
        text= get_and_delete_first_row(file_path)
    )
# Handle any api errors
except SlackApiError as e:
    assert e.response["error"]   


