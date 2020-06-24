import logging
from view.help import get_help_view


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def start_handler(update, context):
    LOGGER.info(f'User with id={update.effective_user["id"]} connected to the bot.')
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=get_help_view()
    )
