
# plot configuration

### Backgrounds

plot['WW']  = {  
                  'nameHR' : 'WW',
                  'color': 2, 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1,
                 }

plot['DY']  = {  
                  'nameHR' : 'DY',
                  'color': 3, 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1,
                 }

plot['TTbar']  = {  
                  'nameHR' : 'TTbar',
                  'color': 5, 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1,
                 }

### Higgs Backgrounds

plot['qqH_htt']  = {  
                  'nameHR' : 'VBF h #rightarrow #tau #tau',
                  'color': 65, 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1,
                 }

plot['ggH_htt']  = {  
                  'nameHR' : 'gg h #rightarrow #tau #tau',
                  'color': 69, 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1,
                 }

plot['ggH_hww']  = {  
                  'nameHR' : 'gg h',
                  'color': 95, 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1,
                 }

'''
plot['qqH_hww'] = {  
                  'nameHR' : 'VBF h #rightarrow WW (STD)',
                  'color': 95, 
                  'isSignal' : 3,
                  'isData'   : 0,
                  'scale'    : 1,
                  }
'''
##### VBF Higgs Signals

plot['VBFH0PM'] = {  
                  'nameHR' : 'VBF h',
                  'color': 4, 
                  'isSignal' : 3, 
                  'isData'   : 0,
                  'scale'    : 1,
                  }

plot['VBFH0M']  =   {
                      'nameHR' : 'VBF 0^{-}',
                      'color' : 1,
                      'isSignal' : 3, 
                      'isData'   : 0,
                      'scale'    : 1,
                     }

plot['VBFH0PH']  =    {
                      'nameHR' : 'VBF 0^{+}',
                      'color' : 2,
                      'isSignal' : 3,
                      'isData'   : 0,
                      'scale'    : 1,
                      }

'''

plot['VBFH0PHf05']  = {
                      'nameHR' : 'h-0^{+} mix',
                      'color' : 4,
                      'isSignal' : 3,
                      'isData'   : 0,
                      'scale'    : 1,
                      }

plot['VBFH0Mf05']  = {  
                   'nameHR' : 'h-0^{-} mix',
                   'color': 2, 
                   'isSignal' : 3,
                   'isData'   : 0,
                   'scale'    : 1,
                 }

'''

'''
plot['VBFH0M_rw0PM']  = {  
                  'nameHR' : 'SM h (0^{-} reweighted)',
                  'color': 2, 
                  'isSignal' : 3,
                  'isData'   : 0,
                  'scale'    : 1,
                 }

plot['VBFH0PM_rw0M']  = {  
                  'nameHR' : '0^{-} (SM h reweighted)',
                  'color': 6, 
                  'isSignal' : 3,
                  'isData'   : 0,
                  'scale'    : 1,
                 }
'''

# VH

plot['VH0PM'] = {  
                  'nameHR' : 'V h ',
                  'color': 3, 
                  'isSignal' : 3, 
                  'isData'   : 0,
                  'scale'    : 1,
                  }

plot['VH0M']  =   {
                      'nameHR' : 'V 0^{-}',
                      'color' : 8,
                      'isSignal' : 3, 
                      'isData'   : 0,
                      'scale'    : 1,
                     }

plot['VH0PH']  =   {
                      'nameHR' : 'V 0^{+}',
                      'color' : 7,
                      'isSignal' : 3, 
                      'isData'   : 0,
                      'scale'    : 1,
                     }

'''
plot['VH0M_rw0PM']  = {  
                  'nameHR' : 'SM h (0^{-} reweighted)',
                  'color': 2, 
                  'isSignal' : 3,
                  'isData'   : 0,
                  'scale'    : 1,
                 }

plot['VH0PM_rw0M']  = {  
                  'nameHR' : '0^{-} (SM h reweighted)',
                  'color': 6, 
                  'isSignal' : 3,
                  'isData'   : 0,
                  'scale'    : 1,
                 }
'''

# additional options

legend['lumi'] = 'L = 35.9/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'




