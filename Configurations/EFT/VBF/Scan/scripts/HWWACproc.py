#!/usr/bin/env python

import CombineHarvester.CombineTools.ch as ch
import ROOT 
import sys

args = sys.argv[1:]
assert (len(args) >= 2)

BIN = args[0]
KD  = args[1]

print BIN, KD 

cmb = ch.CombineHarvester()
cmb.SetFlag('check-negative-bins-on-import', 0)

cmb.ParseDatacard("datacards/"+BIN+"/"+KD+"/datacard.txt")

# Rebin Mode 1 : Starts from bin with lowest content which fails the condition. Tries moving left and right merging bins until threshold is met.
# Chooses from left and right to minimise number of bins lost
# Repeats with new lowest bin until all bins pass threshold
# SetBinUncertFraction : The threshold on the bin uncertainty fraction for which we consider merging bins

rebin = ch.AutoRebin()
rebin.SetBinThreshold(0.0)
rebin.SetBinUncertFraction(0.25)
rebin.SetRebinMode(1)
rebin.SetPerformRebin(True) 
rebin.SetVerbosity(0)
rebin.Rebin(cmb, cmb)

writer = ch.CardWriter('datacards_proc/'+BIN+'/'+KD+'/datacard.txt',
                       'datacards_proc/'+BIN+'/'+KD+'/shapes/histos_'+BIN+'.root')

writer.WriteCards('', cmb) 
