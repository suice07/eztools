<!--
 * @Author: Auier qi.mei@outlook.com
 * @Date: 2024-08-07 10:12:29
 * @LastEditors: Auier qi.mei@outlook.com
 * @LastEditTime: 2024-08-23 10:25:53
 * Copyright (c) 2024 by Auier qi.mei@outlook.com, All Rights Reserved. 
-->
# eztools
easy tools for everyday use

## Change and Build
```
python setup.py build
python setup.py sdist
```
## Installation
build and install step by step
```
cd eztools/dist
pip install eztools-0.1.1.tar.gz
```
or you can use the script
```
bash install.sh
```
## Updates
### [v0.1.2] - 2024-08-23
#### Changes
    - add chemtool

#### Known issue
    - column chaning function over stupid

### [v0.1.2] - 2024-08-12
#### Changes
    - add retrivial function

#### Known issue
    - column chaning function over stupid

### [v0.1.2] - 2024-08-07
#### Changes
    - add json load and dump tool
    - add stupid column changing function in dftool, will update later
    - add keyword filtering tool, add column filter with pattern_search and acurate search
#### Known issue
    - column changing function over stupid