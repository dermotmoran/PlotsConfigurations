
# input 1 : HVV
# input 2 : EFTH0M, EFTH0PH, EFTH0L1

combine -d cards/$1_$2_c.root -n $1_$2_cScan -M MultiDimFit -t -1 -m 125 --algo grid --points 2000 

rm combine_logger.out
mv higgsCombine$1_$2_cScan.MultiDimFit.mH125*.root hists/

# root -l hists/higgsCombine'$1'_'$2'_cScan.MultiDimFit.mH125.root
# limit->Draw("2*deltaNLL:C2:C1>>h(30,-0.5,0.5,30,-1,1)","2*deltaNLL<10","prof colz")
# limit->SetMarkerStyle(34);
# limit->Draw("C2:C1","quantileExpected == -1","P same")
