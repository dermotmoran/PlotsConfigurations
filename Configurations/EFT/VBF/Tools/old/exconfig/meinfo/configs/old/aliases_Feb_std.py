
import os
import copy
import inspect
import ROOT

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2016
configurations = os.path.dirname(configurations) # VBF
configurations = os.path.dirname(configurations) # EFT
configurations = os.path.dirname(configurations) # Configurations

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

eleWP = 'mva_90p_Iso2016'
muWP = 'cut_Tight80x'

aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}

aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

# Fake leptons transfer factor
aliases['fakeW'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
    'samples': ['Fake']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
    'samples': ['Fake']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
    'samples': ['Fake']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
    'samples': ['Fake']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
    'samples': ['Fake']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
    'samples': ['Fake']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
    'samples': ['Fake']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
    'samples': ['Fake']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
    'samples': ['Fake']
}

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)',
    'samples': mc
}

aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['TTbar']
}

aliases['ptllDYW_NLO'] = {
    'expr': '(0.87*(gen_ptll<10)+(0.379119+0.099744*gen_ptll-0.00487351*gen_ptll**2+9.19509e-05*gen_ptll**3-6.0212e-07*gen_ptll**4)*(gen_ptll>=10 && gen_ptll<45)+(9.12137e-01+1.11957e-04*gen_ptll-3.15325e-06*gen_ptll**2-4.29708e-09*gen_ptll**3+3.35791e-11*gen_ptll**4)*(gen_ptll>=45 && gen_ptll<200) + 1*(gen_ptll>200))',
    'samples': ['DY']
}

# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples

# No jet with pt > 30 GeV
aliases['zeroJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) < 30.'
}

aliases['oneJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) > 30.'
}

aliases['multiJet'] = {
    'expr': 'Alt$(CleanJet_pt[1], 0) > 30.'
}

# Lepton centrality

aliases['lepcen1'] = {
    'expr': 'abs((Lepton_eta[0] - (CleanJet_eta[0]+CleanJet_eta[1])/2)/detajj)'
}

aliases['lepcen2'] = {
    'expr': 'abs((Lepton_eta[1] - (CleanJet_eta[0]+CleanJet_eta[1])/2)/detajj)'
}

################################################# EFT with MELA #############################################
# Couplings (gXHWW^2 = JHUXSHWWa1/JHUXSHWWaX) and cross-sections (JHUXSHWWaX) 
# https://github.com/hroskes/anomalouscouplingsconstants/blob/04fc990ad2452c79506de79474fe2c83243bb39f/constants.py#L75-L93
# https://twiki.cern.ch/twiki/bin/view/CMS/Run2MCProductionforHiggsProperties#POWHEG_ggH_Production_JHUGen_H_W

# Couplings used in JHUGen 

aliases['g2VBF']  = {'expr': '0.27196538'}
aliases['g4VBF']  = {'expr': '0.29797901870'}
aliases['g2ZH']   = {'expr': '0.112481'}
aliases['g4ZH']   = {'expr': '0.144057'}
aliases['g2WH']   = {'expr': '0.0998956'}
aliases['g4WH']   = {'expr': '0.1236136'}

# Cross-sections : Decay

aliases['JHUXSHWWa1']   = {'expr': '312.04019'}
aliases['JHUXSHWWa2']   = {'expr': '242.6283'}
aliases['JHUXSHWWa3']   = {'expr': '100.79135'} 
aliases['JHUXSHWWL1']   = {'expr': '1.6475531e-06'}
aliases['JHUXSHWWa1a2'] = {'expr': '1149.9181'}
aliases['JHUXSHWWa1a3'] = {'expr': '624.7195'}
aliases['JHUXSHWWa1L1'] = {'expr': '5.3585509'}

# Cross-sections : Production

aliases['JHUXSVBFa1']   = {'expr': '968.88143'}
aliases['JHUXSVBFa2']   = {'expr': '13097.831'}
aliases['JHUXSVBFa3']   = {'expr': '10910.237'}
aliases['JHUXSVBFL1']   = {'expr': '0.00020829261'}
aliases['JHUXSVBFa1a2'] = {'expr': '2207.6738'}
aliases['JHUXSVBFa1a3'] = {'expr': '1936.4327'}
aliases['JHUXSVBFa1L1'] = {'expr': '2861.7003'}

