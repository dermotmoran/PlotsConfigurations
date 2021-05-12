

import sys
import ROOT 
import numpy as np
import shutil
import math
from os import path
from array import array

import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)

def plot(AC,FAC):

 src = path.realpath("hists/higgsCombine"+AC+"_cScan.MultiDimFit.mH125.root")
 F = ROOT.TFile.Open(''+src+'', 'read')
 T = F.Get("limit")

 x, y, z = array('d'), array('d'), array('d')
 for evt in T : 
  C1 = evt.C1
  C2 = evt.C2
  dNLL = evt.deltaNLL
  if (2*dNLL) < 5 :
   x.append(C1)
   y.append(C2)
   z.append(2*dNLL)

 n = len(x)
 gr = ROOT.TGraph2D(n, x, y, z)

 
 NRGBs = 5
 NCont = 256
 stops = [ 0.00, 0.30, 0.61, 0.84, 1.00 ]
 blue = [0.00, 0.00, 0.57, 0.90, 0.51]
 green = [0.00, 0.65, 0.95, 0.20, 0.00]
 red = [0.51, 0.55, 0.15, 0.00, 0.10]
 stopsArray = array("d", stops)
 redArray = array("d", red)
 greenArray = array("d", green)
 blueArray = array("d", blue)
 ROOT.TColor.CreateGradientColorTable(NRGBs, stopsArray, redArray, greenArray, blueArray, NCont)
 ROOT.gStyle.SetNumberContours(NCont)

 canvas = ROOT.TCanvas('canvas', '', 500, 500)
 gr.GetHistogram().GetXaxis().SetTitle('#delta c_{Z}')
 gr.GetHistogram().GetYaxis().SetTitle(''+FAC+'')
 size = gr.GetHistogram().GetXaxis().GetLabelSize()
 r = 0.7
 gr.GetHistogram().GetXaxis().SetLabelSize(size*r);
 gr.GetHistogram().GetYaxis().SetLabelSize(size*r);
 #gr.GetHistogram().GetXaxis().SetLabelOffset(size*r)
 gr.GetHistogram().GetYaxis().SetLabelOffset(size*r)

 gr.Draw("P")
 gr.Draw("colz")
 T.SetMarkerStyle(34)
 T.Draw("C2:C1","quantileExpected == -1","P same")
 canvas.SaveAs("plots/"+AC+"_c.pdf")
 canvas.SaveAs("plots/"+AC+"_c.png")
 canvas.SaveAs("plots/"+AC+"_c.root")


###########################################

plot("HVV_EFTH0M","#tilde{C}_{ZZ}")
plot("HVV_EFTH0PH","C_{ZZ}")
plot("HVV_EFTH0L1","C_{ZB}")
