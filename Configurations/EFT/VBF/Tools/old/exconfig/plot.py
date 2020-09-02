
# plot configuration

### Backgrounds

plot['WW']  = {  
                  'nameHR' : 'WW',
                  'color': 7, 
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
                  'color': 6, 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1,
                 }

plot['ggH_htt']  = {  
                  'nameHR' : 'gg h #rightarrow #tau #tau',
                  'color': 12, 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1,
                 }

plot['ggH_hww']  = {  
                  'nameHR' : 'gg h',
                  'color': 12, 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1,
                 }


'''
plot['qqH_hww'] = {  
                  'nameHR' : 'VBF h #rightarrow WW (STD)',
                  'color': 95, 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1,
                  }
'''

##### VBF Higgs Signals

plot['VBFH0PM'] = {  
                  'nameHR' : 'VBF h',
                  'color': 2, 
                  'isSignal' : 3, 
                  'isData'   : 0,
                  'scale'    : 1,
                  }

plot['VBFH0M']  =   {
                      'nameHR' : 'VBF 0^{-}',
                      'color' : 2,
                      'isSignal' : 3, 
                      'isData'   : 0,
                      'scale'    : 1,
                     }

plot['VBFH0M_Int']  =    {
                      'nameHR' : 'VBF h-0^{-} Int',
                      'color' : 2,
                      'isSignal' : 3,
                      'isData'   : 0,
                      'scale'    : 1,
                      }


'''
plot['VBFH0PH']  =    {
                      'nameHR' : 'VBF 0^{+}',
                      'color' : 2,
                      'isSignal' : 3,
                      'isData'   : 0,
                      'scale'    : 1,
                      }

plot['VBFH0PH_Int']  =    {
                      'nameHR' : 'VBF h-0^{+} Int',
                      'color' : 2,
                      'isSignal' : 3,
                      'isData'   : 0,
                      'scale'    : 1,
                      }

plot['VBFH0L1']  =    {
                      'nameHR' : 'VBF 0^{#Lambda 1}',
                      'color' : 3,
                      'isSignal' : 0,
                      'isData'   : 0,
                      'scale'    : 1,
                      }
'''

# VH

plot['VH0PM'] = {  
                  'nameHR' : 'VH h ',
                  'color': 4, 
                  'isSignal' : 3, 
                  'isData'   : 0,
                  'scale'    : 1,
                  }

plot['VH0M']  =   {
                      'nameHR' : 'VH 0^{-}',
                      'color' : 4,
                      'isSignal' : 3, 
                      'isData'   : 0,
                      'scale'    : 1,
                     }

plot['VH0M_Int']  =   {
                      'nameHR' : 'VH h-0^{-} Int',
                      'color' : 4,
                      'isSignal' : 3, 
                      'isData'   : 0,
                      'scale'    : 1,
                     }

'''
plot['VH0PH']  =   {
                      'nameHR' : 'VH 0^{+}',
                      'color' : 4,
                      'isSignal' : 3, 
                      'isData'   : 0,
                      'scale'    : 1,
                     }

plot['VH0PH_Int']  =   {
                      'nameHR' : 'VH h-0^{+} Int',
                      'color' : 4,
                      'isSignal' : 3, 
                      'isData'   : 0,
                      'scale'    : 1,
                     }

plot['VH0L1']  =   {
                      'nameHR' : 'VH 0^{#Lambda 1}',
                      'color' : 7,
                      'isSignal' : 3, 
                      'isData'   : 0,
                      'scale'    : 1,
                     }
'''

# data

'''
plot['DATA']  = { 
                  'nameHR' : 'Data',
                  'color': 1 ,  
                  'isSignal' : 0,
                  'isData'   : 1,
                  'isBlind'  : 1
                }
'''

# additional options

legend['lumi'] = 'L = 35.9/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'




