#### EFT Signals 
 
signals_ggH = [] 
signals_VBF = [] 
signals_WH = [] 
signals_ZH = [] 
 
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
addSampleWeight(samples,'VBF_H0PM','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(ME_VBF_H0PM/ME_VBF_H0PM)')  
addSampleWeight(samples,'VBF_H0PM','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(ME_VBF_H0PM/ME_VBF_H0M)')  
addSampleWeight(samples,'VBF_H0PM','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(ME_VBF_H0PM/ME_VBF_H0PH)')  
addSampleWeight(samples,'VBF_H0PM','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(ME_VBF_H0PM/ME_VBF_H0L1)')  
addSampleWeight(samples,'VBF_H0PM','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(ME_VBF_H0PM/ME_VBF_H0Mf05)')   
addSampleWeight(samples,'VBF_H0PM','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(ME_VBF_H0PM/ME_VBF_H0PHf05)')  
addSampleWeight(samples,'VBF_H0PM','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(ME_VBF_H0PM/ME_VBF_H0L1f05)')  
signals_VBF.append('VBF_H0PM')  
 
samples['VBF_H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0M','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(ME_VBF_H0M_M0/ME_VBF_H0PM)')  
addSampleWeight(samples,'VBF_H0M','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(ME_VBF_H0M_M0/ME_VBF_H0M)')  
addSampleWeight(samples,'VBF_H0M','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(ME_VBF_H0M_M0/ME_VBF_H0PH)')  
addSampleWeight(samples,'VBF_H0M','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(ME_VBF_H0M_M0/ME_VBF_H0L1)')  
addSampleWeight(samples,'VBF_H0M','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(ME_VBF_H0M_M0/ME_VBF_H0Mf05)')   
addSampleWeight(samples,'VBF_H0M','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(ME_VBF_H0M_M0/ME_VBF_H0PHf05)')  
addSampleWeight(samples,'VBF_H0M','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(ME_VBF_H0M_M0/ME_VBF_H0L1f05)')  
signals_VBF.append('VBF_H0M')  
 
samples['VBF_H0M_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0M_M1','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(ME_VBF_H0M_M1/ME_VBF_H0PM)')  
addSampleWeight(samples,'VBF_H0M_M1','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(ME_VBF_H0M_M1/ME_VBF_H0M)')  
addSampleWeight(samples,'VBF_H0M_M1','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(ME_VBF_H0M_M1/ME_VBF_H0PH)')  
addSampleWeight(samples,'VBF_H0M_M1','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(ME_VBF_H0M_M1/ME_VBF_H0L1)')  
addSampleWeight(samples,'VBF_H0M_M1','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(ME_VBF_H0M_M1/ME_VBF_H0Mf05)')   
addSampleWeight(samples,'VBF_H0M_M1','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(ME_VBF_H0M_M1/ME_VBF_H0PHf05)')  
addSampleWeight(samples,'VBF_H0M_M1','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(ME_VBF_H0M_M1/ME_VBF_H0L1f05)')  
signals_VBF.append('VBF_H0M_M1')  
 
samples['VBF_H0M_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0M_M2','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(ME_VBF_H0M_M2/ME_VBF_H0PM)')  
addSampleWeight(samples,'VBF_H0M_M2','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(ME_VBF_H0M_M2/ME_VBF_H0M)')  
addSampleWeight(samples,'VBF_H0M_M2','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(ME_VBF_H0M_M2/ME_VBF_H0PH)')  
addSampleWeight(samples,'VBF_H0M_M2','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(ME_VBF_H0M_M2/ME_VBF_H0L1)')  
addSampleWeight(samples,'VBF_H0M_M2','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(ME_VBF_H0M_M2/ME_VBF_H0Mf05)')   
addSampleWeight(samples,'VBF_H0M_M2','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(ME_VBF_H0M_M2/ME_VBF_H0PHf05)')  
addSampleWeight(samples,'VBF_H0M_M2','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(ME_VBF_H0M_M2/ME_VBF_H0L1f05)')  
signals_VBF.append('VBF_H0M_M2')  
 
samples['VBF_H0M_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0M_M3','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(ME_VBF_H0M_M3/ME_VBF_H0PM)')  
addSampleWeight(samples,'VBF_H0M_M3','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(ME_VBF_H0M_M3/ME_VBF_H0M)')  
addSampleWeight(samples,'VBF_H0M_M3','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(ME_VBF_H0M_M3/ME_VBF_H0PH)')  
addSampleWeight(samples,'VBF_H0M_M3','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(ME_VBF_H0M_M3/ME_VBF_H0L1)')  
addSampleWeight(samples,'VBF_H0M_M3','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(ME_VBF_H0M_M3/ME_VBF_H0Mf05)')   
addSampleWeight(samples,'VBF_H0M_M3','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(ME_VBF_H0M_M3/ME_VBF_H0PHf05)')  
addSampleWeight(samples,'VBF_H0M_M3','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(ME_VBF_H0M_M3/ME_VBF_H0L1f05)')  
signals_VBF.append('VBF_H0M_M3')  
 
samples['VBF_H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0PH','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(ME_VBF_H0PH_M0/ME_VBF_H0PM)')  
addSampleWeight(samples,'VBF_H0PH','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(ME_VBF_H0PH_M0/ME_VBF_H0M)')  
addSampleWeight(samples,'VBF_H0PH','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(ME_VBF_H0PH_M0/ME_VBF_H0PH)')  
addSampleWeight(samples,'VBF_H0PH','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(ME_VBF_H0PH_M0/ME_VBF_H0L1)')  
addSampleWeight(samples,'VBF_H0PH','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(ME_VBF_H0PH_M0/ME_VBF_H0Mf05)')   
addSampleWeight(samples,'VBF_H0PH','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(ME_VBF_H0PH_M0/ME_VBF_H0PHf05)')  
addSampleWeight(samples,'VBF_H0PH','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(ME_VBF_H0PH_M0/ME_VBF_H0L1f05)')  
signals_VBF.append('VBF_H0PH')  
 
