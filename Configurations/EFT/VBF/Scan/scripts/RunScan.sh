
# input : hm, hp, hl

combineCards.py \
hww2l2v_13TeV_SRVBF=../Full2016/datacards/hww2l2v_13TeV_SRVBF/kd_vbf_$1/datacard.txt \
hww2l2v_13TeV_SRVH=../Full2016/datacards/hww2l2v_13TeV_SRVH/kd_vh_$1/datacard.txt \
#hww2l2v_13TeV_SRBVH=../Full2016/datacards/hww2l2v_13TeV_SRBVH/kd_Vh_$1/datacard.txt \
> cards/$1.txt

text2workspace.py cards/$1.txt -o cards/$1.root -P HiggsAnalysis.CombinedLimit.HWWCouplings:HWWCouplings --PO Float_$1 > scale.txt

combine -d cards/$1.root -n $1 -M MultiDimFit -v 7 -s 1 -t -1 -m 125 --algo grid --points 1000 --setParameters muV=1,muF=1,Fai=0.0 --redefineSignalPOIs=Fai --X-rtd OPTIMIZE_BOUNDS=0 --X-rtd TMCSO_AdaptivePseudoAsimov=0 --alignEdges=1

# --setParameterRanges Fai=-0.02,0.02 

rm combine_logger.out
mv higgsCombine$1.MultiDimFit.mH125*.root hists/higgsCombine$1.MultiDimFit.mH125.root

#combine -d cards/$1.root -n $1_fmu -M MultiDimFit -m 125 --algo grid --points 1000 --setParameters muV=1,Fai=0 --redefineSignalPOIs=Fai --freezeParameters muV -t -1 --X-rtd OPTIMIZE_BOUNDS=0 --X-rtd TMCSO_AdaptivePseudoAsimov=0 --alignEdges=1

#rm combine_logger.out
#mv higgsCombine$1_fmu.MultiDimFit.mH125.root hists/

echo " "
echo 'root -l hists/higgsCombine'$1'.MultiDimFit.mH125.root'
echo 'limit->Draw("2*deltaNLL:Fai")'


