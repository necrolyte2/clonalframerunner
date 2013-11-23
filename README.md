Open a command window
Change directory to this directory


Simple Example Run:
python clonalframe.py --iterations 3 --args "-x 10 -y 10 -z 10"

Notice how you have to put the arguments for ClonalFrame.bin itself inside of " " after the --args.
You should be able to use any combination of clonal frame arguments inside of there.
!!! 
  Don't put the inifile and outfile arguments for ClonalFrame inside though. YOu need to supply those after all the arguments
   or don't supply them and all *.dat files will be used
!!!

Try this to get some more usage/help information about how to use the script.
python clonalframe.py --help