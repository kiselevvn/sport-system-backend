import djclick as click
from tqdm import tqdm

from backend.apps.services.services import (  # get_fake_full_female_name,
    DateManager,
    get_fake_email,
    get_fake_full_male_name,
)
from backend.apps.users.services import create_sportsman_service


@click.command()
@click.option("--count", default=3, help="Count created sportsmans")
@click.option("--year", help="Year of birthday")
def command(count, year):

    for i in tqdm(range(0, count)):
        full_name = get_fake_full_male_name()
        fake_email = get_fake_email(full_name)
        birthday = DateManager.random_date_year(year=year)
        fake_data_user = {
            "email": fake_email,
            "username": fake_email,
            "password": "qqqq1111qqqq",
            "birthday": birthday,
            **full_name,
        }
        create_sportsman_service(**fake_data_user)
