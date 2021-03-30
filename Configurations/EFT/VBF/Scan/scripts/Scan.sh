
# input 1 : HVV, HGG
# input 2 : H0M, H0PH, H0L1

combine -d cards/$1_$2.root -n $1_$2Scan -M MultiDimFit -t -1 -m 125 --algo grid --points 200 --setParameters muV=1.0,Fai=0.0 --redefineSignalPOIs=Fai

rm combine_logger.out
mv higgsCombine$1_$2Scan.MultiDimFit.mH125*.root hists/

# --freezeParameters CMS_scale_e_2016,CMS_scale_m_2016,CMS_eff_m_2016,CMS_eff_e_2016,CMS_scale_JESHF_2016,CMS_scale_JESBBEC1,CMS_scale_JESRelativeSample_2016,CMS_scale_JESEC2,CMS_scale_JESFlavorQCD,CMS_scale_JESBBEC1_2016,CMS_scale_JESAbsolute,CMS_scale_JESHF,CMS_scale_JESEC2_2016,CMS_scale_JESAbsolute_2016,CMS_scale_JESRelativeBal,CMS_btag_jes,CMS_btag_lf,CMS_btag_lfstats1_2016,CMS_btag_lfstats2_2016,CMS_btag_hfstats1_2016,CMS_btag_hfstats2_2016,CMS_btag_cferr1,CMS_btag_cferr2,CMS_PUID_2016,CMS_scale_met_2016,CMS_eff_prefiring_2016,CMS_eff_hwwtrigger_2016,PS_ISR,PS_FSR,CMS_PU_2016,QCDscale_top_2j,QCDscale_V,QCDscale_VV,QCDscale_ggVV,QCDscale_qqH,QCDscale_VH,QCDscale_ggZH,QCDscale_ttH,QCDscale_WWewk,QCDscale_qqbar_ACCEPT,QCDscale_gg_ACCEPT,pdf_Higgs_gg,pdf_Higgs_ttH,pdf_Higgs_qqbar,pdf_qqbar,pdf_Higgs_gg_ACCEPT,pdf_gg_ACCEPT,pdf_Higgs_qqbar_ACCEPT,pdf_qqbar_ACCEPT,lumi_13TeV_2016,lumi_13TeV_XYFact,lumi_13TeV_BBDefl,lumi_13TeV_DynBeta,lumi_13TeV_Ghosts,CMS_fake_syst_em,CMS_fake_syst_me,CMS_fake_e_2016,CMS_fake_stat_e_2016,CMS_fake_m_2016,CMS_fake_stat_m_2016,UE_CUET,singleTopToTTbar,CMS_hww_VgStarScale,CMS_hww_VZScale,CMS_hww_WWresum_2j,CMS_hww_WWqscale_2j,CMS_hww_CRSR_accept_DY,CMS_hww_CRSR_accept_top 

# SIG SHAPES : --freezeParameters CMS_scale_e_2016,CMS_scale_m_2016,CMS_eff_m_2016,CMS_eff_e_2016,CMS_scale_JESHF_2016,CMS_scale_JESBBEC1,CMS_scale_JESRelativeSample_2016,CMS_scale_JESEC2,CMS_scale_JESFlavorQCD,CMS_scale_JESBBEC1_2016,CMS_scale_JESAbsolute,CMS_scale_JESHF,CMS_scale_JESEC2_2016,CMS_scale_JESAbsolute_2016,CMS_scale_JESRelativeBal,CMS_btag_jes,CMS_btag_lf,CMS_btag_lfstats1_2016,CMS_btag_lfstats2_2016,CMS_btag_hfstats1_2016,CMS_btag_hfstats2_2016,CMS_btag_cferr1,CMS_btag_cferr2,CMS_PUID_2016,CMS_scale_met_2016,CMS_eff_prefiring_2016,CMS_eff_hwwtrigger_2016,PS_ISR,PS_FSR,CMS_PU_2016 
# LUMI : lumi_13TeV_2016,lumi_13TeV_XYFact,lumi_13TeV_BBDefl,lumi_13TeV_DynBeta,lumi_13TeV_Ghosts
# FAKE : CMS_fake_syst_em,CMS_fake_syst_me,CMS_fake_e_2016,CMS_fake_stat_e_2016,CMS_fake_m_2016,CMS_fake_stat_m_2016
# QCD/PDF NORM : QCDscale_top_2j,QCDscale_V,QCDscale_VV,QCDscale_ggVV,QCDscale_qqH,QCDscale_VH,QCDscale_ggZH,QCDscale_ttH,QCDscale_WWewk,QCDscale_qqbar_ACCEPT,QCDscale_gg_ACCEPT,pdf_Higgs_gg,pdf_Higgs_ttH,pdf_Higgs_qqbar,pdf_qqbar,pdf_Higgs_gg_ACCEPT,pdf_gg_ACCEPT,pdf_Higgs_qqbar_ACCEPT,pdf_qqbar_ACCEPT

# ALL SYS (NOT FLOATING NORM)--freezeParameters allConstrainedNuisances

# Verbosity : -v 7 
# Seed? : -s 1
# --X-rtd MINIMIZER_analytic
# --X-rtd OPTIMIZE_BOUNDS=0 --X-rtd TMCSO_AdaptivePseudoAsimov=0 --alignEdges=1
# --setParameterRanges Fai=-0.02,0.02 
# --freezeParameters muV 
# --robustFit=1

# --redefineSignalPOIs=Fai,muV
# root -l hists/higgsCombine'$1'.MultiDimFit.mH125.root
# limit->Draw("2*deltaNLL:Fai")
# limit->Draw("2*deltaNLL:Fai:muV>>h(40,0,10,40,-1,1)","","prof colz")


