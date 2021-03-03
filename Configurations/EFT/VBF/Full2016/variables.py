# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and 

'''
variables['ptjj'] = { 'name' : 'ptjj[0]',
                     'range': (50,0,1000),
                     'xaxis': 'p_{T}^{jj}',
                     'fold' : 3 
                   }

variables['ptl1'] = { 'name' : 'Lepton_pt[0]',
                     'range': (20,0,400),
                     'xaxis': 'p_{T}^{lep1}',
                     'fold' : 3 
                   }

variables['ptl2'] = { 'name' : 'Lepton_pt[1]',
                     'range': (20,0,400),
                      'xaxis': 'p_{T}^{lep2}',
                     'fold' : 3 
                   }

variables['met'] = { 'name' : 'PuppiMET_pt',
                     'range': (20,0,400),
                     'xaxis': 'MET',
                     'fold' : 3 
                   }

variables['mjj2'] = { 'name' : 'mjj',
                     'range': (80,0,400),
                     'xaxis': 'm_{jj}',
                     'fold' : 3 
                   }

variables['detajj'] = { 'name' : 'detajj',
                        'range': (30,0,10),
                        'xaxis': '#Delta#eta_{jj}',
                        'fold' : 3 
                   }

variables['lepcen1'] = { 'name' : 'lepcen1[0]',
                         'range': (25,0,5),
                         'xaxis': 'Centrality_{l1}',
                         'fold' : 3 
                        }

variables['lepcen2'] = { 'name' : 'lepcen2[0]',
                         'range': (25,0,5),
                         'xaxis': 'Centrality_{l2}',
                         'fold' : 3 
                        }

variables['njet'] = { 'name' : 'njet',
                      'range': (6,0,6),
                      'xaxis': 'number of jets',
                      'fold' : 3 
                   }

variables['nfjet'] = { 'name' : 'nCleanFatJet', # pt and tau21 cuts applied
                      'range': (5,0,5),
                      'xaxis': 'number of fat jets',
                      'fold' : 3 
                   }

variables['ptll'] = {   'name': 'ptll',
                        'range': (20,0,400),
                        'xaxis': 'p_{T}^{ll}',
                        'fold': 3
                       }

variables['mtw1'] = { 'name' : 'mtw1',
                     'range': (20,0,200),
                      'xaxis': 'm_{T}^{W1}',
                     'fold' : 3
                    }

variables['hm'] = { 'name' : 'hm',
                     'range': (20,0,400),
                     'xaxis': 'm_{H}',
                     'fold' : 3
                   }
'''


'''
#DEFAULT
variables['classvbf'] = { 
     'name': 'vbfdnn',
     'range' : ([0.25,0.4,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,1.0],),
     #'range' : ([0.3,0.4,0.5,0.6,0.7,0.8,1],),
     'xaxis' : 'DNN discriminant vbf',
     'fold'  : 3,
}
'''

'''
#S=5,B=10,E=0.2
variables['classvbf'] = { 
     'name': 'vbfdnn',
     'range' : ([0,0.545,0.635,0.695,0.745,0.785,1.],),
     'xaxis' : 'DNN discriminant vbf',
     'fold'  : 3,
}


variables['classtop'] = { 
     'name': 'topdnn',
     'range' : (15,0.25,1.),
      #'range' : ([0.3,0.4,0.5,0.6,0.7,0.8,1],),
     'xaxis' : 'DNN discriminant top',
     'fold'  : 3,
}


variables['classww'] = { 
     'name': 'wwdnn', 
     'range' : (15,0.25,1.),
     #'range' : ([0.3,0.4,0.5,0.6,0.7,0.8,1],),
     'xaxis' : 'DNN discriminant ww',
     'fold'  : 3,
}


#S=5,B=10,E=0.2
variables['classggh'] = { 
     'name': 'gghdnn',
     'range' : ([0.,0.485, 0.555, 0.615, 0.665, 0.715, 0.775, 0.865, 1.],),
     'xaxis' : 'DNN discriminant ggh',
     'fold'  : 3,
}

'''

'''
#DEFAULT
variables['classggh'] = { 
     'name': 'gghdnn',
     'range' : ([0.25,0.4,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,1.0],),
     #'range' : ([0.3,0.4,0.5,0.6,0.7,0.8,1],),
     'xaxis' : 'DNN discriminant ggh',
     'fold'  : 3,
}
'''


variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                         'fold' : 3
                        }

variables['mjj'] = { 'name' : 'mjj',
                     'range': (25,0,1000),
                     'xaxis': 'm_{jj}',
                     'fold' : 3 
                   }

variables['dphi'] = { 'name' : 'dphis',
                      'range': (10,-3.2,3.2),
                     'xaxis': 'DPhi_{jj}',
                     'fold' : 3 
                   }

variables['mll'] = { 'name' : 'mll',
                     'range': ([10,25,35,40,45,50,55,70,90,210],),
                     'xaxis': 'm_{ll}',
                     'fold' : 3 
                   }

'''
variables['mth'] = { 'name' : 'mth',
                     'range': (20,0,200),
                     'xaxis': 'm_{T}^{H}',
                     'fold' : 3
                   }


variables['pTWW'] = { 'name' : 'pTWW',
                     'range': (25,0,1000),
                     'xaxis': 'p_{T}^{H}',
                     'fold' : 3
                   }

'''
####################################

