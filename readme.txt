\Python27\ScriptsĿ¼����pip�Ĺ��������Ҫ�Ȱ�װ���¹���
pip install PySide
pip install Ghost.py

��װpip���ߣ��ο�http://pip-cn.readthedocs.io/en/latest/installing.html#id6
ʹ�����
apt-get install -y python-pip

�ο����ϣ���������Щ����
http://jeanphix.me/Ghost.py/#open



�����¼��


Unable to locate package qtmobility-dev


apt-get install -y build-essential cmake libqt4-dev libxml2-dev libxslt1-dev 
apt-get install -y python-qt4
apt-get install -y python-ghost



���⣺��ô֪��apt-get��Ҫ��װ���������
���磺
boost�⣺
sudo apt-get install libboost-dev
libcurl�⣺
sudo apt-get install libcurl4-openssl-dev

libboost-dev��libcurl4-openssl-dev�����������ô���ģ���֪������boost��libcur��
ֱ��ʹ��sudo apt-get install boost �ǲ��еġ�

�𰸣�aptitude search boost  ������aptitude��Ҫapt-get�ķ�ʽ��װ

�������python��ʱ����ִ�������
>>> from ghost import Ghost
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/dist-packages/ghost/__init__.py", line 2, in <module>
    from .ghost import (
  File "/usr/lib/python2.7/dist-packages/ghost/ghost.py", line 17, in <module>
    from .bindings import (
  File "/usr/lib/python2.7/dist-packages/ghost/bindings.py", line 74, in <module
>
    QtWebKit = _import('QtWebKit')
  File "/usr/lib/python2.7/dist-packages/ghost/bindings.py", line 41, in _import
    module = __import__(name)
ImportError: No module named QtWebKit
�����Ѿ���װ��python-qt4��˵���Ѿ���װ��QtWebKitģ���ˣ�����Ϊʲô���ɹ��أ�
Ȼ��ֱ�ӳ���ʹ��apt-get install -y python-ghost��װghost��û����ʾʧ�ܣ��������е�ʱ���ǳ���û��QtWebKit������
���ݴ�����ʾ����ghostĿ¼�µ�bindings.py�ļ�(/usr/lib/python2.7/dist-packages/ghost/bindings)��������
��11���б���  bindings = ["PySide", "PyQt4"]
��36���к���
def _import(name):
    if binding is None:
        return LazyBinding()

    name = "%s.%s" % (binding.__name__, name)
    module = __import__(name)
    for n in name.split(".")[1:]:
        module = getattr(module, n)
    return module
����������binding�����е�PySide��������PySide��û��QtWebKit�����е��´����޸ķ�������bindings = ["PySide", "PyQt4"]��Ϊbindings = ["PyQt4"]��ǰ�����Ѿ���װ��python-qt4


�޸��������binding�ļ������л��ǳ������£�
>>> ghost=Ghost()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/dist-packages/ghost/ghost.py", line 295, in __init__
    'an X instance')
ghost.ghost.Error: Xvfb is required to a ghost run outside an X instance
ԭ������Ҫ��װxvfb��ʹ��apt-get install -y xvfb��װ�ȿ��ԡ�

�ܽᣬ�ڰ�װGhost.py��������ֱ�Ӱ�װpython-qt4��xvfb�������������⿴������룩������Ҫ��װPySideҲ���ԡ�


ʹ��ghost.py(webkit)���Ժܷ�����ȡjavascript�ӿڵ���������
ghost.py��װ
��һ������װPySide (ubuntu), centos�°�װ����PySide����(yum install qtwebkit qtwebkit-devel)
sudo apt-get install cmake
sudo apt-get install libqt4-dev
sudo apt-get install qt4-dev-tools   
sudo apt-get install qtmobility-dev
sudo apt-get install python2.7-dev
sudo apt-get install libphonon-dev
pip install wheel
wget https://pypi.python.org/packages/source/P/PySide/PySide-1.2.2.tar.gz
tar -xvzf PySide-1.2.2.tar.gz
cd PySide-1.2.2
python setup.py bdist_wheel --qmake=/usr/bin/qmake-qt4
python pyside_postinstall.py -install
��һ��2: �����û��X��linuxϵͳ��ʹ��ghost.py����Ҫ��װ xvfb
sudo apt-get install xvfb
yum install xorg-X11-server-Xvfb
��xvfbִ��:
xvfb-run --auto-servernum --server-args="-screen 0 1280x760x24"  python x.py
�ڶ���: ��װghost.py
pip install ghost.py