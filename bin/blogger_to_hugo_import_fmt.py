#!/usr/bin/env python3
"""
Follow up formatting after using the hugo to blogger import tool.
All the blogger posts we have written so far do not utilize $$ for display
mathematics, making the parsing a big easier.
"""
import argparse
from glob import glob
import sys
import os
import re


# Compiled regex that match environments.
begin_re = re.compile(r'\\begin{(.*?)}')
end_re = re.compile(r'\\end{(.*?)}')


def begin_sub(match):
    return '\n\n{{< display >}}\n```\n' + match.group() + '\n\n'


def end_sub(match):
    return match.group() + '\n```\n{{< /display >}}\n'


def fmt(content: str):
    content = (
        content
        .replace(r"<a name='more'></a>", '\n\n<!--more-->')
        .replace(r'<br />', '\n')
        .replace(r'\[', '\n\n{{< display >}}\n```\n\\[\n')
        .replace(r'\]', '\n\\]\n```\n{{< /display >}}\n\n')
        .replace(r'\(', '{{< inline "`\\( ')
        .replace(r'\)', '\\)`"')
    )
    # content = begin_re.sub(begin_sub, content)
    # content = end_re.sub(end_sub, content)

    # Replace inline math with inline shortcode.
    formatted = []
    left = True
    for sym in content:
        if sym == '$':
            sym = '{{< inline "`\\( ' if left else ' \\)`" }}>'
            left = not left
        formatted.append(sym)
    return ''.join(formatted)


def fmt_file(path: str):
    basedir, filename = os.path.split(path)
    print('Formatting {}'.format(path))
    with open(path, 'r') as original:
        formatted_content = fmt(original.read())
    with open(os.path.join(basedir, 'formatted', filename), 'w+') as formatted:
        formatted.write(formatted_content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Format blogger-to-hugo imports")
    parser.add_argument(
        'dir',
        help='Directory containing exported files to format.'
    )
    parser.add_argument(
        '--files',
        default='*.md',
        help='Pattern of files to format.'
    )
    args = parser.parse_args()

    if not os.path.exists(args.dir):
        raise ValueError('Input dir does not exist.')
    formatted_dir = os.path.join(os.path.join(args.dir, 'formatted'))
    if not os.path.exists(formatted_dir):
        os.mkdir(formatted_dir)

    for path in glob(os.path.join(args.dir, args.files)):
        fmt_file(path)
