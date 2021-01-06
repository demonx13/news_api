# info_data = [f"post#{ i }" for i in range(99)]

def data_from_page(data, page=1, article_limit=10):
    """
    """
    if page == 0:
        page = 1
    max_page = len(data) // article_limit + 1
    if max_page < page:
        return []

    # print(f'len {len(data)}')
    # print(f' max {max_page}')
    # print(data[(page-1)*article_limit:page*article_limit])
    return data[(page-1)*article_limit:page*article_limit]


def value_validator(value):
    """check value for int type
    """
    try:
        val = int(value)
        val = 1 if val < 1 else val
    except Exception as ex:
        val = 1
    return val


def value_validator_news(value):
    """check value for int type
    """
    try:
        val = int(value)
        return True if val > 0 else False
    except Exception as ex:
        return False