aliases['JHUXSZHa1']   = {'expr': '1436880.4'}
aliases['JHUXSZHa2']   = {'expr': '1.1360424e+08'}
aliases['JHUXSZHa3']   = {'expr': '69241514'}
aliases['JHUXSZHL1']   = {'expr': '5.3610896'}
aliases['JHUXSZHa1a2'] = {'expr': '678434.94'}
aliases['JHUXSZHa1a3'] = {'expr': '2873685.9'}
aliases['JHUXSZHa1L1'] = {'expr': '1091656.8'}

aliases['JHUXSWHa1']   = {'expr': '14813072'}
aliases['JHUXSWHa2']   = {'expr': '1.4845783e+09'}
aliases['JHUXSWHa3']   = {'expr': '9.6943028e+08'}
aliases['JHUXSWHL1']   = {'expr': '53.687994'}
aliases['JHUXSWHa1a2'] = {'expr': '7879980.3'}
aliases['JHUXSWHa1a3'] = {'expr': '29626131'}
aliases['JHUXSWHa1L1'] = {'expr': '12092167'}

# Interference XS / g

aliases['JHUXSVBFa1a2_I'] = {'expr':'(JHUXSVBFa1a2 - JHUXSVBFa1 - (g2VBF**2)*JHUXSVBFa2)/g2VBF'}
aliases['JHUXSWHa1a2_I']  = {'expr':'(JHUXSWHa1a2  - JHUXSWHa1  - (g2WH**2)*JHUXSWHa2)/g2WH'}
aliases['JHUXSZHa1a2_I']  = {'expr':'(JHUXSZHa1a2  - JHUXSZHa1  - (g2ZH**2)*JHUXSZHa2)/g2ZH'}

aliases['JHUXSVBFa1a3_I'] = {'expr':'0'}
aliases['JHUXSWHa1a3_I']  = {'expr':'0'}
aliases['JHUXSZHa1a3_I']  = {'expr':'0'}

# Norm Weights

aliases['H0M_W']     = { 'expr': '(JHUXSHWWa3/JHUXSHWWa1)'}
aliases['H0PH_W']    = { 'expr': '(JHUXSHWWa2/JHUXSHWWa1)'}
aliases['H0L1_W']    = { 'expr': '(JHUXSHWWL1/JHUXSHWWa1)'}
aliases['H0Mf05_W']  = { 'expr': '(JHUXSHWWa1a3/JHUXSHWWa1)'}
aliases['H0PHf05_W'] = { 'expr': '(JHUXSHWWa1a2/JHUXSHWWa1)'}

aliases['VBFH0M_W']     = { 'expr': '(JHUXSVBFa3/JHUXSVBFa1)'}
aliases['VBFH0PH_W']    = { 'expr': '(JHUXSVBFa2/JHUXSVBFa1)'}
aliases['VBFH0L1_W']    = { 'expr': '(JHUXSVBFL1/JHUXSVBFa1)'}
aliases['VBFH0Mf05_W']  = { 'expr': '(JHUXSVBFa1 + JHUXSVBFa1a3_I*g4VBF + JHUXSVBFa3*(g4VBF**2))/JHUXSVBFa1'}
aliases['VBFH0PHf05_W'] = { 'expr': '(JHUXSVBFa1 + JHUXSVBFa1a2_I*g2VBF + JHUXSVBFa2*(g2VBF**2))/JHUXSVBFa1'}

aliases['WH0M_W']     = { 'expr': '(JHUXSWHa3/JHUXSWHa1)'}
aliases['WH0PH_W']    = { 'expr': '(JHUXSWHa2/JHUXSWHa1)'}
aliases['WH0L1_W']    = { 'expr': '(JHUXSWHL1/JHUXSWHa1)'}
aliases['WH0Mf05_W']  = { 'expr': '(JHUXSWHa1 + JHUXSWHa1a3_I*g4WH + JHUXSWHa3*(g4WH**2))/JHUXSWHa1'}
aliases['WH0PHf05_W'] = { 'expr': '(JHUXSWHa1 + JHUXSWHa1a2_I*g2WH + JHUXSWHa2*(g2WH**2))/JHUXSWHa1'}

