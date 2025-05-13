from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    twilio_account_id: str = ""
    twilio_auth_token: str = ""
    twilio_from_phone: str = ""
    thegame_use_sample: bool = True
    thegame_sample_language: str = "es"
    thegame_message_file: str = "./messages.txt"
    thegame_phone_list: str = "./phone_list.txt"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

