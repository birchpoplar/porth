
def lex_line:

    return []


def lex_file(file_path):
    with open(file_path, "r") as f:
        [(file_path, row, col, token)
         for (row, line) in enumerate(f.readlines())
         for (col, token) in lex_line(line)]
