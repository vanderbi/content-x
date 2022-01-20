#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Converts files markdown files in md/ to html files in html/

:Mod: main.py

:Author:
    Colin Smith

:Created:
    1/1/22
"""

import markdown
from markdown.extensions.toc import TocExtension
import os


def convert_md_to_html(md: str, html: str):
    """
    Convert markdown files to html files

    :param md: Path to directory of markdown files
    :param html: Path to directory of html files
    """
    files = os.listdir(md)
    for file in files:
        with open(md + file, 'r') as f:
            text = f.read()
            res = markdown.markdown(text, extensions=[TocExtension(marker='[TOC]', toc_depth='2-6')])
        with open(html + os.path.splitext(file)[0] + '.html', 'w') as f:
            f.write(res)


def main():
    convert_md_to_html("md/", "html/")
    return 0


if __name__ == '__main__':
    main()
