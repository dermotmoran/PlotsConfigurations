
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
################## DATA ###################                                                        
###########################################   
                                                   
samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA*LepWPCut*2', # 2 to get norm ~#Bkg events
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 40
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))

###########################################
#############  BACKGROUNDS  ###############
###########################################

samples['DY'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'DYJetsToTT_MuEle_M-50'),
    'weight': mcCommonWeight,
    'FilesPerJob': 6,
}
addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50', 'ptllDYW_NLO')

samples['TTbar'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1
}
addSampleWeight(samples, 'TTbar', 'TTTo2L2Nu', 'Top_pTrw')

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
    'weight': mcCommonWeight + '*nllW',
    'FilesPerJob': 3
}

############ Normal Higgs Samples ############

samples['ggH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 20
}

samples['qqH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 12
}

samples['ggH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 12,
}


'''
samples['qqH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 12,
}
'''

#### EFT Signals 
 
signals = [] 
 
# Original VBF MC samples 
 
samples['VBF_H0PM_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*VBF_H0PM_W', 
   'FilesPerJob': 1 
} 
 
samples['VBF_H0M_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*VBF_H0M_W', 
   'FilesPerJob': 1 
} 
 
samples['VBF_H0Mf05_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*VBF_H0Mf05_W', 
   'FilesPerJob': 1 
} 
 
samples['VBF_H0PH_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*VBF_H0PH_W', 
   'FilesPerJob': 1 
} 
 
samples['VBF_H0PHf05_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*VBF_H0PHf05_W', 
   'FilesPerJob': 1 
} 
 
samples['VBF_H0L1_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*VBF_H0L1_W', 
   'FilesPerJob': 1 
} 
 
samples['VBF_H0L1f05_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*VBF_H0L1f05_W', 
   'FilesPerJob': 1 
} 
 
# Reweighted VBF samples 
 
