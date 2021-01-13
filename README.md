```
    author: 热狗得小舔狗
    createtTime: 2021-1-3

```

# 免责声明：此代码仅供学习使用，任何使用与作者无关

# PC端职教云
链接是这个: [https://zjy2.icve.com.cn/portal/login.html](https://zjy2.icve.com.cn/portal/login.html)

代码写的太乱了， 因为一开始没想搞，就搞了个登录
然后不知不觉随便写了一下刷课，ppt 所以都搞一个文件里啦 --懒


### python version--3.7.4
### 一些基本库
### 以后不会更新


#### 功能
1. 刷ppt
2. 刷视频
3. 评论


#### notice
没写任何报错处理, 重新运行即可！
(有些问题：你看懂源码的话。)
ex: 
    评论过的, 还会再次评论(可以修改)
    评论问题：
        (每篇评论有四个)
        pc端有限制, 差不多一分钟后才能进入下一个评论


#### 使用
1. 在login函数里, 输入用户名, 密码即可
2. 验证码问题：
    1. cmd中手动输入
    2. img文件夹下, 有图片处理代码, pytesseract识别没对过(没训练)


#### 思路
1. get_acw_tc函数           会给headers中cookie设置acw_tc参
2. get_code函数             获取验证码图片(只能请求一次, 否则失效), 会给headers中cookie设置verifycode参数
3. login函数                登录 后去返回json数据.但好像都没用到, 会给headers中cookie设置auth参数
4. get_course_list函数      获取你的课程 ex：数学 语文
5. choose函数               选择你要刷的课程
6. into_course函数          进入课程(特乱, 不高兴)里面调用很多方法, 实现的刷课功能都在里面写了
-----------------------------------------------------------------------------------------------
###### 以下都是 into_course函数调用的函数
7. get_processs_list函数    获取首目录信息
8. get_topicId函数          获取请求需要的data参数
9. get_cellid函数           获取请求需要的data参数
10. get_view_directory函数  进入刷课页面(视频, ppt, 评论页面)
11. add_view_content函数    评论功能
12. video函数               视频功能
13. ppt函数                 ppt功能

#### 太差劲了, 算了
大家伙, 凑合着刷吧.....

###### 可以给个小星星嘛， hhhh
