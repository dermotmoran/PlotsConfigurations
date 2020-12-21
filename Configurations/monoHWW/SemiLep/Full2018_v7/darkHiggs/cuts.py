super_cut = [ 
    'nLepton>=1',
    # SingleMuon trigger: IsoMu24, SingleElectron trigger: HLT_Ele32_WPTight_Gsf
    '((Lepton_pt[0]>24. && abs(Lepton_pdgId[0])==13) || (Lepton_pt[0]>32. && abs(Lepton_pdgId[0])==11))',
    'Sum$(CleanJet_pt>30.)>=2',
    'MHlnjj_m_jj > -1', # Require 2 good CleanJets (pt > 30; abs(eta) < 4.7; Jet_jetId >= 2; pujetid == 'custom')
]

supercut = ' && '.join(super_cut)

def combinecut(cut_list):
    comb_cut = []
    for cut in cut_list:
        comb_cut.extend(cut)
    return comb_cut

def addcut(name, exprs):
    cuts[name] = ' && '.join(exprs)

is_el    = ['abs(Lepton_pdgId[0])==11']
is_mu    = ['abs(Lepton_pdgId[0])==13']

#veto_1l      = ['Alt$(Lepton_pt[1],0)<10.']
#veto_1l_I    = ['(nLepton>=2 && Lepton_pt[1] > 20)']
mt_lmet      = ['mtw1 > 80']
mt_lmet_I    = ['mtw1 < 50']
met          = ['PuppiMET_pt > 60']
met_I        = ['PuppiMET_pt < 50']
dphi_l_jj    = ['MHlnjj_dphi_jjVl < 1.8']
dphi_ljj_met = ['MHlnjj_dphi_ljjVmet > 2.']
dr_l_jj      = ['MHlnjj_dr_jjVl < 3.']
pt_ljj       = ['MHlnjj_pt_ljj > 60']
pt_ljj_I     = ['MHlnjj_pt_ljj < 60']
veto_1l      = ['Alt$(Lepton_pt[1],0)<10.']
veto_1l_I    = ['(nLepton>=2 && Lepton_pt[1] > 20)']
veto_b       = ['bVeto']
veto_b_I     = ['bReq']
m_jj         = ['(MHlnjj_m_jj > 65. && MHlnjj_m_jj < 105.)']
m_jj_I       = ['(MHlnjj_m_jj < 65. || MHlnjj_m_jj > 105.)']

SC       = super_cut
SR       = combinecut([super_cut, mt_lmet  , met  , dphi_l_jj, dphi_ljj_met, dr_l_jj, pt_ljj  , m_jj  , veto_b  , veto_1l  ])
CR       = combinecut([super_cut, mt_lmet  , met  , dphi_l_jj, dphi_ljj_met, dr_l_jj, pt_ljj_I, veto_b  , veto_1l  ])
SB       = combinecut([super_cut, mt_lmet  , met  , dphi_l_jj, dphi_ljj_met, dr_l_jj, pt_ljj  , m_jj_I, veto_b  , veto_1l  ])
TCR      = combinecut([super_cut, mt_lmet  , met  , dphi_l_jj, dphi_ljj_met, dr_l_jj, pt_ljj  , m_jj  , veto_b_I, veto_1l  ])
DYCR     = combinecut([super_cut, mt_lmet  , met  , dphi_l_jj, dphi_ljj_met, dr_l_jj, pt_ljj  , m_jj  , veto_b  , veto_1l_I])
QER      = combinecut([super_cut, mt_lmet_I, met_I, dphi_l_jj, dphi_ljj_met, dr_l_jj, pt_ljj  , m_jj  , veto_b  , veto_1l  ])

# Electron
addcut('ElCh_SC'  , combinecut([is_el, SC  ]))
addcut('ElCh_SR'  , combinecut([is_el, SR  ]))
addcut('ElCh_CR'  , combinecut([is_el, CR  ]))
addcut('ElCh_SB'  , combinecut([is_el, SB  ]))
addcut('ElCh_TCR' , combinecut([is_el, TCR ]))
#addcut('ElCh_DYCR', combinecut([is_el, DYCR]))
addcut('ElCh_QER' , combinecut([is_el, QER ]))

# Muon
addcut('MuCh_SC'  , combinecut([is_mu, SC  ]))
addcut('MuCh_SR'  , combinecut([is_mu, SR  ]))
addcut('MuCh_CR'  , combinecut([is_mu, CR  ]))
addcut('MuCh_SB'  , combinecut([is_mu, SB  ]))
addcut('MuCh_TCR' , combinecut([is_mu, TCR ]))
#addcut('MuCh_DYCR', combinecut([is_mu, DYCR]))
addcut('MuCh_QER' , combinecut([is_mu, QER ]))

# Mjj fit channel
addcut('Mjj_CR'  , combinecut([CR]))


