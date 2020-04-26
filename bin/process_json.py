#!/usr/bin/env bash
# -*- coding: utf-8 -*-
import argparse
import json
import logging
from configparser import ConfigParser
from pathlib import Path
from typing import Iterable, TextIO
from datetime import datetime as dt, timedelta as td

import pandas as pd

log = logging.getLogger(__name__)
config = ConfigParser()


class FileProcessor():
    def __init__(self, *inputs: TextIO):
        self.inputs = inputs

    def extract(self, *args: TextIO) -> Iterable[dict]:
        for arg in args:
            log.info(f"{arg=}")
            for i in arg.readlines():
                yield json.loads(i)

    def transform(self, *args: dict) -> Iterable[dict]:
        for arg in args:
            log.debug(f'{arg=}')
            yield from pd.json_normalize(arg).to_dict(orient='records')

    def load(self, *args: dict) -> None:
        print(json.dumps(args, indent=2))

    def process(self) -> None:
        self.load(*self.transform(*self.extract(*self.inputs)))


def run(*paths, loglevel='warning'):
    logging.basicConfig(
        level=getattr(logging, loglevel.upper()),
        format='[%(levelname)s %(asctime)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    log.info('start=%s' % (start:=dt.now()))
    processor = FileProcessor(*paths)
    processor.process()
    log.info('duration=%s' % (dt.now() - start))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--loglevel", choices={"info", "debug", "warning"}, default="warning"
    )
    parser.add_argument("path", nargs="+", type=argparse.FileType('r'))
    args = parser.parse_args()
    run(*args.path, loglevel=args.loglevel)


if __name__ == "__main__":
    main()
