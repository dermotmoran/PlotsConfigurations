
#!/bin/bash

printf "HVV H0L1 \n"

combineCards.py \
hww2l2v_13TeV_of2j_vbf=../Full2016/datacards/hww2l2v_13TeV_of2j_vbf/HVV_H0L1_Proc/datacard.txt \
hww2l2v_13TeV_of2j_vh=../Full2016/datacards/hww2l2v_13TeV_of2j_vh/HVV_H0L1_Proc/datacard.txt \
hww2l2v_13TeV_top_of2j=../Full2016/datacards/hww2l2v_13TeV_top_of2j/HVV_H0L1/datacard.txt \
hww2l2v_13TeV_dytt_of2j=../Full2016/datacards/hww2l2v_13TeV_dytt_of2j/HVV_H0L1/datacard.txt \
> cards/HVV_H0L1.txt

text2workspace.py cards/HVV_H0L1.txt -o cards/HVV_H0L1.root -P HiggsAnalysis.CombinedLimit.HWWCouplings:HWWCouplings --PO H0L1 > cards/scale_HVV_H0L1.txt

printf "HVV H0LZg \n"

combineCards.py \
hww2l2v_13TeV_of2j_vbf=../Full2016/datacards/hww2l2v_13TeV_of2j_vbf/HVV_H0LZg_Proc/datacard.txt \
hww2l2v_13TeV_of2j_vh=../Full2016/datacards/hww2l2v_13TeV_of2j_vh/HVV_H0LZg_Proc/datacard.txt \
hww2l2v_13TeV_top_of2j=../Full2016/datacards/hww2l2v_13TeV_top_of2j/HVV_H0LZg/datacard.txt \
hww2l2v_13TeV_dytt_of2j=../Full2016/datacards/hww2l2v_13TeV_dytt_of2j/HVV_H0LZg/datacard.txt \
> cards/HVV_H0LZg.txt

text2workspace.py cards/HVV_H0LZg.txt -o cards/HVV_H0LZg.root -P HiggsAnalysis.CombinedLimit.HWWCouplings:HWWCouplings --PO H0LZg > cards/scale_HVV_H0LZg.txt


printf "HGG H0M \n"

combineCards.py \
hww2l2v_13TeV_of2j_ggh_thmip=../Full2016/datacards/hww2l2v_13TeV_of2j_ggh_thmip/HGG_H0M_Proc/datacard.txt \
hww2l2v_13TeV_of2j_ggh_thmin=../Full2016/datacards/hww2l2v_13TeV_of2j_ggh_thmin/HGG_H0M_Proc/datacard.txt \
hww2l2v_13TeV_of2j_ggh_lhmip=../Full2016/datacards/hww2l2v_13TeV_of2j_ggh_lhmip/HGG_H0M_Proc/datacard.txt \
hww2l2v_13TeV_of2j_ggh_lhmin=../Full2016/datacards/hww2l2v_13TeV_of2j_ggh_lhmin/HGG_H0M_Proc/datacard.txt \
hww2l2v_13TeV_top_of2j=../Full2016/datacards/hww2l2v_13TeV_top_of2j/HGG_H0M/datacard.txt \
hww2l2v_13TeV_dytt_of2j=../Full2016/datacards/hww2l2v_13TeV_dytt_of2j/HGG_H0M/datacard.txt \
> cards/HGG_H0M.txt

text2workspace.py cards/HGG_H0M.txt -o cards/HGG_H0M.root -P HiggsAnalysis.CombinedLimit.HWWCouplings:HWWCouplings --PO H0M > cards/scale_HGG_H0M.txt

printf "HVV H0M \n"

combineCards.py \
hww2l2v_13TeV_of2j_vbf_hmip=../Full2016/datacards/hww2l2v_13TeV_of2j_vbf_hmip/HVV_H0M_Proc/datacard.txt \
hww2l2v_13TeV_of2j_vbf_hmin=../Full2016/datacards/hww2l2v_13TeV_of2j_vbf_hmin/HVV_H0M_Proc/datacard.txt \
hww2l2v_13TeV_of2j_vh_hmip=../Full2016/datacards/hww2l2v_13TeV_of2j_vh_hmip/HVV_H0M_Proc/datacard.txt \
hww2l2v_13TeV_of2j_vh_hmin=../Full2016/datacards/hww2l2v_13TeV_of2j_vh_hmin/HVV_H0M_Proc/datacard.txt \
hww2l2v_13TeV_top_of2j=../Full2016/datacards/hww2l2v_13TeV_top_of2j/HVV_H0M/datacard.txt \
hww2l2v_13TeV_dytt_of2j=../Full2016/datacards/hww2l2v_13TeV_dytt_of2j/HVV_H0M/datacard.txt \
> cards/HVV_H0M.txt

text2workspace.py cards/HVV_H0M.txt -o cards/HVV_H0M.root -P HiggsAnalysis.CombinedLimit.HWWCouplings:HWWCouplings --PO H0M > cards/scale_HVV_H0M.txt

printf "HVV H0PH \n"

combineCards.py \
hww2l2v_13TeV_of2j_vbf_hpip=../Full2016/datacards/hww2l2v_13TeV_of2j_vbf_hpip/HVV_H0PH_Proc/datacard.txt \
hww2l2v_13TeV_of2j_vbf_hpin=../Full2016/datacards/hww2l2v_13TeV_of2j_vbf_hpin/HVV_H0PH_Proc/datacard.txt \
hww2l2v_13TeV_of2j_vh_hpip=../Full2016/datacards/hww2l2v_13TeV_of2j_vh_hpip/HVV_H0PH_Proc/datacard.txt \
hww2l2v_13TeV_of2j_vh_hpin=../Full2016/datacards/hww2l2v_13TeV_of2j_vh_hpin/HVV_H0PH_Proc/datacard.txt \
hww2l2v_13TeV_top_of2j=../Full2016/datacards/hww2l2v_13TeV_top_of2j/HVV_H0PH/datacard.txt \
hww2l2v_13TeV_dytt_of2j=../Full2016/datacards/hww2l2v_13TeV_dytt_of2j/HVV_H0PH/datacard.txt \
> cards/HVV_H0PH.txt

text2workspace.py cards/HVV_H0PH.txt -o cards/HVV_H0PH.root -P HiggsAnalysis.CombinedLimit.HWWCouplings:HWWCouplings --PO H0PH > cards/scale_HVV_H0PH.txt




