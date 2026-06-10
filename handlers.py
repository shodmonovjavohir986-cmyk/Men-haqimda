from aiogram import Router, F
from aiogram.types import CallbackQuery, Message,ReplyKeyboardRemove
from aiogram.filters import CommandStart

from keyboards import menu_btn, ortga_btn

Men_haqimda_handler = Router()


# ✅ START
@Men_haqimda_handler.message(CommandStart())
async def start_cmd(message: Message):
    data = """👋 Assalomu alaykum!

Mening portfolio botimga xush kelibsiz.

🧑‍💻 Isim Familyam: Javohir Shodmonov

Hozirgi kunda IT sohasida tahsil olaman va dasturlash bilan shug‘ullanaman. O‘zimni Strong Junior dasturchi sifatida rivojlantirib bormoqdaman.

🚀 Bilim va ko‘nikmalarim:
• Python dasturlash tili
• Telegram bot yaratish
• Frontend dasturlash (HTML, CSS, JavaScript)
• API va avtomatlashtirish loyihalari

📂 Ushbu bot orqali siz:
• Men haqimda ma'lumot olishingiz
• Loyihalarimni ko‘rishingiz
• Ko‘nikmalarim bilan tanishishingiz
• Men bilan bog‘lanishingiz mumkin

Yangi texnologiyalarni o‘rganish va foydali loyihalar yaratish mening asosiy maqsadim.

Portfolio botimga tashrif buyurganingiz uchun rahmat! 🤝
"""
    await message.answer(data, reply_markup=menu_btn)


# ✅ MEN HAQIMDA
@Men_haqimda_handler.callback_query(F.data == "men_haqimda")
async def men_haqimda(call: CallbackQuery):
    data = """👤 Men haqimda

🪪 Ism va familiya: Javohir Shodmonov
🗓️ Yosh: 15 yosh

📝 Qisqacha ma'lumot:
Men IT sohasiga qiziqadigan yosh dasturchiman. Hozirda dasturlash bo‘yicha bilimlarimni oshirib, turli loyihalar ustida ishlamoqdaman. Kelajakda professional dasturchi bo‘lishni maqsad qilganman.

🎓 Ta'limim
🏫 Maktab: 25-maktab
📚 O‘quv markazi: Academya o‘quv markazi
💻 Yo‘nalish: Dasturlash va zamonaviy IT texnologiyalari

💻 Ko‘nikmalarim
🔹 HTML
🔹 CSS
🔹 JavaScript
🔹 Python
🔹 Django

🛠 Texnologiyalar:
• Telegram Bot Development
• Frontend Development
• Web Development
• Django Framework

🚀 Maqsadim — kuchli Full Stack dasturchi bo‘lish.
"""

    await call.answer()
    await call.message.answer(data,  reply_markup=ortga_btn)


@Men_haqimda_handler.message(F.text == "🔙 Orqaga")
async def ortga(message: Message):
    await message.answer(
        "🔙 Ortga bosildi",
        reply_markup=ReplyKeyboardRemove() 
    )

    
    await message.answer(
          "Asosiy menu:",
        reply_markup=menu_btn
    )



@Men_haqimda_handler.callback_query(F.data == "talimim")
async def men_haqimda(call: CallbackQuery):
    data = """🎓 Ta'limim

🏫 Maktab: 25-maktab

📚 O‘quv markazi: Academya o‘quv markazi

💻 Yo‘nalish: Dasturlash va zamonaviy IT texnologiyalari

Hozirda 25-maktabda tahsil olaman va qo‘shimcha ravishda Academya o‘quv markazida dasturlash yo‘nalishida o‘qiyman. Ta'lim davomida HTML, CSS, JavaScript, Python va Django texnologiyalarini o‘rganib, amaliy loyihalar yaratish orqali o‘z bilim va ko‘nikmalarimni rivojlantirib bormoqdaman.

📈 Doimiy ravishda yangi texnologiyalarni o‘rganish, tajriba orttirish va kelajakda malakali Full Stack dasturchi bo‘lish uchun izlanishda davom etyapman.


"""

    await call.answer()
    await call.message.answer(data,  reply_markup=ortga_btn)


@Men_haqimda_handler.callback_query(F.data == "ko‘nikmalarim")
async def men_haqimda(call: CallbackQuery):
    data = """💻 Ko‘nikmalarim

Dasturlash va web texnologiyalariga qiziqaman hamda quyidagi yo‘nalishlarda bilim va tajribaga egaman:

🌐 **Frontend:**
• HTML5
• CSS3
• JavaScript

⚙️ **Backend:**
• Python
• Django Framework

🤖 **Boshqa ko‘nikmalar:**
• Telegram bot yaratish
• Web sahifalar ishlab chiqish
• API bilan ishlash asoslari
• Muammolarni tahlil qilish va yechim topish
• Jamoada ishlash va doimiy o‘rganishga intilish

🚀 Har kuni yangi texnologiyalarni o‘rganish va amaliy loyihalar orqali o‘z ustimda ishlab, dasturchilik mahoratimni yanada oshirib bormoqdaman.

"""

    await call.answer()
    await call.message.answer(data,  reply_markup=ortga_btn)

@Men_haqimda_handler.callback_query(F.data == "aloqa")
async def men_haqimda(call: CallbackQuery):
    data = """📞 Aloqa
    📱 Telefon: +998 88 191 82 11
    💬 Telegram: @shodmonov2011
    🌐 Instagram: shodmonov.coder

    💬 Hamkorlik, loyiha yoki dasturlash bo‘yicha savollaringiz bo‘lsa, bemalol bog‘lanishingiz mumkin.
    🚀 Birgalikda yangi g‘oyalarni amalga oshirishdan mamnun bo‘laman!
"""

    await call.answer()
    await call.message.answer(data,  reply_markup=ortga_btn)

@Men_haqimda_handler.callback_query(F.data == "manzil")
async def men_haqimda(call: CallbackQuery):
    data = """📍 Manzil

🏳️ Mamlakat: O‘zbekiston
🏞 Viloyat: Surxondaryo viloyati
🏘 Tuman: Uzun tumani
🏡 Mahalla: Serharakat mahallasi

📌 Qo‘shimcha ma'lumot:
Men IT sohasiga qiziqadigan yosh dasturchiman. Doimiy ravishda yangi texnologiyalarni o‘rganib boraman va o‘z ustimda ishlab, amaliy loyihalar orqali tajriba oshirishga harakat qilaman. Maqsadim — kuchli dasturchi bo‘lib, katta IT loyihalarda ishtirok etish.

"""

    await call.answer()
    await call.message.answer(data,  reply_markup=ortga_btn)



