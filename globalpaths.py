# imports
from IPython.display import display, Markdown


# functions
def get_substrings(filename, target_string):
    substrings = []
    with open(filename, 'r') as file:
        for line in file:
            if target_string in line:
                index_eq = line.find('=')
                index_sc = line.find(';')
                if index_sc != -1 and index_sc > index_eq:
                    # Semicolon exists after equal sign, extract substring between them
                    substring = line[index_eq+1:index_sc].strip()
                else:
                    # No semicolon after equal sign, extract substring after equal sign
                    substring = line[index_eq+1:].strip()
                # Escape backslash characters with an extra backslash
                substring = substring.replace('\\', '\\\\')
                substrings.append(substring)
    return substrings


# control center variables
controlcenter = r'../../1ControlCenter.block'

ModelVersion  = get_substrings(controlcenter, r'ModelVersion')[0]
RID           = get_substrings(controlcenter, r'RID')[0]
ParentDir     = get_substrings(controlcenter, r'ParentDir')[0]
ScenarioDir   = get_substrings(controlcenter, r'ScenarioDir')[0]
Description   = get_substrings(controlcenter, r'Description')[0]
MasterPrefix  = get_substrings(controlcenter, r'MasterPrefix')[0]


# general parameter variables
genparams = r'../../0GeneralParameters.block'

UsedZones = get_substrings(genparams, r'UsedZones')[0]
HwyNodes  = get_substrings(genparams, r'HwyNodes')[0]
calib     = get_substrings(genparams, r'calib')[2]


