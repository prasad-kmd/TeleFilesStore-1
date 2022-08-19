# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Files Store Bot! Powered by @sinhagiri_visual_studio .
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🌐 **Website:** [GAMES & SOFTWARES COMMUNITY](https://g-s-community.blogspot.com/)

🤖 **Bot Name:** [GSCOM Files Store](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** [Cloned Repository](https://github.com/prasad-kmd/TeleFilesStore-1)

👥 **Support Group:** [GAMES & SOFTWARES COMMUNITY](https://t.me/+kM0sllYx2LgzYTg1)

📢 **Main Channel:** [SINHAGIRI VISUAL STUDIO](https://t.me/sinhagiri_visual_studio)
"""
	ABOUT_DEV_TEXT = f"""
**GAMES & SOFTWARES COMMUNITY** is aimed to provide those games & software which users want to have. The main goal is to provide direct downloading link without any wait so that users can enjoy unlimited downloads. You can request us about software, game, application etc. and we’ll upload it here as soon as we can.


**GAMES & SOFTWARES COMMUNITY** aims to make easier access to the files for the latest releases, constantly evolving and trying to compete with the time, providing a friendly interface that allow to search for files easier and in more organized way.

**GAMES & SOFTWARES COMMUNITY** is not a file hosting and strictly hosts no contents and files, we provide only index to already published files on the internet, in the same way as mostly search engines do. We are proud of our friendly team and moderators, we have built a real family of people contributing to the site. We are glad to see all these wonderful people on board and with their help and contributions, the site will continue to work and entertain till infinity (Let’s Hope).

The main objective is to provide everybody most convenient and user-friendly interface of **GAMES & SOFTWARES COMMUNITY** to find and download the files people want in much safer way. We are in continue process of developing the site, to make the best of what is possible to set a new standard among the other sites. In the last, heartily thanks to our friendly community that inspires and encourage us to do what we do.

THANK YOU.
__GAMES & SOFTWARES COMMUNITY__
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is **GSCOM File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
