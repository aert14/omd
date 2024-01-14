"""
Bot for playing tic tac toe game with multiple CallbackQueryHandlers.
"""
import logging
import os
import random
from copy import deepcopy

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# get token using BotFather
TOKEN = os.getenv("TG_TOKEN")

CONTINUE_GAME, FINISH_GAME = range(2)

FREE_SPACE = "."
CROSS = "X"
ZERO = "O"


DEFAULT_STATE = [[FREE_SPACE for _ in range(3)] for _ in range(3)]


def get_default_state():
    """Get default state of the game."""
    return deepcopy(DEFAULT_STATE)


def generate_keyfields(
    state: list[list[str]]
) -> list[list[InlineKeyboardButton]]:
    """Generate tic tac toe keyfields 3x3 (telegram buttons)."""
    return [
        [
            InlineKeyboardButton(state[r][c], callback_data=f"{r}{c}")
            for r in range(3)
        ]
        for c in range(3)
    ]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send message on `/start`."""
    context.user_data["keyfields_state"] = get_default_state()
    keyfields = generate_keyfields(context.user_data["keyfields_state"])
    reply_markup = InlineKeyboardMarkup(keyfields)
    await update.message.reply_text(
        "X (your) turn! Please, put X to the free place",
        reply_markup=reply_markup,
    )
    return CONTINUE_GAME


async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Game proccessing."""
    query = update.callback_query
    await query.answer()
    pressed = [int(i) for i in query.data]
    fields = context.user_data["keyfields_state"]

    # Обработка хода пользователя
    if fields[pressed[0]][pressed[1]] == FREE_SPACE:
        fields[pressed[0]][pressed[1]] = CROSS
        winner = check_win(fields)
        if winner:
            reply_markup = InlineKeyboardMarkup(generate_keyfields(fields))
            await query.edit_message_reply_markup(reply_markup=reply_markup)
            await query.message.reply_text(f"{winner} wins!")
            return await end(update, context)
        elif is_fields_full(fields):
            await query.message.reply_text("It's a draw!")
            return await end(update, context)
    else:
        await query.message.reply_text(
            "This space is already taken. Choose another one."
        )
        return CONTINUE_GAME

    # Ход компьютера (если есть свободные клетки)
    if not is_fields_full(fields):
        make_ai_move(fields)
        winner = check_win(fields)
        if winner:
            reply_markup = InlineKeyboardMarkup(generate_keyfields(fields))
            await query.edit_message_reply_markup(reply_markup=reply_markup)
            await query.message.reply_text(f"{winner} wins!")
            return await end(update, context)

    reply_markup = InlineKeyboardMarkup(generate_keyfields(fields))
    await query.edit_message_reply_markup(reply_markup=reply_markup)
    return CONTINUE_GAME


def is_fields_full(fields: list[list[str]]) -> bool:
    """Проверяем, заполнено ли игровое поле полностью."""
    return all(cell != FREE_SPACE for row in fields for cell in row)


def make_ai_move(fields: list[list[str]]) -> None:
    """Делаем ход за ИИ."""
    free_cells = [
        (r, c)
        for r in range(3)
        for c in range(3)
        if fields[r][c] == FREE_SPACE
    ]
    row, col = random.choice(free_cells)
    fields[row][col] = ZERO


def check_win(fields: list[str]) -> bool:
    """Check if crosses or zeros have won the game."""
    # Проверка строк, столбцов и диагоналей на наличие победителя
    for i in range(3):
        if fields[i][0] == fields[i][1] == fields[i][2] != FREE_SPACE:
            return fields[i][0]
        if fields[0][i] == fields[1][i] == fields[2][i] != FREE_SPACE:
            return fields[0][i]

    if fields[0][0] == fields[1][1] == fields[2][2] != FREE_SPACE:
        return fields[0][0]
    if fields[0][2] == fields[1][1] == fields[2][0] != FREE_SPACE:
        return fields[1][1]

    # Если нет победителя, возвращаем None
    return None


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    # reset state to default so you can play again with /start
    context.user_data["keyfields_state"] = get_default_state()
    await update.callback_query.message.reply_text(
        "Game over! Type /start to play again."
    )
    return ConversationHandler.END


def main() -> None:
    """Run the bot"""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Setup conversation handler with the states CONTINUE_GAME and FINISH_GAME
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CONTINUE_GAME: [
                CallbackQueryHandler(game, pattern="^" + f"{r}{c}" + "$")
                for r in range(3)
                for c in range(3)
            ],
            FINISH_GAME: [
                CallbackQueryHandler(end, pattern="^" + f"{r}{c}" + "$")
                for r in range(3)
                for c in range(3)
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
