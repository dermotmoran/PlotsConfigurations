#!/bin/python

import os

if os.path.exists('HTXS_stage1_categories.py') :
  handle = open('HTXS_stage1_categories.py','r')
  exec(handle)
  handle.close()

sampleNames = []
for cat in HTXSStage1_1Categories:
  if 'GG2H_' in cat:
    sampleNames.append(cat.replace('GG2H','ggH_hww'))
    sampleNames.append(cat.replace('GG2H','ggH_htt'))
  elif 'QQ2HQQ_' in cat:
    sampleNames.append(cat.replace('QQ2HQQ','qqH_hww'))
    sampleNames.append(cat.replace('QQ2HQQ','qqH_htt'))
    sampleNames.append(cat.replace('QQ2HQQ','WH_had_hww'))
    sampleNames.append(cat.replace('QQ2HQQ','WH_had_htt'))
    sampleNames.append(cat.replace('QQ2HQQ','ZH_had_hww'))
    sampleNames.append(cat.replace('QQ2HQQ','ZH_had_htt'))
  elif 'QQ2HLNU_' in cat:
    sampleNames.append(cat.replace('QQ2HLNU','WH_lep_hww'))
    sampleNames.append(cat.replace('QQ2HLNU','WH_lep_htt'))
  elif 'QQ2HLL_' in cat:
    sampleNames.append(cat.replace('QQ2HLL','ZH_lep_hww'))
    sampleNames.append(cat.replace('QQ2HLL','ZH_lep_htt'))
  elif 'GG2HLL_' in cat:
    sampleNames.append(cat.replace('GG2HLL','ggZH_lep_hww'))
  elif 'TTH' in cat:
    sampleNames.append(cat.replace('TTH','ttH_hww'))
  elif 'BBH' in cat:
    sampleNames.append(cat.replace('BBH','bbH_hww'))

#os.chdir('Combination')

sampleNames.append('ggH_hww_PTH_200_300')
sampleNames.append('ggH_hww_PTH_300_450')
sampleNames.append('ggH_hww_PTH_450_650')
sampleNames.append('ggH_hww_PTH_GT650')

# Print all samples                                                                                                                                                                                        
print("All samples:")
for s in sampleNames:
  print(s)
print("============")

# Create output directory
os.system("mkdir -p Combination")

#No merging
command="text2workspace.py datacards/Full2018_SF_qqH_HTXS_Stage1p2/comb/datacard.txt -o Combination/Full2018_SF_qqH_HTXS_Stage1p2.root -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO verbose "
for sample in sampleNames:
  if 'FWDH'    in sample: continue
  if '0J'      in sample or '1J' in sample: continue
  # qqH --> 2 jets, mjj > 350
  if 'qqH_hww' in sample:
    # case pth < 200

    # case 350 < mjj < 700
    if 'MJJ_350_700' in sample:
      poi = 'qqH_hww_MJJ_350_700'
      command+="--PO 'map=.*/{}:r_{}[1,-10,10]' ".format(sample,poi)
      print("{0} - {1}".format(sample,poi))

    # case mjj > 700
    elif 'MJJ_GT700' in sample:
      poi = 'qqH_hww_MJJ_GT700'
      command+="--PO 'map=.*/{}:r_{}[1,-10,10]' ".format(sample,poi)
      print("{0} - {1}".format(sample,poi))

    # case pth > 200
    elif 'PTH_GT200' in sample:
      poi = 'qqH_hww_PTH_GT200'
      command+="--PO 'map=.*/{}:r_{}[1,-10,10]' ".format(sample,poi)
      print("{0} - {1}".format(sample,poi))
    else: continue

  # VH --> 2 jets, 60 < mjj < 120
  elif 'WH_had_hww' in sample or 'ZH_had_hww' in sample:
    if 'MJJ_60_120' in sample:
      poi = 'VH_had_hww_MJJ_60_120'
      command+="--PO 'map=.*/{}:r_{}[1,-10,10]' ".format(sample,poi)
      print("{0} - {1}".format(sample,poi))
    else: continue
  else: continue
print("============")

print command
os.system(command)