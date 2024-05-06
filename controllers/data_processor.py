import requests
import string


class DataProcessor:
    @staticmethod
    def get_text(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException:
            return None

    @staticmethod
    def remove_punctuation(text):
        return text.translate(str.maketrans("", "", string.punctuation))
