##  python爬虫初始化代码

**question: 每次写一个小型爬虫文件都要从头开始写, 很多东西都一样, 所以制作这个模板, 减轻重复工作量, 工作更高效哦 !**

1. 导入基本模块

```python
import requests
```

2. 定义初始url地址和headers请求头为空

```python
url = ''

headers = {

}
```

3. 获得响应体, 打印响应体的文本数据

```
response = requests.get(url=url, headers=headers)
html_data = response.text
print(html_data)

```

