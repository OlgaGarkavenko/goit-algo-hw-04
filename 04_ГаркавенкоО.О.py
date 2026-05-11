import os
import shutil
import argparse


# Ex 1
def create_test_data(base_path: str):

    try:
        os.makedirs(base_path, exist_ok=True)

        # Створюємо вкладені папки
        folder1 = os.path.join(base_path, "folder1")
        folder2 = os.path.join(base_path, "folder2")

        os.makedirs(folder1, exist_ok=True)
        os.makedirs(folder2, exist_ok=True)

        # Файли в головній папці
        files_main = {
            "a.txt": "Hello text file",
            "image.jpg": "fake image content",
            "doc.pdf": "fake pdf content",
        }

        # Файли в folder1
        files_folder1 = {
            "x.txt": "inside folder1",
            "y.png": "fake png",
        }

        # Файли в folder2
        files_folder2 = {
            "z.mp3": "fake music",
        }

        def write_files(folder, files_dict):
            for name, content in files_dict.items():
                path = os.path.join(folder, name)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

        write_files(base_path, files_main)
        write_files(folder1, files_folder1)
        write_files(folder2, files_folder2)

        print(f"Тестові файли створено в: {base_path}")

    except Exception as e:
        print(f"Помилка створення тестових даних: {e}")


def copy_and_sort_files(source_dir: str, dest_dir: str):
    try:
        for entry in os.listdir(source_dir):
            source_path = os.path.join(source_dir, entry)

            if os.path.isdir(source_path):
                copy_and_sort_files(source_path, dest_dir)

            elif os.path.isfile(source_path):
                _, ext = os.path.splitext(entry)
                ext = ext[1:] if ext else "no_extension"

                target_folder = os.path.join(dest_dir, ext)
                os.makedirs(target_folder, exist_ok=True)

                target_path = os.path.join(target_folder, entry)
                shutil.copy2(source_path, target_path)

                print(f"Скопійовано: {source_path} -> {target_path}")

    except Exception as e:
        print(f"Помилка: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("dest", nargs="?", default="dist")

    args = parser.parse_args()

    source_dir = os.path.abspath(args.source)
    dest_dir = os.path.abspath(args.dest)

    # створення тестових файлів 
    create_test_data(source_dir)

    os.makedirs(dest_dir, exist_ok=True)

    copy_and_sort_files(source_dir, dest_dir)

    print("Готово!")


if __name__ == "__main__":
    main()

