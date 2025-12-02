from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=".md", callback_data= "to_md")],
            [InlineKeyboardButton(text=".txt", callback_data= "to_txt")],
        ]
    )
cancel_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Отмена", callback_data= "cancel")],
        ]
    )
add_more_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            {InlineKeyboardButton(text="Экспорт", callback_data= "export")},
            [InlineKeyboardButton(text="Отмена", callback_data= "cancel")],
        ]
    )

export_again_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Новый экспорт", callback_data= "start")],
        ]
)