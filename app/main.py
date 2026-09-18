import configparser
from pathlib import Path


def load_config():
    config_file = Path(__file__).parent.parent / "config" / "app.config"

    config = configparser.ConfigParser()
    config.read(config_file)

    return config


def main():
    config = load_config()

    app_name = config["application"]["name"]
    environment = config["application"]["environment"]
    log_level = config["application"]["log_level"]

    print(f"Application: {app_name}")
    print(f"Environment: {environment}")
    print(f"Log Level: {log_level}")


if __name__ == "__main__":
    main()
