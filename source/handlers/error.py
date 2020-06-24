import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def error_handler(update, context):
    LOGGER.warning(f'The error "{context.error}" occurred in update "{str(update)}"')
