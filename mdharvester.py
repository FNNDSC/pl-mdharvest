#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter

from chris_plugin import chris_plugin, PathMapper

import os, sys
from datetime import datetime, timedelta

__version__ = '1.0.0'

DISPLAY_TITLE = r"""
       _                      _ _                               _   
      | |                    | | |                             | |  
 _ __ | |______ _ __ ___   __| | |__   __ _ _ ____   _____  ___| |_ 
| '_ \| |______| '_ ` _ \ / _` | '_ \ / _` | '__\ \ / / _ \/ __| __|
| |_) | |      | | | | | | (_| | | | | (_| | |   \ V /  __/\__ \ |_ 
| .__/|_|      |_| |_| |_|\__,_|_| |_|\__,_|_|    \_/ \___||___/\__|
| |                                                                 
|_|                                                                 
"""

#Can we just use an NLP library or literally just a counter
#Would need to store case-senstive words plus typos?
parser = ArgumentParser(description='!!!CHANGE ME!!! An example ChRIS plugin which '
                                    'counts the number of occurrences of a given '
                                    'word in text files.',
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-s', '--startdate', required=True, type=str, help="the start date")
parser.add_argument('-e', '--enddate', required=True, type=str, help="the end date")
parser.add_argument('-V', '--version', action='version',
                    version=f'%(prog)s {__version__}')


# The main function of this *ChRIS* plugin is denoted by this ``@chris_plugin`` "decorator."
# Some metadata about the plugin is specified here. There is more metadata specified in setup.py.
#
# documentation: https://fnndsc.github.io/chris_plugin/chris_plugin.html#chris_plugin
@chris_plugin(
    parser=parser,
    title='Metadata Harvester',
    category='',                 # ref. https://chrisstore.co/plugins
    min_memory_limit='100Mi',    # supported units: Mi, Gi
    min_cpu_limit='1000m',       # millicores, e.g. "1000m" = 1 CPU core
    min_gpu_limit=0              # set min_ gpu_limit=1 to enable GPU
)
def main(options: Namespace, inputdir: Path, outputdir: Path):
    """
    *ChRIS* plugins usually have two positional arguments: an **input directory** containing
    input files and an **output directory** where to write output files. Command-line arguments
    are passed to this main method implicitly when ``main()`` is called below without parameters.

    :param options: non-positional arguments parsed by the parser given to @chris_plugin
    :param inputdir: directory containing (read-only) input files
    :param outputdir: directory where to write output files
    """
    start_date = options.startdate
    end_date = options.enddate
    print(DISPLAY_TITLE)
    dateTreeBuild(start_date, end_date, outputdir)

def dateTreeBuild(start_date, end_date, outputdir):
    #Create Datetime objects
    try:
        start = datetime.strptime(start_date, '%Y%m%d')
        end = datetime.strptime(end_date, '%Y%m%d')
    except Exception as e:
        print("Hmmm... it seems either the start or end dates are invalid. Please check and try again.")
        sys.exit(1)
    
    #Datetime library should calculate the total difference in days
    total_days:int = (end - start).days + 1

    if(total_days <= 0):
        print("The end date seems to be _before_ the start date. No output created.")

    current_date = start
    for i in range(1, total_days + 1):
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        day = current_date.strftime('%d')

        directory_path = os.path.join(str(outputdir), year, month, day)
        print(f"Making path: {directory_path}") 
        os.makedirs(directory_path, exist_ok = True)
        
        current_date += timedelta(days = 1)


if __name__ == '__main__':
   main()
