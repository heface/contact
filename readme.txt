2、导出的通讯录文件已进一步加密，开启密码是UID_0982A0E6539FDCDBCD49792D2633B6D4。

Git使用
先安装git工具（Git-2.21.0-64-bit.exe官网下载不行，这个地址可以https://pc.qq.com/detail/13/detail_22693.html）。
然后在工作目录下，右键选择 Git Bash Here , 打开git命令行窗口。

1 创建ssh key 
ssh-keygen -t rsa -C "heface@tom.com"

2 登录https://github.com将key添加进去

3 测试key是否可用
ssh -T git@github.com
ssh -v git@github.com

注意：key的路径，win7下放在c:\Users\he\.ssh\ 目录下，否则找不到key。

4 将工程目录克隆到本地
git clone git@github.com:/heface/contact.git

5 提交更改
你可以提出更改（把它们添加到暂存区），使用如下命令：
git add <filename>
git add *
这是 git 基本工作流程的第一步；使用如下命令以实际提交改动：
git commit -m "代码提交信息"
现在，你的改动已经提交到了 HEAD，但是还没到你的远端仓库。

6 推送改动
你的改动现在已经在本地仓库的 HEAD 中了。执行如下命令以将这些改动提交到远端仓库：
git push origin master
可以把 master 换成你想要推送的任何分支。 

如果你还没有克隆现有仓库，并欲将你的仓库连接到某个远程服务器，你可以使用如下命令添加：
git remote add origin <server>
如此你就能够将你的改动推送到所添加的服务器上去了。

7 分支
分支是用来将特性开发绝缘开来的。在你创建仓库的时候，master 是"默认的"分支。在其他分支上进行开发，完成后再将它们合并到主分支上。
branches
创建一个叫做"feature_x"的分支，并切换过去：
git checkout -b feature_x
切换回主分支：
git checkout master
再把新建的分支删掉：
git branch -d feature_x
除非你将分支推送到远端仓库，不然该分支就是 不为他人所见的：
git push origin <branch>

8 更新与合并
要更新你的本地仓库至最新改动，执行：
git pull
以在你的工作目录中 获取（fetch） 并 合并（merge） 远端的改动。
要合并其他分支到你的当前分支（例如 master），执行：
git merge <branch>
在这两种情况下，git 都会尝试去自动合并改动。遗憾的是，这可能并非每次都成功，并可能出现冲突（conflicts）。 这时候就需要你修改这些文件来手动合并这些冲突（conflicts）。改完之后，你需要执行如下命令以将它们标记为合并成功：
git add <filename>
在合并改动之前，你可以使用如下命令预览差异：
git diff <source_branch> <target_branch>

9 标签
为软件发布创建标签是推荐的。这个概念早已存在，在 SVN 中也有。你可以执行如下命令创建一个叫做 1.0.0 的标签：
git tag 1.0.0 1b2e1d63ff
1b2e1d63ff 是你想要标记的提交 ID 的前 10 位字符。可以使用下列命令获取提交 ID：
git log
你也可以使用少一点的提交 ID 前几位，只要它的指向具有唯一性。

10 替换本地改动
假如你操作失误（当然，这最好永远不要发生），你可以使用如下命令替换掉本地改动：
git checkout -- <filename>
此命令会使用 HEAD 中的最新内容替换掉你的工作目录中的文件。已添加到暂存区的改动以及新文件都不会受到影响。

假如你想丢弃你在本地的所有改动与提交，可以到服务器上获取最新的版本历史，并将你本地主分支指向它：
git fetch origin
git reset --hard origin/master


mysql执行脚本
方法一，在 Windows 下使用 cmd 命令执行（或 Unix 或 Linux 控制台下）
【Mysql的bin目录】\mysql –u用户名 –p密码 –D数据库<【sql脚本文件路径全名】，示例：
C:\MySQL\bin\mysql –uroot –p123456 -Dtest<C:\test.sql

注意：
A、如果在 sql 脚本文件中使用了 use 数据库，则 -D数据库 选项可以忽略
B、如果【Mysql的bin目录】中包含空格，则需要使用“”包含，如：“C:\Program Files\MySQL\bin\mysql” –u用户名 –p密码 –D数据库<【sql脚本文件路径全名】
C、如果 sql 没有创建数据库的语句，而且数据库管理中也没有该数据库，那么必须先用命令创建一个空的数据库。

方法二，进入 MySQL 控制台（如：MySQL 5.5 Command Line Client），使用 source 命令执行
打开 MySQL Command Line Client，输入数据库密码进行登录，然后使用 source 命令或者 \.
Mysql>source 【sql脚本文件的路径全名】 或 Mysql>\. 【sql脚本文件的路径全名】，示例：
source C:\test.sql 或者 \. C:\test.sql

mysql错误
提示：ERROR 1044 (42000): Access denied for user ''@'localhost' to database 'mysql'。是因为mysql数据库的user表里，存在用户名为空的账户即匿名账户，实际上是匿名登录的，通过错误提示里的''@'localhost'可以看出来，于是解决办法见方法二。

方法一：（适用于密码不正确的）
0、思路：
? ? 通过屏蔽mysql的登录密码，先进入mysql内部，再通过update命令更新密码
1、关闭mysql
? ? service mysqld stop? ?//linux下使用? ?
? ? net stop mysql? ? //window下使用
2、屏蔽权限
? ? mysqld_safe --skip-grant-table //linux下使用
? ? mysqld?--skip-grant-table? //window下使用
? ? 或者使用如下命令
? ??mysqld_safe --user=mysql --skip-grant-tables --skip-networking & //linux下使用?
? ? 屏幕出现： Starting demo from .....
3、新开起一个终端输入
?? # mysql -u root mysql
?? mysql> UPDATE user SET Password=PASSWORD('newpassword') where USER='root';
?? mysql> FLUSH PRIVILEGES;? ?//更新命令? ?记得要这句话，否则如果关闭先前的终端，又会出现原来的错误
?? mysql> \q

方法二：（适用于存在空密码）
0、思路
? 有时候，mysql虽然拥有了账号和对应的密码。但是，由于存在空密码的情况，会默认登录到空密码中。
? 需要把空密码的账号删除，可以通过如下命令查看所有账户
? select host,user,password from user;
1.关闭mysql
?? # service mysqld stop
2.屏蔽权限
?? # mysqld_safe --skip-grant-table
?? 屏幕出现： Starting demo from .....
3.新开起一个终端输入
?? # mysql -u root mysql
?? mysql> delete from user where USER='';? //删除空密码
?? mysql> FLUSH PRIVILEGES;//记得要这句话，否则如果关闭先前的终端，又会出现原来的错误
?? mysql> \q
