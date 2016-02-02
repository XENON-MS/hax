import ROOT
from tqdm import tqdm
from hax.utils import find_file_in_folders
from hax.config import CONFIG

# An exception you can raise to stop looping over the current dataset
class StopEventLoop(Exception):
    pass


###
# Looping over pax root files
###
def loop_over_dataset(dataset, event_function=lambda event: None, branch_selection='basic'):
    """Execute event_function(event) over all events in the dataset
    Does not return anything: you have to keep track of results yourself (global vars, function attrs, classes, ...)
    branch selection: can be None (all branches are read), 'basic' (CONFIG['basic_branches'] are read), or a list of branches to read.
    """
    # Open the file, load the tree
    # If you get "'TObject' object has no attribute 'GetEntries'" here,
    # we renamed the tree to T1 or TPax or something
    rootfile_name = find_file_in_folders(dataset + '.root', CONFIG['main_data_paths'])
    rootfile = ROOT.TFile(rootfile_name)
    t = rootfile.Get('tree')
    n_events = t.GetEntries()

    if branch_selection == 'basic':
        branch_selection = CONFIG['basic_branches']

    # Activate the desired branches
    if branch_selection:
        t.SetBranchStatus("*", 0)
        for bn in branch_selection:
            t.SetBranchStatus(bn, 1)

    try:
        for event_i in tqdm(range(n_events)):
            t.GetEntry(event_i)
            event = t.events
            event_function(event)
    except StopEventLoop:
        rootfile.Close()
    except Exception as e:
        rootfile.Close()
        raise e


def loop_over_datasets(datasets, *args, **kwargs):
    for dataset in datasets:
        loop_over_dataset(dataset, *args, **kwargs)