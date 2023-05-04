# imports
from IPython.display import display, Markdown
from dbfread import DBF
import pandas as pd
import os
import geopandas as gpd


# functions
def clean(string):
    return string.replace("'", "")

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
controlcenter = os.path.abspath(os.path.join(os.path.dirname(__file__), controlcenter))

ModelVersion      = clean(get_substrings(controlcenter, r'ModelVersion')[0])
UserName          = clean(get_substrings(controlcenter, r'UserName')[0])
UserCompany       = clean(get_substrings(controlcenter, r'UserCompany')[0])
RID               = clean(get_substrings(controlcenter, r'RID')[0])
PythonPath        = clean(get_substrings(controlcenter, r'PythonPath')[0])
Run_UpdateTAZID   = clean(get_substrings(controlcenter, r'Run_UpdateTAZID')[0])
Run_WalkBuffer    = clean(get_substrings(controlcenter, r'Run_WalkBuffer')[0])
TAZ_DBF           = clean(get_substrings(controlcenter, r'TAZ_DBF')[0])
DISTLRG           = 'DISTLRG'
DISTMED           = 'DISTMED'
DISTSML           = 'DISTSML'
EcoEdPassZones    = clean(get_substrings(controlcenter, r'EcoEdPassZones')[0])
FreeFareZones     = clean(get_substrings(controlcenter, r'FreeFareZones')[0])
DemographicYear   = clean(get_substrings(controlcenter, r'DemographicYear')[0])
BE_SEFile         = clean(get_substrings(controlcenter, r'BE_SEFile')[0])
WFRC_SEFile       = clean(get_substrings(controlcenter, r'WFRC_SEFile')[0])
MAG_SEFile        = clean(get_substrings(controlcenter, r'MAG_SEFile')[0])
NetworkYear       = clean(get_substrings(controlcenter, r'NetworkYear')[0])  
UnloadedNetPrefix = clean(get_substrings(controlcenter, r'UnloadedNetPrefix')[0])
MasterPrefix      = clean(get_substrings(controlcenter, r'MasterPrefix')[0])
DefaultProjFile   = clean(get_substrings(controlcenter, r'DefaultProjFile')[0])
tollz_shp         = clean(get_substrings(controlcenter, r'tollz_shp')[0])
pnr_field         = clean(get_substrings(controlcenter, r'pnr_field')[0])
CRT_Fare_Zone     = clean(get_substrings(controlcenter, r'CRT_Fare_Zone')[0])
AddNodeFields     = ';'
LNfield           = clean(get_substrings(controlcenter, r'LNfield')[0])
FTfield           = clean(get_substrings(controlcenter, r'FTfield')[0])
HOVmarker         = clean(get_substrings(controlcenter, r'HOVmarker')[0])
SpdFactor         = clean(get_substrings(controlcenter, r'SpdFactor')[0])
CapFactor         = clean(get_substrings(controlcenter, r'CapFactor')[0])
TranSpeedField    = clean(get_substrings(controlcenter, r'TranSpeedField ')[0])
Rel_LN            = clean(get_substrings(controlcenter, r'Rel_LN')[0])
HOT_Toll_Min      = clean(get_substrings(controlcenter, r'HOT_Toll_Min')[0])
HOT_Toll_Max      = clean(get_substrings(controlcenter, r'HOT_Toll_Max')[0])
AddLinkFields     = ';'
Mlin              = clean(get_substrings(controlcenter, r'Mlin')[0])
Ext_Vol_Count     = clean(get_substrings(controlcenter, r'Ext_Vol_Count')[0])
Ext_TripEndPattern= clean(get_substrings(controlcenter, r'Ext_TripEndPattern')[0])
Ext_TripTable     = clean(get_substrings(controlcenter, r'Ext_TripTable')[0])
ScenarioDir       = clean(get_substrings(controlcenter, r'ScenarioDir')[0])
SpeedCapLookupFile= clean(get_substrings(controlcenter, r'SpeedCapLookupFile')[0])


# general parameter variables
genparams = r'../../0GeneralParameters.block'
genparams = os.path.abspath(os.path.join(os.path.dirname(__file__), genparams))

UsedZones = clean(get_substrings(genparams, r'UsedZones')[0])
HwyNodes  = clean(get_substrings(genparams, r'HwyNodes')[0])
calib     = clean(get_substrings(genparams, r'calib')[2])
calib2    = 'hello'


# se
se_file         = r'../../0_InputProcessing/SE_File_' + RID + '.dbf'
control_se_file = r'../../../../1_Inputs/2_SEData/_ControlTotals/ControlTotal_SE_AllCounties.csv'

df_se_file                     = pd.DataFrame(DBF(os.path.abspath(os.path.join(os.path.dirname(__file__), se_file)),load=True))
df_ControlTotal_SE_AllCounties = pd.read_csv(os.path.abspath(os.path.join(os.path.dirname(__file__), control_se_file))) 

# taz
taz_file = r'../../../../1_Inputs/1_TAZ/TAZ.shp'
taz_shp = gpd.read_file(os.path.abspath(os.path.join(os.path.dirname(__file__), taz_file))) 


