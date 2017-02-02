MacBooktekiMacBook-Pro:~ macbookpro$ sude pop install tweepy
-bash: sude: command not found
MacBooktekiMacBook-Pro:~ macbookpro$ sudo pop install tweepy
Password:
sudo: pop: command not found
MacBooktekiMacBook-Pro:~ macbookpro$ sudo pop install tweepy
sudo: pop: command not found
MacBooktekiMacBook-Pro:~ macbookpro$ sudo pip intsall tweepy
ERROR: unknown command "intsall" - maybe you meant "install"
MacBooktekiMacBook-Pro:~ macbookpro$ sudo pip install tweepy
The directory '/Users/macbookpro/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/macbookpro/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting tweepy
/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:318: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:122: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. You can upgrade to a newer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
  Downloading tweepy-3.5.0-py2.py3-none-any.whl
Collecting requests-oauthlib>=0.4.1 (from tweepy)
  Downloading requests_oauthlib-0.7.0-py2.py3-none-any.whl
Collecting requests>=2.4.3 (from tweepy)
  Downloading requests-2.13.0-py2.py3-none-any.whl (584kB)
    100% |████████████████████████████████| 593kB 1.2MB/s 
Collecting six>=1.7.3 (from tweepy)
  Downloading six-1.10.0-py2.py3-none-any.whl
Collecting oauthlib>=0.6.2 (from requests-oauthlib>=0.4.1->tweepy)
  Downloading oauthlib-2.0.1.tar.gz (122kB)
    100% |████████████████████████████████| 133kB 2.5MB/s 
Installing collected packages: oauthlib, requests, requests-oauthlib, six, tweepy
  Running setup.py install for oauthlib ... done
Successfully installed oauthlib-2.0.1 requests-2.13.0 requests-oauthlib-0.7.0 six-1.10.0 tweepy-3.5.0
MacBooktekiMacBook-Pro:~ macbookpro$ pwd
/Users/macbookpro
MacBooktekiMacBook-Pro:~ macbookpro$ cd ..
MacBooktekiMacBook-Pro:Users macbookpro$ cd ..
MacBooktekiMacBook-Pro:/ macbookpro$ pwd
/
MacBooktekiMacBook-Pro:/ macbookpro$ ls
Applications	Users		dev		net		usr
Library		Volumes		etc		private		var
Network		bin		home		sbin		用户信息
System		cores		mach_kernel	tmp
MacBooktekiMacBook-Pro:/ macbookpro$ cd python
-bash: cd: python: No such file or directory
MacBooktekiMacBook-Pro:/ macbookpro$ ls
Applications	Users		dev		net		usr
Library		Volumes		etc		private		var
Network		bin		home		sbin		用户信息
System		cores		mach_kernel	tmp
MacBooktekiMacBook-Pro:/ macbookpro$ cd library
MacBooktekiMacBook-Pro:library macbookpro$ ls
Application Support	Graphics		QuickTime
Audio			Image Capture		Receipts
Automator		Input Methods		Ruby
Bundles			Internet Plug-Ins	Sandbox
Caches			Java			Screen Savers
ColorPickers		Keyboard Layouts	ScriptingAdditions
ColorSync		Keychains		Scripts
Components		LaunchAgents		Security
Compositions		LaunchDaemons		Speech
Contextual Menu Items	Logs			Spelling
CoreMediaIO		Messages		Spotlight
Desktop Pictures	Modem Scripts		StartupItems
Dictionaries		OpenDirectory		SystemProfiler
DirectoryServices	PDF Services		Updates
Documentation		Perl			User Pictures
Extensions		PreferencePanes		Video
Filesystems		Preferences		WebServer
Fonts			Printers		Widgets
Fonts Disabled		PrivilegedHelperTools	iTunes
Frameworks		Python
Google			QuickLook
MacBooktekiMacBook-Pro:library macbookpro$ cd python
MacBooktekiMacBook-Pro:python macbookpro$ ls
2.3	2.5	2.6	2.7
MacBooktekiMacBook-Pro:python macbookpro$ cd 2.7
MacBooktekiMacBook-Pro:2.7 macbookpro$ ls
site-packages
MacBooktekiMacBook-Pro:2.7 macbookpro$ cd site-packages
MacBooktekiMacBook-Pro:site-packages macbookpro$ ls
README					requests_oauthlib-0.7.0.dist-info
easy-install.pth			scikit_learn-0.18.1.dist-info
examples				six-1.10.0.dist-info
oauthlib				six.py
oauthlib-2.0.1-py2.7.egg-info		six.pyc
pip-9.0.1-py2.7.egg			sklearn
requests				sklearn-0.0-py2.7.egg-info
requests-2.13.0.dist-info		tweepy
requests_oauthlib			tweepy-3.5.0.dist-info
MacBooktekiMacBook-Pro:site-packages macbookpro$ python3
Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from textblob import TextBlob
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'textblob'