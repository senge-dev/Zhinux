# Zhinux

iKun专属Linux系统

Zhinux为递归写法：Zhinux is not Unix.

欢迎光临我的网站：[个人博客](https://senge.dev)

BiliBili视频介绍：[BiliBili](https://www.bilibili.com/video/BV1p8411K7i5)

## 如何贡献

1. Fork该项目，然后在language文件夹中新建.po文件（如pacman.po）

要获取.po文件，请找到.mo文件，然后使用msgunfmt命令进行反编译，下方命令为反编译pacman.mo文件

```bash
msgunfmt /usr/share/locale/zh_CN/LC_MESSAGES/pacman.mo -o $HOME/pacman.po
```

如何寻找某个软件的语言包

以ArchLinux为例，运行该命令来获取语言包

```bash
# 寻找pacman语言包的所在路径，目前只支持修改位于/usr/share/locale目录下的语言包
pacman -Ql pacman | grep zh
```

2. 编辑文件，编辑完成后不要编译，直接将文件上传到项目目录的language-po目录中
3. 发布Pull requests，作者会进行人工审核，在确保准确无误后就会允许修改。

## 注意事项

> - 禁止发布任何NSFW内容
> - 禁止提交任何涉黄以及涉政内容
> - 玩梗需要适度，禁止提交任何网络暴力有关的内容
