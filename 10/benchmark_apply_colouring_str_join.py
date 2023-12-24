from enum import Enum
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


diff_strings = [generate_diff_string(i) for i in range(10)]


class Style(Enum):
    white = 0
    green = 1
    red = 2
    blue = 3


class AnsiColour(Enum):
    red = 31
    green = 32
    blue = 34
    white = 37
    reset = 39


def name2ansi(name: str):
    ansi_int = AnsiColour[name].value
    return f"\033[{ansi_int}m"


style2ansi: dict[int, int] = {style.value: name2ansi(style.name) for style in Style}
reset_ansi = name2ansi("reset")
reset_ansi_b = reset_ansi.encode()

colour_lookup = {
    " ": Style.white.value,
    "+": Style.green.value,
    "-": Style.red.value,
}
ansi_lookup = {
    symbol: style2ansi[style_code] for symbol, style_code in colour_lookup.items()
}


def apply_colouring_str_join(source_text: list[str]) -> str:
    """Apply the string join on all elements at once, no intermediate mapping"""
    all_lines = []
    for diff in source_text:
        lines = []
        source_lines = diff.splitlines(keepends=True)
        for line in source_lines:
            lines.extend([ansi_lookup[line[0]], line, reset_ansi])
        all_lines.extend(lines)
    return "".join(all_lines)


def main():
    result = apply_colouring_str_join(diff_strings)
    print(result, file=stderr)


main()
