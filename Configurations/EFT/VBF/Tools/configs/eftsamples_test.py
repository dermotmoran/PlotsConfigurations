#### EFT Signals 
 
signals_ggH = [] 
signals_VBF = [] 
signals_WH = [] 
signals_ZH = [] 
 
# Original ggH MC samples 
 
samples['H0PM'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PM_W', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PM')  
 
samples['H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0M_W', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0M')  
 
samples['H0Mf05'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0Mf05_W', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0Mf05')  
 
samples['H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PH_W', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PH')  
 
samples['H0PHf05'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PHf05_W', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PHf05')  
 
samples['H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1_W', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1')  
 
samples['H0L1f05'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1f05_W', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1f05')  
 
# Reweighted ggH samples 
 
samples['H0PM_H0PM'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PM_W*(ME_H0PM/ME_H0PM)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PM_H0PM')  
 
samples['H0PM_H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PM_W*(ME_H0M/ME_H0PM)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PM_H0M')  
 
samples['H0PM_H0M_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PM_W*(ME_H0Mf05/ME_H0PM)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PM_H0M_M1')  
 
samples['H0PM_H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PM_W*(ME_H0PH/ME_H0PM)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PM_H0PH')  
 
samples['H0PM_H0PH_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PM_W*(ME_H0PHf05/ME_H0PM)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PM_H0PH_M1')  
 
samples['H0PM_H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PM_W*(ME_H0L1/ME_H0PM)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PM_H0L1')  
 
samples['H0PM_H0L1_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PM_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PM_W*(ME_H0L1f05/ME_H0PM)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PM_H0L1_M1')  
 
samples['H0M_H0PM'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0M_W*(ME_H0PM/ME_H0M)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0M_H0PM')  
 
samples['H0M_H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0M_W*(ME_H0M/ME_H0M)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0M_H0M')  
 
samples['H0M_H0M_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0M_W*(ME_H0Mf05/ME_H0M)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0M_H0M_M1')  
 
samples['H0M_H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0M_W*(ME_H0PH/ME_H0M)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0M_H0PH')  
 
samples['H0M_H0PH_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0M_W*(ME_H0PHf05/ME_H0M)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0M_H0PH_M1')  
 
samples['H0M_H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0M_W*(ME_H0L1/ME_H0M)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0M_H0L1')  
 
samples['H0M_H0L1_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0M_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0M_W*(ME_H0L1f05/ME_H0M)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0M_H0L1_M1')  
 
samples['H0Mf05_H0PM'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0Mf05_W*(ME_H0PM/ME_H0Mf05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0Mf05_H0PM')  
 
samples['H0Mf05_H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0Mf05_W*(ME_H0M/ME_H0Mf05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0Mf05_H0M')  
 
samples['H0Mf05_H0M_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0Mf05_W*(ME_H0Mf05/ME_H0Mf05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0Mf05_H0M_M1')  
 
samples['H0Mf05_H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0Mf05_W*(ME_H0PH/ME_H0Mf05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0Mf05_H0PH')  
 
samples['H0Mf05_H0PH_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0Mf05_W*(ME_H0PHf05/ME_H0Mf05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0Mf05_H0PH_M1')  
 
samples['H0Mf05_H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0Mf05_W*(ME_H0L1/ME_H0Mf05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0Mf05_H0L1')  
 
samples['H0Mf05_H0L1_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0Mf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0Mf05_W*(ME_H0L1f05/ME_H0Mf05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0Mf05_H0L1_M1')  
 
samples['H0PH_H0PM'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PH_W*(ME_H0PM/ME_H0PH)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PH_H0PM')  
 
samples['H0PH_H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PH_W*(ME_H0M/ME_H0PH)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PH_H0M')  
 
samples['H0PH_H0M_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PH_W*(ME_H0Mf05/ME_H0PH)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PH_H0M_M1')  
 
samples['H0PH_H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PH_W*(ME_H0PH/ME_H0PH)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PH_H0PH')  
 
samples['H0PH_H0PH_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PH_W*(ME_H0PHf05/ME_H0PH)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PH_H0PH_M1')  
 
samples['H0PH_H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PH_W*(ME_H0L1/ME_H0PH)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PH_H0L1')  
 
samples['H0PH_H0L1_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PH_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PH_W*(ME_H0L1f05/ME_H0PH)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PH_H0L1_M1')  
 
samples['H0PHf05_H0PM'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PHf05_W*(ME_H0PM/ME_H0PHf05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PHf05_H0PM')  
 
samples['H0PHf05_H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PHf05_W*(ME_H0M/ME_H0PHf05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PHf05_H0M')  
 
samples['H0PHf05_H0M_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PHf05_W*(ME_H0Mf05/ME_H0PHf05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PHf05_H0M_M1')  
 
samples['H0PHf05_H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PHf05_W*(ME_H0PH/ME_H0PHf05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PHf05_H0PH')  
 
samples['H0PHf05_H0PH_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PHf05_W*(ME_H0PHf05/ME_H0PHf05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PHf05_H0PH_M1')  
 
samples['H0PHf05_H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PHf05_W*(ME_H0L1/ME_H0PHf05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PHf05_H0L1')  
 
samples['H0PHf05_H0L1_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0PHf05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0PHf05_W*(ME_H0L1f05/ME_H0PHf05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0PHf05_H0L1_M1')  
 
samples['H0L1_H0PM'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1_W*(ME_H0PM/ME_H0L1)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1_H0PM')  
 
samples['H0L1_H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1_W*(ME_H0M/ME_H0L1)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1_H0M')  
 
samples['H0L1_H0M_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1_W*(ME_H0Mf05/ME_H0L1)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1_H0M_M1')  
 
samples['H0L1_H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1_W*(ME_H0PH/ME_H0L1)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1_H0PH')  
 
samples['H0L1_H0PH_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1_W*(ME_H0PHf05/ME_H0L1)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1_H0PH_M1')  
 
samples['H0L1_H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1_W*(ME_H0L1/ME_H0L1)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1_H0L1')  
 
samples['H0L1_H0L1_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1_W*(ME_H0L1f05/ME_H0L1)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1_H0L1_M1')  
 
samples['H0L1f05_H0PM'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1f05_W*(ME_H0PM/ME_H0L1f05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1f05_H0PM')  
 
samples['H0L1f05_H0M'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1f05_W*(ME_H0M/ME_H0L1f05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1f05_H0M')  
 
samples['H0L1f05_H0M_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1f05_W*(ME_H0Mf05/ME_H0L1f05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1f05_H0M_M1')  
 
samples['H0L1f05_H0PH'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1f05_W*(ME_H0PH/ME_H0L1f05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1f05_H0PH')  
 
samples['H0L1f05_H0PH_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1f05_W*(ME_H0PHf05/ME_H0L1f05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1f05_H0PH_M1')  
 
samples['H0L1f05_H0L1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1f05_W*(ME_H0L1/ME_H0L1f05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1f05_H0L1')  
 
samples['H0L1f05_H0L1_M1'] = { 
   'name':   nanoGetSampleFiles(mcDirectory, 'H0L1f05_ToWWTo2L2Nu'), 
   'weight': mcCommonWeight+ '*H0L1f05_W*(ME_H0L1f05/ME_H0L1f05)', 
   'FilesPerJob': 2, 
} 
signals_ggH.append('H0L1f05_H0L1_M1')  
 
