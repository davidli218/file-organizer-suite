import os
import sys

from typing import List

script_name = "Remove Mac .DS_Store"

script_ascii_art = r"""
   ____     U _____ u   __  __      U  ___ u  __     __   U _____ u       __  __       _         ____
U |  _"\ u  \| ___"|/ U|' \/ '|u     \/"_ \/  \ \   /"/u  \| ___"|/     U|' \/ '|u U  /"\  u  U /"___|
 \| |_) |/   |  _|"   \| |\/| |/     | | | |   \ \ / //    |  _|"       \| |\/| |/  \/ _ \/   \| | u
  |  _ <     | |___    | |  | |  .-,_| |_| |   /\ V /_,-.  | |___        | |  | |   / ___ \    | |/__
  |_| \_\    |_____|   |_|  |_|   \_)-\___/   U  \_/-(_/   |_____|       |_|  |_|  /_/   \_\    \____|
  //   \\_   <<   >>  <<,-,,-.         \\       //         <<   >>      <<,-,,-.    \\    >>   _// \\
 (__)  (__) (__) (__)  (./  \.)       (__)     (__)       (__) (__)      (./  \.)  (__)  (__) (__)(__)
      ____      ____     _  ____       _____      U  ___ u    ____     U _____ u
     |  _"\    / __"| u    / __"| u   |_ " _|      \/"_ \/ U |  _"\ u  \| ___"|/
    /| | | |  <\___ \/    <\___ \/      | |        | | | |  \| |_) |/   |  _|"
    U| |_| |\  u___) |     u___) |     /| |\   .-,_| |_| |   |  _ <     | |___
 _   |____/ u  |____/>>    |____/>>   u |_|U    \_)-\___/    |_| \_\    |_____|
(")   |||_      )(  (__)    )(  (__)  _// \\_        \\      //   \\_   <<   >>
 "   (__)_)    (__)        (__)      (__) (__)      (__)    (__)  (__) (__) (__)
"""


def find_ds_store(dest_dir: str) -> List[str]:
    dest_paths = []

    for parent, dir_names, file_names in os.walk(dest_dir):
        for filename in file_names:
            if filename == ".DS_Store":
                dest_paths.append(os.path.join(parent, filename))

    return dest_paths


def print_task(dest_paths: List[str]) -> None:
    print("The following files will be REMOVED:\n")

    for file_path in dest_paths:
        print(file_path)

    print("\n")


def remove_files(dest_paths: List[str]) -> None:
    for file_path in dest_paths:
        os.remove(file_path)


def init_app():
    print(script_ascii_art)

    if len(sys.argv) != 2:
        print(f"[{script_name}] The script takes one parameter\n")
        exit(-1)

    if not os.path.isdir(sys.argv[1]):
        print(f"[{script_name}] ArgIn<{sys.argv[1]}> isn't a dir\n")
        exit(-1)


def app(dest_dir: str) -> None:
    init_app()

    status = 0

    dest_paths = find_ds_store(dest_dir)

    if len(dest_paths) > 0:
        print_task(dest_paths)

        while (choice := input("Proceed ([y]/n)? ")).upper() not in ('Y', 'N', ''):
            print(f"Invalid choice: {choice}")

        if choice.upper() != 'N':
            remove_files(dest_paths)
        else:
            status += 1

    print(f"\n[{script_name}] {'All Done!' if status == 0 else 'Exiting.'}\n")


if __name__ == '__main__':
    app(sys.argv[1])
