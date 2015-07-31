import argparse
import time
import os

from sumatra.parameters import build_parameters, SimpleParameterSet
from sumatra.projects import load_project


parser = argparse.ArgumentParser(description='Run script with Sumatra.')
parser.add_argument('-p', '--param', metavar='FILE', type=str, default='inline',
                    help='Get parameters from file or from inline script.')
parser.add_argument('-r', '--record', dest='record', action='store_true', default=False,
                    help='Record the script running with Sumatra.')
parser.add_argument('--reason', dest='reason', type=str, default='',
                    help='Write reason for running script.')
args = parser.parse_args()
print args

def sumatra_parameters(filename, start_tag="# PARAMS", end_tag="# END OF PARAMS"):
    with open(filename, 'r') as f:
        lines = f.readlines()
    start, end = lines.index('%s\n'%start_tag), lines.index('%s\n' %end_tag)
    params = ''.join(lines[start+1:end])
    return SimpleParameterSet(params)

def sumatra_record(filename):
    filename = os.path.relpath(filename)
    project = load_project()
    if args.param == 'inline':
        parameters = sumatra_parameters(filename)
    elif os.path.exists(args.param):
        parameters = build_parameters(args.param)

    if args.record:
        record = project.new_record(main_file=filename, reason=args.reason, parameters=parameters)
        record.duration = time.time()
    else:
        record = None
    return project, record, parameters

def sumatra_save(project, record):
    if args.record:
        record.duration = time.time() - record.duration
        record.output_data = record.datastore.find_new_data(record.timestamp)
        project.add_record(record)
        project.save()
        return True
    else:
        return False
