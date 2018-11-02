weibo_read
====
新浪微博简易爬虫，读取特定用户原创微博

*目前只打印了第一页的微博内容*

## 要求

+ python3
+ requests
```bash
pip install requests
```
或者用`pipenv`
```bash
pip install pipenv
pipenv install
pipenv shell
```

## 运行

```shell
python weibo_read.py <uid>
```

比如打印[深圳天气](https://weibo.com/szmb)的微博
```shell
python weibo_read.py 1871802012
```

## 备注

如果一定要用python2来执行，可以在前面添加：

```shell
reload(sys)
sys.setdefaultencoding('utf-8')
```

## TODO

+ 支持打印所有页面的微博（~~其实只要url中添加`page`参数就可以了~~)