aliases['ZH0M_W']     = { 'expr': '(JHUXSZHa3/JHUXSZHa1)'}
aliases['ZH0PH_W']    = { 'expr': '(JHUXSZHa2/JHUXSZHa1)'}
aliases['ZH0L1_W']    = { 'expr': '(JHUXSZHL1/JHUXSZHa1)'}
aliases['ZH0Mf05_W']  = { 'expr': '(JHUXSZHa1 + JHUXSZHa1a3_I*g4ZH + JHUXSZHa3*(g4ZH**2))/JHUXSZHa1'}
aliases['ZH0PHf05_W'] = { 'expr': '(JHUXSZHa1 + JHUXSZHa1a2_I*g2ZH + JHUXSZHa2*(g2ZH**2))/JHUXSZHa1'}

# Constants as a function of hm 

cons = [
    'CVBF','CWH','CZH',
    'G4VBF','G4WH','G4ZH',
    'G2VBF','G2WH','G2ZH',
    'L1VBF','L1WH','L1ZH',
]

for con in cons:
    aliases[con] = {
    'linesToAdd': ['.L %s/EFT/VBF/Full2016/meinfo/getconstant.cc+' % configurations ],
    'class': 'GetConstant',
    'args': (con,),
}

# VBF KDs

aliases['kd_smvbf']     = { 'expr': '1/(1+((me_qcd_hsm*CVBF)/me_vbf_hsm))' }
aliases['kd_hmvbf']     = { 'expr': '1/(1+((me_qcd_hsm*CVBF)/(me_vbf_hm*G4VBF**2)))' }
aliases['kd_hpvbf']     = { 'expr': '1/(1+((me_qcd_hsm*CVBF)/(me_vbf_hp*G2VBF**2)))' }
aliases['kd_hlvbf']     = { 'expr': '1/(1+((me_qcd_hsm*CVBF)/(me_vbf_hl*L1VBF**2)))' }
aliases['kd_vbf']       = { 'expr': 'max(max(kd_smvbf, kd_hmvbf), max(kd_hpvbf, kd_hlvbf))' }

aliases['kd_vbf_hm']    = { 'expr': '1/(1+(me_vbf_hsm/(me_vbf_hm*G4VBF**2)))' }
aliases['kd_vbf_hp']    = { 'expr': '1/(1+(me_vbf_hsm/(me_vbf_hp*G2VBF**2)))' }
aliases['kd_vbf_hl']    = { 'expr': '1/(1+(me_vbf_hsm/(me_vbf_hl*L1VBF**2)))' }
aliases['kd_vbf_mixhm'] = { 'expr': '(me_vbf_mixhm - me_vbf_hsm - me_vbf_hm)/(2*sqrt(me_vbf_hsm*me_vbf_hm))' }
aliases['kd_vbf_mixhp'] = { 'expr': '(me_vbf_mixhp - me_vbf_hsm - me_vbf_hp)/(2*sqrt(me_vbf_hsm*me_vbf_hp))' }

# VH KDs

