# sync_async

`sync_async` is a lib that allows for optional asynchronous behavior in method calls. It provides the flexibility to
create methods that can be used both synchronously and asynchronously.

## Features

- **Async and Sync Compatibility**: Easily create functions that work in both synchronous and asynchronous contexts.
- **Flexible Initialization**: Use `AsyncObj` for classes requiring asynchronous initialization.
- **Decorator for Async Methods**: Simplify async method usage with the `sync_compat` decorator.

## Installation

Install via pip:

```bash
pip install sync_async
```

## Usage

### sync_async_factory

_Create a function that can be called synchronously or asynchronously:_

```python
from sync_async import sync_async_factory


def sync_func(x):
    return x * 2


async def async_func(x):
    await asyncio.sleep(0.1)
    return x * 2


sync_async = sync_async_factory(sync_func, async_func)

# Usage:
result = sync_async(5)  # Synchronous

async def main(): # Asynchronous
    result = await sync_async(5)
```

### `@sync_compat` Decorator

Make an async function compatible with sync calls

```python
from sync_async import sync_compat

@sync_compat
async def async_function(x):
    await asyncio.sleep(0.1)
    return x * 2

# Usage:
result = async_function(5)     # Synchronous
async def main(): # Asynchronous
    result = await sync_async(5)

```


### `AsyncObj` Class

Create a class that can be initialized asynchronously:

```python
from sync_async import AsyncObj

class MyAsyncClass(AsyncObj):
    async def __ainit__(self, x):
        self.x = x

# Usage:
async def main():
    obj = await MyAsyncClass(10)
    print(obj.x)
```

### Licence
This project is licensed under the MIT License.



