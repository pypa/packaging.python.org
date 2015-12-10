Where do packages come from?
============================
Packages can be distributed in a bunch of ways! PyPI is a great way to get packages that you want, but by no means the only way! Here are three main ways to get packages that you want:

* Use pip to install packages that are hosted on PyPI
* Download the source code from a version control repository like GitHub, 
* Download an archive from someone's website. 


PyPI is an index of packages- it maintains a searchable list of all of the packages people submit to it.  That makes it easy for people to find packages that they might want to use.   But, PyPI is not the only index. It is certainly popular, but there are a number of other ways to find packages on-line. You can see this list (https://wiki.python.org/moin/PyPiImplementations#Tools_.2F_Extensions) that gives you a few other indexes that implement the same standard. That means you can still use pip with them. 

An example using Django
--

Let's talk about an example: the Django package. Django is a web framework for Python.  We're going to look at the three methods of getting a package to see how they work.

1. PyPI and pip
----

Django is released on PyPI, so you can download it with pip! 

	pip install Django==1.9
	
*Side note: You might have pip already, but if you don't, you can follow the instructions found here: (https://pip.pypa.io/en/stable/installing/).*

2. Version Control Repository
----

In this case, Django is available on GitHub. 
	
	cd aDirectory
	git clone https://github.com/django/django.git
	python setup.py install

*For this to work, you will need to have git installed: (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).*

3. Downloading an archive file 
----

And finally, if you're not into either of those two options, you can download an archive file: 

Django provides a tar.gz file both on their website and on the PyPI site that you can download:

https://pypi.python.org/pypi/Django/1.9

However, you will need to unzip this file and ensure that there are no previous versions of Django installed on your system. You can just delete the files if they are around. This is generally handled by pip, but if you don't want to use pip, you'll need to do those things yourself. 

Using Windows:
------
You might need a zipping tool, such as 7-Zip to unzip when archives are .tar.gz files. Regular zip files can be handled by the operating system itself.
Then, run the command prompt (cmd) as an administrator. You must be in the Django directory. To finish the install, run the following command:
    python setup.py install

On a Unix system
------
The following commands will install Django for you:

	tar xzvf Django-1.4.2.tar.gz
	cd Django-*
	sudo python setup.py install

	
Using pip, git, or downloading an archive file do all get you to the same place, it just depends on your preference as to which one you choose.
