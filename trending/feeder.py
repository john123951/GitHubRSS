#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Dict

from feedgen.feed import FeedGenerator


def generate_rss(trending_list: List[Dict]) -> str:
    # feed generator
    feed_generator = FeedGenerator()
    feed_generator.title('GitHub Trending')
    feed_generator.generator('GithubRSS')
    feed_generator.link(href='http://john123951.github.io/GitHubRSS', rel='alternate')
    feed_generator.description('Daily Trending of GitHub')

    trending_list.reverse()

    host = 'https://www.github.com{}'

    for index, project in enumerate(trending_list):
        f_item = feed_generator.add_item()
        f_item.title(project['projectName'])
        f_item.link(href=host.format(project['link']))
        f_item.description(project['desc'])

    # feed_generator.atom_file('atom.xml')  # Write the ATOM feed to a file
    # feed_generator.rss_file('rss.xml')  # Write the RSS feed to a file

    # Generate the RSS feed as a string
    rss_feed = feed_generator.rss_str(pretty=True)
    if isinstance(rss_feed, bytes):
        rss_feed = rss_feed.decode('utf-8')
    return rss_feed
