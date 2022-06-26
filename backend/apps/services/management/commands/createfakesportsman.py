import djclick as click
from tqdm import tqdm
from backend.apps.services.services import (
    # get_fake_full_female_name,
    get_fake_full_male_name,
    get_fake_email,
)
from backend.apps.users.services import create_sportsman_service


@click.command()
@click.option("--count", default=3, help="Count created sportsmans")
def command(count):

    for i in tqdm(range(0, count)):
        full_name = get_fake_full_male_name()
        fake_email = get_fake_email(full_name)

        fake_data_user = {
            "email": fake_email,
            "username": fake_email,
            "password": "qqqq1111qqqq",
            **full_name,
        }
        create_sportsman_service(**fake_data_user)
