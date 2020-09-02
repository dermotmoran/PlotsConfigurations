
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

###########################################
#############  VBF AC SIGNALS  ##################
###########################################

signals = []

samples['VBFH0PM'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2
}
signals.append('VBFH0PM')

samples['VBFH0M'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu'),
    'weight': mcCommonWeight + '*VBFH0M_W',
    'FilesPerJob': 1
}
signals.append('VBFH0M')


samples['VBFH0M_H10'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
}

addSampleWeight(samples,'VBFH0M_H10','VBF_H0M_ToWWTo2L2Nu',    'VBFH0M_W*(HM10/(gen_pme_hm*gen_dme_hm))*.5') 
addSampleWeight(samples,'VBFH0M_H10','VBF_H0PM_ToWWTo2L2Nu',   '(HM10/(gen_pme_hsm*gen_dme_hsm))*.5')
signals.append('VBFH0M_H10')

samples['VBFH0M_H1p50'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
}

addSampleWeight(samples,'VBFH0M_H1p50','VBF_H0M_ToWWTo2L2Nu',    'VBFH0M_W*(HM1p50/(gen_pme_hm*gen_dme_hm))*.5') 
addSampleWeight(samples,'VBFH0M_H1p50','VBF_H0PM_ToWWTo2L2Nu',   '(HM1p50/(gen_pme_hsm*gen_dme_hsm))*.5')
signals.append('VBFH0M_H1p50')


samples['VBFH0M_H01'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
}

addSampleWeight(samples,'VBFH0M_H01','VBF_H0M_ToWWTo2L2Nu',    'VBFH0M_W*(HM01/(gen_pme_hm*gen_dme_hm))*.5') 
addSampleWeight(samples,'VBFH0M_H01','VBF_H0PM_ToWWTo2L2Nu',   '(HM01/(gen_pme_hsm*gen_dme_hsm))*.5')
signals.append('VBFH0M_H01')




'''
samples['VBFH0PH'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu'),
    'weight': mcCommonWeight + '*VBFH0PH_W',
    'FilesPerJob': 2
}
signals.append('VBFH0PH')

samples['VBFH0PH_Int'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2
}
addSampleWeight(samples,'VBFH0PH_Int','VBF_H0PHf05_ToWWTo2L2Nu', 'VBFH0PHf05_W*(1/g2_VBF)')
addSampleWeight(samples,'VBFH0PH_Int','VBF_H0PH_ToWWTo2L2Nu',    'VBFH0PH_W*g2_VBF*-1') 
addSampleWeight(samples,'VBFH0PH_Int','VBF_H0PM_ToWWTo2L2Nu',    '(1/g2_VBF)*-1')
signals.append('VBFH0PH_Int')
'''

'''
samples['VBFH0L1'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu'),
    'weight': mcCommonWeight + '*VBFH0L1_W',
    'FilesPerJob': 2
}
signals.append('VBFH0L1')
'''

###########################################
#############  VH  AC SIGNALS  ##################
###########################################

samples['VH0PM'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu' ) + \
            nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu' ),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}
signals.append('VH0PM')

samples['VH0M'] = {
    'name':  nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu' ) + \
             nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu' ),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}
addSampleWeight(samples,'VH0M','WH_H0M_ToWWTo2L2Nu','WH0M_W')
addSampleWeight(samples,'VH0M','ZH_H0M_ToWWTo2L2Nu','ZH0M_W')
signals.append('VH0M')

samples['VH0M_Int'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') ,
    'weight': mcCommonWeight,
    'FilesPerJob': 2,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
}
addSampleWeight(samples,'VH0M_Int','WH_H0Mf05_ToWWTo2L2Nu', 'WH0Mf05_W*(1/g4_WH)')
addSampleWeight(samples,'VH0M_Int','ZH_H0Mf05_ToWWTo2L2Nu', 'ZH0Mf05_W*(1/g4_ZH)')
addSampleWeight(samples,'VH0M_Int','WH_H0M_ToWWTo2L2Nu',    'WH0M_W*g4_WH*-1') 
addSampleWeight(samples,'VH0M_Int','ZH_H0M_ToWWTo2L2Nu',    'ZH0M_W*g4_ZH*-1') 
addSampleWeight(samples,'VH0M_Int','WH_H0PM_ToWWTo2L2Nu',   '(1/g4_WH)*-1')
addSampleWeight(samples,'VH0M_Int','ZH_H0PM_ToWWTo2L2Nu',   '(1/g4_ZH)*-1')
signals.append('VH0M_Int')


'''
samples['VH0PH'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu' ) + \
            nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu' ),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}
addSampleWeight(samples,'VH0PH','WH_H0PH_ToWWTo2L2Nu','WH0PH_W')
addSampleWeight(samples,'VH0PH','ZH_H0PH_ToWWTo2L2Nu','ZH0PH_W')
signals.append('VH0PH')

samples['VH0PH_Int'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + \
              nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') ,
    'weight': mcCommonWeight,
    'FilesPerJob': 2
}
addSampleWeight(samples,'VH0PH_Int','WH_H0PHf05_ToWWTo2L2Nu', 'WH0PHf05_W*(1/g2_WH)')
addSampleWeight(samples,'VH0PH_Int','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH0PHf05_W*(1/g2_ZH)')
addSampleWeight(samples,'VH0PH_Int','WH_H0PH_ToWWTo2L2Nu', 'WH0PH_W*g2_WH*-1') 
addSampleWeight(samples,'VH0PH_Int','ZH_H0PH_ToWWTo2L2Nu', 'ZH0PH_W*g2_ZH*-1') 
addSampleWeight(samples,'VH0PH_Int','WH_H0PM_ToWWTo2L2Nu', '(1/g2_WH)*-1')
addSampleWeight(samples,'VH0PH_Int','ZH_H0PM_ToWWTo2L2Nu', '(1/g2_ZH)*-1')
signals.append('VH0PH_Int')
'''

'''
samples['VH0L1'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu' ) + \
            nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu' ),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}
addSampleWeight(samples,'VH0L1','WH_H0L1_ToWWTo2L2Nu','WH0L1_W')
addSampleWeight(samples,'VH0L1','ZH_H0L1_ToWWTo2L2Nu','ZH0L1_W')
signals.append('VH0L1')
'''

############ Normal Higgs Samples ############

samples['ggH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 20
}
signals.append('ggH_htt')

samples['qqH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 12
}
signals.append('qqH_htt')

samples['ggH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 12,
}
signals.append('ggH_hww')


'''
samples['qqH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 12,
}
signals.append('qqH_hww')
'''
