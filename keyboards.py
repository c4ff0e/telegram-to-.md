from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=".md", callback_data= "to_md")],
            [InlineKeyboardButton(text=".txt", callback_data= "to_txt")],
        ]
    )
cancel_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Отменить", callback_data= "cancel")],
        ]
    )