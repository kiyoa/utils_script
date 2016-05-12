# -*- coding:utf-8 -*-

from redis import Redis

# Redis列表的边界下标
LEFTMOST = 0
RIGHTMOST = -1


class RedisListSecondPack:

    def __init__(self, name, client=Redis()):
        self.name = name
        self.client = client

    def left_append(self, content):
        # 从列表最左边追加value
        return self.client.lpush(self.name, content)

    def right_append(self, content):
        # 从列表最右边追加value
        return self.client.rpush(self.name, content)

    def read(self, start=LEFTMOST, stop=RIGHTMOST):
        # 获取裂变[start: stop]之间数据，默认状态下获取所有
        return self.client.lrange(self.name, start, stop)

    def length(self):
        # 获取列表长度
        return self.client.llen(self.name)

    def clear(self):
        # 因为del是Python的保留字
        # 所以redis-py用delete代替del命令
        self.client.delete(self.name)

    def keep(self, size):
        # 只保留列表范围内的条目
        self.client.ltrim(self.name, LEFTMOST, size-1)


if __name__ == '__main__':
    import json
    client = Redis(host='localhost', port=6379, db=0)
    list_operate_client = RedisListSecondPack('SHOWPAYBIZ000001', client)
    for x in range(4):
        list_operate_client.left_append(json.dumps({'a': 'my %s data' % str(x)}))
    print list_operate_client.read(), list_operate_client.length()
    list_operate_client.keep(3)
    print list_operate_client.read(), list_operate_client.length()
    list_operate_client.clear()




