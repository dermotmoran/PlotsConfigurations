

import sys
import ROOT 
import numpy as np
import shutil
import math
from os import path
from array import array

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)


def plot(AC,FAC):

 src = path.realpath("hists/higgsCombine"+AC+".MultiDimFit.mH125.root")
 F = ROOT.TFile.Open(''+src+'', 'read')
 T = F.Get("limit")

 x, y = array('d'), array('d')

 for evt in T : 
  Fai = evt.Fai
  dNLL = evt.deltaNLL
  x.append(Fai)
  y.append(2*dNLL)

 n = len(x)

 gr = ROOT.TGraph(n, x, y)
 gr.SetMarkerColor(1)
 gr.SetMarkerStyle(7)
# gr.SetMaximum(1.5)
 gr.GetXaxis().SetTitle(''+FAC+'')
 gr.GetYaxis().SetTitle('-2 #Delta ln L') 

 canvas = ROOT.TCanvas('canvas', '', 500, 500)
 gr.Draw("AP")
 canvas.SaveAs("plots/"+AC+".pdf")
 canvas.SaveAs("plots/"+AC+".png")

###########################################

plot("H0M","F_{a3}cos(#phi_{a3})")
plot("H0PH","F_{a2}cos(#phi_{a2})")
plot("H0L1","F_{#Lambda 1}cos(#phi_{#Lambda 1})")

#plot("hm_fmu","F_{a3}cos(#phi_{a3})") 
#plot("hp_fmu","F_{a2}cos(#phi_{a2})") 
#plot("hl_fmu","F_{#Lambda 1}cos(#phi_{#Lambda 1})") 
