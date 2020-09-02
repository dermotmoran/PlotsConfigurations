
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

################################################                                                   
############ DATA DECLARATION ##################                                                   
################################################                                
                   
DataRun = [
    ['F','Run2016F-Nano1June2019-v1'],
    ['G','Run2016G-Nano1June2019-v1'],
    ['H','Run2016H-Nano1June2019-v1']
]

DataSets = ['MuonEG']

DataTrig = {
    'MuonEG'         : ' Trigger_ElMu' ,
}

#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include bstag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'
                                  
###########################################
#############  VBF AC SIGNALS  ##################
###########################################

signals = []

samples['VBFH0PM'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'),
    'weight': mcCommonWeight + '*(1/7)',
    'FilesPerJob': 2,
}
addSampleWeight(samples,'VBFH0PM','VBF_H0M_ToWWTo2L2Nu',     'VBFH0M_W*(MEH0PM/MEH0M)') 
addSampleWeight(samples,'VBFH0PM','VBF_H0PH_ToWWTo2L2Nu',    'VBFH0PH_W*(MEH0PM/MEH0PH)')
addSampleWeight(samples,'VBFH0PM','VBF_H0L1_ToWWTo2L2Nu',    'VBFH0L1_W*(MEH0PM/MEH0L1)')
addSampleWeight(samples,'VBFH0PM','VBF_H0Mf05_ToWWTo2L2Nu',  'VBFH0Mf05_W*(MEH0PM/MEH0Mf05VBF)') 
addSampleWeight(samples,'VBFH0PM','VBF_H0PHf05_ToWWTo2L2Nu', 'VBFH0PHf05_W*(MEH0PM/MEH0PHf05VBF)')
addSampleWeight(samples,'VBFH0PM','VBF_H0L1f05_ToWWTo2L2Nu', 'VBFH0L1f05_W*(MEH0PM/MEH0L1f05VBF)')
signals.append('VBFH0PM')


samples['VBFH0M'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'),
    'weight': mcCommonWeight + '*(1/7)',
    'FilesPerJob': 2,
}
addSampleWeight(samples,'VBFH0M','VBF_H0PM_ToWWTo2L2Nu',    '(MEH0M/MEH0PM)')
addSampleWeight(samples,'VBFH0M','VBF_H0M_ToWWTo2L2Nu',     'VBFH0M_W') 
addSampleWeight(samples,'VBFH0M','VBF_H0PH_ToWWTo2L2Nu',    'VBFH0PH_W*(MEH0M/MEH0PH)')
addSampleWeight(samples,'VBFH0M','VBF_H0L1_ToWWTo2L2Nu',    'VBFH0L1_W*(MEH0M/MEH0L1)')
addSampleWeight(samples,'VBFH0M','VBF_H0Mf05_ToWWTo2L2Nu',  'VBFH0Mf05_W*(MEH0M/MEH0Mf05VBF)') 
addSampleWeight(samples,'VBFH0M','VBF_H0PHf05_ToWWTo2L2Nu', 'VBFH0PHf05_W*(MEH0M/MEH0PHf05VBF)')
addSampleWeight(samples,'VBFH0M','VBF_H0L1f05_ToWWTo2L2Nu', 'VBFH0L1f05_W*(MEH0M/MEH0L1f05VBF)')
signals.append('VBFH0M')

samples['VBFH0Mp25'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'),
    'weight': mcCommonWeight + '*(1/7)',
    'FilesPerJob': 2,
}
addSampleWeight(samples,'VBFH0Mp25','VBF_H0PM_ToWWTo2L2Nu',    '(MEH0Mp25/MEH0PM)')
addSampleWeight(samples,'VBFH0Mp25','VBF_H0M_ToWWTo2L2Nu',     'VBFH0M_W*(MEH0Mp25/MEH0M)') 
addSampleWeight(samples,'VBFH0Mp25','VBF_H0PH_ToWWTo2L2Nu',    'VBFH0PH_W*(MEH0Mp25/MEH0PH)')
addSampleWeight(samples,'VBFH0Mp25','VBF_H0L1_ToWWTo2L2Nu',    'VBFH0L1_W*(MEH0Mp25/MEH0L1)')
addSampleWeight(samples,'VBFH0Mp25','VBF_H0Mf05_ToWWTo2L2Nu',  'VBFH0Mf05_W*(MEH0Mp25/MEH0Mf05VBF)') 
addSampleWeight(samples,'VBFH0Mp25','VBF_H0PHf05_ToWWTo2L2Nu', 'VBFH0PHf05_W*(MEH0Mp25/MEH0PHf05VBF)')
addSampleWeight(samples,'VBFH0Mp25','VBF_H0L1f05_ToWWTo2L2Nu', 'VBFH0L1f05_W*(MEH0Mp25/MEH0L1f05VBF)')
signals.append('VBFH0Mp25')

