#!/usr/bin/env python3
"""
Follow up formatting after using the hugo to blogger import tool.
All the blogger posts we have written so far do not utilize $$ for display
mathematics, making the parsing a big easier.

Example usage:
bin/blogger_to_hugo.py \
  --src=$HOME/Documents/blogger/posts \
  --tar=$HOME/src/blog/content/post/blogger-mmark
"""
import argparse
from glob import glob
import sys
import os
import re

def fmt(content: str):
    """Convert an Blogger post (previously converted from XML to Markdown) into
    formatted markdown.
    """


    # NOTE: Best to keep it simple, with fewever regexs where possible.
    # inline_dollars_re = re.compile(r'\$.+?\$')
    # inline_parens_re = re.compile(r'\\\(|\\\)')
    re_begin = re.compile(r'\\begin{(equation|align)\*?}')
    re_end = re.compile(r'\\end{(equation|align)\*?}')
    # display_re = re.compile(r'\\begin{(equation|align)\*?}.+?\\end{(equation|align)\*?}')
    # label_re = re.compile(r'\\label{(.*?)}')
    # We never use $$ to delimit display nor do we use $ in latex ,
    # so $...$ always wraps inline math.

    cnt = (
        content
        .replace('blogimport = true', 'markup = "mmark"\nblogimport = true')
        # < and > in latex will cause issues with highlighting. Use \lt.
        .replace('&lt;', '<')
        .replace('&gt;', '>')
        .replace('``', '"')
        .replace("''", '"')
        # .replace(r'\\', '\\\\\n')  # Causes mmark to render code instead of math
        .replace(r'\hat', r'\widehat')  # \hat renders oddly in mathjax
        .replace(r'&amp;', r'&')
        .replace(r'amp;', r'&')
        .replace(r'&nbsp;', ' ')
        .replace('$', '$$')
        .replace(r'\(', '$$')
        .replace(r'\)', '$$')
        .replace(r'\[', r'\begin{equation*}')
        .replace(r'\]', r'\end{equation*}')
        .replace(r"<a name='more'></a>", '\n\n<!--more-->\n\n')
        .replace(r'<br />', '\n')
        .replace(
            '[author]\n\tname = "Shawn O\'Hare"\n\turi = "https://plus.google.com/115904086044687543049"',
            '')
    )
    # cnt = inline_dollars_re.sub(lambda m: r'$' + m.group() + '$', cnt)
    # cnt = inline_parens_re.sub(r'$$', cnt)
    # cnt = display_re.sub(lambda m: '\n\n$$' + m.group() + '$$\n\n', cnt)
    cnt = re_begin.sub(lambda m: '\n\n$$' + m.group() + '\n', cnt)
    cnt = re_end.sub(lambda m: '\n' + m.group() + '$$\n\n', cnt)
    # cnt = label_re.sub(lambda m: m.group() + '\n', cnt)

    return cnt


def fmt_file(path: str, tar: str):
    filename = os.path.basename(path)
    print('Formatting {}'.format(path))
    with open(path, 'r') as original:
        with open(os.path.join(tar, filename), 'w') as formatted:
            formatted.write(fmt(original.read()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Format blogger-to-hugo imports")
    parser.add_argument(
        '--src',
        required=True,
        help='Directory containing exported files to format.'
    )
    parser.add_argument(
        '--tar',
        required=True,
        help='Output directory.'
    )
    parser.add_argument(
        '--files',
        default='*.md',
        help='Pattern of files to format.'
    )
    args = parser.parse_args()

    if not os.path.exists(args.src):
        raise ValueError('Input directory {} does not exist.'.format(args.src))
    if not os.path.exists(args.tar):
        os.mkdir(args.tar)

    for path in glob(os.path.join(args.src, args.files)):
        fmt_file(path, args.tar)
