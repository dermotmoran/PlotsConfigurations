#!/bin/bash
## text2workspace: --PO verbose


massmodel=${1}

what=${2}  ## sig or limit

cat=${3}  ## 0jet or 1jet or 01jet or 2jet or all

directory=${4}

workdir=/afs/cern.ch/user/l/lorusso/work/Higgs_highmass/Full_2016_V2/CMSSW_8_0_26_patch1/work/PlotsConfigurations/Configurations/EXO/WWlvlv_VBF/Full2016/${directory}
combinedir=/afs/cern.ch/user/l/lorusso/work/Higgs_highmass/Combine/CMSSW_7_4_7/src/

cd $combinedir
eval `scramv1 runtime -sh`
cd -

#if [ "${massmodel}" = "750_NWA" ]; then
# 
#        cp ${workdir}/ICHEP2016.*txt .
# 
#        if [ "${cat}" == "all" ]; then
#          text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel  --PO 'map=.*/ggH_hww*:1' --PO 'map=.*/qqH_hww*:1' --PO 'map=.*/ggH_hww_:0' --PO 'map=.*/qqH_hww_:0' --PO 'map=.*/ggH_hww_'${massmodel}':r[1,-10,10]' --PO 'map=.*/qqH_hww_'${massmodel}':r' ICHEP2016.txt -o ICHEP2016.workspace.mH750_NWA.root -m 750
# 
# 
#        else
#          text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel  --PO 'map=.*/ggH_hww*:1' --PO 'map=.*/qqH_hww*:1' --PO 'map=.*/ggH_hww_:0' --PO 'map=.*/qqH_hww_:0' --PO 'map=.*/ggH_hww_'${massmodel}':r[1,-10,10]' --PO 'map=.*/qqH_hww_'${massmodel}':r' ICHEP2016.${cat}.txt -o ICHEP2016.workspace.${cat}.mH750_NWA.root -m 750
#        fi
# 
#        cp ICHEP2016.workspace* ${workdir}
# 
#else

        cp ${workdir}/MORIOND2017.*txt .

        m=${massmodel%_*}
        echo $m

        if [ "${cat}" == "all" ]; then
         
text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel MORIOND2017.txt -o MORIOND2017.workspace.mH${massmodel}.root -m ${m} -v 1 &> log.workspace.mH${massmodel}.root

        else

          text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel MORIOND2017.${cat}.txt -o MORIOND2017.workspace.${cat}.mH${massmodel}.root -m ${m} -v 1 &> log.workspace.${cat}.mH${massmodel}.txt

        fi

        cp MORIOND2017.workspace* ${workdir}
        cp log.workspace* ${workdir}

#fi

if [ "${what}" == "sig" ]; then
	if [ "${cat}" == "all" ]; then
  	  combine -M ProfileLikelihood --significance -t -1 --expectSignal 1 MORIOND2017.workspace.mH${massmodel}.root       &> Significance.MORIOND2017.mH${massmodel}.txt
        else
          combine -M ProfileLikelihood --significance -t -1 --expectSignal 1 MORIOND2017.workspace.${cat}.mH${massmodel}.root       &> Significance.${cat}.MORIOND2017.mH${massmodel}.txt
        fi
        cp Significance* ${workdir}

else
        if [ "${cat}" == "all" ]; then
          combine -M Asymptotic -t -1 --expectSignal 1 --run expected MORIOND2017.workspace.mH${massmodel}.root      &> Limit.MORIOND2017.mH${massmodel}.txt
        else
          combine -M Asymptotic -t -1 --expectSignal 1 --run expected MORIOND2017.workspace.${cat}.mH${massmodel}.root      &> Limit.${cat}.MORIOND2017.mH${massmodel}.txt
        fi
        cp Limit* ${workdir}

fi



#text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel  --PO 'map=.*/ggH_hww*:1' --PO 'map=.*/qqH_hww*:1' --PO 'map=.*/ggH_hww_:0' --PO 'map=.*/qqH_hww_:0' --PO 'map=.*/ggH_hww_'${massmodel}':r[1,-10,10]' --PO 'map=.*/qqH_hww_'${massmodel}':r'  --PO 'map=.*/ggH_hww_750_NWA:0' --PO 'map=.*/qqH_hww_750_NWA:0' --PO 'map=.*/ggH_hww_INT'${massmodel}':sqrt_scaling=expr::sqrt_scaling("TMath::Sqrt(@0)",r)' --PO 'map=.*Top*/ggH_hww_INT'${massmodel}':0' --PO 'map=.*DYtt*/ggH_hww_INT'${massmodel}':0' --PO 'map=of0jDYtt/qqH_hww_300_c10brn00:0' --PO 'map=of1jDYtt/Fake:0' MORIOND2017.txt -o MORIOND2017.workspace.mH${massmodel}.root -m ${m} -v 1 &> log.workspace.mH${massmodel}.root
# 
#        else

#         text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel  --PO 'map=.*/ggH_hww*:1' --PO 'map=.*/qqH_hww*:1' --PO 'map=.*/ggH_hww_:0' --PO 'map=.*/qqH_hww_:0' --PO 'map=.*/ggH_hww_'${massmodel}':r[1,-10,10]' --PO 'map=.*/qqH_hww_'${massmodel}':r' --PO 'map=.*/ggH_hww_750_NWA:0' --PO 'map=.*/qqH_hww_750_NWA:0' --PO 'map=.*/ggH_hww_INT'${massmodel}':sqrt_scaling=expr::sqrt_scaling("TMath::Sqrt(@0)",r)' --PO 'map=.*Top*/ggH_hww_INT'${massmodel}':0' --PO 'map=.*DYtt*/ggH_hww_INT'${massmodel}':0' --PO 'map=of0jDYtt/qqH_hww_300_c10brn00:0' --PO 'map=of1jDYtt/Fake:0' MORIOND2017.${cat}.txt -o MORIOND2017.workspace.${cat}.mH${massmodel}.root -m ${m} -v 1 &> log.workspace.${cat}.mH${massmodel}.root