aliases['kd_smwh'] = { 'expr': '1/(1+((me_qcd_hsm*CWH)/me_wh_hsm))' }
aliases['kd_smzh'] = { 'expr': '1/(1+((me_qcd_hsm*CZH)/(me_zh_hsm)))' }
aliases['kd_smvh'] = { 'expr': 'max(kd_smwh, kd_smzh)' }
aliases['kd_hmwh'] = { 'expr': '1/(1+((me_qcd_hsm*CWH)/(me_wh_hm*G4WH**2)))' }
aliases['kd_hmzh'] = { 'expr': '1/(1+((me_qcd_hsm*CZH)/(me_zh_hm*G4ZH**2)))' }
aliases['kd_hmvh'] = { 'expr': 'max(kd_hmwh, kd_hmzh)' }
aliases['kd_hpwh'] = { 'expr': '1/(1+((me_qcd_hsm*CWH)/(me_wh_hp*G2WH**2)))' }
aliases['kd_hpzh'] = { 'expr': '1/(1+((me_qcd_hsm*CZH)/(me_zh_hp*G2ZH**2)))' }
aliases['kd_hpvh'] = { 'expr': 'max(kd_hpwh, kd_hpzh)' }
aliases['kd_hlwh'] = { 'expr': '1/(1+((me_qcd_hsm*CWH)/(me_wh_hl*L1WH**2)))' }
aliases['kd_hlzh'] = { 'expr': '1/(1+((me_qcd_hsm*CZH)/(me_zh_hl*L1ZH**2)))' }
aliases['kd_hlvh'] = { 'expr': 'max(kd_hlwh, kd_hlzh)' }
aliases['kd_vh']   = { 'expr': 'max(max(kd_smvh, kd_hmvh), max(kd_hpvh, kd_hlvh))' }

aliases['kd_wh_hm']    = { 'expr': '1/(1+(me_wh_hsm/(me_wh_hm*G4WH**2)))' }
aliases['kd_zh_hm']    = { 'expr': '1/(1+(me_zh_hsm/(me_zh_hm*G4ZH**2)))' }
aliases['kd_vh_hm']    = { 'expr': 'max(kd_wh_hm, kd_zh_hm)' }

aliases['kd_wh_hp']    = { 'expr': '1/(1+(me_wh_hsm/(me_wh_hp*G2WH**2)))' }
aliases['kd_zh_hp']    = { 'expr': '1/(1+(me_zh_hsm/(me_zh_hp*G2ZH**2)))' }
aliases['kd_vh_hp']    = { 'expr': 'max(kd_wh_hp, kd_zh_hp)' }

aliases['kd_wh_hl']    = { 'expr': '1/(1+(me_wh_hsm/(me_wh_hl*L1WH**2)))' }
aliases['kd_zh_hl']    = { 'expr': '1/(1+(me_zh_hsm/(me_zh_hl*L1ZH**2)))' }
aliases['kd_vh_hl']    = { 'expr': 'max(kd_wh_hl, kd_zh_hl)' }

aliases['kd_wh_mixhm'] = { 'expr': '(me_wh_mixhm - me_wh_hsm - me_wh_hm)/(2*sqrt(me_wh_hsm*me_wh_hm))' }
aliases['kd_zh_mixhm'] = { 'expr': '(me_zh_mixhm - me_zh_hsm - me_zh_hm)/(2*sqrt(me_zh_hsm*me_zh_hm))' }
aliases['kd_vh_mixhm'] = { 'expr': 'max(kd_wh_mixhm, kd_zh_mixhm)' }

aliases['kd_wh_mixhp'] = { 'expr': '(me_wh_mixhp - me_wh_hsm - me_wh_hp)/(2*sqrt(me_wh_hsm*me_wh_hp))' }
aliases['kd_zh_mixhp'] = { 'expr': '(me_zh_mixhp - me_zh_hsm - me_zh_hp)/(2*sqrt(me_zh_hsm*me_zh_hp))' }
aliases['kd_vh_mixhp'] = { 'expr': 'max(kd_wh_mixhp, kd_zh_mixhp)' }

# Constants as a function of boosted hm (bhm)

bcons = [
    'CVBFb','CWHb','CZHb',
    'G4VBFb','G4WHb','G4ZHb',
    'G2VBFb','G2WHb','G2ZHb',
    'L1VBFb','L1WHb','L1ZHb',
]

for bcon in bcons:
    aliases[bcon] = {
    'linesToAdd': ['.L %s/EFT/VBF/Full2016/meinfo/getconstantb.cc+' % configurations ],
    'class': 'GetConstantb',
    'args': (bcon,),
}

# Boosted VH KDs

