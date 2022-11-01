import requests

import requests


def main():
    data = {
        "station": "Station One",
        "lorries": 1,
        "tons": 22,
    }
    post_result = requests.post(url="http://127.0.0.1:6543/passage", json=data)
    post_result.raise_for_status()


if __name__ == '__main__':
    main()