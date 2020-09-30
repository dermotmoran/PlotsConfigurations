 #!/usr/bin/env python

#################################################

## production mechanisms

Prod = [ "ggH" ]

## Original MC samples  

SigOrg  = [ "H0PM", "H0M", "H0Mf05", "H0PH", "H0PHf05", "H0L1", "H0L1f05" ] 

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

###################### samples  ##########################

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

 for so in SigOrg :  # Use this for weights variable test

  sampleOrg = ""+fp+so+""
 
  config += "samples['"+sampleOrg+"'] = { \n"
  config += "   'name':   "   
  config += "nanoGetSampleFiles(mcDirectory, '"+sampleOrg+"_ToWWTo2L2Nu'), \n"
  config += "   'weight': mcCommonWeight+ '*"+sampleOrg+"_W', \n"
  config += "   'FilesPerJob': 2, \n"
  config += "} \n"
  config += "signals_"+p+".append('"+sampleOrg+"')  \n"
  config += " \n"

 config += "# Reweighted "+p+" samples \n"
 config += " \n"

 for so in SigOrg : 

  sampleOrg = ""+fp+so+""
  for s, me in SigRW :

     meRW = "ME_"+fp+me+""

     maxw = ""
     if sampleOrg is "WH_H0M" or sampleOrg is "ZH_H0M" :
      if "H0PM"    is s : maxw = "0.9"
      if "H0M_M1"  is s : maxw = "5"
      if "H0M_M2"  is s : maxw = "20"
      if "H0M_M3"  is s : maxw = "30"
      if "H0PH"    is s : maxw = "40"
      if "H0PH_M1" is s : maxw = "5"
      if "H0PH_M2" is s : maxw = "30"
      if "H0PH_M3" is s : maxw = "70"
      if "H0L1"    is s : maxw = "120"
      if "H0L1_M1" is s : maxw = "6"
      if "H0L1_M2" is s : maxw = "20"
      if "H0L1_M3" is s : maxw = "30"

     config += "samples['"+sampleOrg+"_"+s+"'] = { \n"
     config += "   'name':   "   
     config += "nanoGetSampleFiles(mcDirectory, '"+sampleOrg+"_ToWWTo2L2Nu'), \n"
     if maxw is "" :
      config += "   'weight': mcCommonWeight+ '*"+sampleOrg+"_W*("+meRW+"/ME_"+sampleOrg+")', \n"
     else :
      config += "   'weight': mcCommonWeight+ '*"+sampleOrg+"_W*min("+meRW+"/ME_"+sampleOrg+","+maxw+")', \n"
     config += "   'FilesPerJob': 2, \n"
     config += "} \n"
     config += "signals_"+p+".append('"+sampleOrg+"_"+s+"')  \n"
     config += " \n"

fout = open ("/afs/cern.ch/work/d/dmoran/private/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/EFT/VBF/Tools/configs/eftsamples_test.py", "w")
fout.write( config )

########################## weights #############################################################################################
### If including this should run 1 production mechanism at a time.

config =  "#### EFT Signal weights \n"
config += " \n"

for p in Prod :

 config += "# "+p+" MC weights \n"
 config += " \n"

 fp = ""+p+"_"
 SigRW = SigRW2
 if p == "ggH" : 
  fp = ""
  SigRW = SigRW1

 for so in SigOrg :

  sampleOrg = ""+fp+so+""

  for s, me in SigRW :

    variable = "wgt_"+sampleOrg+"_"+s+""
    meRW = "ME_"+fp+me+""

    r1 = "0"
    r2 = "5000"
    if "H0L1" in so : 
     r1 = "10000000000"
     r2 = "10000000000000000000"
    elif "H0L1" in s : 
     r1 = "0"
     r2 = "20000"

    config += "variables['"+variable+"'] = { 'name' : '"+meRW+"/ME_"+sampleOrg+"', \n"
    config += "                     'range': (50000,"+r1+","+r2+"), 'xaxis': 'weight', 'fold' : 3 } \n"
    config += " \n"

fout = open ("/afs/cern.ch/work/d/dmoran/private/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/EFT/VBF/Tools/configs/eftweights_test.py", "w")
fout.write( config )


         
