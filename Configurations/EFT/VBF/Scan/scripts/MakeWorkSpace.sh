#!/bin/bash

printf "H0M \n"

combineCards.py \
hww2l2v_13TeV_SRVBF1=../Full2016/datacards_proc/hww2l2v_13TeV_of2j_vbf_hmip/KD_H0M/datacard.txt \
hww2l2v_13TeV_SRVBF2=../Full2016/datacards_proc/hww2l2v_13TeV_of2j_vbf_hmin/KD_H0M/datacard.txt \
hww2l2v_13TeV_SRVH1=../Full2016/datacards_proc/hww2l2v_13TeV_of2j_vh_hmip/KD_H0M/datacard.txt \
hww2l2v_13TeV_SRVH2=../Full2016/datacards_proc/hww2l2v_13TeV_of2j_vh_hmin/KD_H0M/datacard.txt \
hww2l2v_13TeV_CRTop=../Full2016/datacards/hww2l2v_13TeV_top_of2j/KD_H0M/datacard.txt \
hww2l2v_13TeV_CRDY=../Full2016/datacards/hww2l2v_13TeV_dytt_of2j/KD_H0M/datacard.txt \
> cards/H0M_HVV.txt

text2workspace.py cards/H0M_HVV.txt -o cards/H0M_HVV.root -P HiggsAnalysis.CombinedLimit.HWWCouplings:HWWCouplings --PO H0M > cards/scale_H0M.txt

printf "H0PH \n"

combineCards.py \
hww2l2v_13TeV_SRVBF1=../Full2016/datacards_proc/hww2l2v_13TeV_of2j_vbf_hpip/KD_H0PH/datacard.txt \
hww2l2v_13TeV_SRVBF2=../Full2016/datacards_proc/hww2l2v_13TeV_of2j_vbf_hpin/KD_H0PH/datacard.txt \
hww2l2v_13TeV_SRVH1=../Full2016/datacards_proc/hww2l2v_13TeV_of2j_vh_hpip/KD_H0PH/datacard.txt \
hww2l2v_13TeV_SRVH2=../Full2016/datacards_proc/hww2l2v_13TeV_of2j_vh_hpin/KD_H0PH/datacard.txt \
hww2l2v_13TeV_CRTop=../Full2016/datacards/hww2l2v_13TeV_top_of2j/KD_H0PH/datacard.txt \
hww2l2v_13TeV_CRDY=../Full2016/datacards/hww2l2v_13TeV_dytt_of2j/KD_H0PH/datacard.txt \
> cards/H0PH_HVV.txt

text2workspace.py cards/H0PH_HVV.txt -o cards/H0PH_HVV.root -P HiggsAnalysis.CombinedLimit.HWWCouplings:HWWCouplings --PO H0PH > cards/scale_H0PH.txt


printf "H0L1 \n"

combineCards.py \
hww2l2v_13TeV_SRVBF=../Full2016/datacards_proc/hww2l2v_13TeV_of2j_vbf/KD_H0L1/datacard.txt \
hww2l2v_13TeV_SRVH=../Full2016/datacards_proc/hww2l2v_13TeV_of2j_vh/KD_H0L1/datacard.txt \
hww2l2v_13TeV_CRTop=../Full2016/datacards/hww2l2v_13TeV_top_of2j/KD_H0L1/datacard.txt \
hww2l2v_13TeV_CRDY=../Full2016/datacards/hww2l2v_13TeV_dytt_of2j/KD_H0L1/datacard.txt \
> cards/H0L1_HVV.txt

text2workspace.py cards/H0L1_HVV.txt -o cards/H0L1_HVV.root -P HiggsAnalysis.CombinedLimit.HWWCouplings:HWWCouplings --PO H0L1 > cards/scale_H0L1.txt
