import asyncio
import argparse

from aiopath import AsyncPath
from aioshutil import copyfile
from utilities.logger import Logger
from utilities.constants import Constants

logger = Logger()


def get_args():
    parser = argparse.ArgumentParser(description=Constants.sort_files)
    parser.add_argument(
        "-s", "--source", default="test_folder", help=Constants.source_path
    )
    parser.add_argument("-t", "--target", default="target", help=Constants.target_path)
    return parser.parse_args()


async def read_folder(source: AsyncPath):
    all_files = []
    async for path in source.iterdir():
        if await path.is_file():
            all_files.append(path)
        else:
            all_files.extend(await read_folder(path))
    return all_files


async def gather_files(files, target: AsyncPath):
    tasks = []
    for file in files:
        new_path = target / file.name
        tasks.append(copyfile(file, new_path))
    await asyncio.gather(*tasks)


async def copy_files():
    args = get_args()
    source = AsyncPath(args.source)
    target = AsyncPath(args.target)

    # Ensure target directory exists
    await target.mkdir(parents=True, exist_ok=True)

    files = await read_folder(source)
    await gather_files(files, target)
