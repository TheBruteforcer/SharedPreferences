# SharedPreferences
 Data sharing between python files without importing, or saving data for later usage without .yaml or any configration files
# Usage
<li>Download SharedPrefernces.py file</li>
<li>Import SharedPrefernces</li>

```python

from SharedPrefernces import *

```

<li> Create your first shared preferences component .</li>

<br>

```python

prefrence = SharedPrefrences(Name = 'my_new_pref', Developer_mode = True) 

```

<li> Add your data .</li>

<br>

```python

prefrence.AddKeyWithValue('UserName', 'OmarEllaban')

```
Output : # This output only appears if DevMode is True. 
```
python PS C:\Users\max\Desktop\MyWorkplace\main.py

log raise - >
 added key UserName with value OmarEllaban to preference test1,
 Preferences files in C:/main : ['my_new_pref.dat', 'my_new_pref.dir'],
 Current data in test1 => {'UserName': 'OmarEllaban'}

```

<li> Edit a key. </li>

<br>

```python

prference.EditKeyValue('UserName', 'OmarMohamed')

```

<li> Retrieve value from a key. </li>

<br>

```python

username = preference.Retrieve('UserName')
print(username)

```
Output:
```
 python PS C:\Users\max\Desktop\MyWorkplace\main.py
 
 OmarMohamed
```

<li> Delete a key. </li>

<br>

```python

preference.DeleteKey('Username')

```
<li> List all shared prefrences in your workplace. </li>

<br>

```python

prefrence.PrefrencesList()

```

```shell

['my_new_pref']

```

# Why you must use SharedPreferences module.?
Because of,
<li>Stability and efficiency </li>

<li>Store data for using in any application either if it written in C# or C++ or any programming language</li>

<li>You will not use importing your python scripts anymore</li>

<li>To prevent complexity in your scripts</li>

<li>Dealing with any programming language script or any application</li>

<li> It transfers Android and mobile application to computer applications development with python.</li>

<li> It's already an invention ! </li>

# Credits
This script is fully programmed by Omar Ellaban.
MIT license.

# Mechanism

```python

# I will write it soon 

```

# Some hints

<li>You should use developer mode in first usage.</li>