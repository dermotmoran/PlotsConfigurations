
import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # VBFH2016
configurations = os.path.dirname(configurations) # EFT
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

################################################
################# SKIMS ########################
################################################

mcProduction  = 'Summer16_102X_nAODv5_Full2016v6'
mcSteps = 'MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6{var}__VBFl2EFT'

dataReco = 'Run2016_102X_nAODv5_Full2016v6'
dataSteps = 'DATAl1loose2016v6__l2loose__l2tightOR2016v6__VBFl2EFT'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory  = makeMCDirectory()

dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include bstag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'
 




