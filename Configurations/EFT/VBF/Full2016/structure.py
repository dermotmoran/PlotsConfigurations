
# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py    
#                    

structure['VBFH0PM'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0PM_Org'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0M'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0M_Org'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0Mf05_Org'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0M_M1'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0M_M2'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0M_M3'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0PH'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0PH_Org'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0PHf05_Org'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0PH_M1'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0PH_M2'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0PH_M3'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0L1'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0L1_Org'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0L1f05_Org'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0L1_M1'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0L1_M2'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['VBFH0L1_M3'] = {
                  'isSignal' : 1,
                  'isData'   : 0
                  }

structure['WW'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['DY'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['TTbar'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['qqH_htt'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['ggH_htt'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

structure['ggH_hww'] = {
                  'isSignal' : 0,
                  'isData'   : 0
                  }

# data

structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }

print "INSTRUCTURE"
print cuts
#print nuisances['WWresum0j']
print "OK"

#for nuis in nuisances.itervalues():
#  if 'cutspost' in nuis:
#    nuis['cuts'] = nuis['cutspost'](nuis, cuts)
#    print nuis



