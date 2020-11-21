

#  索引（index） --> 类型（type）--> 文档（Docments） --> 字段（Files）

from elasticsearch import Elasticsearch

# 链接es服务
host = '10.54.16.9:9200'
es = Elasticsearch([host])

# 指定mappings和settings


def create(index, body=None):
    """
    创建索引
    :param index: 索引名称
    :return: {'acknowledged': True, 'shards_acknowledged': True, 'index': 'student1'}
    """
    if es.indices.exists(index=index):
        es.indices.delete(index=index)  # 删除索引
    res = es.indices.create(index=index, body=body)
    return res


def delete(index):
    """
    删除索引
    :param index: 索引名称
    :return: True 或 False
    """
    if not es.indices.exists(index):
        return False
    else:
        res = es.indices.delete(index=index)
        return res['acknowledged']


def add(index, body, id=None):
    """
    (单条数据添加或更新)添加或更新文档记录，更新文档时传对应的id即可
    使用方法：
    `
    body = {"name": "long", "age": 11,"height": 111}
    add(index=index_name,body=body)
    或
    body = {"name": "long", "age": 11,"height": 111}
    add(index=index_name,body=body,id=1)
    `
    :param index: 索引名称
    :param body:文档内容
    :param id: 是否指定id,如不指定就会使用生成的字符串
    :return:{'_index': 'student1', '_type': '_doc', '_id': 'nuwKDXIBujABphC4rbcq', '_version': 1, 'result': 'created', '_shards': {'total': 2, 'successful': 1, 'failed': 0}, '_seq_no': 0, '_primary_term': 1}
    """
    res = es.index(index=index, body=body, id=id)
    return res['_id']  # 返回 id


def search(index=None,id=None,doc_type=None):
    """
    查询记录：如果没有索引名称的话默认就会查询全部的索引信息
    :param index:查询的索引名称
    :param doc_type:文档类型
    :param id:是否指定id
    :return:
    """
    if not index:
        return es.search()
    else:
        return es.search(index=index)


if __name__ == '__main__':
    import json

    index_name = 'user_browser_index'  # 索引名称  浏览：user_browser_index    收藏 user_collection_index
    res = search(index=index_name)
    print(json.dumps(res,ensure_ascii=False))