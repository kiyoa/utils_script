# utils_script

## redis_list_operate.py

**对redis列表的操作**
```
lpush: 列表存在则直接在最左边添加一条data，不存在则新建一个，然后追加
lpush: 列表存在则直接在最右边添加一条data，不存在则新建一个，然后追加
llen: 获取列表中元素个数
ltrim: 截断列表只保留size个元素
delete: 删除该条记录
lrange: 从左到右获取[start: stop]之间的元素
```

