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
add_more_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            {InlineKeyboardButton(text="Экспорт", callback_data= "export")},
            [InlineKeyboardButton(text="Добавить ещё", callback_data= "add_more")],
            [InlineKeyboardButton(text="Отменить", callback_data= "cancel")],
        ]
    )