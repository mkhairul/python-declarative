## Install
```pip install -e git+http://github.com/mkhairul/python_declarative.git#egg=python_declarative ```

## Getting started
- create a file in the project folder, default.yml
```yaml
project: testing project
jobs:
  calculate:
    set_value: 10
    add: 10
    add: 100
    subtract: 5
    multiply: 3
    output: stdout
```
- create a file in the project folder, index.py
```python
from library.core.configurator import Configurator

Configurator().run()
```
