import logging
import copy


class ColoredFormatter(logging.Formatter):  # [8]

    RESET = "\033[0m"
    COLORS = {
        logging.DEBUG: "\033[34m",  # Синий
        logging.INFO: "\033[32m",  # Зеленый
        logging.WARNING: "\033[33m",  # Желтый
        logging.ERROR: "\033[31m",  # Красный
        logging.CRITICAL: "\033[31;1m"  # Ярко-красный
    }

    EMOJIS = {
        logging.DEBUG: "🔍 ",
        logging.INFO: "🚀 ",
        logging.WARNING: "🟡 ",
        logging.ERROR: "❌ ",
        logging.CRITICAL: "🚨 "
    }

    def format(self, record: logging.LogRecord):
        record = copy.copy(record)

        color = self.COLORS.get(record.levelno, "")
        emoji = self.EMOJIS.get(record.levelno, "")

        if color:
            record.levelname = f"{color}{record.levelname}{self.RESET}"

        record.msg = f"{emoji}{record.msg}"

        return super().format(record)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)

        formatter = ColoredFormatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    logger.propagate = False
    return logger
