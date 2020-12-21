# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py    
#                    
structure['DY']  = {  
    'isSignal' : 0,
    'isData'   : 0
}

structure['Fake_ee']  = {  
    'isSignal' : 0,
    'isData'   : 0,
    'removeFromCuts' : [ k for k in cuts if 'ee' not in k],
}

structure['Fake_mm']  = {  
    'isSignal' : 0,
    'isData'   : 0,
    'removeFromCuts' : [ k for k in cuts if 'mm' not in k],
}

structure['Fake_df']  = {
    'isSignal' : 0,
    'isData'   : 0,
    'removeFromCuts' : [ k for k in cuts if 'df' not in k],
}

structure['top'] = {   
    'isSignal' : 0,
    'isData'   : 0 
}

structure['WW']  = {
    'isSignal' : 0,
    'isData'   : 0    
}

structure['WWewk']  = {
    'isSignal' : 0,
    'isData'   : 0
}

structure['ggWW']  = {
    'isSignal' : 0,
    'isData'   : 0    
}

structure['Vg']  = { 
    'isSignal' : 0,
    'isData'   : 0 
}

structure['VgS_L'] = {
    'isSignal' : 0,
    'isData'   : 0
}

structure['VgS_H'] = {
    'isSignal' : 0,
    'isData'   : 0
}

structure['VZ']  = { 
    'isSignal' : 0,
    'isData'   : 0 
}

structure['VVV']  = { 
    'isSignal' : 0,
    'isData'   : 0 
}

structure['ggH'] = {
    'isSignal' : 1,
    'isData'   : 0    
}

for signal in signals:
    print(signal)
    structure[signal] = {
        'isSignal' : 1,
        'isData'   : 0
    }


# data

structure['DATA']  = { 
    'isSignal' : 0,
    'isData'   : 1 
}

print "INSTRUCTURE"
print cuts
print "OK"

for nuis in nuisances.itervalues():
  if 'cutspost' in nuis:
    nuis['cuts'] = nuis['cutspost'](nuis, cuts)
    print nuis
