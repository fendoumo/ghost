\Python27\Scripts目录下有pip的工具命令，需要先安装以下工具
pip install PySide
pip install Ghost.py

安装pip工具，参考http://pip-cn.readthedocs.io/en/latest/installing.html#id6
使用命令：
apt-get install -y python-pip

参考资料，资料上有些出入
http://jeanphix.me/Ghost.py/#open



杂项记录：


Unable to locate package qtmobility-dev


apt-get install -y build-essential cmake libqt4-dev libxml2-dev libxslt1-dev 
apt-get install -y python-qt4
apt-get install -y python-ghost



问题：怎么知道apt-get需要安装的软件名称
比如：
boost库：
sudo apt-get install libboost-dev
libcurl库：
sudo apt-get install libcurl4-openssl-dev

libboost-dev和libcurl4-openssl-dev这个名字是怎么来的，我知道他叫boost和libcur。
直接使用sudo apt-get install boost 是不行的。

答案：aptitude search boost  ，但是aptitude需要apt-get的方式安装

运行这个python的时候出现错误如下
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
但是已经安装了python-qt4，说明已经安装了QtWebKit模块了，但是为什么不成功呢？
然后直接尝试使用apt-get install -y python-ghost安装ghost，没有提示失败，但是运行的时候还是出现没有QtWebKit！！！
根据错误提示，打开ghost目录下的bindings.py文件(/usr/lib/python2.7/dist-packages/ghost/bindings)，发现在
第11行有变量  bindings = ["PySide", "PyQt4"]
在36行有函数
def _import(name):
    if binding is None:
        return LazyBinding()

    name = "%s.%s" % (binding.__name__, name)
    module = __import__(name)
    for n in name.split(".")[1:]:
        module = getattr(module, n)
    return module
函数会先找binding变量中的PySide，发现在PySide中没有QtWebKit，所有导致错误，修改方法，将bindings = ["PySide", "PyQt4"]改为bindings = ["PyQt4"]，前提是已经安装了python-qt4


修改了上面的binding文件后，运行还是出错，如下：
>>> ghost=Ghost()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/dist-packages/ghost/ghost.py", line 295, in __init__
    'an X instance')
ghost.ghost.Error: Xvfb is required to a ghost run outside an X instance
原因是需要安装xvfb，使用apt-get install -y xvfb安装既可以。

总结，在安装Ghost.py的条件是直接安装python-qt4，xvfb，（其他依赖库看情况加入），不需要安装PySide也可以。


使用ghost.py(webkit)可以很方便爬取javascript接口等生成数据
ghost.py安装
第一步：安装PySide (ubuntu), centos下安装参照PySide官网(yum install qtwebkit qtwebkit-devel)
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
第一步2: 如果在没有X的linux系统下使用ghost.py还需要安装 xvfb
sudo apt-get install xvfb
yum install xorg-X11-server-Xvfb
用xvfb执行:
xvfb-run --auto-servernum --server-args="-screen 0 1280x760x24"  python x.py
第二步: 安装ghost.py
pip install ghost.py