aliases['kd_smWh'] = { 'expr': '1/(1+((me_QCD_hsm*CWHb)/me_Wh_hsm))' }
aliases['kd_smZh'] = { 'expr': '1/(1+((me_QCD_hsm*CZHb)/(me_Zh_hsm)))' }
aliases['kd_smVh'] = { 'expr': 'max(kd_smWh, kd_smZh)' }
aliases['kd_hmWh'] = { 'expr': '1/(1+((me_QCD_hsm*CWHb)/(me_Wh_hm*G4WHb**2)))' }
aliases['kd_hmZh'] = { 'expr': '1/(1+((me_QCD_hsm*CZHb)/(me_Zh_hm*G4ZHb**2)))' }
aliases['kd_hmVh'] = { 'expr': 'max(kd_hmWh, kd_hmZh)' }
aliases['kd_hpWh'] = { 'expr': '1/(1+((me_QCD_hsm*CWHb)/(me_Wh_hp*G2WHb**2)))' }
aliases['kd_hpZh'] = { 'expr': '1/(1+((me_QCD_hsm*CZHb)/(me_Zh_hp*G2ZHb**2)))' }
aliases['kd_hpVh'] = { 'expr': 'max(kd_hpWh, kd_hpZh)' }
aliases['kd_hlWh'] = { 'expr': '1/(1+((me_QCD_hsm*CWHb)/(me_Wh_hl*L1WHb**2)))' }
aliases['kd_hlZh'] = { 'expr': '1/(1+((me_QCD_hsm*CZHb)/(me_Zh_hl*L1ZHb**2)))' }
aliases['kd_hlVh'] = { 'expr': 'max(kd_hlWh, kd_hlZh)' }
aliases['kd_Vh']   = { 'expr': 'max(max(kd_smVh, kd_hmVh), max(kd_hpVh, kd_hlVh))' }

aliases['kd_Wh_hm']    = { 'expr': '1/(1+(me_Wh_hsm/(me_Wh_hm*G4WHb**2)))' }
aliases['kd_Zh_hm']    = { 'expr': '1/(1+(me_Zh_hsm/(me_Zh_hm*G4ZHb**2)))' }
aliases['kd_Vh_hm']    = { 'expr': 'max(kd_Wh_hm, kd_Zh_hm)' }

aliases['kd_Wh_hp']    = { 'expr': '1/(1+(me_Wh_hsm/(me_Wh_hp*G2WHb**2)))' }
aliases['kd_Zh_hp']    = { 'expr': '1/(1+(me_Zh_hsm/(me_Zh_hp*G2ZHb**2)))' }
aliases['kd_Vh_hp']    = { 'expr': 'max(kd_Wh_hp, kd_Zh_hp)' }

aliases['kd_Wh_hl']    = { 'expr': '1/(1+(me_Wh_hsm/(me_Wh_hl*L1WHb**2)))' }
aliases['kd_Zh_hl']    = { 'expr': '1/(1+(me_Zh_hsm/(me_Zh_hl*L1ZHb**2)))' }
aliases['kd_Vh_hl']    = { 'expr': 'max(kd_Wh_hl, kd_Zh_hl)' }

aliases['kd_Wh_mixhm'] = { 'expr': '(me_Wh_mixhm - me_Wh_hsm - me_Wh_hm)/(2*sqrt(me_Wh_hsm*me_Wh_hm))' }
aliases['kd_Zh_mixhm'] = { 'expr': '(me_Zh_mixhm - me_Zh_hsm - me_Zh_hm)/(2*sqrt(me_Zh_hsm*me_Zh_hm))' }
aliases['kd_Vh_mixhm'] = { 'expr': 'max(kd_Wh_mixhm, kd_Zh_mixhm)' }

aliases['kd_Wh_mixhp'] = { 'expr': '(me_Wh_mixhp - me_Wh_hsm - me_Wh_hp)/(2*sqrt(me_Wh_hsm*me_Wh_hp))' }
aliases['kd_Zh_mixhp'] = { 'expr': '(me_Zh_mixhp - me_Zh_hsm - me_Zh_hp)/(2*sqrt(me_Zh_hsm*me_Zh_hp))' }
aliases['kd_Vh_mixhp'] = { 'expr': 'max(kd_Wh_mixhp, kd_Zh_mixhp)' }

