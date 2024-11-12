from environs import Env
from dataclasses import dataclass

@dataclass
class Bots:
    bot_token: str
    admin_id: int
    href_apartment_price_prediction: str
    href_business_card: str

@dataclass
class Settings:
    bots: Bots

def get_settings(path: str):
    env = Env()
    env.read_env()
    # env.read_env(path)
    print()
    return Settings(
        bots=Bots(
            bot_token=env.str('TOKEN'),
            admin_id=env.int('ADMIN_ID'),
            href_apartment_price_prediction=env.str('WEB_APP_APARTMENT_PRICE_PREDICTION'),
            href_business_card=env.str('WEB_APP_BUSINESS_CARD')
        )
    )

settings = get_settings('.env')
print(settings)