from linebot.models import MessageEvent, TextMessage, TextSendMessage

from .line import linebot_api
from .line import webhook_handler as handler


@handler.add(MessageEvent, message=(TextMessage))
def handling_message(event):
    if isinstance(event, MessageEvent) and \
        isinstance(event.message, TextMessage):
        messages = event.message.text

        echo_messages = TextSendMessage(text=messages)
        linebot_api.reply_message(
            reply_token=event.reply_token,
            messages=echo_messages,
        )

    return "OK"