samples['VBF_H0PM'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0PM','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(MEH0PM/MEH0PM)')  
addSampleWeight(samples,'VBF_H0PM','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(MEH0PM/MEH0M)')  
addSampleWeight(samples,'VBF_H0PM','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(MEH0PM/MEH0PH)')  
addSampleWeight(samples,'VBF_H0PM','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(MEH0PM/MEH0L1)')  
addSampleWeight(samples,'VBF_H0PM','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(MEH0PM/MEH0Mf05VBF)')   
addSampleWeight(samples,'VBF_H0PM','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(MEH0PM/MEH0PHf05VBF)')  
addSampleWeight(samples,'VBF_H0PM','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(MEH0PM/MEH0L1f05VBF)')  
signals.append('VBF_H0PM')  
 
samples['VBF_H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0M','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(MEH0M_M0/MEH0PM)')  
addSampleWeight(samples,'VBF_H0M','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(MEH0M_M0/MEH0M)')  
addSampleWeight(samples,'VBF_H0M','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(MEH0M_M0/MEH0PH)')  
addSampleWeight(samples,'VBF_H0M','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(MEH0M_M0/MEH0L1)')  
addSampleWeight(samples,'VBF_H0M','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(MEH0M_M0/MEH0Mf05VBF)')   
addSampleWeight(samples,'VBF_H0M','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(MEH0M_M0/MEH0PHf05VBF)')  
addSampleWeight(samples,'VBF_H0M','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(MEH0M_M0/MEH0L1f05VBF)')  
signals.append('VBF_H0M')  
 
samples['VBF_H0M_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0M_M1','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(MEH0M_M1/MEH0PM)')  
addSampleWeight(samples,'VBF_H0M_M1','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(MEH0M_M1/MEH0M)')  
addSampleWeight(samples,'VBF_H0M_M1','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(MEH0M_M1/MEH0PH)')  
addSampleWeight(samples,'VBF_H0M_M1','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(MEH0M_M1/MEH0L1)')  
addSampleWeight(samples,'VBF_H0M_M1','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(MEH0M_M1/MEH0Mf05VBF)')   
addSampleWeight(samples,'VBF_H0M_M1','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(MEH0M_M1/MEH0PHf05VBF)')  
addSampleWeight(samples,'VBF_H0M_M1','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(MEH0M_M1/MEH0L1f05VBF)')  
signals.append('VBF_H0M_M1')  
 
samples['VBF_H0M_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0M_M2','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(MEH0M_M2/MEH0PM)')  
addSampleWeight(samples,'VBF_H0M_M2','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(MEH0M_M2/MEH0M)')  
addSampleWeight(samples,'VBF_H0M_M2','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(MEH0M_M2/MEH0PH)')  
addSampleWeight(samples,'VBF_H0M_M2','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(MEH0M_M2/MEH0L1)')  
addSampleWeight(samples,'VBF_H0M_M2','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(MEH0M_M2/MEH0Mf05VBF)')   
addSampleWeight(samples,'VBF_H0M_M2','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(MEH0M_M2/MEH0PHf05VBF)')  
addSampleWeight(samples,'VBF_H0M_M2','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(MEH0M_M2/MEH0L1f05VBF)')  
signals.append('VBF_H0M_M2')  
 
samples['VBF_H0M_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0M_M3','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(MEH0M_M3/MEH0PM)')  
addSampleWeight(samples,'VBF_H0M_M3','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(MEH0M_M3/MEH0M)')  
addSampleWeight(samples,'VBF_H0M_M3','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(MEH0M_M3/MEH0PH)')  
addSampleWeight(samples,'VBF_H0M_M3','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(MEH0M_M3/MEH0L1)')  
addSampleWeight(samples,'VBF_H0M_M3','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(MEH0M_M3/MEH0Mf05VBF)')   
addSampleWeight(samples,'VBF_H0M_M3','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(MEH0M_M3/MEH0PHf05VBF)')  
addSampleWeight(samples,'VBF_H0M_M3','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(MEH0M_M3/MEH0L1f05VBF)')  
signals.append('VBF_H0M_M3')  
 
samples['VBF_H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0PH','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(MEH0PH_M0/MEH0PM)')  
addSampleWeight(samples,'VBF_H0PH','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(MEH0PH_M0/MEH0M)')  
addSampleWeight(samples,'VBF_H0PH','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(MEH0PH_M0/MEH0PH)')  
addSampleWeight(samples,'VBF_H0PH','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(MEH0PH_M0/MEH0L1)')  
addSampleWeight(samples,'VBF_H0PH','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(MEH0PH_M0/MEH0Mf05VBF)')   
addSampleWeight(samples,'VBF_H0PH','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(MEH0PH_M0/MEH0PHf05VBF)')  
addSampleWeight(samples,'VBF_H0PH','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(MEH0PH_M0/MEH0L1f05VBF)')  
signals.append('VBF_H0PH')  
 
samples['VBF_H0PH_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0PH_M1','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(MEH0PH_M1/MEH0PM)')  
addSampleWeight(samples,'VBF_H0PH_M1','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(MEH0PH_M1/MEH0M)')  
addSampleWeight(samples,'VBF_H0PH_M1','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(MEH0PH_M1/MEH0PH)')  
addSampleWeight(samples,'VBF_H0PH_M1','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(MEH0PH_M1/MEH0L1)')  
addSampleWeight(samples,'VBF_H0PH_M1','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(MEH0PH_M1/MEH0Mf05VBF)')   
addSampleWeight(samples,'VBF_H0PH_M1','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(MEH0PH_M1/MEH0PHf05VBF)')  
addSampleWeight(samples,'VBF_H0PH_M1','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(MEH0PH_M1/MEH0L1f05VBF)')  
signals.append('VBF_H0PH_M1')  
 
samples['VBF_H0PH_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0PH_M2','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(MEH0PH_M2/MEH0PM)')  
addSampleWeight(samples,'VBF_H0PH_M2','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(MEH0PH_M2/MEH0M)')  
addSampleWeight(samples,'VBF_H0PH_M2','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(MEH0PH_M2/MEH0PH)')  
addSampleWeight(samples,'VBF_H0PH_M2','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(MEH0PH_M2/MEH0L1)')  
addSampleWeight(samples,'VBF_H0PH_M2','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(MEH0PH_M2/MEH0Mf05VBF)')   
addSampleWeight(samples,'VBF_H0PH_M2','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(MEH0PH_M2/MEH0PHf05VBF)')  
addSampleWeight(samples,'VBF_H0PH_M2','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(MEH0PH_M2/MEH0L1f05VBF)')  
signals.append('VBF_H0PH_M2')  
 
samples['VBF_H0PH_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0PH_M3','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(MEH0PH_M3/MEH0PM)')  
addSampleWeight(samples,'VBF_H0PH_M3','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(MEH0PH_M3/MEH0M)')  
addSampleWeight(samples,'VBF_H0PH_M3','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(MEH0PH_M3/MEH0PH)')  
addSampleWeight(samples,'VBF_H0PH_M3','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(MEH0PH_M3/MEH0L1)')  
addSampleWeight(samples,'VBF_H0PH_M3','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(MEH0PH_M3/MEH0Mf05VBF)')   
addSampleWeight(samples,'VBF_H0PH_M3','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(MEH0PH_M3/MEH0PHf05VBF)')  
addSampleWeight(samples,'VBF_H0PH_M3','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(MEH0PH_M3/MEH0L1f05VBF)')  
signals.append('VBF_H0PH_M3')  
 
samples['VBF_H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0L1','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(MEH0L1_M0/MEH0PM)')  
addSampleWeight(samples,'VBF_H0L1','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(MEH0L1_M0/MEH0M)')  
addSampleWeight(samples,'VBF_H0L1','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(MEH0L1_M0/MEH0PH)')  
addSampleWeight(samples,'VBF_H0L1','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(MEH0L1_M0/MEH0L1)')  
addSampleWeight(samples,'VBF_H0L1','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(MEH0L1_M0/MEH0Mf05VBF)')   
addSampleWeight(samples,'VBF_H0L1','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(MEH0L1_M0/MEH0PHf05VBF)')  
addSampleWeight(samples,'VBF_H0L1','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(MEH0L1_M0/MEH0L1f05VBF)')  
signals.append('VBF_H0L1')  
 
samples['VBF_H0L1_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0L1_M1','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(MEH0L1_M1/MEH0PM)')  
addSampleWeight(samples,'VBF_H0L1_M1','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(MEH0L1_M1/MEH0M)')  
addSampleWeight(samples,'VBF_H0L1_M1','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(MEH0L1_M1/MEH0PH)')  
addSampleWeight(samples,'VBF_H0L1_M1','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(MEH0L1_M1/MEH0L1)')  
addSampleWeight(samples,'VBF_H0L1_M1','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(MEH0L1_M1/MEH0Mf05VBF)')   
addSampleWeight(samples,'VBF_H0L1_M1','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(MEH0L1_M1/MEH0PHf05VBF)')  
addSampleWeight(samples,'VBF_H0L1_M1','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(MEH0L1_M1/MEH0L1f05VBF)')  
signals.append('VBF_H0L1_M1')  
 
samples['VBF_H0L1_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0L1_M2','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(MEH0L1_M2/MEH0PM)')  
addSampleWeight(samples,'VBF_H0L1_M2','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(MEH0L1_M2/MEH0M)')  
addSampleWeight(samples,'VBF_H0L1_M2','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(MEH0L1_M2/MEH0PH)')  
addSampleWeight(samples,'VBF_H0L1_M2','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(MEH0L1_M2/MEH0L1)')  
addSampleWeight(samples,'VBF_H0L1_M2','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(MEH0L1_M2/MEH0Mf05VBF)')   
addSampleWeight(samples,'VBF_H0L1_M2','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(MEH0L1_M2/MEH0PHf05VBF)')  
addSampleWeight(samples,'VBF_H0L1_M2','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(MEH0L1_M2/MEH0L1f05VBF)')  
signals.append('VBF_H0L1_M2')  
 
samples['VBF_H0L1_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0L1_M3','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(MEH0L1_M3/MEH0PM)')  
addSampleWeight(samples,'VBF_H0L1_M3','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(MEH0L1_M3/MEH0M)')  
addSampleWeight(samples,'VBF_H0L1_M3','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(MEH0L1_M3/MEH0PH)')  
addSampleWeight(samples,'VBF_H0L1_M3','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(MEH0L1_M3/MEH0L1)')  
addSampleWeight(samples,'VBF_H0L1_M3','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(MEH0L1_M3/MEH0Mf05VBF)')   
addSampleWeight(samples,'VBF_H0L1_M3','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(MEH0L1_M3/MEH0PHf05VBF)')  
addSampleWeight(samples,'VBF_H0L1_M3','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(MEH0L1_M3/MEH0L1f05VBF)')  
signals.append('VBF_H0L1_M3')  
 
# Original WH MC samples 
 
samples['WH_H0PM_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*WH_H0PM_W', 
   'FilesPerJob': 1 
} 
 
samples['WH_H0M_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*WH_H0M_W', 
   'FilesPerJob': 1 
} 
 
samples['WH_H0Mf05_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*WH_H0Mf05_W', 
   'FilesPerJob': 1 
} 
 
samples['WH_H0PH_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*WH_H0PH_W', 
   'FilesPerJob': 1 
} 
 
samples['WH_H0PHf05_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*WH_H0PHf05_W', 
   'FilesPerJob': 1 
} 
 
samples['WH_H0L1_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*WH_H0L1_W', 
   'FilesPerJob': 1 
} 
 
samples['WH_H0L1f05_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*WH_H0L1f05_W', 
   'FilesPerJob': 1 
} 
 
# Reweighted WH samples 
 
samples['WH_H0PM'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0PM','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(MEH0PM/MEH0PM)')  
addSampleWeight(samples,'WH_H0PM','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(MEH0PM/MEH0M, 0.9)')  
addSampleWeight(samples,'WH_H0PM','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(MEH0PM/MEH0PH)')  
addSampleWeight(samples,'WH_H0PM','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(MEH0PM/MEH0L1)')  
addSampleWeight(samples,'WH_H0PM','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(MEH0PM/MEH0Mf05WH)')   
addSampleWeight(samples,'WH_H0PM','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(MEH0PM/MEH0PHf05WH)')  
addSampleWeight(samples,'WH_H0PM','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(MEH0PM/MEH0L1f05WH)')  
signals.append('WH_H0PM')  
 
samples['WH_H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0M','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(MEH0M_M0/MEH0PM)')  
addSampleWeight(samples,'WH_H0M','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*(MEH0M_M0/MEH0M)')  
addSampleWeight(samples,'WH_H0M','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(MEH0M_M0/MEH0PH)')  
addSampleWeight(samples,'WH_H0M','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(MEH0M_M0/MEH0L1)')  
addSampleWeight(samples,'WH_H0M','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(MEH0M_M0/MEH0Mf05WH)')   
addSampleWeight(samples,'WH_H0M','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(MEH0M_M0/MEH0PHf05WH)')  
addSampleWeight(samples,'WH_H0M','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(MEH0M_M0/MEH0L1f05WH)')  
signals.append('WH_H0M')  
 
samples['WH_H0M_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0M_M1','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(MEH0M_M1/MEH0PM)')  
addSampleWeight(samples,'WH_H0M_M1','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(MEH0M_M1/MEH0M, 5)')  
addSampleWeight(samples,'WH_H0M_M1','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(MEH0M_M1/MEH0PH)')  
addSampleWeight(samples,'WH_H0M_M1','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(MEH0M_M1/MEH0L1)')  
addSampleWeight(samples,'WH_H0M_M1','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(MEH0M_M1/MEH0Mf05WH)')   
addSampleWeight(samples,'WH_H0M_M1','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(MEH0M_M1/MEH0PHf05WH)')  
addSampleWeight(samples,'WH_H0M_M1','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(MEH0M_M1/MEH0L1f05WH)')  
signals.append('WH_H0M_M1')  
 
samples['WH_H0M_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0M_M2','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(MEH0M_M2/MEH0PM)')  
addSampleWeight(samples,'WH_H0M_M2','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(MEH0M_M2/MEH0M, 20)')  
addSampleWeight(samples,'WH_H0M_M2','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(MEH0M_M2/MEH0PH)')  
addSampleWeight(samples,'WH_H0M_M2','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(MEH0M_M2/MEH0L1)')  
addSampleWeight(samples,'WH_H0M_M2','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(MEH0M_M2/MEH0Mf05WH)')   
addSampleWeight(samples,'WH_H0M_M2','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(MEH0M_M2/MEH0PHf05WH)')  
addSampleWeight(samples,'WH_H0M_M2','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(MEH0M_M2/MEH0L1f05WH)')  
signals.append('WH_H0M_M2')  
 
samples['WH_H0M_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0M_M3','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(MEH0M_M3/MEH0PM)')  
addSampleWeight(samples,'WH_H0M_M3','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(MEH0M_M3/MEH0M, 30)')  
addSampleWeight(samples,'WH_H0M_M3','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(MEH0M_M3/MEH0PH)')  
addSampleWeight(samples,'WH_H0M_M3','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(MEH0M_M3/MEH0L1)')  
addSampleWeight(samples,'WH_H0M_M3','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(MEH0M_M3/MEH0Mf05WH)')   
addSampleWeight(samples,'WH_H0M_M3','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(MEH0M_M3/MEH0PHf05WH)')  
addSampleWeight(samples,'WH_H0M_M3','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(MEH0M_M3/MEH0L1f05WH)')  
signals.append('WH_H0M_M3')  
 
samples['WH_H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0PH','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(MEH0PH_M0/MEH0PM)')  
addSampleWeight(samples,'WH_H0PH','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(MEH0PH_M0/MEH0M, 40)')  
addSampleWeight(samples,'WH_H0PH','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(MEH0PH_M0/MEH0PH)')  
addSampleWeight(samples,'WH_H0PH','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(MEH0PH_M0/MEH0L1)')  
addSampleWeight(samples,'WH_H0PH','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(MEH0PH_M0/MEH0Mf05WH)')   
addSampleWeight(samples,'WH_H0PH','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(MEH0PH_M0/MEH0PHf05WH)')  
addSampleWeight(samples,'WH_H0PH','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(MEH0PH_M0/MEH0L1f05WH)')  
signals.append('WH_H0PH')  
 
samples['WH_H0PH_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0PH_M1','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(MEH0PH_M1/MEH0PM)')  
addSampleWeight(samples,'WH_H0PH_M1','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(MEH0PH_M1/MEH0M, 5)')  
addSampleWeight(samples,'WH_H0PH_M1','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(MEH0PH_M1/MEH0PH)')  
addSampleWeight(samples,'WH_H0PH_M1','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(MEH0PH_M1/MEH0L1)')  
addSampleWeight(samples,'WH_H0PH_M1','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(MEH0PH_M1/MEH0Mf05WH)')   
addSampleWeight(samples,'WH_H0PH_M1','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(MEH0PH_M1/MEH0PHf05WH)')  
addSampleWeight(samples,'WH_H0PH_M1','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(MEH0PH_M1/MEH0L1f05WH)')  
signals.append('WH_H0PH_M1')  
 
samples['WH_H0PH_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0PH_M2','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(MEH0PH_M2/MEH0PM)')  
addSampleWeight(samples,'WH_H0PH_M2','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(MEH0PH_M2/MEH0M, 30)')  
addSampleWeight(samples,'WH_H0PH_M2','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(MEH0PH_M2/MEH0PH)')  
addSampleWeight(samples,'WH_H0PH_M2','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(MEH0PH_M2/MEH0L1)')  
addSampleWeight(samples,'WH_H0PH_M2','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(MEH0PH_M2/MEH0Mf05WH)')   
addSampleWeight(samples,'WH_H0PH_M2','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(MEH0PH_M2/MEH0PHf05WH)')  
addSampleWeight(samples,'WH_H0PH_M2','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(MEH0PH_M2/MEH0L1f05WH)')  
signals.append('WH_H0PH_M2')  
 
samples['WH_H0PH_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0PH_M3','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(MEH0PH_M3/MEH0PM)')  
addSampleWeight(samples,'WH_H0PH_M3','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(MEH0PH_M3/MEH0M, 70)')  
addSampleWeight(samples,'WH_H0PH_M3','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(MEH0PH_M3/MEH0PH)')  
addSampleWeight(samples,'WH_H0PH_M3','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(MEH0PH_M3/MEH0L1)')  
addSampleWeight(samples,'WH_H0PH_M3','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(MEH0PH_M3/MEH0Mf05WH)')   
addSampleWeight(samples,'WH_H0PH_M3','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(MEH0PH_M3/MEH0PHf05WH)')  
addSampleWeight(samples,'WH_H0PH_M3','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(MEH0PH_M3/MEH0L1f05WH)')  
signals.append('WH_H0PH_M3')  
 
samples['WH_H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0L1','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(MEH0L1_M0/MEH0PM)')  
addSampleWeight(samples,'WH_H0L1','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(MEH0L1_M0/MEH0M, 120)')  
addSampleWeight(samples,'WH_H0L1','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(MEH0L1_M0/MEH0PH)')  
addSampleWeight(samples,'WH_H0L1','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(MEH0L1_M0/MEH0L1)')  
addSampleWeight(samples,'WH_H0L1','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(MEH0L1_M0/MEH0Mf05WH)')   
addSampleWeight(samples,'WH_H0L1','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(MEH0L1_M0/MEH0PHf05WH)')  
addSampleWeight(samples,'WH_H0L1','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(MEH0L1_M0/MEH0L1f05WH)')  
signals.append('WH_H0L1')  
 
samples['WH_H0L1_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0L1_M1','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(MEH0L1_M1/MEH0PM)')  
addSampleWeight(samples,'WH_H0L1_M1','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(MEH0L1_M1/MEH0M, 6)')  
addSampleWeight(samples,'WH_H0L1_M1','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(MEH0L1_M1/MEH0PH)')  
addSampleWeight(samples,'WH_H0L1_M1','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(MEH0L1_M1/MEH0L1)')  
addSampleWeight(samples,'WH_H0L1_M1','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(MEH0L1_M1/MEH0Mf05WH)')   
addSampleWeight(samples,'WH_H0L1_M1','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(MEH0L1_M1/MEH0PHf05WH)')  
addSampleWeight(samples,'WH_H0L1_M1','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(MEH0L1_M1/MEH0L1f05WH)')  
signals.append('WH_H0L1_M1')  
 
samples['WH_H0L1_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0L1_M2','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(MEH0L1_M2/MEH0PM)')  
addSampleWeight(samples,'WH_H0L1_M2','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(MEH0L1_M2/MEH0M, 20)')  
addSampleWeight(samples,'WH_H0L1_M2','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(MEH0L1_M2/MEH0PH)')  
addSampleWeight(samples,'WH_H0L1_M2','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(MEH0L1_M2/MEH0L1)')  
addSampleWeight(samples,'WH_H0L1_M2','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(MEH0L1_M2/MEH0Mf05WH)')   
addSampleWeight(samples,'WH_H0L1_M2','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(MEH0L1_M2/MEH0PHf05WH)')  
addSampleWeight(samples,'WH_H0L1_M2','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(MEH0L1_M2/MEH0L1f05WH)')  
signals.append('WH_H0L1_M2')  
 
samples['WH_H0L1_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0L1_M3','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(MEH0L1_M3/MEH0PM)')  
addSampleWeight(samples,'WH_H0L1_M3','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(MEH0L1_M3/MEH0M, 30)')  
addSampleWeight(samples,'WH_H0L1_M3','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(MEH0L1_M3/MEH0PH)')  
addSampleWeight(samples,'WH_H0L1_M3','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(MEH0L1_M3/MEH0L1)')  
addSampleWeight(samples,'WH_H0L1_M3','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(MEH0L1_M3/MEH0Mf05WH)')   
addSampleWeight(samples,'WH_H0L1_M3','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(MEH0L1_M3/MEH0PHf05WH)')  
addSampleWeight(samples,'WH_H0L1_M3','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(MEH0L1_M3/MEH0L1f05WH)')  
signals.append('WH_H0L1_M3')  
 
# Original ZH MC samples 
 
samples['ZH_H0PM_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*ZH_H0PM_W', 
   'FilesPerJob': 1 
} 
 
samples['ZH_H0M_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*ZH_H0M_W', 
   'FilesPerJob': 1 
} 
 
samples['ZH_H0Mf05_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*ZH_H0Mf05_W', 
   'FilesPerJob': 1 
} 
 
samples['ZH_H0PH_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*ZH_H0PH_W', 
   'FilesPerJob': 1 
} 
 
samples['ZH_H0PHf05_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*ZH_H0PHf05_W', 
   'FilesPerJob': 1 
} 
 
samples['ZH_H0L1_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*ZH_H0L1_W', 
   'FilesPerJob': 1 
} 
 
samples['ZH_H0L1f05_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*ZH_H0L1f05_W', 
   'FilesPerJob': 1 
} 
 
# Reweighted ZH samples 
 
samples['ZH_H0PM'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0PM','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(MEH0PM/MEH0PM)')  
addSampleWeight(samples,'ZH_H0PM','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(MEH0PM/MEH0M, 0.9)')  
addSampleWeight(samples,'ZH_H0PM','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(MEH0PM/MEH0PH)')  
addSampleWeight(samples,'ZH_H0PM','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(MEH0PM/MEH0L1)')  
addSampleWeight(samples,'ZH_H0PM','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(MEH0PM/MEH0Mf05ZH)')   
addSampleWeight(samples,'ZH_H0PM','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(MEH0PM/MEH0PHf05ZH)')  
addSampleWeight(samples,'ZH_H0PM','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(MEH0PM/MEH0L1f05ZH)')  
signals.append('ZH_H0PM')  
 
samples['ZH_H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0M','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(MEH0M_M0/MEH0PM)')  
addSampleWeight(samples,'ZH_H0M','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*(MEH0M_M0/MEH0M)')  
addSampleWeight(samples,'ZH_H0M','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(MEH0M_M0/MEH0PH)')  
addSampleWeight(samples,'ZH_H0M','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(MEH0M_M0/MEH0L1)')  
addSampleWeight(samples,'ZH_H0M','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(MEH0M_M0/MEH0Mf05ZH)')   
addSampleWeight(samples,'ZH_H0M','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(MEH0M_M0/MEH0PHf05ZH)')  
addSampleWeight(samples,'ZH_H0M','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(MEH0M_M0/MEH0L1f05ZH)')  
signals.append('ZH_H0M')  
 
samples['ZH_H0M_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0M_M1','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(MEH0M_M1/MEH0PM)')  
addSampleWeight(samples,'ZH_H0M_M1','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(MEH0M_M1/MEH0M, 5)')  
addSampleWeight(samples,'ZH_H0M_M1','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(MEH0M_M1/MEH0PH)')  
addSampleWeight(samples,'ZH_H0M_M1','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(MEH0M_M1/MEH0L1)')  
addSampleWeight(samples,'ZH_H0M_M1','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(MEH0M_M1/MEH0Mf05ZH)')   
addSampleWeight(samples,'ZH_H0M_M1','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(MEH0M_M1/MEH0PHf05ZH)')  
addSampleWeight(samples,'ZH_H0M_M1','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(MEH0M_M1/MEH0L1f05ZH)')  
signals.append('ZH_H0M_M1')  
 
samples['ZH_H0M_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0M_M2','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(MEH0M_M2/MEH0PM)')  
addSampleWeight(samples,'ZH_H0M_M2','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(MEH0M_M2/MEH0M, 20)')  
addSampleWeight(samples,'ZH_H0M_M2','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(MEH0M_M2/MEH0PH)')  
addSampleWeight(samples,'ZH_H0M_M2','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(MEH0M_M2/MEH0L1)')  
addSampleWeight(samples,'ZH_H0M_M2','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(MEH0M_M2/MEH0Mf05ZH)')   
addSampleWeight(samples,'ZH_H0M_M2','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(MEH0M_M2/MEH0PHf05ZH)')  
addSampleWeight(samples,'ZH_H0M_M2','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(MEH0M_M2/MEH0L1f05ZH)')  
signals.append('ZH_H0M_M2')  
 
samples['ZH_H0M_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0M_M3','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(MEH0M_M3/MEH0PM)')  
addSampleWeight(samples,'ZH_H0M_M3','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(MEH0M_M3/MEH0M, 30)')  
addSampleWeight(samples,'ZH_H0M_M3','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(MEH0M_M3/MEH0PH)')  
addSampleWeight(samples,'ZH_H0M_M3','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(MEH0M_M3/MEH0L1)')  
addSampleWeight(samples,'ZH_H0M_M3','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(MEH0M_M3/MEH0Mf05ZH)')   
addSampleWeight(samples,'ZH_H0M_M3','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(MEH0M_M3/MEH0PHf05ZH)')  
addSampleWeight(samples,'ZH_H0M_M3','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(MEH0M_M3/MEH0L1f05ZH)')  
signals.append('ZH_H0M_M3')  
 
samples['ZH_H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0PH','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(MEH0PH_M0/MEH0PM)')  
addSampleWeight(samples,'ZH_H0PH','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(MEH0PH_M0/MEH0M, 40)')  
addSampleWeight(samples,'ZH_H0PH','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(MEH0PH_M0/MEH0PH)')  
addSampleWeight(samples,'ZH_H0PH','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(MEH0PH_M0/MEH0L1)')  
addSampleWeight(samples,'ZH_H0PH','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(MEH0PH_M0/MEH0Mf05ZH)')   
addSampleWeight(samples,'ZH_H0PH','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(MEH0PH_M0/MEH0PHf05ZH)')  
addSampleWeight(samples,'ZH_H0PH','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(MEH0PH_M0/MEH0L1f05ZH)')  
signals.append('ZH_H0PH')  
 
samples['ZH_H0PH_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0PH_M1','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(MEH0PH_M1/MEH0PM)')  
addSampleWeight(samples,'ZH_H0PH_M1','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(MEH0PH_M1/MEH0M, 5)')  
addSampleWeight(samples,'ZH_H0PH_M1','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(MEH0PH_M1/MEH0PH)')  
addSampleWeight(samples,'ZH_H0PH_M1','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(MEH0PH_M1/MEH0L1)')  
addSampleWeight(samples,'ZH_H0PH_M1','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(MEH0PH_M1/MEH0Mf05ZH)')   
addSampleWeight(samples,'ZH_H0PH_M1','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(MEH0PH_M1/MEH0PHf05ZH)')  
addSampleWeight(samples,'ZH_H0PH_M1','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(MEH0PH_M1/MEH0L1f05ZH)')  
signals.append('ZH_H0PH_M1')  
 
samples['ZH_H0PH_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0PH_M2','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(MEH0PH_M2/MEH0PM)')  
addSampleWeight(samples,'ZH_H0PH_M2','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(MEH0PH_M2/MEH0M, 30)')  
addSampleWeight(samples,'ZH_H0PH_M2','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(MEH0PH_M2/MEH0PH)')  
addSampleWeight(samples,'ZH_H0PH_M2','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(MEH0PH_M2/MEH0L1)')  
addSampleWeight(samples,'ZH_H0PH_M2','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(MEH0PH_M2/MEH0Mf05ZH)')   
addSampleWeight(samples,'ZH_H0PH_M2','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(MEH0PH_M2/MEH0PHf05ZH)')  
addSampleWeight(samples,'ZH_H0PH_M2','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(MEH0PH_M2/MEH0L1f05ZH)')  
signals.append('ZH_H0PH_M2')  
 
samples['ZH_H0PH_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0PH_M3','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(MEH0PH_M3/MEH0PM)')  
addSampleWeight(samples,'ZH_H0PH_M3','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(MEH0PH_M3/MEH0M, 70)')  
addSampleWeight(samples,'ZH_H0PH_M3','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(MEH0PH_M3/MEH0PH)')  
addSampleWeight(samples,'ZH_H0PH_M3','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(MEH0PH_M3/MEH0L1)')  
addSampleWeight(samples,'ZH_H0PH_M3','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(MEH0PH_M3/MEH0Mf05ZH)')   
addSampleWeight(samples,'ZH_H0PH_M3','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(MEH0PH_M3/MEH0PHf05ZH)')  
addSampleWeight(samples,'ZH_H0PH_M3','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(MEH0PH_M3/MEH0L1f05ZH)')  
signals.append('ZH_H0PH_M3')  
 
samples['ZH_H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0L1','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(MEH0L1_M0/MEH0PM)')  
addSampleWeight(samples,'ZH_H0L1','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(MEH0L1_M0/MEH0M, 120)')  
addSampleWeight(samples,'ZH_H0L1','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(MEH0L1_M0/MEH0PH)')  
addSampleWeight(samples,'ZH_H0L1','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(MEH0L1_M0/MEH0L1)')  
addSampleWeight(samples,'ZH_H0L1','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(MEH0L1_M0/MEH0Mf05ZH)')   
addSampleWeight(samples,'ZH_H0L1','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(MEH0L1_M0/MEH0PHf05ZH)')  
addSampleWeight(samples,'ZH_H0L1','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(MEH0L1_M0/MEH0L1f05ZH)')  
signals.append('ZH_H0L1')  
 
samples['ZH_H0L1_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0L1_M1','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(MEH0L1_M1/MEH0PM)')  
addSampleWeight(samples,'ZH_H0L1_M1','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(MEH0L1_M1/MEH0M, 6)')  
addSampleWeight(samples,'ZH_H0L1_M1','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(MEH0L1_M1/MEH0PH)')  
addSampleWeight(samples,'ZH_H0L1_M1','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(MEH0L1_M1/MEH0L1)')  
addSampleWeight(samples,'ZH_H0L1_M1','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(MEH0L1_M1/MEH0Mf05ZH)')   
addSampleWeight(samples,'ZH_H0L1_M1','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(MEH0L1_M1/MEH0PHf05ZH)')  
addSampleWeight(samples,'ZH_H0L1_M1','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(MEH0L1_M1/MEH0L1f05ZH)')  
signals.append('ZH_H0L1_M1')  
 
samples['ZH_H0L1_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0L1_M2','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(MEH0L1_M2/MEH0PM)')  
addSampleWeight(samples,'ZH_H0L1_M2','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(MEH0L1_M2/MEH0M, 20)')  
addSampleWeight(samples,'ZH_H0L1_M2','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(MEH0L1_M2/MEH0PH)')  
addSampleWeight(samples,'ZH_H0L1_M2','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(MEH0L1_M2/MEH0L1)')  
addSampleWeight(samples,'ZH_H0L1_M2','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(MEH0L1_M2/MEH0Mf05ZH)')   
addSampleWeight(samples,'ZH_H0L1_M2','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(MEH0L1_M2/MEH0PHf05ZH)')  
addSampleWeight(samples,'ZH_H0L1_M2','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(MEH0L1_M2/MEH0L1f05ZH)')  
signals.append('ZH_H0L1_M2')  
 
samples['ZH_H0L1_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0L1_M3','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(MEH0L1_M3/MEH0PM)')  
addSampleWeight(samples,'ZH_H0L1_M3','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(MEH0L1_M3/MEH0M, 30)')  
addSampleWeight(samples,'ZH_H0L1_M3','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(MEH0L1_M3/MEH0PH)')  
addSampleWeight(samples,'ZH_H0L1_M3','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(MEH0L1_M3/MEH0L1)')  
addSampleWeight(samples,'ZH_H0L1_M3','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(MEH0L1_M3/MEH0Mf05ZH)')   
addSampleWeight(samples,'ZH_H0L1_M3','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(MEH0L1_M3/MEH0PHf05ZH)')  
addSampleWeight(samples,'ZH_H0L1_M3','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(MEH0L1_M3/MEH0L1f05ZH)')  
signals.append('ZH_H0L1_M3')  
 
