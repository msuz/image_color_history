# image_color_history

## setup git env
```
$ ssh-keygen -t rsa
$ cat ~/.ssh/id_rsa.pub # -> https://github.com/settings/keys

$ vim ~/.ssh/config
$ cat ~/.ssh/config
Host github
  HostName github.com
  IdentityFile ~/.ssh/id_rsa
  User git

$ eval `ssh-agent`
$ ssh-add ~/.ssh/id_rsa
$ ssh-add -l
$ ssh -T git@github.com

$ echo '.DS_Store' >> ~/.gitignore_global
$ echo '__pycache__' >> ~/.gitignore_global
$ git config --global core.excludesfile ~/.gitignore_global 

$ git config --global user.name "msuz"
$ git config --global user.email "msuz@example.com"
```

## clone git repository
```
$ git clone github:msuz/image_color_history.git
```

## setup python env
```
$ python --version
Python 3.8.5

$ pip install -r requirements.txt 
$ pip freeze
numpy==1.19.1
opencv-contrib-python==4.3.0.36
opencv-python==4.3.0.36
```

## run unittest
```
$ python -m unittest -v tests.test_ich
test_default_values (tests.test_ich.ImageColorHistoryTestCase) ... ok
test_get_pixcel_bgr_list (tests.test_ich.ImageColorHistoryTestCase) ... ok
test_load_image_data (tests.test_ich.ImageColorHistoryTestCase) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

```
$ python -m unittest -v tests.test_ich.ImageColorHistoryTestCase.test_default_values
test_default_values (tests.test_ich.ImageColorHistoryTestCase) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## run app
```
todo: update

$ python pixel.py 
pixel.py
[[196 196 196   0   0   0]
 [114 114 114 192 192 192]
 [ 68  68  68 255 255 255]]
```