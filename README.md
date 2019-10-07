# missevan-spider

#### 介绍
missevan爬虫，可以当做Aplayer自定义来源

#### 使用说明

1.编辑config.ini

download代表要不要下载，如果要下载，程序将把封面和mp3文件下载到当前路径的cover和mp3目录

outfile代表输出文件，如music.js

usetitle代表是否自定义文件标题，默认使用原标题进行歌词查找。

server代表音乐网站服务器，用来搜索歌词

| 取值    | 含义   |
| :------ | :----- |
| netease | 网易云 |
| tencent | QQ音乐 |
| xiami   | 虾米   |
| kugou   | 酷狗   |

maxlrc代表最多显示的歌词条数。

2.输入url后面?id=......的一串数字。

![](https://images.gitee.com/uploads/images/2019/0901/141425_6f6ec58d_5151366.png)

3.如果你要自定义标题，请输入标题，程序会自动搜索歌词和作者。

![js.PNG](https://i.loli.net/2019/09/08/aPA6GHbWuQgBize.png)

4.输入e结束后，程序自动写入music.js，如图所示：

![](https://i.loli.net/2019/09/08/lkP4NvAwLS56ycC.png)

#### 使用注意

1.要用python3运行

2.没有的库全部装上