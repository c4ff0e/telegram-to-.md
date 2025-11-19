import keyboards
from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command, StateFilter
from bot_main import Converter
import logging
router = Router()

@router.callback_query(F.data == "to_md")
async def to_md(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(collected = [])
    await state.set_state(Converter.wait_for_messages_md)
    await callback.message.answer("""
Отправьте сообщения, которые будут экспортированы в файл

<b>ФОРМАТ .md НЕ ПОДДЕРЖИВАЕТ ИЗОБРАЖЕНИЯ. ОНИ БУДУТ ПРОИГНОРИРОВАНЫ</b>

<b>После отправки напишите команду /done</b>""", reply_markup=keyboards.cancel_kb)

@router.message(Command("done"), Converter.wait_for_messages_md)
async def finish_md(message: Message, state: FSMContext):
    messages = await state.get_data()
    collected = messages.get("collected", [])
    await message.answer(f"Получено {len(collected)} сообщений\n\nХотите добавить больше сообщений?", reply_markup=keyboards.add_more_kb)
    

@router.message(Converter.wait_for_messages_md)
async def collect_messages(message: Message, state: FSMContext):
    messages = await state.get_data()
    collected = messages.get("collected", [])
    collected.append(message)
    await state.update_data(collected = collected)

@router.callback_query(F.data == "add_more")
async def add_more(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    to_md(callback, state)
    
@router.callback_query(Converter.wait_for_messages_md, F.data == "export")
async def export_md(callback: types.CallbackQuery, state: FSMContext):
    gathered = await state.get_data()
    collected = gathered.get("collected", [])
    for message in collected:
        logging.info(message) #e_changed=None suggested_post_approved=None suggested_post_approval_failed=None suggested_post_declined=None suggested_post_paid=None suggested_post_refunded=None video_chat_scheduled=None video_chat_started=None video_chat_ended=None video_chat_participants_invited=None web_app_data=None reply_markup=None forward_date=None forward_from=None forward_from_chat=None forward_from_message_id=None forward_sender_name=None forward_signature=None user_shared=None
    await callback.answer()
    await state.clear()