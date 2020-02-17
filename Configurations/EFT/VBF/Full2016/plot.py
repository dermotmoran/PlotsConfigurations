
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
                  'nameHR' : 'gg h #rightarrow WW',
                  'color': 95, 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1,
                 }


##### VBF Higgs Signals

plot['VBFH0PM'] = {  
                  'nameHR' : 'VBF h #rightarrow WW',
                  'color': 4, 
                  'isSignal' : 3, 
                  'isData'   : 0,
                  'scale'    : 1,
                  }

plot['VBFH0M']  =   {
                      'nameHR' : '0^{-}',
                      'color' : 1,
                      'isSignal' : 3, 
                      'isData'   : 0,
                      'scale'    : 1,
                     }

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
                  'color': 2, 
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

plot['VBFH0PH']  =    {
                      'nameHR' : '0^{+}',
                      'color' : 2,
                      'isSignal' : 3,
                      'isData'   : 0,
                      'scale'    : 1,
                      }

plot['VBFH0PHf05']  = {
                      'nameHR' : 'h-0^{+} mix',
                      'color' : 4,
                      'isSignal' : 3,
                      'isData'   : 0,
                      'scale'    : 1,
                      }

'''

# additional options

legend['lumi'] = 'L = 35.9/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'




