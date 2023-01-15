from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="xoxb-VOTPUSK-TOKEN")

try:
    response = client.chat_postMessage(
        channel="#канал-для-репортов",
        text="404 Error found at https://votpusk.ru/notfound"
    )
    print(response)
except SlackApiError as e:
    print("Error sending message: {}".format(e))
