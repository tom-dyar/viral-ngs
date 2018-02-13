'''Automated recording of data provenance and metrics.

This module enables the following:
   - automated recording of metadata and metrics in a uniform format into a centralized place, regardless of where analyses are run
   - answering questions like:
      - how was a given data file made?  (by what command, with what parameters, using what code version)
      - Which workflow versions (parameters, code versions) tend to produce the best results for which kinds of input, 
      according to given metrics?
   - avoiding redundant computation, when a command is re-run with the same inputs and same implementation of the command

../metadata_utils.py provides external command-line interface for querying provenance data.
'''

from ._metadata.argparse_arg_types import InFile, OutFile, InFiles, OutFiles, InFilesPrefix, OutFilesPrefix
from ._metadata.recording import (
    # interface with cmd.py
    add_metadata_tracking, 
    # for use by pipe/rules/common.rules to create a common ID for a sequence of steps run as part of same pipeline execution
    set_run_id
)

# for use by metadata_utils.py
from ._metadata.provenance_graph import ProvenanceGraph
