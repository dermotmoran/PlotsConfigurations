
# variables

#variables = {}
    

'''
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  

                        'xaxis' : 'events', 
                        'fold' : 3
                        }


variables['genLepton_pt']  = {   'name': 'LeptonGen_pt',
                        'range' : (20,0,200),
                        'xaxis' : 'p_{T}^{Gen}',
                        'fold' : 3
                        }
'''

variables['mjj'] = { 'name' : 'mjj',
                     'range': (80,0,4000),
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

variables['hmVSkdhm'] = {   'name': 'hm:kd_hm', 
                            'range': ([0.0,0.25,0.5,0.75,1.0],[50,100,125,150,175,200,250,400]),
                            'xaxis': 'm_{H} : D_{0^{-}}',
                            'fold': 3
                        }

variables['mllVSkdhm'] = {   'name': 'mll:kd_hm', 
                             'range': ([0.0,0.25,0.5,0.75,1.0],[10,15,20,25,30,40,50,60,70],),
                           'xaxis': 'm_{ll} : D_{0^{-}}',
                           'fold': 3
                       }

variables['hm'] = { 'name' : 'hm',
                     'range': (20,0,400),
                     'xaxis': 'm_{H}',
                     'fold' : 3
                   }


variables['kd_smvbf'] = { 'name' : 'kd_smvbf',
                       'range': (20,0,1),
                       'xaxis': 'D_{h VBF}',
                       'fold' : 3
                     }

variables['kd_hmvbf'] = { 'name' : 'kd_hmvbf',
                       'range': (20,0,1),
                       'xaxis': 'D_{0^{-} VBF}',
                       'fold' : 3
                     }

variables['kd_vbf'] = { 'name' : 'kd_vbf',
                       'range': (20,0,1),
                       'xaxis': 'D_{VBF}',
                       'fold' : 3
                     }

variables['kd_hm'] = { 'name' : 'kd_hm',
                       'range': (20,0,1),
                       'xaxis': 'D_{0^{-}}',
                       'fold' : 3
                     }

variables['kd_mixhm'] = { 'name' : 'kd_mixhm',
                          'range': (20,-1,1),
                          'xaxis': 'D_{CP}',
                          'fold' : 3
                        }

variables['kd_hp'] = { 'name' : 'kd_hp',
                       'range': (20,0,1),
                       'xaxis': 'D_{0^{+}}',
                       'fold' : 3
                     }

variables['kd_mixhp'] = { 'name' : 'kd_mixhp',
                          'range': (20,-1,1),
                          'xaxis': 'D_{Int}',
                          'fold' : 3
                        }


'''
variables['dphill'] = { 'name' : 'dphill',
                     'range': (20,0,3.14),
                     'xaxis': '#Delta#Phi_{ll}',
                     'fold' : 3
                }

variables['pTWW'] = {   'name': 'pTWW',
                           'range': (20,0,200),
                           'xaxis': 'p_{T}^{WW}',
                           'fold': 3
                       }

variables['mllVSmth_pt2ge20'] = {   'name': 'mll:mth',            #   variable name    
                             'range' : ([60,80,90,100,110,120,130,150,200],[12,25,35,40,45,50,55,70,90,210],),            #   variable range
                             'xaxis' : 'm_{ll} : m_{T}^{H}',      #   x axis name
                             'fold' : 3 ,
                             # do weighted plot too
                             'doWeight' : 1,
                             'binX'     : 8,
                             'binY'     : 9
                             #
                             }

variables['mllVSmth_pt2lt20'] = {   'name': 'mll:mth',            #   variable name    
                             'range' : ([60,80,90,110,130,150,200],[12,25,40,50,70,90,210],),            #   variable range
                             'xaxis' : 'm_{ll} : m_{T}^{H}',      #   x axis name
                             'fold' : 3 ,
                             # do weighted plot too
                             'doWeight' : 1,
                             'binX'     : 6,
                             'binY'     : 6
                             #
                             }
'''
