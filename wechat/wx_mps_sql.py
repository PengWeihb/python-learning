def add_article():
    """ Save Article data
    
    :return: sql
    """

    sql = 'insert into tb_article(msg_id,date_time,"type",msg_data,title,author,cover,digest,' \
          'content_url,source_url,del_flag,ext_data,create_time) VALUES' \
          '(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    return sql


def add_article_comment():
    """ Save Article comment data

    :return: sql
    """

    sql = 'insert into tb_article_comment(comment_id,nick_name,logo_url,content_id,content,like_num,' \
          'comment_time,reply_content,reply_create_time,reply_like_num,reply_data,create_time) VALUES' \
          '(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    return sql


def find_article():
    """ Select from Article

    :return: sql
    """

    sql = 'select content_url from tb_article where title like %s'

    return sql


def find_article_comment():
    """ Select from Article Comment

    :return: sql
    """

    sql = 'select nick_name,content,logo_url,comment_time from tb_article_comment where content like %s'

    return sql