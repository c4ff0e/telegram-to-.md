import keyboards
from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.types import Message
from aiogram.types import (                                       
      MessageOriginUser, MessageOriginHiddenUser,                   
      MessageOriginChannel, MessageOriginChat,                      
  )
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command, StateFilter
from bot_main import Converter
import logging
import datetime
router = Router()

@router.callback_query(F.data == "to_md")
async def to_md(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(collected = [])
    await state.set_state(Converter.wait_for_messages_md)
    await callback.message.answer("""
Отправьте сообщения, которые будут экспортированы в файл

<b>ФОРМАТ .md НЕ ПОДДЕРЖИВАЕТ ИЗОБРАЖЕНИЯ. ОНИ БУДУТ ПРОИГНОРИРОВАНЫ.</b>

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
    
@router.callback_query(Converter.wait_for_messages_md, F.data == "export")
async def export_md(callback: types.CallbackQuery, state: FSMContext):
    gathered = await state.get_data()
    collected = gathered.get("collected", [])
    await state.clear()
    to_export = []
    for message in collected:
        if message.date:
            to_export.append(f"{message.date.strftime('%Y-%m-%d %H:%M:%S')}\n")
        if message.from_user:
            to_export.append(f"From: *{message.from_user.first_name} {message.from_user.last_name}*\n")
        if message.forward_origin:
            origin = message.forward_origin
            if isinstance(origin, MessageOriginUser):
                to_export.append(f"Message from: *{origin.from_user.first_name} {origin.from_user.last_name}*\n")
            #to_export.append(f"Forwarded from: *{message.forward_origin.from_user.first_name} {message.forward_origin.from_user.last_name}*\n")
        if message.text:
            to_export.append(message.text)
        
    print(to_export)
    await callback.answer()
    await state.clear()
    