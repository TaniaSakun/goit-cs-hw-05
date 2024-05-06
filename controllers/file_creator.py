import os
from faker import Faker
from random import randint, choice

fake = Faker()

extensions = [
    ".txt",
    ".zip",
    ".rar",
    ".jpg",
    ".jpeg",
    ".png",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".pdf",
]


def create_file(path):
    with open(path, "wb") as file:
        file.truncate(randint(100, 10000))


def generate_files(
    path, ext_list=extensions, depth=3, files_per_folder=10
):
    if depth <= 0:
        return

    for _ in range(randint(1, 5)):
        folder_name = fake.word()
        folder_path = os.path.join(path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        for _ in range(randint(files_per_folder // 2, files_per_folder)):
            file_name = fake.word() + choice(ext_list)
            file_path = os.path.join(folder_path, file_name)
            create_file(file_path)

        generate_files(
            folder_path,
            ext_list=ext_list,
            depth=depth - 1,
            files_per_folder=randint(
                files_per_folder // 2, files_per_folder
            ),
        )


def remove_generated_files(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(path)
