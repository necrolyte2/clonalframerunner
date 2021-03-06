from subprocess import check_call, PIPE, CalledProcessError
import multiprocessing
from glob import glob
import os
from os.path import *
import shlex
import argparse
import sys

THIS_DIR = dirname( abspath( __file__ ) )

# ClonalFrame.bin -x 1000000 -y 250000 -z 100

# For this release I've only tested on windows and linux
# Can add more easily by adding the platform that would be reported by
# platform.system() into this list and then adding the cooresponding
# directory under extlib and putting the ClonalFrame executable in that folder
# The executable needs to be named ClonalFrame.bin(in the linux folder I simply
#  symlinked ClonalFrame -> ClonalFrame.bin)
KNOWN_PLATFORMS = ('Windows','Linux')

def binary( ):
    '''
        Return the path to the binary for this platform
    '''
    import platform
    system = platform.system()
    if system not in KNOWN_PLATFORMS:
        print 'I don\'t know what operating system you are using'
        sys.exit( 1 )
    return join( THIS_DIR, 'extlib', platform.system(), 'ClonalFrame.bin' )

def run_clonalframe( infile, outfile, cframeargs, *args, **kwargs ):
    '''
        Runs clonalframe with the given args and input files

        @param infile - Input dat file for clonalframe
        @param outfile - Ouput file to give to clonalframe
        @param cframeargs - Args to pass to clonal frame
    '''
    kwargs.update( {'infile':infile,'outfile':outfile} )
    cframe = binary()
    args = shlex.split(cframeargs) + [infile,outfile]
    cmd = [cframe] + args
    logfile = outfile + '.log'
    try:
        with open(outfile+'.stderr','w') as stderr:
            with open(outfile+'.stdout','w') as stdout:
                print "Running {}".format(cmd)
                return check_call( cmd, stdout=stdout, stderr=stderr )
    except CalledProcessError as e:
        print "Failed running {}".format(cmd)
        print e
        return -1

def main( args ):
    infiles = args.infiles
    outdir = args.outputdir
    cframeargs = args.cframeargs
    iterations = args.iterations
    if infiles:
        make_outputdir( outdir )
        run_parallel( infiles, outdir, iterations, cframeargs )
    else:
        print "No input files specified"

def make_outputdir( outdir ):
    if not isdir( outdir ):
        try:
            os.makedirs( outdir )
        except Exception as e:
            print "Cannot create output directory {}".format(outdir)
            print e
            sys.exit( 1 )

def run_parallel( infiles, outdir, iterations, cframeargs ):
    p = multiprocessing.Pool()
    print "Running {} iterations across the following input files utilizing {} cpus:".format(iterations,multiprocessing.cpu_count())
    print infiles
    print "Placing all output files into {}".format(outdir)
    jobs = []
    for infile in infiles:
        for outfile in getoutfilenames( infile, outdir, iterations ):
            jobs.append( (infile, outfile, cframeargs) )
    p.map( run_clonalframe_p, jobs )

def run_clonalframe_p( jobspec ):
    '''
        Simply run run_clonalframe with jobspec expanded
        Useful for map function

        @param jobspec - (infile, outfile, cframeargs)
    '''
    return run_clonalframe( *jobspec )

def getoutfilenames( infile, outpath, iterations ):
    '''
        Return outfilename for a given infile
        @param infile - Input file path
        @param outpath - Output directory
        @param iterations - How many iterations there will be
    '''
    fmt = basename(infile) + '.{}.out.dat'
    outpaths = [join(outpath,fmt.format(i)) for i in range(1,iterations+1)]
    return outpaths

def parse_args( argv=sys.argv[1:] ):
    parser = argparse.ArgumentParser(
        description='Runs clonalframe in windows'
    )

    parser.add_argument(
        '--infiles',
        dest='infiles',
        nargs='+',
        default=glob('*.dat'),
        help='List of input files. Default is all .dat files in current directory'
    )

    parser.add_argument(
        '-o',
        dest='outputdir',
        default='iterations_output',
        help='filepath or directory to put output files. All input files will be '\
            ' appended with .<iteration>.out.dat inside of that directory. Default is a folder in the current directory named iterations_output.'
    )

    parser.add_argument(
        '--iterations',
        dest='iterations',
        type=int,
        default=1,
        help='How many times to run ClonalFrame per input file. Default is 1 iteration.'
    )

    parser.add_argument(
        '--args',
        dest='cframeargs',
        help='List of args to pass to cframe(Must surround with \''
    )

    return parser.parse_args( argv )

if __name__ == '__main__':
    args = parse_args()
    main( args )
