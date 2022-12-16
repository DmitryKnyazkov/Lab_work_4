import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = r"""####\s(?P<position>\d+?)\.\s\[(?P<Book>.+?)\]\((?P<book_url>https://amzn.+?)\).+?by\s+(?P<author>.+?)\s\((?P<recommended>\d\d?\.\d?%).+?\(((?P<cover_url>https://www.daolf.com/images/python_book_list/\d\d?.png#center)).+?(?P<description>\".+?\")"""
#r"""\s(?P<position>\d+?)\.\s\[(?P<Book>.+?)\].+?(?P<book_url>https://amzn.+?)\).+?by\s+(?P<author>\w+\s\w+)\s\((?P<recommended>\d\d?\.\d?%)"""

# поиск позиции r"""####\s(?P<position>\d+?)\.\s\["""
# поиск названия книги r"""\.\s\[(?P<Book>.+?)\]"""
# поиск сайта r"""(?P<book_url>https://amzn.+?)\).+?"""
# поиск авторов r"""by\s(?P<author>(?:\w+\s\w+(?:\'\w+)?(?:\s&\s)?)+)\s\("""   второй вариант by\s+(?P<author>.+?)\(
# поиск рекомендаций r"""\s\((?P<recommended>\d\d?\.\d?%)"""
# поиск обложки r"""((?P<cover_url>https://www.daolf.com/images/python_book_list/\d\d?.png#center))"""
# поиск описания r"""\".+?\""""

def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        list_ = []
        for book in book_pattern.finditer(f.read()):
            book_dict = book.groupdict()
            #print(book_dict)

            list_.append(book_dict)
        list_s = sorted(list_, key=lambda x: int(x["position"]))

        print(json.dumps(list_s, indent=4))


if __name__ == '__main__':
    task()
