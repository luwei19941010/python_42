### day41

#### 1.HTML文件

#### 2.标签

```
1.双闭合标签<html>content</html>
2.单闭合标签<meta charset="UTF-8">
```



##### head标签

- meta 基本网站元信息标签
- title 网站的标题
- link 链接css文件
- script 链接JavaScript文件
- style 内嵌样式（css)

##### body标签

- h1~h6 标题标签
- p标签 段落标签
- br 换行
- a anchor 锚点 超链接标签
  - href 链接的网址
    - #top 回到顶部
  - title 鼠标悬浮上的标题
  - style 行内样式
    - text-decoration:none;
    - color:yellow;
  - target 目标
    - 默认是_self 在当前页面中打开新的链接
    - _blank 在新的空白页面上打开链接
  - img
    - src 链接图片资源
    - title 标签
    - style 
      - text-decoration:none;
      - color:yellow;
    - alt 图片加载失败的时候 
  - 字体标签
    - u
    - strong 加粗
    - em 倾斜
    - i 倾斜
  - ul 无序列表
    - type
    - <li>
  - ol有序列表
    - type 
    - <li>
  - table
    - border 表边框粗细
    - cellspacing 表格框空隙
    - width 标签宽度
    - cellpadding 表格格子大小
    - <tr>
    - <td>
  - form
    - action 服务器地址端口
    - method
      - post 没有大小限制，也不会显示在浏览器上
      - get 上传信息有大小限制2K，且会显示在浏览器上
    - <input>
      - type控件的类型
        - text文本输入框
        - password密码框
        - radio单选框
        - checkbox多选框
        - select 下拉菜单
        - datetime-local 时间
        - textinput 文本输入框
        - submit 提交
    - name
      - 名称 提交服务器的键值对的name
    - value
      - 值 提交服务器的键值对的value
    - select 标签
      -  name multiple:多选框
      - selected 默认选择
      - option value
    - textarea
      - name
      - value
      - cols
      - rows 

HTML特征：

- 对换行和空格不敏感
- 空白折叠

 