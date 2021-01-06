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


def page_validator(value):
    """check value for int type
    """
    try:
        page = int(value)
        page = 1 if page < 1 else page
    except Exception as ex:
        page = 1
    return page