################## Additional variables ##############################

#aliases['TwoJet'] = { 'expr': 'CleanJet_pt[0]>=30 && CleanJet_pt[1]>=30 \
#                    && abs(CleanJet_eta[0])<4.7 && abs(CleanJet_eta[1])<4.7 \
#                    && CleanJet_pt[2]<30'}

#aliases['VJet'] = { 'expr': 'CleanFatJet_pt[0]>=200  \
#                           && abs(CleanFatJet_eta[0])<2.4 \
#                           && (MV>70 && MV<110)'}


aliases['mV'] = { 'expr': 'FatJet_msoftdrop[CleanFatJet_jetIdx[0]]' }

aliases['j1_px'] = { 'expr': 'CleanJet_pt[0]*cos(CleanJet_phi[0])' }
aliases['j2_px'] = { 'expr': 'CleanJet_pt[1]*cos(CleanJet_phi[1])' }
aliases['j1_py'] = { 'expr': 'CleanJet_pt[0]*sin(CleanJet_phi[0])' }
aliases['j2_py'] = { 'expr': 'CleanJet_pt[1]*sin(CleanJet_phi[1])' }
aliases['ptjj'] = { 'expr': 'sqrt(pow(j1_px + j2_px,2) + pow(j1_py + j2_py,2))' }

###########################################################################

# B tagging

aliases['bVeto'] = {
    'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0'
}

aliases['bReq'] = {
    'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) >= 1'
}

# CR definitions

aliases['topcr'] = {
    'expr': 'mtw2>30 && mll>50 && ((zeroJet && !bVeto) || bReq)'
}

aliases['dycr'] = {
    'expr': 'mth>0 && bVeto'
  #  'expr': 'mth<60 && mll>40 && mll<80 && bVeto'
}

aliases['wwcr'] = {
    'expr': 'mth>60 && mtw2>30 && mll>100 && bVeto'
}

# SR definition

aliases['sr'] = {
    'expr': 'mth>60 && mtw2>30 && bVeto'
}

# B tag scale factors

btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepCSV_94XSF_V2_B_F.csv' % os.getenv('CMSSW_BASE')

aliases['Jet_btagSF_shapeFix'] = {
    'linesToAdd': [
        'gSystem->Load("libCondFormatsBTauObjects.so");',
        'gSystem->Load("libCondToolsBTau.so");',
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        '.L %s/patches/btagsfpatch.cc+' % configurations
    ],
    'class': 'BtagSF',
    'args': (btagSFSource,),
    'samples': mc
}

aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shapeFix[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
    'samples': mc
}

for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
    aliases['Jet_btagSF_shapeFix_up_%s' % shift] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'up_' + shift),
        'samples': mc
    }
    aliases['Jet_btagSF_shapeFix_down_%s' % shift] = {
        'class': 'BtagSF',
        'args': (btagSFSource, 'down_' + shift),
        'samples': mc
    }
    
    for targ in ['bVeto', 'bReq']:
        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_shapeFix', 'btagSF_shapeFix_up_%s' % shift)

        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_shapeFix', 'btagSF_shapeFix_down_%s' % shift)

    aliases['btagSF%sup' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
        'samples': mc
    }

# data/MC scale factors


aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut', 'btagSF', 'PrefireWeight']),
    'samples': mc
}

# variations
aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc
}

# GGHUncertaintyProducer wasn't run for 2017 nAODv5 non-private
thus = [
    'ggH_mu',
    'ggH_res',
    'ggH_mig01',
    'ggH_mig12',
    'ggH_VBF2j',
    'ggH_VBF3j',
    'ggH_pT60',
    'ggH_pT120',
    'ggH_qmtop'
]

for thu in thus:
    aliases[thu] = {
        'linesToAdd': ['.L %s/Differential/gghuncertainty.cc+' % configurations],
        'class': 'GGHUncertainty',
        'args': (thu,),
        'samples': ['ggH_hww','ggH_hww_ALT']
    }
    