def DeclareKD3D(Prod,AC,Xaxis):

 kdmbinning = [0,0.5,0.75,1] # Main category 
 mllbinning = [10,35,55,90,210] # Subcategory
 kdbinning = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] # In each kdm*mll bin plot KD_BSM (12 bins of KD_BSM) 

 Cuts = ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_'+Prod+'','hww2l2v_13TeV_of2j_'+Prod+'_'+AC+'ip','hww2l2v_13TeV_of2j_'+Prod+'_'+AC+'in']

 if AC is "hl" : Cuts = ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_'+Prod+'']

 name = ''
 kdbin = ['1'] # folding underflow -> always 1
 for ikd in range(1, len(kdbinning) - 1):
    kdbin.append('(kd_'+Prod+'_'+AC+' >= %1.1f)' % kdbinning[ikd])
 name += '+'.join(kdbin)
 name += ' + %d*(' % (len(kdbinning) - 1)
 mllbin = [] # 1-1 for first bin
 for imll in range(1, len(mllbinning) - 1):
    mllbin.append('(mll >= %d)' % mllbinning[imll])
 name += '+'.join(mllbin)
 name += ')'
 name += ' + %d*(' % ((len(kdbinning) - 1)*(len(mllbinning) - 1))
 kdmbin = [] # 1-1 for first bin
 for ikdm in range(1, len(kdmbinning) - 1):
    kdmbin.append('(kd_'+Prod+' >= %1.1f)' % kdmbinning[ikdm])
 name += '+'.join(kdmbin)
 name += ') - 0.5'

 variables['kd3d_'+Prod+'_'+AC+''] = {
    'name': name,
    'range': (120, 0., 120.), # 3 x 4 x 10
    'xaxis': Xaxis, 
    'cuts' : Cuts
 }

##################################

############ VBF KD ############## 

variables['kd_vbf'] = { 'name' : 'kd_vbf',
                       'range': (20,0,1),
                       'xaxis': 'D_{VBF}',
                       'fold' : 3,
                       'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vbf']
                     }

variables['kd_vbf_hm'] = { 'name' : 'kd_vbf_hm',
                       'range': (20,0,1),
                       'xaxis': 'D_{VBF 0^{-}}',
                       'fold' : 3,
                       'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vbf']
                     }

variables['kd_vbf_hp'] = { 'name' : 'kd_vbf_hp',
                       'range': (20,0,1),
                       'xaxis': 'D_{VBF 0^{+}}',
                       'fold' : 3,
                       'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vbf']
                     }

variables['kd_vbf_hl'] = { 'name' : 'kd_vbf_hl',
                       'range': (20,0,1),
                        'xaxis': 'D_{VBF 0^{#Lambda 1}}',
                       'fold' : 3,
                       'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vbf']
                     }

variables['kd_vbf_mixhm'] = { 'name' : 'kd_vbf_mixhm',
                              'range': (20,-1,1),
                          'xaxis': 'D_{VBF CP}',
                          'fold' : 3,
                          'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vbf']
                        }

variables['kd_vbf_mixhp'] = { 'name' : 'kd_vbf_mixhp',
                          'range': (20,-1,1),
                          'xaxis': 'D_{VBF Int}',
                          'fold' : 3,
                          'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vbf']
                        }

DeclareKD3D('vbf','hm','D_{VBF 0^{-}}')
DeclareKD3D('vbf','hp','D_{VBF 0^{+}}')
DeclareKD3D('vbf','hl','D_{VBF 0^{#Lambda 1}}')

############ VH KD ######################

variables['kd_vh'] = { 'name' : 'kd_vh',
                       'range': (20,0,1),
                       'xaxis': 'D_{VH}',
                       'fold' : 3,
                       'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vh']
                     }

variables['kd_vh_hm'] = { 'name' : 'kd_vh_hm',
                       'range': (20,0,1),
                       'xaxis': 'D_{VH 0^{-}}',
                       'fold' : 3,
                       'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vh']
                     }

variables['kd_vh_hp'] = { 'name' : 'kd_vh_hp',
                       'range': (20,0,1),
                       'xaxis': 'D_{VH 0^{+}}',
                       'fold' : 3,
                       'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vh']
                     }

variables['kd_vh_hl'] = { 'name' : 'kd_vh_hl',
                       'range': (20,0,1),
                       'xaxis': 'D_{VH 0^{#Lambda 1}}',
                       'fold' : 3,
                       'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vh']
                     }


variables['kd_vh_mixhm'] = { 'name' : 'kd_vh_mixhm',
                             'range': (20,-1,1),
                          'xaxis': 'D_{VH CP}',
                          'fold' : 3,
                          'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vh']
                        }

variables['kd_vh_mixhp'] = { 'name' : 'kd_vh_mixhp',
                             'range': (20,-1,1),
                          'xaxis': 'D_{VH Int}',
                          'fold' : 3,
                          'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vh']
                        }


variables['kd2d_vh_hm'] = { 'name': 'kd_vh_hm:mll',   
                         'range' : ([10,35,45,55,90,210],[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],),     
                         'xaxis' : 'D_{VH 0^{-}:m_{ll}}',     
                         'fold' : 3,
                         'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vh','hww2l2v_13TeV_of2j_vh_hmip','hww2l2v_13TeV_of2j_vh_hmin']
                          }

variables['kd2d_vh_hp'] = { 'name': 'kd_vh_hp:mll',   
                         'range' : ([10,35,45,55,90,210],[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],),     
                            'xaxis' : 'D_{VH 0^{+}:m_{ll}}',     
                         'fold' : 3,
                         'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vh','hww2l2v_13TeV_of2j_vh_hpip','hww2l2v_13TeV_of2j_vh_hpin']
                          }

variables['kd2d_vh_hl'] = { 'name': 'kd_vh_hl:mll',   
                         'range' : ([10,35,45,55,90,210],[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],),     
                         'xaxis' : 'D_{VH 0^{#Lambda 1}:m_{ll}}',     
                         'fold' : 3,
                         'cuts' : ['hww2l2v_13TeV_top_of2j','hww2l2v_13TeV_dytt_of2j','hww2l2v_13TeV_of2j_vh']
                          }


