#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from typing import List, Dict

from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy


async def github_trending_crawler(proxy=None, verbose=True) -> List[Dict]:
    # Define the extraction schema
    schema = {
        "name": "Github Trending Projects",
        "baseSelector": "div.Box article",
        "fields": [
            {
                "name": "projectName",
                "selector": "article>h2.h3",
                "type": "text",
            },
            {
                "name": "desc",
                "selector": "article>p",
                "type": "text",
            },
            {
                "name": "language",
                "selector": '[itemprop="programmingLanguage"]',
                "type": "text",
            },
            {
                "name": "stars",
                "selector": "article .mt-2>a:nth-of-type(1)",
                "type": "text",
            },
            {
                "name": "todayStars",
                "selector": "article .float-sm-right",
                "type": "text",
            },
            {
                "name": "forks",
                "selector": "article .mt-2>a:nth-of-type(2)",
                "type": "text",
            },
            {
                "name": "link",
                "selector": "article h2>a[href]",
                "type": "attribute",
                "attribute": "href"
            }
        ],
    }

    extraction_strategy = JsonCssExtractionStrategy(schema, verbose=verbose)

    async with AsyncWebCrawler(verbose=verbose, proxy=proxy) as crawler:
        result = await crawler.arun(
            url="https://github.com/trending",
            extraction_strategy=extraction_strategy,
            bypass_cache=True,
        )

        assert result.success, "Failed to crawl the page"

        projects = json.loads(result.extracted_content)
        print(f"Successfully extracted {len(projects)} github trending")
        print(json.dumps(projects, indent=2, ensure_ascii=False))

        return projects