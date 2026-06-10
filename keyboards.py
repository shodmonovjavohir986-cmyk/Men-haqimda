from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, KeyboardButton,ReplyKeyboardMarkup
from aiogram import Router


inline_router = Router()

ortga_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔙 Orqaga")]
    ],
    resize_keyboard=True
)

menu_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👤 Men haqimda", callback_data="men_haqimda"),
            InlineKeyboardButton(text="🎓 Ta'limim", callback_data="talimim")
        ],
        [
            InlineKeyboardButton(text="💻 Ko‘nikmalarim", callback_data="ko‘nikmalarim"),
            InlineKeyboardButton(text="📞 Aloqa", callback_data="aloqa")
        ],
        [
            InlineKeyboardButton(text="📍 Manzil", callback_data="manzil")
        ]
    ]
)