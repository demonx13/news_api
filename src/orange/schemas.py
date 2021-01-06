from drf_yasg import openapi

# NewsByCategory
page_param = openapi.Parameter('page',
                               openapi.IN_QUERY,
                               description="page param",
                               type=openapi.TYPE_INTEGER)


# NewsDetail
id_news_param = openapi.Parameter('id',
                                  openapi.IN_QUERY,
                                  description="id param",
                                  required=True,
                                  type=openapi.TYPE_INTEGER)
