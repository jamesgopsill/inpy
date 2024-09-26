# Inpy
A python package for parsing, manipulating and writing Abaqus input files. 



## Contents

- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Documentation](#documentation)
- [Formatting](#formatting)
- [Testing](#testing)

## Getting started

The package is still under active and early development so I have not put is on pypy just yet. You can still test it in your projects by linking directly to the [repo](https://stackoverflow.com/questions/15268953/how-to-install-python-package-from-github).

```
> pip install git+https://github.com/jamesgopsill/inpy.git#egg=gtr
```

You can then use it in your python code like so:


**TODO** There will be examples available in the `examples` folder if you want to learn more about what the tool can do. We will also have an API docs page that will give detailed information on the packages functionality.

## Contributing

I recommend creating a virtual environment for development work.

```
python -m venv .venv
```

Activate it using.

```
[Mac/Linux]
> source .venv/bin/activate
[Windows]
> .venv/Scripts/activate
```

And then install the development requirements.

```
> pip install -r requirements_dev.txt
```

You can then install a 'live' version of the package in your virtual environment. The package will reflect the changes you make to the source code.

```
> pip install -e .
```

## Documentation

Documentation will be generated using [pdoc](https://pdoc.dev/):

```
> pdoc ./src/inpy
```

```
> pdoc ./src/inpy -o ./docs
```

## Formatting

We format the code using [ruff](https://pypi.org/project/ruff/). There is also a [vscode plugin](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).

## Testing

Testing uses [unittest](https://docs.python.org/3/library/unittest.html).

```
python -m unittest -v
```