# pyautoeios

Python bindings for `libRemoteInput` library and port of the lape `Reflection` package from [Brandon-T/Reflection][reflection].

### How would I use this?

###### Installation

```batch
python -m pip install -i https://test.pypi.org/simple/ pyautoeios
```

###### Usage:

I add scripts to the [examples](examples) as I port modules of [Brandon-T/Reflection][reflection] and add new methods.

Here is a simple login example:

```python
import getpass
import pyautoeios as pyauto

pyauto.inject_clients()
for client in pyauto.clients:
    pyauto.pair_client(client)
    email = input("enter your username:")
    password = getpass.getpass()
    im = pyauto.screenshot()
    im.show()
    pyauto.static.login(client, email, password)
    im = pyauto.screenshot()
    im.show()
```


### What are the features?

- [x] Works with python 3.8
- [x] installable via pip
- [x] Pip install dependancies for you (*needs more testing.* compare your versions to [Pipfile](/Pipfile))
- [x] Wraps well liked [pyautogui](https://github.com/asweigart/pyautogui/) interface
- [x] Transparent Image finding *when opencv is installed*
- [x] Injecting into multiple clients (so threads can be used for multi-boxing)
- [x] no *known* memory leaks.
- [x] pytest for unit testing
- [x] login methods


### Alpha Status

**everything** is subject to change in
future releases. This is because I want the 1.0.0 release to actually be
something people like using.

That said. I welcome your usage and feedback so we can make this a good library
for boting.

Even if things will change before the 1.0.0 release, once something is in version
control or pypi, its there forever. I have no intention of deleteing commits from
github. (unless I am forced to by some lawyer somewhere)


### What are you planning on adding?


###### Top Priority Features

1. Create methods for interacting with grand exchange.
1. Port Interfaces for bank standing skills from [Brandon-T/Reflection][reflection]
    - Port `Inventory.simba` -> `inventory.py`
    - Port `Bank.simba` -> `bank.py`
1. Port Interfaces for smithing skills from [Brandon-T/Reflection][reflection]
    - Port `Interfaces.simba` -> `interfaces.py`
    - Port `Bank.simba` -> `bank.py`
1. porting of other modules from [Brandon-T/Reflection][reflection]

###### Lower Priority Features

1. Login screen world switcher logic (*for now just ensure you are on a valid world for your user*)
1. integration of color methods from [BenLand100/srbot](https://github.com/BenLand100/srbot/tree/master/srbot)
1. porting modules from [SRL/SRL](https://github.com/SRL/SRL) or [ollydev/SRL-Development](https://github.com/ollydev/SRL-Development)


### Why are you making this?

I think programming should be *fun*. For me, python is *an enjoyable language*
and botting **old school** is a fun programming activity.


### Progess Tracking

see [PROGRESS.md](PROGRESS.md)

[reflection]: https://github.com/Brandon-T/Reflection
