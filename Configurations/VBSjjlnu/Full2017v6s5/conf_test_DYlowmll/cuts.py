# cuts

# Second lepton veto already done in post-processing 
#and Lepton WP setup in samples.py
supercut = '(   (abs(Lepton_pdgId[0])==11 && Lepton_pt[0]>38) \
             || (abs(Lepton_pdgId[0])==13 && Lepton_pt[0]>30 ) ) \
            && vbs_0_pt > 50 && vbs_1_pt > 30 \
            && PuppiMET_pt > 30 \
            && deltaeta_vbs >= 2.5  \
            && mjj_vbs >= 500 \
            && Mtw_lep < 185 \
            && (abs(vbs_0_eta)<2.65  || abs(vbs_0_eta)>3.139 || (Jet_puId[VBS_jets_maxmjj_massWZ[0]] & (1 << 0))==1) \
            && (abs(vbs_1_eta)<2.65  || abs(vbs_1_eta)>3.139 || (Jet_puId[VBS_jets_maxmjj_massWZ[1]] & (1 << 0))==1) \
            && (abs(vjet_0_eta)<2.65 || abs(vjet_0_eta)>3.139 || (Jet_puId[V_jets_maxmjj_massWZ[0]] & (1 << 0))==1) \
            && (abs(vjet_1_eta)<2.65 || abs(vjet_1_eta)>3.139 || (Jet_puId[V_jets_maxmjj_massWZ[1]] & (1 << 0))==1) \
            '


#########################################################################
###############|----------------------------------|######################
###############|          Resolved category       |######################
###############|----------------------------------|######################
#########################################################################

#####################################
##  W-onshell, bveto --> Signal

cuts["res_ele_cutsip"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && whad_pt < 200 \
                                && sip3d_cut \
                                '


cuts["res_ele"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && whad_pt < 200 \
                                '


cuts["res_mu"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && whad_pt < 200 \
                                '

# cuts["res_ele_lowMtw"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && (mjj_vjet <= 65 || mjj_vjet >= 105) \
#                                 && bVeto \
#                                 && whad_pt < 200 \
#                                 && Mtw_lep < 50 \
#                                 '


# cuts["res_mu_lowMtw"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && (mjj_vjet <= 65 || mjj_vjet >= 105) \
#                                 && bVeto \
#                                 && whad_pt < 200 \
#                                 && Mtw_lep < 50 \
#                                 '


# cuts["res_ele_highMtw"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && (mjj_vjet <= 65 || mjj_vjet >= 105) \
#                                 && bVeto \
#                                 && whad_pt < 200 \
#                                 && Mtw_lep >= 50 \
#                                 '


# cuts["res_mu_highMtw"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && (mjj_vjet <= 65 || mjj_vjet >= 105) \
#                                 && bVeto \
#                                 && whad_pt < 200 \
#                                 && Mtw_lep >= 50 \
#                                 '




# ##################################
# # Woff shell, bveto ---> WJet region

# cuts["res_wjetcr_dnnall_ele"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && (mjj_vjet <= 65 || mjj_vjet >= 105) \
#                                 && bVeto \
#                                 && whad_pt < 200 \
#                                 '


# cuts["res_wjetcr_dnnall_ele_cutsip"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && (mjj_vjet <= 65 || mjj_vjet >= 105) \
#                                 && bVeto \
#                                 && whad_pt < 200 \
#                                 && ( abs(Lepton_eta[0])<1.49 || Electron_sip3d[Lepton_electronIdx[0]] < sip3d_cut ) \
#                                 '


# cuts["res_wjetcr_dnnall_mu"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && (mjj_vjet <= 65 || mjj_vjet >= 105) \
#                                 && bVeto \
#                                 && whad_pt < 200 \
#                                 '



# ###############################################
# #Top


### Top Tight region

# cuts["res_topcr_dnnall_ele"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 && bReqTight \
#                                 && whad_pt < 200 \
#                                 '

# cuts["res_topcr_dnnall_ele_cutsip"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==11 \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 && bReqTight \
#                                 && whad_pt < 200 \
#                                 && ( abs(Lepton_eta[0])<1.49 || Electron_sip3d[Lepton_electronIdx[0]] < sip3d_cut ) \
#                                 '


# cuts["res_topcr_dnnall_mu"] = 'VBS_category==1 \
#                                 && abs(Lepton_pdgId[0])==13 \
#                                 && vjet_0_pt > 30 && vjet_1_pt > 30 \
#                                 && mjj_vjet > 65 && mjj_vjet < 105 \
#                                 && bReqTight \
#                                 && whad_pt < 200 \
#                                 '



