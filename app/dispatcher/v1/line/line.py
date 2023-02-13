from linebot import LineBotApi, WebhookHandler

from app.constants import settings

linebot_api = linebot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
webhook_handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)
