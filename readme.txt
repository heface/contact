2��������ͨѶ¼�ļ��ѽ�һ�����ܣ�����������UID_0982A0E6539FDCDBCD49792D2633B6D4��

Gitʹ��
�Ȱ�װgit���ߣ�Git-2.21.0-64-bit.exe�������ز��У������ַ����https://pc.qq.com/detail/13/detail_22693.html����
Ȼ���ڹ���Ŀ¼�£��Ҽ�ѡ�� Git Bash Here , ��git�����д��ڡ�

1 ����ssh key 
ssh-keygen -t rsa -C "heface@tom.com"

2 ��¼https://github.com��key��ӽ�ȥ

3 ����key�Ƿ����
ssh -T git@github.com
ssh -v git@github.com

ע�⣺key��·����win7�·���c:\Users\he\.ssh\ Ŀ¼�£������Ҳ���key��

4 ������Ŀ¼��¡������
git clone git@github.com:/heface/contact.git

5 �ύ����
�����������ģ���������ӵ��ݴ�������ʹ���������
git add <filename>
git add *
���� git �����������̵ĵ�һ����ʹ������������ʵ���ύ�Ķ���
git commit -m "�����ύ��Ϣ"
���ڣ���ĸĶ��Ѿ��ύ���� HEAD�����ǻ�û�����Զ�˲ֿ⡣

6 ���͸Ķ�
��ĸĶ������Ѿ��ڱ��زֿ�� HEAD ���ˡ�ִ�����������Խ���Щ�Ķ��ύ��Զ�˲ֿ⣺
git push origin master
���԰� master ��������Ҫ���͵��κη�֧�� 

����㻹û�п�¡���вֿ⣬��������Ĳֿ����ӵ�ĳ��Զ�̷������������ʹ������������ӣ�
git remote add origin <server>
�������ܹ�����ĸĶ����͵�����ӵķ�������ȥ�ˡ�

7 ��֧
��֧�����������Կ�����Ե�����ġ����㴴���ֿ��ʱ��master ��"Ĭ�ϵ�"��֧����������֧�Ͻ��п�������ɺ��ٽ����Ǻϲ�������֧�ϡ�
branches
����һ������"feature_x"�ķ�֧�����л���ȥ��
git checkout -b feature_x
�л�������֧��
git checkout master
�ٰ��½��ķ�֧ɾ����
git branch -d feature_x
�����㽫��֧���͵�Զ�˲ֿ⣬��Ȼ�÷�֧���� ��Ϊ���������ģ�
git push origin <branch>

8 ������ϲ�
Ҫ������ı��زֿ������¸Ķ���ִ�У�
git pull
������Ĺ���Ŀ¼�� ��ȡ��fetch�� �� �ϲ���merge�� Զ�˵ĸĶ���
Ҫ�ϲ�������֧����ĵ�ǰ��֧������ master����ִ�У�
git merge <branch>
������������£�git ���᳢��ȥ�Զ��ϲ��Ķ����ź����ǣ�����ܲ���ÿ�ζ��ɹ��������ܳ��ֳ�ͻ��conflicts���� ��ʱ�����Ҫ���޸���Щ�ļ����ֶ��ϲ���Щ��ͻ��conflicts��������֮������Ҫִ�����������Խ����Ǳ��Ϊ�ϲ��ɹ���
git add <filename>
�ںϲ��Ķ�֮ǰ�������ʹ����������Ԥ�����죺
git diff <source_branch> <target_branch>

9 ��ǩ
Ϊ�������������ǩ���Ƽ��ġ�����������Ѵ��ڣ��� SVN ��Ҳ�С������ִ�����������һ������ 1.0.0 �ı�ǩ��
git tag 1.0.0 1b2e1d63ff
1b2e1d63ff ������Ҫ��ǵ��ύ ID ��ǰ 10 λ�ַ�������ʹ�����������ȡ�ύ ID��
git log
��Ҳ����ʹ����һ����ύ ID ǰ��λ��ֻҪ����ָ�����Ψһ�ԡ�

