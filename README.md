# pipd [![Build Status](https://travis-ci.org/ryansmick/pipd.svg?branch=master)](https://travis-ci.org/ryansmick/pipd)
Pip add-on to track dependencies

## Purpose

By default, pip doesn't include an effective dependency tracking method for packages that are installed. I realized this one day when I went to uninstall a package with what felt like a million dependencies and all that pip removed was the top-level package. This didn't seem right to me, since I no longer needed the other 100 packages that were installed with that single pip command. For that reason, I decided to create a toolto track dependencies among installed packages and to uninstall all the packages that are no longer needed as dependencies for a removed package. Thus, pipd was born.

## Installation

I recommend installing the package in your global python3 distribution so that you can use the script from any directory, whether in a virtual environment or not. You can do this by running the following commands outside of any virtual environment:

```Shell
$ git clone https://github.com/ryansmick/pipd.git
$ cd pipd
$ pip3 install .
```

This will add a script called "pipd" to your path, allowing you to use pipd from any directory.

## Usage

Pipd currently has two commands: tree, and uninstall.

The tree command is used to print a tree representation of the dependencies of packages currently installed with pip. It can be invoked by running `pipd tree` in the terminal.

The uninstall command is used to uninstall a given package and all of its dependencies. It keeps track of whether or not a given package is relied on, and will prompt you if the package you are trying to uninstall is a dependency for another package. You can invoke this functionality by running `pipd uninstall <package_names>`.  This functionality is the main purpose of the project, and I recommend using this as a replacement for the generic `pip uninstall` command.

Pipd was made for use within virtual environments, and using it to uninstall packages in a global environment has not been tested.

## TODO

* Update tree printing algorithm
* Update graph after uninstall
* Add method to save and load graph from file rather than building fresh each time
* Create new algorithm to handle circular dependencies
