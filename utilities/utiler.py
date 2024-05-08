import argparse
import matplotlib.pyplot as plt

from random import randint
from controllers.folder_copier import copy_files
from utilities.constants import Constants
from utilities.logger import Logger
from controllers.data_processor import DataProcessor
from controllers.map_reducer import MapReducer
from controllers.file_creator import generate_files, remove_generated_files

source_path = "./test_folder"
target_path = "./dist"
logger = Logger()


def parse_args():
    try:
        parser = argparse.ArgumentParser(description=Constants.sort_files)
        parser.add_argument(
            "-s", "--source", default=source_path, help=Constants.source_path
        )
        parser.add_argument(
            "-t", "--target", default=target_path, help=Constants.target_path
        )
        return parser.parse_args()
    except Exception as e:
        logger.error(e)


async def first_task(path):
    generate_files(path, depth=3, files_per_folder=randint(10, 20))

    logger.config()
    await copy_files()
    logger.info(Constants.all_files_sorted)

    remove_generated_files(path)


def visualize_top_words(result, n=10):
    top_words = sorted(result.items(), key=lambda x: x[1], reverse=True)[:n]
    plt.figure(figsize=(10, 6))
    plt.barh(
        [word[0] for word in top_words],
        [word[1] for word in top_words],
        color=Constants.sky_blue,
    )
    plt.xlabel(Constants.frequency_axis_label)
    plt.ylabel(Constants.word_axis_label)
    plt.title(Constants.table_title.format(n))
    plt.gca().invert_yaxis()
    plt.show()


def second_task():
    url = Constants.wiki_url
    text = DataProcessor.get_text(url)

    if text:
        result = MapReducer.map_reduce(text)
        print(Constants.successfully_loaded_text.format(url))
        visualize_top_words(result)

    else:
        print(Constants.failure_loaded_text.format(url))
