import json
from dataclasses import asdict


class Serializer:

    @staticmethod
    def save(song, filename):

        with open(
            filename,
            "w"
        ) as f:

            json.dump(
                asdict(song),
                f,
                indent=4
            )