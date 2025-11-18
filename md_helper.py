import keyboards
from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

@router.callback_query(F.data == "to_md")
async def to_md(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("md")