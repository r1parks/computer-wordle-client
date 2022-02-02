#!/usr/bin/env python3

import requests
from urllib.parse import urljoin

BASE_URL = 'https://wordle.bobparks.info'
BASE_URL = 'http://localhost:8080'


def start_new_game():
    url = urljoin(BASE_URL, 'new/')
    response = requests.get(url)
    print(str(response))
    return response.json()


def get_game_status(game_id):
    url = urljoin(BASE_URL, f'status/{game_id}/')
    response = requests.get(url)
    return response.json()


def make_guess(game_id, guess):
    url = urljoin(BASE_URL, 'guess/')
    json_data = {'game_id': game_id, 'guess': guess}
    response = requests.post(url, json=json_data)
    return response.json()
