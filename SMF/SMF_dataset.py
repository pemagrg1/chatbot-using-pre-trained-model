#!/usr/bin/env python
#  coding=utf-8
#  Copyright (c) Microsoft Corporation.
#  Licensed under the MIT license.

"""Corpus for SMF"""

import datasets
import jsonlines


_DESCRIPTION = """\
SMF
"""

_CITATION = """\
SMF
"""

_WEBPAGE = ""


class SMF(datasets.GeneratorBasedBuilder):
    """SMF"""

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "Context": datasets.Value("string"),
                    "Response": datasets.Value("string"),
                    "Knowledge": datasets.Value("string"),
                }
            ),
            homepage=_WEBPAGE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):

        train_path = 'json_data/train_music_feat.jsonl'
        validation_path = 'json_data/test_music_feat.jsonl'
        test_path = 'json_data/test_music_feat.jsonl'
        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={
                                    "filepath": train_path}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={
                                    "filepath": validation_path}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={
                                    "filepath": test_path}),
        ]

    def _generate_examples(self, filepath):

        key = 0
        with open(filepath, "r", encoding="utf-8") as reader:

            for item in jsonlines.Reader(reader):
                yield key, item
                key += 1
