# cuts

supercut = ' mll > 12 \
             && std_vector_lepton_pt[0]>20 && std_vector_lepton_pt[1]>10 && std_vector_lepton_pt[2]<10 \
             && (abs(std_vector_lepton_flavour[1]) == 13 || (std_vector_lepton_pt[0]>25 && std_vector_lepton_pt[1]>13) )  \
             && metTtrk > 20 \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
               '               

cuts['0j_ee_in'] = 'std_vector_jet_pt[0] < 30 \
             && fabs(91.1876 - mll) < 7.5  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
             && dymvaggh > 0.6 \
               '

cuts['1j_ee_in'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] < 30 ) \
             && fabs(91.1876 - mll) < 7.5  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
             && dymvaggh > 0.6 \
               '

cuts['2j_ggH_ee_in'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] >= 30 ) \
             && fabs(91.1876 - mll) < 7.5  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
             && dymvaggh > 0.6 \
             && (abs(detajj) < 3.5) \
               '

cuts['2j_VBF_ee_in'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] >= 30 ) \
             && fabs(91.1876 - mll) < 7.5  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
             && dymvavbf > 0.6 \
             && (mjj >= 400 && abs(detajj) >= 3.5) \
               '

cuts['0j_uu_in'] = 'std_vector_jet_pt[0] < 30 \
             && fabs(91.1876 - mll) < 7.5  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
             && dymvaggh > 0.6 \
               '
               
cuts['1j_uu_in'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] < 30 ) \
             && fabs(91.1876 - mll) < 7.5  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
             && dymvaggh > 0.6 \
               '

cuts['2j_ggH_uu_in'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] >= 30 ) \
             && fabs(91.1876 - mll) < 7.5  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
             && dymvaggh > 0.6 \
             && (abs(detajj) < 3.5) \
               '

cuts['2j_VBF_uu_in'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] >= 30 ) \
             && fabs(91.1876 - mll) < 7.5  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
             && dymvavbf > 0.6 \
             && (mjj >= 400 && abs(detajj) >= 3.5) \
               '

cuts['0j_df_in'] = 'std_vector_jet_pt[0] < 30 \
             && fabs(91.1876 - mll) < 7.5  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)   \
             && dymvaggh > 0.6 \
               '

cuts['1j_df_in'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] < 30 ) \
             && fabs(91.1876 - mll) < 7.5  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)   \
             && dymvaggh > 0.6 \
               '

cuts['2j_ggH_df_in'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] >= 30 ) \
             && fabs(91.1876 - mll) < 7.5  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)   \
             && dymvaggh > 0.6 \
             && (abs(detajj) < 3.5) \
               '

cuts['2j_VBF_df_in'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] >= 30 ) \
             && fabs(91.1876 - mll) < 7.5  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)   \
             && dymvavbf > 0.6 \
             && (mjj >= 400 && abs(detajj) >= 3.5) \
               '

cuts['0j_ee_out'] = 'std_vector_jet_pt[0] < 30 \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
             && dymvaggh > 0.6 \
               '

cuts['1j_ee_out'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] < 30 ) \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
             && dymvaggh > 0.6 \
               '

cuts['2j_ggH_ee_out'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] >= 30 ) \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
             && dymvaggh > 0.6 \
             && (abs(detajj) < 3.5) \
               '

cuts['2j_VBF_ee_out'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] >= 30 ) \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
             && dymvavbf > 0.6 \
             && (mjj >= 400 && abs(detajj) >= 3.5) \
               '

cuts['0j_uu_out'] = 'std_vector_jet_pt[0] < 30 \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
             && dymvaggh > 0.6 \
               '

cuts['1j_uu_out'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] < 30 ) \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
             && dymvaggh > 0.6 \
               '

cuts['2j_ggH_uu_out'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] >= 30 ) \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
             && dymvaggh > 0.6 \
             && (abs(detajj) < 3.5) \
               '

cuts['2j_VBF_uu_out'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] >= 30 ) \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
             && dymvavbf > 0.6 \
             && (mjj >= 400 && abs(detajj) >= 3.5) \
               '

cuts['0j_df_out'] = 'std_vector_jet_pt[0] < 30 \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)   \
             && dymvaggh > 0.6 \
               '

cuts['1j_df_out'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] < 30 ) \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)   \
             && dymvaggh > 0.6 \
               '

cuts['2j_ggH_df_out'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] >= 30 ) \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)   \
             && dymvaggh > 0.6 \
             && (abs(detajj) < 3.5) \
               '

cuts['2j_VBF_df_out'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] >= 30 ) \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)   \
             && dymvavbf > 0.6 \
             && (mjj >= 400 && abs(detajj) >= 3.5) \
               '
