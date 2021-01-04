qwer = [f'ffff{er}' for er in range(96)]

qwer1 = [
]


def data_from_page(data, page=1, article_limit=10):
    """
    :param data:
    :param page:
    :param article_limit:
    :return:
    """
    max_page = len(data) // article_limit + 1
    print(f'len {len(data)}')
    print(f' max {max_page}')
    print(data[(page-1)*article_limit:page*article_limit])

    return data[(page-1)*article_limit:page*article_limit]


# data_from_page(qwer, page=1)
