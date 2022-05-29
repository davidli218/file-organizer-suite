import os
import sys

from typing import List, Tuple

script_name = "Remove Mac ._"

script_ascii_art = r"""
                 .-'''-.                             
_______         '   _    \                           
\  ___ `'.    /   /` '.   \                          
 ' |--.\  \  .   |     \  '                          
 | |    \  ' |   '      |  '  .|                     
 | |     |  '\    \     / / .' |_                    
 | |     |  | `.   ` ..' /.'     |                   
 | |     ' .'    '-...-'`'--.  .-'                   
 | |___.' /'                |  |                     
/_______.'/                 |  |   ________________  
\_______|/                  |  '.'|________________| 
                U _____ u   |   /                                                                                    
                \| ___"|/   `'-'                               
   ____   _      |  _|"      _      _   _     
U /"___| |"|     | |___  U  /"\  u | \ |"|    
\| | u U | | u   |_____|  \/ _ \/ <|  \| |>   
 | |/__ \| |/__  <<   >>  / ___ \ U| |\  |u   
  \____| |_____|(__) (__)/_/   \_\ |_| \_|    
 _// \\  //  \\           \\    >> ||   \\,-. 
(__)(__)(_")("_)         (__)  (__)(_")  (_/  

"""


def find_dot_(dest_dir: str) -> List[Tuple[str, str]]:
    dot_file_pairs = []

    for parent, dir_names, file_names in os.walk(dest_dir):
        for filename in file_names:
            if len(filename) > 3 and filename[:2] == '._':
                dot_file_pairs.append(
                    (os.path.join(parent, filename),
                     os.path.join(parent, filename[2:]))
                )

    return dot_file_pairs


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


def app(dest_dir: str):
    init_app()

    dot_file_pairs = find_dot_(dest_dir)

    status = 0
    scheduled_dot_files = []
    suspected_dot_files = []

    if len(dot_file_pairs) > 0:
        for dot_file, org_file in dot_file_pairs:
            if os.path.exists(org_file):
                scheduled_dot_files.append(dot_file)
            else:
                suspected_dot_files.append(dot_file)

        print("The following files will be REMOVED:\n")
        for file in scheduled_dot_files:
            print('&/' + os.path.relpath(file, dest_dir))
        print()

        while (choice := input("Proceed ([y]/n)? ")).upper() not in ('Y', 'N', ''):
            print(f"Invalid choice: {choice}")

        if choice.upper() != 'N':
            remove_files(scheduled_dot_files)
        else:
            status += 1

        print("\n\n[Suspected Files]")
        for file in suspected_dot_files:
            print('&/' + os.path.relpath(file, dest_dir))

    print(f"\n[{script_name}] {'All Done!' if status == 0 else 'Exiting.'}\n")


if __name__ == '__main__':
    app(sys.argv[1])
