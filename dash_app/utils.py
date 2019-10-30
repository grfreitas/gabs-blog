import dash_html_components as html

import os
import importlib


def get_content():
    posts = os.listdir('pages/posts')

    for post in posts:
        post = post.split('.')[0]
        content = importlib.import_module('pages.posts.' + post)

        author = content.author
        title = content.title
        date = content.date

    return [html.P(posts)]
