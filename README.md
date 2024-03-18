# SharedPreferences
 Data sharing between python files without importing, or saving data for later usage without .yaml or any configration files
# Usage
<li>Download SharedPrefernces.py file</li>
<li>Import SharedPrefernces</li>

```python
from SharedPrefernces import *
```

<li> Create your first shared preferences component .</li>

```python
prefrence = SharedPrefrences(Name = 'my_new_pref', Developer_mode = True) 
```

<li> Add your data .</li>

```python
prefrence.AddKeyWithValue('UserName', 'OmarEllaban')
```

```bash
python PS C:\Users\max\Desktop\MyWorkplace\main.py
log raise - >
 added key UserName with value OmarEllaban to preference test1,
 Preferences files in C:/main : ['my_new_pref.dat', 'my_new_pref.dir'],
 Current data in test1 => {'UserName': 'OmarEllaban'}
```