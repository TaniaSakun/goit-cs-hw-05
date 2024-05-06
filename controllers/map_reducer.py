from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict
from controllers.data_processor import DataProcessor


class MapReducer:
    @staticmethod
    def map_function(word):
        return word, 1

    @staticmethod
    def shuffle_function(mapped_values):
        shuffled = defaultdict(list)
        for key, value in mapped_values:
            shuffled[key].append(value)
        return shuffled.items()

    @staticmethod
    def reduce_function(key_values):
        key, values = key_values
        return key, sum(values)

    @staticmethod
    def map_reduce(text, search_words=None):
        text = DataProcessor.remove_punctuation(text)
        words = text.split()

        if search_words:
            words = [word for word in words if word in search_words]

        with ThreadPoolExecutor() as executor:
            mapped_values = list(executor.map(MapReducer.map_function, words))

        shuffled_values = MapReducer.shuffle_function(mapped_values)

        with ThreadPoolExecutor() as executor:
            reduced_values = list(
                executor.map(MapReducer.reduce_function, shuffled_values)
            )

        return dict(reduced_values)