samples['VBF_H0PH_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0PH_M1','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(ME_VBF_H0PH_M1/ME_VBF_H0PM)')  
addSampleWeight(samples,'VBF_H0PH_M1','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(ME_VBF_H0PH_M1/ME_VBF_H0M)')  
addSampleWeight(samples,'VBF_H0PH_M1','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(ME_VBF_H0PH_M1/ME_VBF_H0PH)')  
addSampleWeight(samples,'VBF_H0PH_M1','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(ME_VBF_H0PH_M1/ME_VBF_H0L1)')  
addSampleWeight(samples,'VBF_H0PH_M1','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(ME_VBF_H0PH_M1/ME_VBF_H0Mf05)')   
addSampleWeight(samples,'VBF_H0PH_M1','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(ME_VBF_H0PH_M1/ME_VBF_H0PHf05)')  
addSampleWeight(samples,'VBF_H0PH_M1','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(ME_VBF_H0PH_M1/ME_VBF_H0L1f05)')  
signals_VBF.append('VBF_H0PH_M1')  
 
samples['VBF_H0PH_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0PH_M2','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(ME_VBF_H0PH_M2/ME_VBF_H0PM)')  
addSampleWeight(samples,'VBF_H0PH_M2','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(ME_VBF_H0PH_M2/ME_VBF_H0M)')  
addSampleWeight(samples,'VBF_H0PH_M2','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(ME_VBF_H0PH_M2/ME_VBF_H0PH)')  
addSampleWeight(samples,'VBF_H0PH_M2','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(ME_VBF_H0PH_M2/ME_VBF_H0L1)')  
addSampleWeight(samples,'VBF_H0PH_M2','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(ME_VBF_H0PH_M2/ME_VBF_H0Mf05)')   
addSampleWeight(samples,'VBF_H0PH_M2','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(ME_VBF_H0PH_M2/ME_VBF_H0PHf05)')  
addSampleWeight(samples,'VBF_H0PH_M2','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(ME_VBF_H0PH_M2/ME_VBF_H0L1f05)')  
signals_VBF.append('VBF_H0PH_M2')  
 
samples['VBF_H0PH_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0PH_M3','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(ME_VBF_H0PH_M3/ME_VBF_H0PM)')  
addSampleWeight(samples,'VBF_H0PH_M3','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(ME_VBF_H0PH_M3/ME_VBF_H0M)')  
addSampleWeight(samples,'VBF_H0PH_M3','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(ME_VBF_H0PH_M3/ME_VBF_H0PH)')  
addSampleWeight(samples,'VBF_H0PH_M3','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(ME_VBF_H0PH_M3/ME_VBF_H0L1)')  
addSampleWeight(samples,'VBF_H0PH_M3','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(ME_VBF_H0PH_M3/ME_VBF_H0Mf05)')   
addSampleWeight(samples,'VBF_H0PH_M3','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(ME_VBF_H0PH_M3/ME_VBF_H0PHf05)')  
addSampleWeight(samples,'VBF_H0PH_M3','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(ME_VBF_H0PH_M3/ME_VBF_H0L1f05)')  
signals_VBF.append('VBF_H0PH_M3')  
 
samples['VBF_H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0L1','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(ME_VBF_H0L1_M0/ME_VBF_H0PM)')  
addSampleWeight(samples,'VBF_H0L1','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(ME_VBF_H0L1_M0/ME_VBF_H0M)')  
addSampleWeight(samples,'VBF_H0L1','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(ME_VBF_H0L1_M0/ME_VBF_H0PH)')  
addSampleWeight(samples,'VBF_H0L1','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(ME_VBF_H0L1_M0/ME_VBF_H0L1)')  
addSampleWeight(samples,'VBF_H0L1','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(ME_VBF_H0L1_M0/ME_VBF_H0Mf05)')   
addSampleWeight(samples,'VBF_H0L1','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(ME_VBF_H0L1_M0/ME_VBF_H0PHf05)')  
addSampleWeight(samples,'VBF_H0L1','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(ME_VBF_H0L1_M0/ME_VBF_H0L1f05)')  
signals_VBF.append('VBF_H0L1')  
 
samples['VBF_H0L1_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0L1_M1','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(ME_VBF_H0L1_M1/ME_VBF_H0PM)')  
addSampleWeight(samples,'VBF_H0L1_M1','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(ME_VBF_H0L1_M1/ME_VBF_H0M)')  
addSampleWeight(samples,'VBF_H0L1_M1','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(ME_VBF_H0L1_M1/ME_VBF_H0PH)')  
addSampleWeight(samples,'VBF_H0L1_M1','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(ME_VBF_H0L1_M1/ME_VBF_H0L1)')  
addSampleWeight(samples,'VBF_H0L1_M1','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(ME_VBF_H0L1_M1/ME_VBF_H0Mf05)')   
addSampleWeight(samples,'VBF_H0L1_M1','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(ME_VBF_H0L1_M1/ME_VBF_H0PHf05)')  
addSampleWeight(samples,'VBF_H0L1_M1','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(ME_VBF_H0L1_M1/ME_VBF_H0L1f05)')  
signals_VBF.append('VBF_H0L1_M1')  
 
samples['VBF_H0L1_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0L1_M2','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(ME_VBF_H0L1_M2/ME_VBF_H0PM)')  
addSampleWeight(samples,'VBF_H0L1_M2','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(ME_VBF_H0L1_M2/ME_VBF_H0M)')  
addSampleWeight(samples,'VBF_H0L1_M2','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(ME_VBF_H0L1_M2/ME_VBF_H0PH)')  
addSampleWeight(samples,'VBF_H0L1_M2','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(ME_VBF_H0L1_M2/ME_VBF_H0L1)')  
addSampleWeight(samples,'VBF_H0L1_M2','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(ME_VBF_H0L1_M2/ME_VBF_H0Mf05)')   
addSampleWeight(samples,'VBF_H0L1_M2','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(ME_VBF_H0L1_M2/ME_VBF_H0PHf05)')  
addSampleWeight(samples,'VBF_H0L1_M2','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(ME_VBF_H0L1_M2/ME_VBF_H0L1f05)')  
signals_VBF.append('VBF_H0L1_M2')  
 
