#!/usr/bin/env python
import sys
import distro
import os


class ZhinuxError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Zhinux:
    def __init__(self):
        self.distro = distro.id()
        self.help_info = """参数：
\t-i, --install 安装语言包
\t-u, --uninstall 卸载语言包
\t-h, --help 显示帮助信息"""
        if self.distro not in ["arch", "manjaro", "endeavouros", "garuda", "artix", "arcolinux"]:
            raise ZhinuxError("目前该脚本仅支持 Arch Linux及其衍生版本，暂不支持其他发行版。")
        self.uid = os.getuid()
        self.file_dir = "/usr/share/locale/zh_CN/LC_MESSAGES"
        if self.uid == 0 and not os.path.exists(self.file_dir):
            os.mkdir("/usr/share/locale/zh_CN/LC_MESSAGES/zhinux-backup")
        self.backup_dir = "/usr/share/locale/zh_CN/LC_MESSAGES/zhinux-backup"

    def check_uid(self):
        if self.uid != 0:
            raise ZhinuxError("请使用root权限运行该脚本")

    def install(self):
        self.check_uid()
        for file in os.listdir("language-po"):
            if file.endswith(".po"):
                if not os.path.exists(self.file_dir + file[:-3] + ".mo"):
                    print("语言包" + file[:-3] + "不存在，下方为可能需要安装的软件包")
                    os.system("pacman -Ss " + file[:-3])
                    print("跳过语言包" + file[:-3])
                    input("按回车键继续，按Ctrl+C退出程序...")
                    continue
                os.rename(self.file_dir + file[:-3] + ".mo", self.backup_dir + file[:-3] + ".mo")
                result = os.system("msgfmt file -o " + self.file_dir + file[:-3] + ".mo")
                if result != 0:
                    print("编译语言包" + file[:-3] + "失败，正在还原")
                    os.rename(self.backup_dir + file[:-3] + ".mo", self.file_dir + file[:-3] + ".mo")
                    input("按回车键继续，按Ctrl+C退出程序...")
                    continue
                print("编译语言包" + file[:-3] + "成功")
            else:
                print("跳过文件" + file)
                input("按回车键继续，按Ctrl+C退出程序...")

    def uninstall(self):
        self.check_uid()
        # 恢复所有备份，并删除backup文件夹
        for file in os.listdir(self.backup_dir):
            os.rename(self.backup_dir + file, self.file_dir + file)
            print("恢复语言包" + file[:-3] + "成功")
        os.rmdir(self.backup_dir)

    def help(self):
        print(self.help_info)


if __name__ == '__main__':
    zhinux = Zhinux()
    try:
        param = sys.argv[1]
    except IndexError:
        print("参数不能为空")
        zhinux.help()
        sys.exit(1)
    if param in ["--install", "-i"]:
        zhinux.install()
    elif param in ["--uninstall", "-u"]:
        zhinux.uninstall()
    elif param in ["--help", "-h"]:
        zhinux.help()
    else:
        print("未知参数" + param)
        zhinux.help()
        sys.exit(1)
