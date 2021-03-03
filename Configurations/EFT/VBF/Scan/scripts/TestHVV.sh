
# input 1 : H0M, H0PH, H0L1

#### IMPACTS #####

combineTool.py -M Impacts -d cards/$1_HVV.root -n $1_HVV -m 125 --doInitialFit -t -1 --setParameters muV=1.0,Fai=0.35 --redefineSignalPOIs=Fai --freezeParameters=muV --X-rtd MINIMIZER_analytic 
combineTool.py -M Impacts -d cards/$1_HVV.root -n $1_HVV -m 125 --doFits -t -1 --setParameters muV=1.0,Fai=0.35 --redefineSignalPOIs=Fai --freezeParameters=muV --X-rtd MINIMIZER_analytic 
combineTool.py -M Impacts -d cards/$1_HVV.root -n $1_HVV -m 125 -o aimpacts_$1.json -t -1 --setParameters muV=1.0,Fai=0.35 --redefineSignalPOIs=Fai --freezeParameters=muV 
plotImpacts.py -i aimpacts_$1.json -o aimpacts_$1

rm combine_logger.out
mv higgsCombine_*Fit*_$1_*.MultiDimFit.mH125*.root hists/
mv aimpacts_$1.* plots/

### FIT DIAGNOSTICS #####

#combine --saveNormalizations --saveShapes --saveWithUncertainties -n $1 -M FitDiagnostics cards/$1_HVV.root -t -1 --setParameters muV=1.0,Fai=0.35 --redefineSignalPOIs=Fai --freezeParameters=muV --X-rtd MINIMIZER_analytic 
#python scripts/diffNuisances.py fitDiagnostics$1.root --poi Fai --all -g outputfile_$1.root 

#mv fitDiagnostics$1.root hists/fitDiagnostics$1.root
#mv outputfile_$1.root hists/outputfile_$1.root

### OPTIONS ###

# --plots --signalPdfNames='ggH*,vbfH*' and --backgroundPdfNames='*DY*,*WW*,*Top*'
# -t -1 --expectSignal=1 (use setparameters if POIs in not just Mu) gives prefit asimov dataset 
# --toysFreq gives post fit asimov dataset

# --robustFit 
# --X-rtd MINIMIZER_analytic 
# --X-rtd FITTER_NEW_CROSSING_ALGO
# --X-rtd FITTER_NEVER_GIVE_UP
# --X-rtd FITTER_BOUND