samples['VBF_H0L1_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'VBF_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'VBF_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'VBF_H0L1_M3','VBF_H0PM_ToWWTo2L2Nu',    'VBF_H0PM_W*(ME_VBF_H0L1_M3/ME_VBF_H0PM)')  
addSampleWeight(samples,'VBF_H0L1_M3','VBF_H0M_ToWWTo2L2Nu',     'VBF_H0M_W*(ME_VBF_H0L1_M3/ME_VBF_H0M)')  
addSampleWeight(samples,'VBF_H0L1_M3','VBF_H0PH_ToWWTo2L2Nu',    'VBF_H0PH_W*(ME_VBF_H0L1_M3/ME_VBF_H0PH)')  
addSampleWeight(samples,'VBF_H0L1_M3','VBF_H0L1_ToWWTo2L2Nu',    'VBF_H0L1_W*(ME_VBF_H0L1_M3/ME_VBF_H0L1)')  
addSampleWeight(samples,'VBF_H0L1_M3','VBF_H0Mf05_ToWWTo2L2Nu',  'VBF_H0Mf05_W*(ME_VBF_H0L1_M3/ME_VBF_H0Mf05)')   
addSampleWeight(samples,'VBF_H0L1_M3','VBF_H0PHf05_ToWWTo2L2Nu', 'VBF_H0PHf05_W*(ME_VBF_H0L1_M3/ME_VBF_H0PHf05)')  
addSampleWeight(samples,'VBF_H0L1_M3','VBF_H0L1f05_ToWWTo2L2Nu', 'VBF_H0L1f05_W*(ME_VBF_H0L1_M3/ME_VBF_H0L1f05)')  
signals_VBF.append('VBF_H0L1_M3')  
 
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
addSampleWeight(samples,'WH_H0PM','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(ME_WH_H0PM/ME_WH_H0PM)')  
addSampleWeight(samples,'WH_H0PM','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(ME_WH_H0PM/ME_WH_H0M, 0.9)')  
addSampleWeight(samples,'WH_H0PM','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(ME_WH_H0PM/ME_WH_H0PH)')  
addSampleWeight(samples,'WH_H0PM','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(ME_WH_H0PM/ME_WH_H0L1)')  
addSampleWeight(samples,'WH_H0PM','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(ME_WH_H0PM/ME_WH_H0Mf05)')   
addSampleWeight(samples,'WH_H0PM','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(ME_WH_H0PM/ME_WH_H0PHf05)')  
addSampleWeight(samples,'WH_H0PM','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(ME_WH_H0PM/ME_WH_H0L1f05)')  
signals_WH.append('WH_H0PM')  
 
samples['WH_H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0M','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(ME_WH_H0M_M0/ME_WH_H0PM)')  
addSampleWeight(samples,'WH_H0M','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*(ME_WH_H0M_M0/ME_WH_H0M)')  
addSampleWeight(samples,'WH_H0M','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(ME_WH_H0M_M0/ME_WH_H0PH)')  
addSampleWeight(samples,'WH_H0M','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(ME_WH_H0M_M0/ME_WH_H0L1)')  
addSampleWeight(samples,'WH_H0M','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(ME_WH_H0M_M0/ME_WH_H0Mf05)')   
addSampleWeight(samples,'WH_H0M','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(ME_WH_H0M_M0/ME_WH_H0PHf05)')  
addSampleWeight(samples,'WH_H0M','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(ME_WH_H0M_M0/ME_WH_H0L1f05)')  
signals_WH.append('WH_H0M')  
 
samples['WH_H0M_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0M_M1','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(ME_WH_H0M_M1/ME_WH_H0PM)')  
addSampleWeight(samples,'WH_H0M_M1','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(ME_WH_H0M_M1/ME_WH_H0M, 5)')  
addSampleWeight(samples,'WH_H0M_M1','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(ME_WH_H0M_M1/ME_WH_H0PH)')  
addSampleWeight(samples,'WH_H0M_M1','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(ME_WH_H0M_M1/ME_WH_H0L1)')  
addSampleWeight(samples,'WH_H0M_M1','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(ME_WH_H0M_M1/ME_WH_H0Mf05)')   
addSampleWeight(samples,'WH_H0M_M1','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(ME_WH_H0M_M1/ME_WH_H0PHf05)')  
addSampleWeight(samples,'WH_H0M_M1','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(ME_WH_H0M_M1/ME_WH_H0L1f05)')  
signals_WH.append('WH_H0M_M1')  
 
samples['WH_H0M_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0M_M2','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(ME_WH_H0M_M2/ME_WH_H0PM)')  
addSampleWeight(samples,'WH_H0M_M2','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(ME_WH_H0M_M2/ME_WH_H0M, 20)')  
addSampleWeight(samples,'WH_H0M_M2','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(ME_WH_H0M_M2/ME_WH_H0PH)')  
addSampleWeight(samples,'WH_H0M_M2','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(ME_WH_H0M_M2/ME_WH_H0L1)')  
addSampleWeight(samples,'WH_H0M_M2','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(ME_WH_H0M_M2/ME_WH_H0Mf05)')   
addSampleWeight(samples,'WH_H0M_M2','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(ME_WH_H0M_M2/ME_WH_H0PHf05)')  
addSampleWeight(samples,'WH_H0M_M2','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(ME_WH_H0M_M2/ME_WH_H0L1f05)')  
signals_WH.append('WH_H0M_M2')  
 
samples['WH_H0M_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0M_M3','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(ME_WH_H0M_M3/ME_WH_H0PM)')  
addSampleWeight(samples,'WH_H0M_M3','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(ME_WH_H0M_M3/ME_WH_H0M, 30)')  
addSampleWeight(samples,'WH_H0M_M3','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(ME_WH_H0M_M3/ME_WH_H0PH)')  
addSampleWeight(samples,'WH_H0M_M3','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(ME_WH_H0M_M3/ME_WH_H0L1)')  
addSampleWeight(samples,'WH_H0M_M3','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(ME_WH_H0M_M3/ME_WH_H0Mf05)')   
addSampleWeight(samples,'WH_H0M_M3','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(ME_WH_H0M_M3/ME_WH_H0PHf05)')  
addSampleWeight(samples,'WH_H0M_M3','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(ME_WH_H0M_M3/ME_WH_H0L1f05)')  
signals_WH.append('WH_H0M_M3')  
 
samples['WH_H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0PH','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(ME_WH_H0PH_M0/ME_WH_H0PM)')  
addSampleWeight(samples,'WH_H0PH','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(ME_WH_H0PH_M0/ME_WH_H0M, 40)')  
addSampleWeight(samples,'WH_H0PH','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(ME_WH_H0PH_M0/ME_WH_H0PH)')  
addSampleWeight(samples,'WH_H0PH','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(ME_WH_H0PH_M0/ME_WH_H0L1)')  
addSampleWeight(samples,'WH_H0PH','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(ME_WH_H0PH_M0/ME_WH_H0Mf05)')   
addSampleWeight(samples,'WH_H0PH','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(ME_WH_H0PH_M0/ME_WH_H0PHf05)')  
addSampleWeight(samples,'WH_H0PH','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(ME_WH_H0PH_M0/ME_WH_H0L1f05)')  
signals_WH.append('WH_H0PH')  
 
samples['WH_H0PH_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0PH_M1','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(ME_WH_H0PH_M1/ME_WH_H0PM)')  
addSampleWeight(samples,'WH_H0PH_M1','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(ME_WH_H0PH_M1/ME_WH_H0M, 5)')  
addSampleWeight(samples,'WH_H0PH_M1','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(ME_WH_H0PH_M1/ME_WH_H0PH)')  
addSampleWeight(samples,'WH_H0PH_M1','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(ME_WH_H0PH_M1/ME_WH_H0L1)')  
addSampleWeight(samples,'WH_H0PH_M1','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(ME_WH_H0PH_M1/ME_WH_H0Mf05)')   
addSampleWeight(samples,'WH_H0PH_M1','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(ME_WH_H0PH_M1/ME_WH_H0PHf05)')  
addSampleWeight(samples,'WH_H0PH_M1','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(ME_WH_H0PH_M1/ME_WH_H0L1f05)')  
signals_WH.append('WH_H0PH_M1')  
 
samples['WH_H0PH_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0PH_M2','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(ME_WH_H0PH_M2/ME_WH_H0PM)')  
addSampleWeight(samples,'WH_H0PH_M2','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(ME_WH_H0PH_M2/ME_WH_H0M, 30)')  
addSampleWeight(samples,'WH_H0PH_M2','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(ME_WH_H0PH_M2/ME_WH_H0PH)')  
addSampleWeight(samples,'WH_H0PH_M2','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(ME_WH_H0PH_M2/ME_WH_H0L1)')  
addSampleWeight(samples,'WH_H0PH_M2','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(ME_WH_H0PH_M2/ME_WH_H0Mf05)')   
addSampleWeight(samples,'WH_H0PH_M2','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(ME_WH_H0PH_M2/ME_WH_H0PHf05)')  
addSampleWeight(samples,'WH_H0PH_M2','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(ME_WH_H0PH_M2/ME_WH_H0L1f05)')  
signals_WH.append('WH_H0PH_M2')  
 
samples['WH_H0PH_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0PH_M3','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(ME_WH_H0PH_M3/ME_WH_H0PM)')  
addSampleWeight(samples,'WH_H0PH_M3','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(ME_WH_H0PH_M3/ME_WH_H0M, 70)')  
addSampleWeight(samples,'WH_H0PH_M3','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(ME_WH_H0PH_M3/ME_WH_H0PH)')  
addSampleWeight(samples,'WH_H0PH_M3','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(ME_WH_H0PH_M3/ME_WH_H0L1)')  
addSampleWeight(samples,'WH_H0PH_M3','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(ME_WH_H0PH_M3/ME_WH_H0Mf05)')   
addSampleWeight(samples,'WH_H0PH_M3','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(ME_WH_H0PH_M3/ME_WH_H0PHf05)')  
addSampleWeight(samples,'WH_H0PH_M3','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(ME_WH_H0PH_M3/ME_WH_H0L1f05)')  
signals_WH.append('WH_H0PH_M3')  
 
samples['WH_H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0L1','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(ME_WH_H0L1_M0/ME_WH_H0PM)')  
addSampleWeight(samples,'WH_H0L1','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(ME_WH_H0L1_M0/ME_WH_H0M, 120)')  
addSampleWeight(samples,'WH_H0L1','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(ME_WH_H0L1_M0/ME_WH_H0PH)')  
addSampleWeight(samples,'WH_H0L1','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(ME_WH_H0L1_M0/ME_WH_H0L1)')  
addSampleWeight(samples,'WH_H0L1','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(ME_WH_H0L1_M0/ME_WH_H0Mf05)')   
addSampleWeight(samples,'WH_H0L1','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(ME_WH_H0L1_M0/ME_WH_H0PHf05)')  
addSampleWeight(samples,'WH_H0L1','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(ME_WH_H0L1_M0/ME_WH_H0L1f05)')  
signals_WH.append('WH_H0L1')  
 
samples['WH_H0L1_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0L1_M1','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(ME_WH_H0L1_M1/ME_WH_H0PM)')  
addSampleWeight(samples,'WH_H0L1_M1','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(ME_WH_H0L1_M1/ME_WH_H0M, 6)')  
addSampleWeight(samples,'WH_H0L1_M1','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(ME_WH_H0L1_M1/ME_WH_H0PH)')  
addSampleWeight(samples,'WH_H0L1_M1','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(ME_WH_H0L1_M1/ME_WH_H0L1)')  
addSampleWeight(samples,'WH_H0L1_M1','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(ME_WH_H0L1_M1/ME_WH_H0Mf05)')   
addSampleWeight(samples,'WH_H0L1_M1','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(ME_WH_H0L1_M1/ME_WH_H0PHf05)')  
addSampleWeight(samples,'WH_H0L1_M1','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(ME_WH_H0L1_M1/ME_WH_H0L1f05)')  
signals_WH.append('WH_H0L1_M1')  
 
samples['WH_H0L1_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0L1_M2','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(ME_WH_H0L1_M2/ME_WH_H0PM)')  
addSampleWeight(samples,'WH_H0L1_M2','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(ME_WH_H0L1_M2/ME_WH_H0M, 20)')  
addSampleWeight(samples,'WH_H0L1_M2','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(ME_WH_H0L1_M2/ME_WH_H0PH)')  
addSampleWeight(samples,'WH_H0L1_M2','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(ME_WH_H0L1_M2/ME_WH_H0L1)')  
addSampleWeight(samples,'WH_H0L1_M2','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(ME_WH_H0L1_M2/ME_WH_H0Mf05)')   
addSampleWeight(samples,'WH_H0L1_M2','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(ME_WH_H0L1_M2/ME_WH_H0PHf05)')  
addSampleWeight(samples,'WH_H0L1_M2','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(ME_WH_H0L1_M2/ME_WH_H0L1f05)')  
signals_WH.append('WH_H0L1_M2')  
 
samples['WH_H0L1_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'WH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'WH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'WH_H0L1_M3','WH_H0PM_ToWWTo2L2Nu',    'WH_H0PM_W*(ME_WH_H0L1_M3/ME_WH_H0PM)')  
addSampleWeight(samples,'WH_H0L1_M3','WH_H0M_ToWWTo2L2Nu',     'WH_H0M_W*min(ME_WH_H0L1_M3/ME_WH_H0M, 30)')  
addSampleWeight(samples,'WH_H0L1_M3','WH_H0PH_ToWWTo2L2Nu',    'WH_H0PH_W*(ME_WH_H0L1_M3/ME_WH_H0PH)')  
addSampleWeight(samples,'WH_H0L1_M3','WH_H0L1_ToWWTo2L2Nu',    'WH_H0L1_W*(ME_WH_H0L1_M3/ME_WH_H0L1)')  
addSampleWeight(samples,'WH_H0L1_M3','WH_H0Mf05_ToWWTo2L2Nu',  'WH_H0Mf05_W*(ME_WH_H0L1_M3/ME_WH_H0Mf05)')   
addSampleWeight(samples,'WH_H0L1_M3','WH_H0PHf05_ToWWTo2L2Nu', 'WH_H0PHf05_W*(ME_WH_H0L1_M3/ME_WH_H0PHf05)')  
addSampleWeight(samples,'WH_H0L1_M3','WH_H0L1f05_ToWWTo2L2Nu', 'WH_H0L1f05_W*(ME_WH_H0L1_M3/ME_WH_H0L1f05)')  
signals_WH.append('WH_H0L1_M3')  
 
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
addSampleWeight(samples,'ZH_H0PM','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(ME_ZH_H0PM/ME_ZH_H0PM)')  
addSampleWeight(samples,'ZH_H0PM','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(ME_ZH_H0PM/ME_ZH_H0M, 0.9)')  
addSampleWeight(samples,'ZH_H0PM','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(ME_ZH_H0PM/ME_ZH_H0PH)')  
addSampleWeight(samples,'ZH_H0PM','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(ME_ZH_H0PM/ME_ZH_H0L1)')  
addSampleWeight(samples,'ZH_H0PM','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(ME_ZH_H0PM/ME_ZH_H0Mf05)')   
addSampleWeight(samples,'ZH_H0PM','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(ME_ZH_H0PM/ME_ZH_H0PHf05)')  
addSampleWeight(samples,'ZH_H0PM','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(ME_ZH_H0PM/ME_ZH_H0L1f05)')  
signals_ZH.append('ZH_H0PM')  
 
samples['ZH_H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0M','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(ME_ZH_H0M_M0/ME_ZH_H0PM)')  
addSampleWeight(samples,'ZH_H0M','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*(ME_ZH_H0M_M0/ME_ZH_H0M)')  
addSampleWeight(samples,'ZH_H0M','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(ME_ZH_H0M_M0/ME_ZH_H0PH)')  
addSampleWeight(samples,'ZH_H0M','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(ME_ZH_H0M_M0/ME_ZH_H0L1)')  
addSampleWeight(samples,'ZH_H0M','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(ME_ZH_H0M_M0/ME_ZH_H0Mf05)')   
addSampleWeight(samples,'ZH_H0M','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(ME_ZH_H0M_M0/ME_ZH_H0PHf05)')  
addSampleWeight(samples,'ZH_H0M','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(ME_ZH_H0M_M0/ME_ZH_H0L1f05)')  
signals_ZH.append('ZH_H0M')  
 
samples['ZH_H0M_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0M_M1','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(ME_ZH_H0M_M1/ME_ZH_H0PM)')  
addSampleWeight(samples,'ZH_H0M_M1','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(ME_ZH_H0M_M1/ME_ZH_H0M, 5)')  
addSampleWeight(samples,'ZH_H0M_M1','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(ME_ZH_H0M_M1/ME_ZH_H0PH)')  
addSampleWeight(samples,'ZH_H0M_M1','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(ME_ZH_H0M_M1/ME_ZH_H0L1)')  
addSampleWeight(samples,'ZH_H0M_M1','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(ME_ZH_H0M_M1/ME_ZH_H0Mf05)')   
addSampleWeight(samples,'ZH_H0M_M1','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(ME_ZH_H0M_M1/ME_ZH_H0PHf05)')  
addSampleWeight(samples,'ZH_H0M_M1','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(ME_ZH_H0M_M1/ME_ZH_H0L1f05)')  
signals_ZH.append('ZH_H0M_M1')  
 
samples['ZH_H0M_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0M_M2','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(ME_ZH_H0M_M2/ME_ZH_H0PM)')  
addSampleWeight(samples,'ZH_H0M_M2','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(ME_ZH_H0M_M2/ME_ZH_H0M, 20)')  
addSampleWeight(samples,'ZH_H0M_M2','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(ME_ZH_H0M_M2/ME_ZH_H0PH)')  
addSampleWeight(samples,'ZH_H0M_M2','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(ME_ZH_H0M_M2/ME_ZH_H0L1)')  
addSampleWeight(samples,'ZH_H0M_M2','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(ME_ZH_H0M_M2/ME_ZH_H0Mf05)')   
addSampleWeight(samples,'ZH_H0M_M2','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(ME_ZH_H0M_M2/ME_ZH_H0PHf05)')  
addSampleWeight(samples,'ZH_H0M_M2','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(ME_ZH_H0M_M2/ME_ZH_H0L1f05)')  
signals_ZH.append('ZH_H0M_M2')  
 
samples['ZH_H0M_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0M_M3','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(ME_ZH_H0M_M3/ME_ZH_H0PM)')  
addSampleWeight(samples,'ZH_H0M_M3','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(ME_ZH_H0M_M3/ME_ZH_H0M, 30)')  
addSampleWeight(samples,'ZH_H0M_M3','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(ME_ZH_H0M_M3/ME_ZH_H0PH)')  
addSampleWeight(samples,'ZH_H0M_M3','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(ME_ZH_H0M_M3/ME_ZH_H0L1)')  
addSampleWeight(samples,'ZH_H0M_M3','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(ME_ZH_H0M_M3/ME_ZH_H0Mf05)')   
addSampleWeight(samples,'ZH_H0M_M3','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(ME_ZH_H0M_M3/ME_ZH_H0PHf05)')  
addSampleWeight(samples,'ZH_H0M_M3','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(ME_ZH_H0M_M3/ME_ZH_H0L1f05)')  
signals_ZH.append('ZH_H0M_M3')  
 
samples['ZH_H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0PH','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(ME_ZH_H0PH_M0/ME_ZH_H0PM)')  
addSampleWeight(samples,'ZH_H0PH','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(ME_ZH_H0PH_M0/ME_ZH_H0M, 40)')  
addSampleWeight(samples,'ZH_H0PH','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(ME_ZH_H0PH_M0/ME_ZH_H0PH)')  
addSampleWeight(samples,'ZH_H0PH','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(ME_ZH_H0PH_M0/ME_ZH_H0L1)')  
addSampleWeight(samples,'ZH_H0PH','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(ME_ZH_H0PH_M0/ME_ZH_H0Mf05)')   
addSampleWeight(samples,'ZH_H0PH','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(ME_ZH_H0PH_M0/ME_ZH_H0PHf05)')  
addSampleWeight(samples,'ZH_H0PH','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(ME_ZH_H0PH_M0/ME_ZH_H0L1f05)')  
signals_ZH.append('ZH_H0PH')  
 
samples['ZH_H0PH_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0PH_M1','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(ME_ZH_H0PH_M1/ME_ZH_H0PM)')  
addSampleWeight(samples,'ZH_H0PH_M1','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(ME_ZH_H0PH_M1/ME_ZH_H0M, 5)')  
addSampleWeight(samples,'ZH_H0PH_M1','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(ME_ZH_H0PH_M1/ME_ZH_H0PH)')  
addSampleWeight(samples,'ZH_H0PH_M1','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(ME_ZH_H0PH_M1/ME_ZH_H0L1)')  
addSampleWeight(samples,'ZH_H0PH_M1','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(ME_ZH_H0PH_M1/ME_ZH_H0Mf05)')   
addSampleWeight(samples,'ZH_H0PH_M1','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(ME_ZH_H0PH_M1/ME_ZH_H0PHf05)')  
addSampleWeight(samples,'ZH_H0PH_M1','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(ME_ZH_H0PH_M1/ME_ZH_H0L1f05)')  
signals_ZH.append('ZH_H0PH_M1')  
 
samples['ZH_H0PH_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0PH_M2','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(ME_ZH_H0PH_M2/ME_ZH_H0PM)')  
addSampleWeight(samples,'ZH_H0PH_M2','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(ME_ZH_H0PH_M2/ME_ZH_H0M, 30)')  
addSampleWeight(samples,'ZH_H0PH_M2','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(ME_ZH_H0PH_M2/ME_ZH_H0PH)')  
addSampleWeight(samples,'ZH_H0PH_M2','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(ME_ZH_H0PH_M2/ME_ZH_H0L1)')  
addSampleWeight(samples,'ZH_H0PH_M2','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(ME_ZH_H0PH_M2/ME_ZH_H0Mf05)')   
addSampleWeight(samples,'ZH_H0PH_M2','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(ME_ZH_H0PH_M2/ME_ZH_H0PHf05)')  
addSampleWeight(samples,'ZH_H0PH_M2','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(ME_ZH_H0PH_M2/ME_ZH_H0L1f05)')  
signals_ZH.append('ZH_H0PH_M2')  
 
samples['ZH_H0PH_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0PH_M3','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(ME_ZH_H0PH_M3/ME_ZH_H0PM)')  
addSampleWeight(samples,'ZH_H0PH_M3','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(ME_ZH_H0PH_M3/ME_ZH_H0M, 70)')  
addSampleWeight(samples,'ZH_H0PH_M3','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(ME_ZH_H0PH_M3/ME_ZH_H0PH)')  
addSampleWeight(samples,'ZH_H0PH_M3','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(ME_ZH_H0PH_M3/ME_ZH_H0L1)')  
addSampleWeight(samples,'ZH_H0PH_M3','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(ME_ZH_H0PH_M3/ME_ZH_H0Mf05)')   
addSampleWeight(samples,'ZH_H0PH_M3','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(ME_ZH_H0PH_M3/ME_ZH_H0PHf05)')  
addSampleWeight(samples,'ZH_H0PH_M3','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(ME_ZH_H0PH_M3/ME_ZH_H0L1f05)')  
signals_ZH.append('ZH_H0PH_M3')  
 
samples['ZH_H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0L1','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(ME_ZH_H0L1_M0/ME_ZH_H0PM)')  
addSampleWeight(samples,'ZH_H0L1','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(ME_ZH_H0L1_M0/ME_ZH_H0M, 120)')  
addSampleWeight(samples,'ZH_H0L1','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(ME_ZH_H0L1_M0/ME_ZH_H0PH)')  
addSampleWeight(samples,'ZH_H0L1','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(ME_ZH_H0L1_M0/ME_ZH_H0L1)')  
addSampleWeight(samples,'ZH_H0L1','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(ME_ZH_H0L1_M0/ME_ZH_H0Mf05)')   
addSampleWeight(samples,'ZH_H0L1','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(ME_ZH_H0L1_M0/ME_ZH_H0PHf05)')  
addSampleWeight(samples,'ZH_H0L1','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(ME_ZH_H0L1_M0/ME_ZH_H0L1f05)')  
signals_ZH.append('ZH_H0L1')  
 
samples['ZH_H0L1_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0L1_M1','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(ME_ZH_H0L1_M1/ME_ZH_H0PM)')  
addSampleWeight(samples,'ZH_H0L1_M1','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(ME_ZH_H0L1_M1/ME_ZH_H0M, 6)')  
addSampleWeight(samples,'ZH_H0L1_M1','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(ME_ZH_H0L1_M1/ME_ZH_H0PH)')  
addSampleWeight(samples,'ZH_H0L1_M1','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(ME_ZH_H0L1_M1/ME_ZH_H0L1)')  
addSampleWeight(samples,'ZH_H0L1_M1','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(ME_ZH_H0L1_M1/ME_ZH_H0Mf05)')   
addSampleWeight(samples,'ZH_H0L1_M1','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(ME_ZH_H0L1_M1/ME_ZH_H0PHf05)')  
addSampleWeight(samples,'ZH_H0L1_M1','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(ME_ZH_H0L1_M1/ME_ZH_H0L1f05)')  
signals_ZH.append('ZH_H0L1_M1')  
 
samples['ZH_H0L1_M2'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0L1_M2','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(ME_ZH_H0L1_M2/ME_ZH_H0PM)')  
addSampleWeight(samples,'ZH_H0L1_M2','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(ME_ZH_H0L1_M2/ME_ZH_H0M, 20)')  
addSampleWeight(samples,'ZH_H0L1_M2','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(ME_ZH_H0L1_M2/ME_ZH_H0PH)')  
addSampleWeight(samples,'ZH_H0L1_M2','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(ME_ZH_H0L1_M2/ME_ZH_H0L1)')  
addSampleWeight(samples,'ZH_H0L1_M2','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(ME_ZH_H0L1_M2/ME_ZH_H0Mf05)')   
addSampleWeight(samples,'ZH_H0L1_M2','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(ME_ZH_H0L1_M2/ME_ZH_H0PHf05)')  
addSampleWeight(samples,'ZH_H0L1_M2','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(ME_ZH_H0L1_M2/ME_ZH_H0L1f05)')  
signals_ZH.append('ZH_H0L1_M2')  
 
samples['ZH_H0L1_M3'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'ZH_H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'ZH_H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'ZH_H0L1_M3','ZH_H0PM_ToWWTo2L2Nu',    'ZH_H0PM_W*(ME_ZH_H0L1_M3/ME_ZH_H0PM)')  
addSampleWeight(samples,'ZH_H0L1_M3','ZH_H0M_ToWWTo2L2Nu',     'ZH_H0M_W*min(ME_ZH_H0L1_M3/ME_ZH_H0M, 30)')  
addSampleWeight(samples,'ZH_H0L1_M3','ZH_H0PH_ToWWTo2L2Nu',    'ZH_H0PH_W*(ME_ZH_H0L1_M3/ME_ZH_H0PH)')  
addSampleWeight(samples,'ZH_H0L1_M3','ZH_H0L1_ToWWTo2L2Nu',    'ZH_H0L1_W*(ME_ZH_H0L1_M3/ME_ZH_H0L1)')  
addSampleWeight(samples,'ZH_H0L1_M3','ZH_H0Mf05_ToWWTo2L2Nu',  'ZH_H0Mf05_W*(ME_ZH_H0L1_M3/ME_ZH_H0Mf05)')   
addSampleWeight(samples,'ZH_H0L1_M3','ZH_H0PHf05_ToWWTo2L2Nu', 'ZH_H0PHf05_W*(ME_ZH_H0L1_M3/ME_ZH_H0PHf05)')  
addSampleWeight(samples,'ZH_H0L1_M3','ZH_H0L1f05_ToWWTo2L2Nu', 'ZH_H0L1f05_W*(ME_ZH_H0L1_M3/ME_ZH_H0L1f05)')  
signals_ZH.append('ZH_H0L1_M3')  
 
# Original ggH MC samples 
 
samples['H0PM_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*H0PM_W', 
   'FilesPerJob': 1 
} 
 
samples['H0M_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*H0M_W', 
   'FilesPerJob': 1 
} 
 
samples['H0Mf05_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*H0Mf05_W', 
   'FilesPerJob': 1 
} 
 
samples['H0PH_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*H0PH_W', 
   'FilesPerJob': 1 
} 
 
samples['H0PHf05_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*H0PHf05_W', 
   'FilesPerJob': 1 
} 
 
samples['H0L1_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*H0L1_W', 
   'FilesPerJob': 1 
} 
 
samples['H0L1f05_Org'] = { 
   'name': nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*H0L1f05_W', 
   'FilesPerJob': 1 
} 
 
# Reweighted ggH samples 
 
samples['H0PM'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'H0PM','H0PM_ToWWTo2L2Nu',    'H0PM_W*(ME_H0PM/ME_H0PM)')  
addSampleWeight(samples,'H0PM','H0M_ToWWTo2L2Nu',     'H0M_W*(ME_H0PM/ME_H0M)')  
addSampleWeight(samples,'H0PM','H0PH_ToWWTo2L2Nu',    'H0PH_W*(ME_H0PM/ME_H0PH)')  
addSampleWeight(samples,'H0PM','H0L1_ToWWTo2L2Nu',    'H0L1_W*(ME_H0PM/ME_H0L1)')  
addSampleWeight(samples,'H0PM','H0Mf05_ToWWTo2L2Nu',  'H0Mf05_W*(ME_H0PM/ME_H0Mf05)')   
addSampleWeight(samples,'H0PM','H0PHf05_ToWWTo2L2Nu', 'H0PHf05_W*(ME_H0PM/ME_H0PHf05)')  
addSampleWeight(samples,'H0PM','H0L1f05_ToWWTo2L2Nu', 'H0L1f05_W*(ME_H0PM/ME_H0L1f05)')  
signals_ggH.append('H0PM')  
 
samples['H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'H0M','H0PM_ToWWTo2L2Nu',    'H0PM_W*(ME_H0M/ME_H0PM)')  
addSampleWeight(samples,'H0M','H0M_ToWWTo2L2Nu',     'H0M_W*(ME_H0M/ME_H0M)')  
addSampleWeight(samples,'H0M','H0PH_ToWWTo2L2Nu',    'H0PH_W*(ME_H0M/ME_H0PH)')  
addSampleWeight(samples,'H0M','H0L1_ToWWTo2L2Nu',    'H0L1_W*(ME_H0M/ME_H0L1)')  
addSampleWeight(samples,'H0M','H0Mf05_ToWWTo2L2Nu',  'H0Mf05_W*(ME_H0M/ME_H0Mf05)')   
addSampleWeight(samples,'H0M','H0PHf05_ToWWTo2L2Nu', 'H0PHf05_W*(ME_H0M/ME_H0PHf05)')  
addSampleWeight(samples,'H0M','H0L1f05_ToWWTo2L2Nu', 'H0L1f05_W*(ME_H0M/ME_H0L1f05)')  
signals_ggH.append('H0M')  
 
samples['H0M_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'H0M_M1','H0PM_ToWWTo2L2Nu',    'H0PM_W*(ME_H0Mf05/ME_H0PM)')  
addSampleWeight(samples,'H0M_M1','H0M_ToWWTo2L2Nu',     'H0M_W*(ME_H0Mf05/ME_H0M)')  
addSampleWeight(samples,'H0M_M1','H0PH_ToWWTo2L2Nu',    'H0PH_W*(ME_H0Mf05/ME_H0PH)')  
addSampleWeight(samples,'H0M_M1','H0L1_ToWWTo2L2Nu',    'H0L1_W*(ME_H0Mf05/ME_H0L1)')  
addSampleWeight(samples,'H0M_M1','H0Mf05_ToWWTo2L2Nu',  'H0Mf05_W*(ME_H0Mf05/ME_H0Mf05)')   
addSampleWeight(samples,'H0M_M1','H0PHf05_ToWWTo2L2Nu', 'H0PHf05_W*(ME_H0Mf05/ME_H0PHf05)')  
addSampleWeight(samples,'H0M_M1','H0L1f05_ToWWTo2L2Nu', 'H0L1f05_W*(ME_H0Mf05/ME_H0L1f05)')  
signals_ggH.append('H0M_M1')  
 
samples['H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'H0PH','H0PM_ToWWTo2L2Nu',    'H0PM_W*(ME_H0PH/ME_H0PM)')  
addSampleWeight(samples,'H0PH','H0M_ToWWTo2L2Nu',     'H0M_W*(ME_H0PH/ME_H0M)')  
addSampleWeight(samples,'H0PH','H0PH_ToWWTo2L2Nu',    'H0PH_W*(ME_H0PH/ME_H0PH)')  
addSampleWeight(samples,'H0PH','H0L1_ToWWTo2L2Nu',    'H0L1_W*(ME_H0PH/ME_H0L1)')  
addSampleWeight(samples,'H0PH','H0Mf05_ToWWTo2L2Nu',  'H0Mf05_W*(ME_H0PH/ME_H0Mf05)')   
addSampleWeight(samples,'H0PH','H0PHf05_ToWWTo2L2Nu', 'H0PHf05_W*(ME_H0PH/ME_H0PHf05)')  
addSampleWeight(samples,'H0PH','H0L1f05_ToWWTo2L2Nu', 'H0L1f05_W*(ME_H0PH/ME_H0L1f05)')  
signals_ggH.append('H0PH')  
 
samples['H0PH_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'H0PH_M1','H0PM_ToWWTo2L2Nu',    'H0PM_W*(ME_H0PHf05/ME_H0PM)')  
addSampleWeight(samples,'H0PH_M1','H0M_ToWWTo2L2Nu',     'H0M_W*(ME_H0PHf05/ME_H0M)')  
addSampleWeight(samples,'H0PH_M1','H0PH_ToWWTo2L2Nu',    'H0PH_W*(ME_H0PHf05/ME_H0PH)')  
addSampleWeight(samples,'H0PH_M1','H0L1_ToWWTo2L2Nu',    'H0L1_W*(ME_H0PHf05/ME_H0L1)')  
addSampleWeight(samples,'H0PH_M1','H0Mf05_ToWWTo2L2Nu',  'H0Mf05_W*(ME_H0PHf05/ME_H0Mf05)')   
addSampleWeight(samples,'H0PH_M1','H0PHf05_ToWWTo2L2Nu', 'H0PHf05_W*(ME_H0PHf05/ME_H0PHf05)')  
addSampleWeight(samples,'H0PH_M1','H0L1f05_ToWWTo2L2Nu', 'H0L1f05_W*(ME_H0PHf05/ME_H0L1f05)')  
signals_ggH.append('H0PH_M1')  
 
samples['H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'H0L1','H0PM_ToWWTo2L2Nu',    'H0PM_W*(ME_H0L1/ME_H0PM)')  
addSampleWeight(samples,'H0L1','H0M_ToWWTo2L2Nu',     'H0M_W*(ME_H0L1/ME_H0M)')  
addSampleWeight(samples,'H0L1','H0PH_ToWWTo2L2Nu',    'H0PH_W*(ME_H0L1/ME_H0PH)')  
addSampleWeight(samples,'H0L1','H0L1_ToWWTo2L2Nu',    'H0L1_W*(ME_H0L1/ME_H0L1)')  
addSampleWeight(samples,'H0L1','H0Mf05_ToWWTo2L2Nu',  'H0Mf05_W*(ME_H0L1/ME_H0Mf05)')   
addSampleWeight(samples,'H0L1','H0PHf05_ToWWTo2L2Nu', 'H0PHf05_W*(ME_H0L1/ME_H0PHf05)')  
addSampleWeight(samples,'H0L1','H0L1f05_ToWWTo2L2Nu', 'H0L1f05_W*(ME_H0L1/ME_H0L1f05)')  
signals_ggH.append('H0L1')  
 
samples['H0L1_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu') + nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight + '*(1/7)', 
   'FilesPerJob': 2, 
} 
addSampleWeight(samples,'H0L1_M1','H0PM_ToWWTo2L2Nu',    'H0PM_W*(ME_H0L1f05/ME_H0PM)')  
addSampleWeight(samples,'H0L1_M1','H0M_ToWWTo2L2Nu',     'H0M_W*(ME_H0L1f05/ME_H0M)')  
addSampleWeight(samples,'H0L1_M1','H0PH_ToWWTo2L2Nu',    'H0PH_W*(ME_H0L1f05/ME_H0PH)')  
addSampleWeight(samples,'H0L1_M1','H0L1_ToWWTo2L2Nu',    'H0L1_W*(ME_H0L1f05/ME_H0L1)')  
addSampleWeight(samples,'H0L1_M1','H0Mf05_ToWWTo2L2Nu',  'H0Mf05_W*(ME_H0L1f05/ME_H0Mf05)')   
addSampleWeight(samples,'H0L1_M1','H0PHf05_ToWWTo2L2Nu', 'H0PHf05_W*(ME_H0L1f05/ME_H0PHf05)')  
addSampleWeight(samples,'H0L1_M1','H0L1f05_ToWWTo2L2Nu', 'H0L1f05_W*(ME_H0L1f05/ME_H0L1f05)')  
signals_ggH.append('H0L1_M1')  
 