samples['VBFH0Mp50'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'),
    'weight': mcCommonWeight + '*(1/7)',
    'FilesPerJob': 2,
}
addSampleWeight(samples,'VBFH0Mp50','VBF_H0PM_ToWWTo2L2Nu',    '(MEH0Mp50/MEH0PM)')
addSampleWeight(samples,'VBFH0Mp50','VBF_H0M_ToWWTo2L2Nu',     'VBFH0M_W*(MEH0Mp50/MEH0M)') 
addSampleWeight(samples,'VBFH0Mp50','VBF_H0PH_ToWWTo2L2Nu',    'VBFH0PH_W*(MEH0Mp50/MEH0PH)')
addSampleWeight(samples,'VBFH0Mp50','VBF_H0L1_ToWWTo2L2Nu',    'VBFH0L1_W*(MEH0Mp50/MEH0L1)')
addSampleWeight(samples,'VBFH0Mp50','VBF_H0Mf05_ToWWTo2L2Nu',  'VBFH0Mf05_W*(MEH0Mp50/MEH0Mf05VBF)') 
addSampleWeight(samples,'VBFH0Mp50','VBF_H0PHf05_ToWWTo2L2Nu', 'VBFH0PHf05_W*(MEH0Mp50/MEH0PHf05VBF)')
addSampleWeight(samples,'VBFH0Mp50','VBF_H0L1f05_ToWWTo2L2Nu', 'VBFH0L1f05_W*(MEH0Mp50/MEH0L1f05VBF)')
signals.append('VBFH0Mp50')

samples['VBFH0Mp75'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'),
    'weight': mcCommonWeight + '*(1/7)',
    'FilesPerJob': 2,
}
addSampleWeight(samples,'VBFH0Mp75','VBF_H0PM_ToWWTo2L2Nu',    '(MEH0Mp75/MEH0PM)')
addSampleWeight(samples,'VBFH0Mp75','VBF_H0M_ToWWTo2L2Nu',     'VBFH0M_W*(MEH0Mp75/MEH0M)') 
addSampleWeight(samples,'VBFH0Mp75','VBF_H0PH_ToWWTo2L2Nu',    'VBFH0PH_W*(MEH0Mp75/MEH0PH)')
addSampleWeight(samples,'VBFH0Mp75','VBF_H0L1_ToWWTo2L2Nu',    'VBFH0L1_W*(MEH0Mp75/MEH0L1)')
addSampleWeight(samples,'VBFH0Mp75','VBF_H0Mf05_ToWWTo2L2Nu',  'VBFH0Mf05_W*(MEH0Mp75/MEH0Mf05VBF)') 
addSampleWeight(samples,'VBFH0Mp75','VBF_H0PHf05_ToWWTo2L2Nu', 'VBFH0PHf05_W*(MEH0Mp75/MEH0PHf05VBF)')
addSampleWeight(samples,'VBFH0Mp75','VBF_H0L1f05_ToWWTo2L2Nu', 'VBFH0L1f05_W*(MEH0Mp75/MEH0L1f05VBF)')
signals.append('VBFH0Mp75')

####################################################################

samples['VBFH0M_Org'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu'),
    'weight': mcCommonWeight + '*VBFH0M_W',
    'FilesPerJob': 1
}
signals.append('VBFH0M_Org')

samples['VBFH0PM_Org'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1
}
signals.append('VBFH0PM_Org')


