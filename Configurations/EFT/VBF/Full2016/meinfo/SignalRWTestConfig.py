 #!/usr/bin/env python

#################################################

## production mechanisms

Prod = [ "WH", "ZH" ]

## Original MC samples 

SigOrg  = [ "H0PM", "H0M", "H0PH", "H0L1"  ]

## Reweight all original samples to these hypotheses (Sample, ME)

SigRW = [ ("H0PM",    "MEH0PM"),
          ("H0M_M0",  "MEH0M_M0"), ("H0M_M1",  "MEH0M_M1"), ("H0M_M2",  "MEH0M_M2"), ("H0M_M3",  "MEH0M_M3"),
          ("H0PH_M0", "MEH0PH_M0"),("H0PH_M1", "MEH0PH_M1"),("H0PH_M2", "MEH0PH_M2"),("H0PH_M3", "MEH0PH_M3"),
          ("H0L1_M0", "MEH0L1_M0"),("H0L1_M1", "MEH0L1_M1"),("H0L1_M2", "MEH0L1_M2"),("H0L1_M3", "MEH0L1_M3")
        ]

###################### samples  ##########################

config =  "#### EFT Signals \n"
config += " \n"
config += "signals = [] \n"
config += " \n"

for p in Prod :

 config += "# "+p+" MC samples \n"
 config += " \n"

 for so in SigOrg : ### Add original samples (No reweighting)
  sampleOrg = ""+p+"_"+so+""
 
  config += "samples['"+sampleOrg+"'] = { \n"
  config += "   'name':   "   
  config += "nanoGetSampleFiles(mcDirectory, '"+sampleOrg+"_ToWWTo2L2Nu'), \n"
  config += "   'weight': mcCommonWeight+ '*"+sampleOrg+"_W', \n"
  config += "   'FilesPerJob': 2, \n"
  config += "} \n"
  config += "signals.append('"+sampleOrg+"')  \n"
  config += " \n"

 for so in SigOrg : ### Add reweighted samples
  sampleOrg = ""+p+"_"+so+""
  for s, me in SigRW :

     maxw = ""
     if so is "H0M" :
      if "H0PM" is s    : maxw = "0.9"
      if "H0M_M1" is s  : maxw = "5"
      if "H0M_M2" is s  : maxw = "20"
      if "H0M_M3" is s  : maxw = "30"
      if "H0PH_M0" is s : maxw = "40"
      if "H0PH_M1" is s : maxw = "5"
      if "H0PH_M2" is s : maxw = "30"
      if "H0PH_M3" is s : maxw = "70"
      if "H0L1_M0" is s : maxw = "120"
      if "H0L1_M1" is s : maxw = "6"
      if "H0L1_M2" is s : maxw = "20"
      if "H0L1_M3" is s : maxw = "30"

     config += "samples['"+sampleOrg+"_"+s+"'] = { \n"
     config += "   'name':   "   
     config += "nanoGetSampleFiles(mcDirectory, '"+sampleOrg+"_ToWWTo2L2Nu'), \n"
     if maxw is "" :
      config += "   'weight': mcCommonWeight+ '*"+sampleOrg+"_W*("+me+"/ME"+so+")', \n"
     else :
      config += "   'weight': mcCommonWeight+ '*"+sampleOrg+"_W*min("+me+"/ME"+so+","+maxw+")', \n"
     config += "   'FilesPerJob': 2, \n"
     config += "} \n"
     config += "signals.append('"+sampleOrg+"_"+s+"')  \n"
     config += " \n"

fout = open ("meinfo/configs/eftsamples_test.py", "w")
fout.write( config )

########################## weights #############################

config =  "#### EFT Signal weights \n"
config += " \n"

for p in Prod :

 config += "# "+p+" MC weights \n"
 config += " \n"

 for so in SigOrg :
  for s, me in SigRW :

    variable = "wgt"+p+"_"+so+"_"+s+""
 
    r1 = "0"
    r2 = "5000"
    if "H0L1" in so : 
     r1 = "10000000000"
     r2 = "10000000000000000000"
    elif "H0L1" in s : 
     r1 = "0"
     r2 = "20000"

    config += "variables['"+variable+"'] = { 'name' : '"+me+"/ME"+so+"', \n"
    config += "                     'range': (50000,"+r1+","+r2+"), 'xaxis': 'weight', 'fold' : 3 } \n"
    config += " \n"

fout = open ("meinfo/configs/eftweights_test.py", "w")
fout.write( config )



         
