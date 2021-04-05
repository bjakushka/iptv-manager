from abc import ABC, abstractmethod
import urllib.request
import random
import uuid


class BaseSeeder(ABC):
    """Base-class for all db-seeders"""

    def __init__(self, db):
        self.db = db

    def run(self, *args, **kwargs):
        self._execute(*args, **kwargs)

    @abstractmethod
    def _execute(self, *args, **kwargs):  # pragma: no cover
        """Main method, which will be run to execute

        :param list args:
        :param dict kwargs:
        """
        pass


class RandomDataGenerator:
    """Seed database with demo data"""

    _words_source_url = 'https://www.mit.edu/~ecprice/wordlist.10000'
    _words_list = []
    _maxint = 100000

    @classmethod
    def get_random_sentence(cls, min_words=2, max_words=3):
        """Returns sentence with random amount of words.

        :param int min_words:
        :param int max_words:
        :rtype: str
        """
        amount_of_words = random.randint(min_words, max_words)
        words = [cls.get_random_word().capitalize() for __ in
                 range(amount_of_words)]

        return ' '.join(words)

    @classmethod
    def get_random_word(cls):
        """Returns one random word from the list.

        :rtype: str
        """
        possible_words = cls._get_words_list()
        random_index = random.randint(0, len(possible_words) - 1)
        return possible_words[random_index]

    @staticmethod
    def get_random_url(url_base='https://site.example/'):
        """Returns random URL

        :rtype: str
        """
        part1 = (uuid.uuid4()).hex
        part2 = (uuid.uuid4()).hex + (uuid.uuid4()).hex

        return f'{url_base}{part1}/{part2}.m3u'

    @classmethod
    def get_random_bool(cls, divider=2):
        """Returns random boolean value

        Parameter `divider` can be used to specify frequency

        :param int divider:
        :rtype: bool
        """
        return round(random.randint(0, cls._maxint) % divider, 0) == 0

    @classmethod
    def _get_words_list(cls):
        """Returns list of loaded words.

        :rtype: list
        """
        if len(cls._words_list) == 0:
            cls._words_list = cls._load_words_from_url(
                cls._words_source_url
            )

        return cls._words_list

    @staticmethod
    def _load_words_from_url(url):
        """Loads list of words from the Internet and returns list.

        :param str url: URL to source with words
        :rtype: list
        """
        response = urllib.request.urlopen(url)
        words_text = response.read().decode()
        return words_text.splitlines()
