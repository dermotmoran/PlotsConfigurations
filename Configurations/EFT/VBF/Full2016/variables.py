
# variables

#variables = {}
    

variables['mjj'] = { 'name' : 'mjj',
                     'range': (80,0,4000),
                     'xaxis': 'm_{jj}',
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

variables['lepcen1'] = { 'name' : 'lepcen1',
                         'range': (25,0,5),
                         'xaxis': 'Centrality_{l1}',
                         'fold' : 3 
                        }

variables['lepcen2'] = { 'name' : 'lepcen2',
                         'range': (25,0,5),
                         'xaxis': 'Centrality_{l2}',
                         'fold' : 3 
                        }

variables['mll'] = { 'name' : 'mll',
                     'range': (20,0,200),
                     'xaxis': 'm_{ll}',
                     'fold' : 3 
                   }

variables['njet'] = { 'name' : 'njet',
                      'range': (5,0,5),
                      'xaxis': 'number of jets',
                      'fold' : 3 
                   }

variables['ptll'] = {   'name': 'ptll',
                        'range': (20,0,400),
                        'xaxis': 'p_{T}^{ll}',
                        'fold': 3
                       }

variables['mth'] = { 'name' : 'mth',
                     'range': (20,0,200),
                     'xaxis': 'm_{T}^{H}',
                     'fold' : 3
                   }

variables['mtw2'] = { 'name' : 'mtw2',
                     'range': (20,0,200),
                     'xaxis': 'm_{T}^{W2}',
                     'fold' : 3
                    }

variables['mtw1'] = { 'name' : 'mtw1',
                     'range': (20,0,200),
                      'xaxis': 'm_{T}^{W1}',
                     'fold' : 3
                    }

variables['hpt'] = { 'name' : 'hpt',
                     'range': (50,0,1000),
                     'xaxis': 'p_{T}^{H}',
                     'fold' : 3
                   }


variables['hm'] = { 'name' : 'hm',
                     'range': (20,0,400),
                     'xaxis': 'm_{H}',
                     'fold' : 3
                   }

############ VBF KD ############## 

variables['kd_vbf'] = { 'name' : 'kd_vbf',
                       'range': (20,0,1),
                       'xaxis': 'D_{VBF}',
                       'fold' : 3
                     }

variables['kd_vbf_hm'] = { 'name' : 'kd_vbf_hm',
                       'range': (20,0,1),
                       'xaxis': 'D_{VBF 0^{-}}',
                       'fold' : 3
                     }

variables['kd_vbf_mixhm'] = { 'name' : 'kd_vbf_mixhm',
                          'range': (20,-1,1),
                          'xaxis': 'D_{VBF CP}',
                          'fold' : 3
                        }

variables['kd_vbf_hp'] = { 'name' : 'kd_vbf_hp',
                       'range': (20,0,1),
                       'xaxis': 'D_{VBF 0^{+}}',
                       'fold' : 3
                     }

variables['kd_vbf_mixhp'] = { 'name' : 'kd_vbf_mixhp',
                          'range': (20,-1,1),
                          'xaxis': 'D_{VBF Int}',
                          'fold' : 3
                        }

variables['kd_vbf_hl'] = { 'name' : 'kd_vbf_hl',
                       'range': (20,0,1),
                        'xaxis': 'D_{VBF 0^{#Lambda 1}}',
                       'fold' : 3
                     }


############ VH KD ######################

variables['kd_vh'] = { 'name' : 'kd_vh',
                       'range': (20,0,1),
                       'xaxis': 'D_{VH}',
                       'fold' : 3
                     }

variables['kd_vh_hm'] = { 'name' : 'kd_vh_hm',
                       'range': (20,0,1),
                       'xaxis': 'D_{VH 0^{-}}',
                       'fold' : 3
                     }

variables['kd_vh_mixhm'] = { 'name' : 'kd_vh_mixhm',
                          'range': (20,-1,1),
                          'xaxis': 'D_{VH CP}',
                          'fold' : 3
                        }

variables['kd_vh_hp'] = { 'name' : 'kd_vh_hp',
                       'range': (20,0,1),
                       'xaxis': 'D_{VH 0^{+}}',
                       'fold' : 3
                     }

variables['kd_vh_mixhp'] = { 'name' : 'kd_vh_mixhp',
                          'range': (20,-1,1),
                          'xaxis': 'D_{VH Int}',
                          'fold' : 3
                        }

variables['kd_vh_hl'] = { 'name' : 'kd_vh_hl',
                       'range': (20,0,1),
                       'xaxis': 'D_{VH 0^{#Lambda 1}}',
                       'fold' : 3
                     }
