 #!/usr/bin/env python

#################################################

## 4 production mechanisms

Prod = [ "VBF", "WH", "ZH", "ggH" ]

## 7 Original MC samples 

Sig  = [ "H0PM", "H0M", "H0Mf05", "H0PH", "H0PHf05", "H0L1", "H0L1f05" ]

## Reweight all 7 samples to these hypotheses (name, ME) for ggH (1 vertex - 3 hypotheses)

SigRW1 = [("H0PM", "H0PM"),
          ("H0M",  "H0M"), ("H0M_M1", "H0Mf05"),
          ("H0PH", "H0PH"),("H0PH_M1", "H0PHf05"),
          ("H0L1", "H0L1"),("H0L1_M1", "H0L1f05"),
        ]

## Reweight all 7 samples to these hypotheses (name, ME) for VBF, WH, and ZH (2 vertices - 5 hypotheses)

SigRW2 = [("H0PM", "H0PM"),
          ("H0M",  "H0M_M0"), ("H0M_M1",  "H0M_M1"), ("H0M_M2",  "H0M_M2"), ("H0M_M3",  "H0M_M3"),
          ("H0PH", "H0PH_M0"),("H0PH_M1", "H0PH_M1"),("H0PH_M2", "H0PH_M2"),("H0PH_M3", "H0PH_M3"),
          ("H0L1", "H0L1_M0"),("H0L1_M1", "H0L1_M1"),("H0L1_M2", "H0L1_M2"),("H0L1_M3", "H0L1_M3")
        ]

################################################

config =  "#### EFT Signals \n"
config += " \n"
config += "signals_ggH = [] \n"
config += "signals_VBF = [] \n"
config += "signals_WH = [] \n"
config += "signals_ZH = [] \n"
config += " \n"

for p in Prod :

 config += "# Original "+p+" MC samples \n"
 config += " \n"

 fp = ""+p+"_"
 SigRW = SigRW2
 if p == "ggH" : 
  fp = ""
  SigRW = SigRW1

 for s in Sig :

    sample = ""+fp+s+""

    config += "samples['"+sample+"_Org'] = { \n"
    config += "   'name': nanoGetSampleFiles(mcDirectory, '"+sample+"_ToWWTo2L2Nu'), \n"
    config += "   'weight': mcCommonWeight + '*"+sample+"_W', \n"
    config += "   'FilesPerJob': 1 \n"
    config += "} \n"
    config += " \n"

 config += "# Reweighted "+p+" samples \n"
 config += " \n"

 for s, me in SigRW :

    sample = ""+fp+s+""

    config += "samples['"+sample+"'] = { \n"
    config += "   'name':   "   
    config += "nanoGetSampleFiles(mcDirectory, '"+fp+"H0PM_ToWWTo2L2Nu') + "
    config += "nanoGetSampleFiles(mcDirectory, '"+fp+"H0M_ToWWTo2L2Nu') + " 
    config += "nanoGetSampleFiles(mcDirectory, '"+fp+"H0PH_ToWWTo2L2Nu') + "
    config += "nanoGetSampleFiles(mcDirectory, '"+fp+"H0L1_ToWWTo2L2Nu') + " 
    config += "nanoGetSampleFiles(mcDirectory, '"+fp+"H0Mf05_ToWWTo2L2Nu') + " 
    config += "nanoGetSampleFiles(mcDirectory, '"+fp+"H0PHf05_ToWWTo2L2Nu') + " 
    config += "nanoGetSampleFiles(mcDirectory, '"+fp+"H0L1f05_ToWWTo2L2Nu'), \n"
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

    config += "addSampleWeight(samples,'"+sample+"','"+fp+"H0PM_ToWWTo2L2Nu',    '"+fp+"H0PM_W*(ME_"+fp+me+"/ME_"+fp+"H0PM)')  \n"

    if maxw is not "" :
     config += "addSampleWeight(samples,'"+sample+"','"+fp+"H0M_ToWWTo2L2Nu',     '"+fp+"H0M_W*min(ME_"+fp+me+"/ME_"+fp+"H0M, "+maxw+")')  \n"
    else :
     config += "addSampleWeight(samples,'"+sample+"','"+fp+"H0M_ToWWTo2L2Nu',     '"+fp+"H0M_W*(ME_"+fp+me+"/ME_"+fp+"H0M)')  \n"

    config += "addSampleWeight(samples,'"+sample+"','"+fp+"H0PH_ToWWTo2L2Nu',    '"+fp+"H0PH_W*(ME_"+fp+me+"/ME_"+fp+"H0PH)')  \n"
    config += "addSampleWeight(samples,'"+sample+"','"+fp+"H0L1_ToWWTo2L2Nu',    '"+fp+"H0L1_W*(ME_"+fp+me+"/ME_"+fp+"H0L1)')  \n"
    config += "addSampleWeight(samples,'"+sample+"','"+fp+"H0Mf05_ToWWTo2L2Nu',  '"+fp+"H0Mf05_W*(ME_"+fp+me+"/ME_"+fp+"H0Mf05)')   \n"
    config += "addSampleWeight(samples,'"+sample+"','"+fp+"H0PHf05_ToWWTo2L2Nu', '"+fp+"H0PHf05_W*(ME_"+fp+me+"/ME_"+fp+"H0PHf05)')  \n"
    config += "addSampleWeight(samples,'"+sample+"','"+fp+"H0L1f05_ToWWTo2L2Nu', '"+fp+"H0L1f05_W*(ME_"+fp+me+"/ME_"+fp+"H0L1f05)')  \n"
    config += "signals_"+p+".append('"+sample+"')  \n"
    config += " \n"


fout = open ("meinfo/configs/eftsamples.py", "w")
fout.write( config )



         
