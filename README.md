# Monad-Py

## Example

```python
from monads import *


@Result.fnConvert
def getString(fn):
    with open(fn) as fd:
        return fd.read()


filestring = Result("LICENSE.md") >> getString
if filestring.isError():
    # Do whatever with the error
    ...
    exit()

string = filestring.unwrap()
word_set = Lazy(string) >> str.lower >> str.split >> (lambda words: {w for w in words})
keystroke = input("Do you want to see the word set? [y/n] ")
if keystroke == "y":
    # The set will only be calculated if you type y!
    print(word_set.unwrap())
else:
    # None of the functions (str.lower, str.split, ...) are called!
    ...
```
