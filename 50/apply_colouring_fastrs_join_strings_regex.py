from sys import stderr

import fastrs


def generate_diff_string(i):
    line_string = ", ".join(["hello world"] * 5)
    dozen_lines = [line_string] * 12
    for j, l in enumerate(dozen_lines):
        # Introducing 'i' in the match pattern to create variations
        match (j + i) % 10:
            case 0 | 7 | 8:
                prefix = "-"
            case _ if (j + i) in range(2, 6):
                prefix = "+"
            case _:
                prefix = " "
        dozen_lines[j] = f"{prefix}{l}\n"

    return "".join(dozen_lines)


diff_strings = [generate_diff_string(i) for i in range(50)]


def apply_colouring_fastrs_join_strings_regex(source_text: list[str]) -> str:
    """Apply the string join on all elements at once, no intermediate mapping"""
    return fastrs.colour_strings_regex(source_text)


def main():
    result = apply_colouring_fastrs_join_strings_regex(diff_strings)
    print(result, file=stderr)


main()
