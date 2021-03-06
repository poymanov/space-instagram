import requests
import os
from os.path import join as joinpath

IMAGES_PATH = os.environ['IMAGES_PATH']
SPACEX_URL = 'https://api.spacexdata.com/v3/launches/latest'
HUBBLE_COLLECTIONS_URL = 'http://hubblesite.org/api/v3/images/{}'
HUBBLE_IMAGE_URL = 'http://hubblesite.org/api/v3/image/{}'


def collect():
    collect_spacex()
    # collect_hubble()


def collect_spacex():
    response = requests.get(SPACEX_URL)

    if not response.ok:
        return None

    json_data = response.json()

    if 'links' not in json_data or 'flickr_images' not in json_data['links']:
        return None

    images = json_data['links']['flickr_images']

    for i, item in enumerate(images):
        filename = 'spacex{}{}'.format(i + 1, get_file_extension(item))
        save_image(item, filename)


def collect_hubble():
    collections_response = requests.get(HUBBLE_COLLECTIONS_URL.format('news'))

    if not collections_response.ok:
        return None

    for image_item in collections_response.json():
        image_response = requests.get(HUBBLE_IMAGE_URL.format(image_item['id']))

        if not image_response.ok:
            continue

        image_data = image_response.json()

        if 'image_files' not in image_data or not len(image_data['image_files']):
            continue

        image = image_data['image_files'][-1]

        if 'file_url' not in image:
            continue

        image_url = 'http:{}'.format(image['file_url'])
        filename = 'hubble{}{}'.format(image_item['id'], get_file_extension(image_url))
        save_image(image_url, filename)


def save_image(url, filename):
    save_path = joinpath(IMAGES_PATH, filename)
    response = requests.get(url)
    os.makedirs(IMAGES_PATH, exist_ok=True)

    with open(save_path, 'wb') as file:
        file.write(response.content)


def get_file_extension(path):
    return os.path.splitext(path)[1]
