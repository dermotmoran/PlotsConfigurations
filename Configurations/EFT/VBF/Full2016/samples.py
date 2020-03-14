
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

#mcProduction  = 'Summer16_102X_nAODv5_SigOnly_Full2016v5'
#bmcProduction = 'Summer16_102X_nAODv4_Full2016v5'
#mcSteps = 'MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5{var}__VBFl2EFT'

mcProduction  = 'Summer16_102X_nAODv5_Full2016v6'
bmcProduction = 'Summer16_102X_nAODv5_Full2016v6'
mcSteps = 'MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6{var}__VBFl2EFT'

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

def makebMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, bmcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, bmcProduction, mcSteps.format(var=''))

mcDirectory  = makeMCDirectory()
bmcDirectory = makebMCDirectory()

#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

samples['DY'] = {
    'name': nanoGetSampleFiles(bmcDirectory, 'DYJetsToTT_MuEle_M-50'),
    'weight': mcCommonWeight,
    'FilesPerJob': 6,
}

addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50', 'ptllDYW_NLO')

samples['TTbar'] = {
    'name': nanoGetSampleFiles(bmcDirectory, 'TTTo2L2Nu'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1
}

addSampleWeight(samples, 'TTbar', 'TTTo2L2Nu', 'Top_pTrw')

samples['WW'] = {
    'name': nanoGetSampleFiles(bmcDirectory, 'WWTo2L2Nu'),
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

samples['VBFH0M_rw'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu'),
    'weight': mcCommonWeight + '*VBFH0M_W*(gen_me_mixhm/gen_me_hm)',
    'FilesPerJob': 1
}
signals.append('VBFH0M_rw')

samples['VBFH0Mf05'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu'),
    'weight': mcCommonWeight + '*VBFH0Mf05_W',
    'FilesPerJob': 1
}
signals.append('VBFH0Mf05')

samples['VBFH0PH'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu'),
    'weight': mcCommonWeight + '*VBFH0PH_W',
    'FilesPerJob': 2
}
signals.append('VBFH0PH')

samples['VBFH0PH_rw'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu'),
    'weight': mcCommonWeight + '*VBFH0PH_W*(gen_me_mixhp/gen_me_hp)',
    'FilesPerJob': 2
}
signals.append('VBFH0PH_rw')

samples['VBFH0PHf05'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu'),
    'weight': mcCommonWeight  + '*VBFH0PHf05_W',
    'FilesPerJob': 2
}
signals.append('VBFH0PHf05')

samples['VBFH0L1'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu'),
    'weight': mcCommonWeight + '*VBFH0L1_W',
    'FilesPerJob': 2
}
signals.append('VBFH0L1')


###########################################
#############  VH  AC SIGNALS  ##################
###########################################

files = nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu' ) + \
        nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu' )
samples['VH0PM'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}
signals.append('VH0PM')


files = nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu' ) + \
        nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu' )
samples['VH0M'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}
addSampleWeight(samples,'VH0M','WH_H0M_ToWWTo2L2Nu','WH0M_W')
addSampleWeight(samples,'VH0M','ZH_H0M_ToWWTo2L2Nu','ZH0M_W')
signals.append('VH0M')


files = nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu' ) + \
        nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu' )
samples['VH0Mf05'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}
addSampleWeight(samples,'VH0Mf05','WH_H0Mf05_ToWWTo2L2Nu','WH0Mf05_W')
addSampleWeight(samples,'VH0Mf05','ZH_H0Mf05_ToWWTo2L2Nu','ZH0Mf05_W')
signals.append('VH0Mf05')


files = nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu' ) + \
        nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu' ) 
samples['VH0M_rw'] = {
    'name': files,
    'weight': mcCommonWeight + '*(gen_me_mixhm/gen_me_hm)',
    'FilesPerJob': 1,
}
addSampleWeight(samples,'VH0M_rw','WH_H0M_ToWWTo2L2Nu','WH0M_W')
addSampleWeight(samples,'VH0M_rw','ZH_H0M_ToWWTo2L2Nu','ZH0M_W')
signals.append('VH0M_rw')


files = nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu' ) + \
        nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu' )
samples['VH0PH'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}
addSampleWeight(samples,'VH0PH','WH_H0PH_ToWWTo2L2Nu','WH0PH_W')
addSampleWeight(samples,'VH0PH','ZH_H0PH_ToWWTo2L2Nu','ZH0PH_W')
signals.append('VH0PH')


files = nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu' ) + \
        nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu' )
samples['VH0PHf05'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}
addSampleWeight(samples,'VH0PHf05','WH_H0PHf05_ToWWTo2L2Nu','WH0PHf05_W')
addSampleWeight(samples,'VH0PHf05','ZH_H0PHf05_ToWWTo2L2Nu','ZH0PHf05_W')
signals.append('VH0PHf05')


files = nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu' ) + \
        nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu' ) 
samples['VH0PH_rw'] = {
    'name': files,
    'weight': mcCommonWeight + '*(gen_me_mixhp/gen_me_hp)',
    'FilesPerJob': 1,
}
addSampleWeight(samples,'VH0PH_rw','WH_H0PH_ToWWTo2L2Nu','WH0PH_W')
addSampleWeight(samples,'VH0PH_rw','ZH_H0PH_ToWWTo2L2Nu','ZH0PH_W')
signals.append('VH0PH_rw')


files = nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu' ) + \
        nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu' )
samples['VH0L1'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}
addSampleWeight(samples,'VH0L1','WH_H0L1_ToWWTo2L2Nu','WH0L1_W')
addSampleWeight(samples,'VH0L1','ZH_H0L1_ToWWTo2L2Nu','ZH0L1_W')
signals.append('VH0L1')

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

samples['qqH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 12,
}
signals.append('qqH_hww')
