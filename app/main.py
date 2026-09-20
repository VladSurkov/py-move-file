import os


def move_file(command: str) -> None:
    try:
        [cmd, file_to_move, place_to_move] = command.split()

        if cmd != "mv":
            raise ValueError
    except ValueError:
        print("Invalid command")
        raise

    parts_of_path = place_to_move.split("/")
    new_file_name = parts_of_path[-1]

    try:
        if len(parts_of_path) == 1:
            os.rename(file_to_move, new_file_name)
            return

        base_path = os.getcwd()
        path_to_move = os.path.join(base_path, *parts_of_path[:-1])

        os.makedirs(path_to_move, exist_ok=True)

        with (
            open(file_to_move, "r") as file,
            open(os.path.join(path_to_move, new_file_name), "w") as new_file
        ):
            new_file.write(file.read())

        os.remove(file_to_move)
    except FileExistsError:
        raise
