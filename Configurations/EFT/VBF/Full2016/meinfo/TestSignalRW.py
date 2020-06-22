
import sys
import ROOT 
import numpy as np
import shutil
import math
from os import path

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)

src = path.realpath("rootFileVBF/plots_VBF.root")

CheckWgt = True

#########################################################

def CompareRW(Cat, Var, Prod, AC):

 print " " 
 print Cat, Var, Prod, AC
 print " " 

 f = ROOT.TFile.Open(''+src+'', 'read')

 H1 = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+Prod+'_H0PM_'+AC+'') 
 H2 = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+Prod+'_H0M_'+AC+'') 
 H3 = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+Prod+'_H0PH_'+AC+'')
 H4 = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+Prod+'_H0L1_'+AC+'')

 H1.SetDirectory(0)
 H2.SetDirectory(0)
 H3.SetDirectory(0)
 H4.SetDirectory(0)

 H1.SetLineColor(ROOT.kRed)
 H2.SetLineColor(ROOT.kGreen)
 H3.SetLineColor(ROOT.kOrange)
 H4.SetLineColor(ROOT.kBlue)
 H1.SetLineWidth(3)
 H2.SetLineWidth(3)
 H3.SetLineWidth(3)
 H4.SetLineWidth(3)

 if CheckWgt :

  W1 = f.Get('hww2l2v_13TeV_'+Cat+'/wgt'+Prod+'_H0PM_'+AC+'/histo_'+Prod+'_H0PM') # samples without reweighting  
  W2 = f.Get('hww2l2v_13TeV_'+Cat+'/wgt'+Prod+'_H0M_'+AC+'/histo_'+Prod+'_H0M')
  W3 = f.Get('hww2l2v_13TeV_'+Cat+'/wgt'+Prod+'_H0PH_'+AC+'/histo_'+Prod+'_H0PH')
  W4 = f.Get('hww2l2v_13TeV_'+Cat+'/wgt'+Prod+'_H0L1_'+AC+'/histo_'+Prod+'_H0L1')
 
  tot = W2.Integral()
  sum = 0
  for i in range(1, W2.GetXaxis().GetNbins()):
   sum += W2.GetBinContent(i)
   if sum/tot > 0.995 :
    print i, 1 - sum/tot, W2.GetXaxis().GetBinLowEdge(i) , W2.GetXaxis().GetBinCenter(i) 
    break

  print "Entries :", W2.GetEntries()
 
  W1.SetDirectory(0)
  W2.SetDirectory(0)
  W3.SetDirectory(0)
  W4.SetDirectory(0)

  W1.SetLineColor(ROOT.kRed)
  W2.SetLineColor(ROOT.kGreen)
  W3.SetLineColor(ROOT.kOrange)
  W4.SetLineColor(ROOT.kBlue)
  W1.SetLineWidth(3)
  W2.SetLineWidth(3)
  W3.SetLineWidth(3)
  W4.SetLineWidth(3)

 canvasM = ROOT.TCanvas('canvasM', '', 500, 500)
 H1.SetMinimum(0.0005)
 H1.SetMaximum(30*H1.GetMaximum())
 H1.GetXaxis().SetTitle(""+Var+"")
 H1.Draw("hist")
 H1.Draw("same hist")
 H2.Draw("same hist")
 H3.Draw("same hist")
 H4.Draw("same hist")
 legend = ROOT.TLegend(0.9,0.7,1.0,1.0)
 legend.AddEntry(H1,"H0PM","l")
 legend.AddEntry(H2,"H0M","l")
 legend.AddEntry(H3,"H0PH","l")
 legend.AddEntry(H4,"H0L1","l")
 legend.Draw()
 canvasM.SetLogy()
 canvasM.SaveAs("meinfo/plots/RW_"+Cat+"_"+Var+"_"+Prod+AC+".pdf")

 if CheckWgt :

  canvasW = ROOT.TCanvas('canvasW', '', 500, 500)
  canvasW.Divide(2,2)
  canvasW.cd(1)
  W1.Draw("hist")
  ROOT.gPad.SetLogy() 
  ROOT.gPad.SetLogx() 
  canvasW.cd(2)
  W2.Draw("hist")
  ROOT.gPad.SetLogy() 
  ROOT.gPad.SetLogx() 
  legend.Draw()
  canvasW.cd(3)
  W3.Draw("hist")
  ROOT.gPad.SetLogy() 
  ROOT.gPad.SetLogx() 
  canvasW.cd(4)
  W4.Draw("hist")
  ROOT.gPad.SetLogy() 
  ROOT.gPad.SetLogx()
  canvasW.SaveAs("meinfo/plots/Wgt_"+Cat+"_"+Var+"_"+Prod+AC+".pdf")
 
##########################################################

WHConfig = [  ("SRVH",  "kd_vh_hm", "WH", "H0PM"),
              ("SRVH",  "kd_vh_hm", "WH", "H0M_M0"),
              ("SRVH",  "kd_vh_hm", "WH", "H0M_M1"),
              ("SRVH",  "kd_vh_hm", "WH", "H0M_M2"),
              ("SRVH",  "kd_vh_hm", "WH", "H0M_M3"),
              ("SRVH",  "kd_vh_hp", "WH", "H0PH_M0"),
              ("SRVH",  "kd_vh_hp", "WH", "H0PH_M1"),
              ("SRVH",  "kd_vh_hp", "WH", "H0PH_M2"),
              ("SRVH",  "kd_vh_hp", "WH", "H0PH_M3"),
              ("SRVH",  "kd_vh_hl", "WH", "H0L1_M0"), 
              ("SRVH",  "kd_vh_hl", "WH", "H0L1_M1"), 
              ("SRVH",  "kd_vh_hl", "WH", "H0L1_M2"), 
              ("SRVH",  "kd_vh_hl", "WH", "H0L1_M3"), 
]

ZHConfig = [  ("SRVH",  "kd_vh_hm", "ZH", "H0PM"),
              ("SRVH",  "kd_vh_hm", "ZH", "H0M_M0"),
              ("SRVH",  "kd_vh_hm", "ZH", "H0M_M1"),
              ("SRVH",  "kd_vh_hm", "ZH", "H0M_M2"),
              ("SRVH",  "kd_vh_hm", "ZH", "H0M_M3"),
              ("SRVH",  "kd_vh_hp", "ZH", "H0PH_M0"),
              ("SRVH",  "kd_vh_hp", "ZH", "H0PH_M1"),
              ("SRVH",  "kd_vh_hp", "ZH", "H0PH_M2"),
              ("SRVH",  "kd_vh_hp", "ZH", "H0PH_M3"),
              ("SRVH",  "kd_vh_hl", "ZH", "H0L1_M0"), 
              ("SRVH",  "kd_vh_hl", "ZH", "H0L1_M1"), 
              ("SRVH",  "kd_vh_hl", "ZH", "H0L1_M2"), 
              ("SRVH",  "kd_vh_hl", "ZH", "H0L1_M3"), 
]

SigConfig = WHConfig + ZHConfig

for cat, var, prod, sig in SigConfig :
 CompareRW(cat, var, prod, sig)
