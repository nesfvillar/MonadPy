# Monad-Py

## Example

```python
from monads.result import Result


@Result.fnConvert
def getString(fn: str):
    with open(fn) as fd:
        return fd.read()


license = Result("LICENSE.md").bind(
    getString,
    str.lower,
    str.split
)

if license.isOk():
    word_list = license.unwrap()
    print(word_list)
else:
    error = license.getError()
    print(error["exception"])
```
