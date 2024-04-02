# from .helpers.fake_data import MAILBOX_NAMES
import random

from .helpers import id_generator, string_translit
from .helpers.fake_data import MAILBOX_NAMES


def get_fake_email(full_name: dict):
    """
    Возвращает рандомное ФИО
    """
    name = (
        f"{full_name['first_name']}"
        + f"{full_name['last_name']}"
        + f"{full_name['first_name']}"
    )
    translit_name = string_translit(name).replace("'", "")
    public_salt = id_generator()
    mailbox_name = random.choice(MAILBOX_NAMES)
    fake_email = f"{translit_name}" + f"{public_salt}" + f"@{mailbox_name}"
    return fake_email
