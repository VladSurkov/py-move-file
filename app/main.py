import os


def move_file(command: str) -> None:
    [cmd, file_to_move, place_to_move] = command.split()
    folders = place_to_move.split("/")
    new_file_name = folders[-1]

    if cmd == "mv":
        try:
            with open(file_to_move, "r") as file:
                if len(folders) > 1:
                    if not os.path.isdir(folders[0]):
                        for index in range(0, len(folders) - 1):
                            os.mkdir(folders[index])
                            os.chdir(folders[index])
                    else:
                        os.chdir(folders[0])

                        for index in range(1, len(folders) - 1):
                            if os.path.isdir(folders[index]):
                                os.chdir(folders[index])
                            else:
                                os.mkdir(folders[index])
                                os.chdir(folders[index])

                    with open(new_file_name, "w") as new_file:
                        new_file.write(file.read())

                    for _ in range(0, len(folders) - 1):
                        os.chdir("..")

                    os.remove(file_to_move)
                else:
                    os.rename(file_to_move, new_file_name)
        except FileExistsError:
            raise
    else:
        print(f"Unknown command {cmd}")
