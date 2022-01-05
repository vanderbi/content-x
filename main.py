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

def convert_md_to_html(md, html):
    """
    Convert markdown files to html files

    :param md: Path to directory of markdown files
    :param html: Path to directory of html files
    :return: html files written to html
    """
    files = os.listdir(md)
    for file in files:
        f = open(md + file, 'r')
        text = f.read()
        # res = markdown.markdown(text)
        res = markdown.markdown(text, extensions=[TocExtension(marker='[TOC]', toc_depth='2-6')])
        f.close()
        f = open(html + os.path.splitext(file)[0] + '.html', 'w')
        f.write(res)
        f.close()

convert_md_to_html("md/", "html/")