10 �滻���ظĶ�
���������ʧ�󣨵�Ȼ���������Զ��Ҫ�������������ʹ�����������滻�����ظĶ���
git checkout -- <filename>
�������ʹ�� HEAD �е����������滻����Ĺ���Ŀ¼�е��ļ�������ӵ��ݴ����ĸĶ��Լ����ļ��������ܵ�Ӱ�졣

�������붪�����ڱ��ص����иĶ����ύ�����Ե��������ϻ�ȡ���µİ汾��ʷ�������㱾������ָ֧������
git fetch origin
git reset --hard origin/master


mysqlִ�нű�
����һ���� Windows ��ʹ�� cmd ����ִ�У��� Unix �� Linux ����̨�£�
��Mysql��binĿ¼��\mysql �Cu�û��� �Cp���� �CD���ݿ�<��sql�ű��ļ�·��ȫ������ʾ����
C:\MySQL\bin\mysql �Curoot �Cp123456 -Dtest<C:\test.sql

ע�⣺
A������� sql �ű��ļ���ʹ���� use ���ݿ⣬�� -D���ݿ� ѡ����Ժ���
B�������Mysql��binĿ¼���а����ո�����Ҫʹ�á����������磺��C:\Program Files\MySQL\bin\mysql�� �Cu�û��� �Cp���� �CD���ݿ�<��sql�ű��ļ�·��ȫ����
C����� sql û�д������ݿ����䣬�������ݿ������Ҳû�и����ݿ⣬��ô�������������һ���յ����ݿ⡣

������������ MySQL ����̨���磺MySQL 5.5 Command Line Client����ʹ�� source ����ִ��
�� MySQL Command Line Client���������ݿ�������е�¼��Ȼ��ʹ�� source ������� \.
Mysql>source ��sql�ű��ļ���·��ȫ���� �� Mysql>\. ��sql�ű��ļ���·��ȫ������ʾ����
source C:\test.sql ���� \. C:\test.sql

mysql����
��ʾ��ERROR 1044 (42000): Access denied for user ''@'localhost' to database 'mysql'������Ϊmysql���ݿ��user��������û���Ϊ�յ��˻��������˻���ʵ������������¼�ģ�ͨ��������ʾ���''@'localhost'���Կ����������ǽ���취����������

����һ�������������벻��ȷ�ģ�
0��˼·��
? ? ͨ������mysql�ĵ�¼���룬�Ƚ���mysql�ڲ�����ͨ��update�����������
1���ر�mysql
? ? service mysqld stop? ?//linux��ʹ��? ?
? ? net stop mysql? ? //window��ʹ��
2������Ȩ��
? ? mysqld_safe --skip-grant-table //linux��ʹ��
? ? mysqld?--skip-grant-table? //window��ʹ��
? ? ����ʹ����������
? ??mysqld_safe --user=mysql --skip-grant-tables --skip-networking & //linux��ʹ��?
? ? ��Ļ���֣� Starting demo from .....
3���¿���һ���ն�����
?? # mysql -u root mysql
?? mysql> UPDATE user SET Password=PASSWORD('newpassword') where USER='root';
?? mysql> FLUSH PRIVILEGES;? ?//��������? ?�ǵ�Ҫ��仰����������ر���ǰ���նˣ��ֻ����ԭ���Ĵ���
?? mysql> \q

���������������ڴ��ڿ����룩
0��˼·
? ��ʱ��mysql��Ȼӵ�����˺źͶ�Ӧ�����롣���ǣ����ڴ��ڿ�������������Ĭ�ϵ�¼���������С�
? ��Ҫ�ѿ�������˺�ɾ��������ͨ����������鿴�����˻�
? select host,user,password from user;
1.�ر�mysql
?? # service mysqld stop
2.����Ȩ��
?? # mysqld_safe --skip-grant-table
?? ��Ļ���֣� Starting demo from .....
3.�¿���һ���ն�����
?? # mysql -u root mysql
?? mysql> delete from user where USER='';? //ɾ��������
?? mysql> FLUSH PRIVILEGES;//�ǵ�Ҫ��仰����������ر���ǰ���նˣ��ֻ����ԭ���Ĵ���
?? mysql> \q
