# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [

]

HEY_IMG = ""

ALIVE_ANIMATION = [
 ""
]


PM_START_TEXT = """
👋 Hello *{}*!

I am *{}*, a powerful Telegram group management bot.

• I can help you with:
• Moderation tools
• Notes & Filters
• AI utilities
• Anime utilities
• Many more modules

Use the buttons below to explore my features.
"""

START_BTN = [
    [
        InlineKeyboardButton("➕ Add me to your group", url="https://t.me/{}?startgroup=true"),
    ],
    [
        InlineKeyboardButton("📚 Commands", callback_data="help_back"),
        InlineKeyboardButton("ℹ️ About", callback_data="Miko_"),
    ],
    [
        InlineKeyboardButton("👨‍💻 Support", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
]

HELP_STRINGS = """
📚 *Bot Help Menu*

Select a module below to view its commands.
"""



ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/Hydra_Updates"),
        ib(text="SUPPORT", url="https://t.me/hydraXsupport"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]


