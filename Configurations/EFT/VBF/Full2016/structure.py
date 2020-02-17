
# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py    
#                    

structure['VBFH0PM'] = {
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

structure['VBFH0M'] = {
                  'isSignal' : 3,
                  'isData'   : 0
                  }

structure['VBFH0PM_rw0M'] = {
                  'isSignal' : 3,
                  'isData'   : 0
                  }

structure['VBFH0M_rw0PM'] = {
                  'isSignal' : 3,
                  'isData'   : 0
                  }

structure['VBFH0Mf05'] = {
                  'isSignal' : 3,
                  'isData'   : 0
                  }

structure['VBFH0PH'] = {
                  'isSignal' : 3,
                  'isData'   : 0
                  }

structure['VBFH0PHf05'] = {
                  'isSignal' : 3,
                  'isData'   : 0
                  }


print "INSTRUCTURE"
print cuts
#print nuisances['WWresum0j']
print "OK"

#for nuis in nuisances.itervalues():
#  if 'cutspost' in nuis:
#    nuis['cuts'] = nuis['cutspost'](nuis, cuts)
#    print nuis



