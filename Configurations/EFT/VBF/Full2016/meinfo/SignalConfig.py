 #!/usr/bin/env python

#################################################

## 3 production mechanisms

Prod = [ "VBF", "WH", "ZH" ]

## 7 Original MC samples 

Sig  = [ "H0PM", "H0M", "H0Mf05", "H0PH", "H0PHf05", "H0L1", "H0L1f05" ]

## Reweight all 7 samples to these hypotheses (Sample, ME)

SigRW = [ ("H0PM", "MEH0PM"),
          ("H0M",  "MEH0M_M0"), ("H0M_M1",  "MEH0M_M1"), ("H0M_M2",  "MEH0M_M2"), ("H0M_M3",  "MEH0M_M3"),
          ("H0PH", "MEH0PH_M0"),("H0PH_M1", "MEH0PH_M1"),("H0PH_M2", "MEH0PH_M2"),("H0PH_M3", "MEH0PH_M3"),
          ("H0L1", "MEH0L1_M0"),("H0L1_M1", "MEH0L1_M1"),("H0L1_M2", "MEH0L1_M2"),("H0L1_M3", "MEH0L1_M3")
        ]

################################################

config =  "#### EFT Signals \n"
config += " \n"
config += "signals = [] \n"
config += " \n"

for p in Prod :

 config += "# Original "+p+" MC samples \n"
 config += " \n"

 for s in Sig :

    sample = ""+p+"_"+s+""

    config += "samples['"+sample+"_Org'] = { \n"
    config += "   'name': nanoGetSampleFiles(mcDirectory, '"+sample+"_ToWWTo2L2Nu'), \n"
    config += "   'weight': mcCommonWeight + '*"+sample+"_W', \n"
    config += "   'FilesPerJob': 1 \n"
    config += "} \n"
    config += " \n"

 config += "# Reweighted "+p+" samples \n"
 config += " \n"

 for s, me in SigRW :

    sample = ""+p+"_"+s+"" 

    config += "samples['"+sample+"'] = { \n"
    config += "   'name':   "   
    config += "nanoGetSampleFiles(mcDirectory, '"+p+"_H0PM_ToWWTo2L2Nu') + "
    config += "nanoGetSampleFiles(mcDirectory, '"+p+"_H0M_ToWWTo2L2Nu') + " 
    config += "nanoGetSampleFiles(mcDirectory, '"+p+"_H0PH_ToWWTo2L2Nu') + "
    config += "nanoGetSampleFiles(mcDirectory, '"+p+"_H0L1_ToWWTo2L2Nu') + " 
    config += "nanoGetSampleFiles(mcDirectory, '"+p+"_H0Mf05_ToWWTo2L2Nu') + " 
    config += "nanoGetSampleFiles(mcDirectory, '"+p+"_H0PHf05_ToWWTo2L2Nu') + " 
    config += "nanoGetSampleFiles(mcDirectory, '"+p+"_H0L1f05_ToWWTo2L2Nu'), \n"
    config += "   'weight': mcCommonWeight + '*(1/7)', \n"
    config += "   'FilesPerJob': 2, \n"
    config += "} \n"
   
    # 1,10,20,20,100,10,50,100,100,10,20,100 works well!!

    maxw = ""
    if p == "WH" or p == "ZH" :
     if "H0PM" is s    : maxw = "0.9"
     if "H0M_M1" is s  : maxw = "5"
     if "H0M_M2" is s  : maxw = "20"
     if "H0M_M3" is s  : maxw = "30"
     if "H0PH" is s    : maxw = "40"
     if "H0PH_M1" is s : maxw = "5"
     if "H0PH_M2" is s : maxw = "30"
     if "H0PH_M3" is s : maxw = "70"
     if "H0L1" is s    : maxw = "120"
     if "H0L1_M1" is s : maxw = "6"
     if "H0L1_M2" is s : maxw = "20"
     if "H0L1_M3" is s : maxw = "30"

    config += "addSampleWeight(samples,'"+sample+"','"+p+"_H0PM_ToWWTo2L2Nu',    '"+p+"_H0PM_W*("+me+"/MEH0PM)')  \n"

    if maxw is not "" :
     config += "addSampleWeight(samples,'"+sample+"','"+p+"_H0M_ToWWTo2L2Nu',     '"+p+"_H0M_W*min("+me+"/MEH0M, "+maxw+")')  \n"
    else :
     config += "addSampleWeight(samples,'"+sample+"','"+p+"_H0M_ToWWTo2L2Nu',     '"+p+"_H0M_W*("+me+"/MEH0M)')  \n"

    config += "addSampleWeight(samples,'"+sample+"','"+p+"_H0PH_ToWWTo2L2Nu',    '"+p+"_H0PH_W*("+me+"/MEH0PH)')  \n"
    config += "addSampleWeight(samples,'"+sample+"','"+p+"_H0L1_ToWWTo2L2Nu',    '"+p+"_H0L1_W*("+me+"/MEH0L1)')  \n"
    config += "addSampleWeight(samples,'"+sample+"','"+p+"_H0Mf05_ToWWTo2L2Nu',  '"+p+"_H0Mf05_W*("+me+"/MEH0Mf05"+p+")')   \n"
    config += "addSampleWeight(samples,'"+sample+"','"+p+"_H0PHf05_ToWWTo2L2Nu', '"+p+"_H0PHf05_W*("+me+"/MEH0PHf05"+p+")')  \n"
    config += "addSampleWeight(samples,'"+sample+"','"+p+"_H0L1f05_ToWWTo2L2Nu', '"+p+"_H0L1f05_W*("+me+"/MEH0L1f05"+p+")')  \n"
    config += "signals.append('"+sample+"')  \n"
    config += " \n"


fout = open ("meinfo/configs/eftsamples.py", "w")
fout.write( config )



         
