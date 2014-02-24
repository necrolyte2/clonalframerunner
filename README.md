# ClonalFrame Runner

The purpose of this project is to simply make running ClonalFrame over multiple 
input files and multiple iterations over each to be easier.
This project is focused on allowing the user to easily utilize as many CPU's as 
possible to run as many iterations and input files as you can.
This project does not make ClonalFrame itself utilize more than one thread/cpu, 
but instead runs ClonalFrame on each input file using a different cpu so that you can do many analysis all in parallel.

## Installation

### Install Python

Ensure Python is installed(version 2.7+) and in your path

### Install clonalframerunner

You can download it directly from https://github.com/necrolyte2/clonalframerunner/archive/master.zip and unzip that wherever
you want or you can clone the git repository
```
git clone https://github.com/necrolyte2/clonalframerunner.git
```
Note the location that you install clonalframerunner as you will have to reference it's location later when you run the script.

### Windows

All you should have to do is download the latest Windows release from [ClonalFrame][1] and unzip the files into
the extlib/Windows directory.
All you really need is to have the ClonalFrame.bin file inside of the extlib/Windows directory, but you can just copy
everything if you want.

Check out [this link](http://docs.python.org/2/faq/windows.html#how-do-i-run-a-python-program-under-windows) regarding Python on windows.

### Linux

The latest ClonalFrame(v1.2) is bundled inside of the extlib/Linux so you do not
need to install it separately.

You may need to install some pieces of the [GNU Scientific Library] [2]

Ubuntu/Mint/Debian
```
sudo apt-get install libgsl01dbl
```
RedHat

You may need to download/make/install the [GNU Scientific Library][2] manually or possibly find an rpm package that 
contains the file libgsl.so.0

```
yum install gsl gsl-devel gsl-static qt4 qt4-devel
```

## Examples

All examples assume you are inside of the installed clonalframerunner directory. If you are trying to run cframe_runner.py from outside of the installation directory you will have to specify the full path to cframe_runner.py.
Aka.

Linux
```
python /path/to/cframe_runner.py --help
```
Windows
```
python C:\path\to\cframe_runner.py --help
```
There are plans to make it easier to run in the future so this will be unecessary.

### Simplest invocation

The following will execute ClonalFrame as if you had just run ClonalFrame without any arguments.
The only difference is that cframe_runner.py will automatically find all .dat files in the current directory
and run them for you.
```
python cframe_runner.py
```

### Iterations

Sometimes you might want to run all given input files with ClonalFrame multiple times.
The following would run all found .dat files 3 times each creating a separate iteration output file for each iteration.
```
python cframe_runner.py --iterations 3
```

### Customize Arguments sent to ClonalFrame

Most likey you will want to set the -x, -y and -z options for ClonalFrame. This is easy as well.
You should be able to use any combination of clonal frame arguments by utilizing the --args option to cframe_runner.py

```
python cframe_runner.py --args "-x 1000 -y 250 -z 10"
```
__!!! Don't put the inifile and outfile arguments for ClonalFrame inside of the quotes after --args !!!__


### Get more help about how to use cframe_runner.py
```
python cframe_runner.py --help
```

## Known Issues

* [No Status Updates](https://github.com/necrolyte2/clonalframerunner/issues/1)
* [Needs installer](https://github.com/necrolyte2/clonalframerunner/issues/2)

Please [submit](https://github.com/necrolyte2/clonalframerunner/issues) any more issues that you find

## References

* [ClonalFrame][1]
* [GNU Scientific Library][2]

[1]: http://www.xavierdidelot.xtreemhost.com/clonalframe.htm    "ClonalFrame"
[2]: http://www.gnu.org/software/gsl/    "GNU Scientific Library"
