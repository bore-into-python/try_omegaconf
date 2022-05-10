from config import config

def main():
    print(f"Main: {config.the_host = }")
    print(f"Main: {config.dude = }")

    print(f"{config.unity.password}")


if __name__ == "__main__":
    main()

