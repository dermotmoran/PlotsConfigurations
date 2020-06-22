
import sys
import ROOT 
import numpy as np
import shutil
import math
from os import path

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)

#########################################################

G2_VBF = 0.27196538
G4_VBF = 0.29797901870
L1_VBF = -2158.21307286

G2_WH = 0.0998956
G4_WH = 0.1236136
L1_WH = -525.274

G2_ZH = 0.112481
G4_ZH = 0.144057
L1_ZH = -517.788

Gai = np.array(([1**4,0,0,0,0],  
                [0,0,0,0,1**4],  
                [1,.25,.25**2,.25**3,.25**4],  
                [1,.5,  .5**2, .5**3, .5**4],             
                [1,.75,.75**2,.75**3,.75**4]  )) 

l1s = -10000
Gl1 = np.array(([1**4,0,0,0,0],  
                [0,0,0,0,(1*l1s)**4],  
                [1,.25*l1s,(.25*l1s)**2,(.25*l1s)**3,(.25*l1s)**4],  
                [1,.5*l1s, ( .5*l1s)**2,( .5*l1s)**3,( .5*l1s)**4],             
                [1,.75*l1s,(.75*l1s)**2,(.75*l1s)**3,(.75*l1s)**4]  )) 

###################################################################

src = path.realpath("rootFileVBF/plots_VBF.root")
dst = "rootFileVBF/plots_VBF_Int.root"
shutil.copy(src, dst)

print "- Will create interference terms T = [T1(4,0), T2(3,1), T3(2,2), T4(1,3), T5(0,4)]" 
print "from SM-BSM mixture hypotheses : H = [SM(1,0), M0(0,1), M1(1,.25), M2(1,.5), M3(1,.75)] "
print "and G matrices ", Gai, Gl1
print "- Will create new file : "+dst+""
print "with H hists M0(0,1), M1(1,.25), M2(1,.5), M3(1,.75) replaced by T hists T04, T31, T22, T13"
print " "

#########################################################

def createIntTemplates(Cat, Var, Prod, AC, Sys, Test):

 print " " 
 print " ", Cat, Var, Prod, AC, Sys, Test
 print " " 

 f = ROOT.TFile.Open(''+dst+'', 'update')

 SM = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+Prod+'_H0PM'+Sys+'')
 M0 = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+Prod+'_'+AC+Sys+'')
 M1 = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+Prod+'_'+AC+'_M1'+Sys+'')
 M2 = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+Prod+'_'+AC+'_M2'+Sys+'')
 M3 = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+Prod+'_'+AC+'_M3'+Sys+'')

 SM_Org  = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+Prod+'_H0PM_Org'+Sys+'')
 BSM_Org = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+Prod+'_'+AC+'_Org'+Sys+'')
 f05_Org = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+Prod+'_'+AC+'f05_Org'+Sys+'')

 T40 = SM.Clone()
 T31 = SM.Clone()
 T22 = SM.Clone()
 T13 = SM.Clone()
 T04 = SM.Clone()

 T40.SetDirectory(0)
 T31.SetDirectory(0)
 T22.SetDirectory(0)
 T13.SetDirectory(0)
 T04.SetDirectory(0)

 InvG = np.linalg.inv(Gai)
 if AC == "H0L1" : InvG = np.linalg.inv(Gl1)

 T40.Scale( InvG[0][0])
 T40.Add(M0,InvG[0][1])
 T40.Add(M1,InvG[0][2])
 T40.Add(M2,InvG[0][3])
 T40.Add(M3,InvG[0][4])

 T31.Scale( InvG[1][0])
 T31.Add(M0,InvG[1][1])
 T31.Add(M1,InvG[1][2])
 T31.Add(M2,InvG[1][3])
 T31.Add(M3,InvG[1][4])

 T22.Scale( InvG[2][0])
 T22.Add(M0,InvG[2][1])
 T22.Add(M1,InvG[2][2])
 T22.Add(M2,InvG[2][3])
 T22.Add(M3,InvG[2][4])

 T13.Scale( InvG[3][0])
 T13.Add(M0,InvG[3][1])
 T13.Add(M1,InvG[3][2])
 T13.Add(M2,InvG[3][3])
 T13.Add(M3,InvG[3][4])

 T04.Scale( InvG[4][0])
 T04.Add(M0,InvG[4][1])
 T04.Add(M1,InvG[4][2])
 T04.Add(M2,InvG[4][3])
 T04.Add(M3,InvG[4][4])
 
 ######### Tricks for combine #######

 T31Neg = False
 
 if AC == "H0M" :
  print "--------- Force T31 and T13 = 0"
  T31.Scale(0)  
  T13.Scale(0)  

 if T31.Integral() < 0 :
  print "--------- Force T31 positive - Compensate in model! "
  T31.Scale(-1)  
  T31Neg = True

 ####################################
 
 if Test == True :

  print "T40,31,22,13,04 :", T40.Integral(),T31.Integral(),T22.Integral(),T13.Integral(),T04.Integral() 
  print " " 

  Fai = 0.5
  Mu  = 2.0
  if AC == "H0L1" : Fai = -0.5
 
  if Prod=="VBF" :      
   if AC == "H0M"  : G = G4_VBF
   if AC == "H0PH" : G = G2_VBF
   if AC == "H0L1" : G = abs(L1_VBF)
  if Prod=="WH" :      
   if AC == "H0M"  : G = G4_WH
   if AC == "H0PH" : G = G2_WH
   if AC == "H0L1" : G = abs(L1_WH)
  if Prod=="ZH" :      
   if AC == "H0M"  : G = G4_ZH
   if AC == "H0PH" : G = G2_ZH
   if AC == "H0L1" : G = abs(L1_ZH)

  Fa1 = 1-abs(Fai)

  print "Fai, Fa1, Mu and G = ", Fai, Fa1, Mu, G
 
  N40 = Mu**2*Fa1**2
  N31 = Mu**2*np.sign(Fai)*math.sqrt(abs(Fai))*(math.sqrt(Fa1)**3)*G
  N22 = Mu**2*abs(Fai)*Fa1*G**2
  N13 = Mu**2*np.sign(Fai)*(math.sqrt(abs(Fai))**3)*math.sqrt(Fa1)*G**3
  N04 = Mu**2*Fai**2*G**4

  ''' In terms of the couplings!
  g1 = 1
  g2 = 1
  if AC == "H0M"  : g2 = G4_VBF
  if AC == "H0PH" : g2 = G2_VBF
  if AC == "H0L1" : g2 = L1_VBF
  N40 = g1**4
  N31 = (g1**3)*g2
  N22 = (g1**2)*(g2**2)
  N13 = g1*(g2**3)
  N04 = g2**4
  ''' 
 
  if T31Neg is True : N31 = N31*-1
          
  f05 = T40.Clone()
  f05.SetDirectory(0)
  f05.Scale(   N40)
  f05.Add(T31, N31)
  f05.Add(T22, N22)
  f05.Add(T13, N13)
  f05.Add(T04, N04)

  print "BSM Intergal R :", BSM_Org.Integral()/T04.Integral()
  print "SM Intergal R :", SM_Org.Integral()/T40.Integral()
  print "f05 Intergal R :", f05_Org.Integral()/f05.Integral()

  SM.SetLineColor(ROOT.kRed)
  M0.SetLineColor(ROOT.kGreen)
  M1.SetLineColor(ROOT.kCyan)
  M2.SetLineColor(ROOT.kOrange)
  M3.SetLineColor(ROOT.kBlue)
  SM.SetLineWidth(3)
  M0.SetLineWidth(3)
  M1.SetLineWidth(3)
  M2.SetLineWidth(3)
  M3.SetLineWidth(3)

  SM_Org.SetLineColor(ROOT.kBlack)
  BSM_Org.SetLineColor(ROOT.kBlack) 
  f05_Org.SetLineColor(ROOT.kBlack) 
  SM_Org.SetLineWidth(2)
  BSM_Org.SetLineWidth(2)
  f05_Org.SetLineWidth(2)

  f05.SetLineColor(ROOT.kRed)
  f05.SetFillColor(ROOT.kRed)
  T40.SetLineColor(ROOT.kRed)
  T40.SetFillColor(ROOT.kRed)
  T31.SetLineColor(ROOT.kOrange)
  T31.SetFillColor(ROOT.kOrange)
  T22.SetLineColor(ROOT.kCyan)
  T22.SetFillColor(ROOT.kCyan)
  T13.SetLineColor(ROOT.kBlue)
  T13.SetFillColor(ROOT.kBlue)
  T04.SetLineColor(ROOT.kGreen)
  T04.SetFillColor(ROOT.kGreen)
  T40.SetLineWidth(2)
  T31.SetLineWidth(2)
  T22.SetLineWidth(2)
  T13.SetLineWidth(2)
  T04.SetLineWidth(2)

  canvasH = ROOT.TCanvas('canvasH', '', 500, 500)
  M3.SetMinimum(0.001)
  M3.SetMaximum(5*M3.GetMaximum())
  M3.GetXaxis().SetTitle(""+Var+"")
  M3.Draw("hist")
  SM.Draw("same hist")
  M0.Draw("same hist")
  M1.Draw("same hist")
  M2.Draw("same hist")
  legend = ROOT.TLegend(0.2,0.6,0.35,0.9)
  legend.AddEntry(SM,"H1","l")
  legend.AddEntry(M0,"H2","l")
  legend.AddEntry(M1,"H3","l")
  legend.AddEntry(M2,"H4","l")
  legend.AddEntry(M3,"H5","l")
  legend.Draw()
  canvasH.SetLogy()
  canvasH.SaveAs("meinfo/plots/H_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")

  canvasBSM = ROOT.TCanvas('canvasBSM', '', 500, 500)
  T04.SetMinimum(0.001)
  T04.SetMaximum(1.5*T04.GetMaximum())
  T04.GetXaxis().SetTitle(""+Var+"")
  T04.Draw("hist")
  BSM_Org.Draw("same e")
  legend = ROOT.TLegend(0.3,0.75,0.7,0.9)
  legend.AddEntry(BSM_Org,"pure BSM MC","l")
  legend.AddEntry(T04,"T5 template","f")
  legend.Draw()
  canvasBSM.SaveAs("meinfo/plots/BSM_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")

  canvasSM = ROOT.TCanvas('canvasSM', '', 500, 500)
  T40.SetMinimum(0.001)
  T40.SetMaximum(1.5*T40.GetMaximum())
  T40.GetXaxis().SetTitle(""+Var+"")
  T40.Draw("hist")
  SM_Org.Draw("same e")
  legend = ROOT.TLegend(0.3,0.75,0.7,0.9)
  legend.AddEntry(SM_Org,"pure SM MC","l")
  legend.AddEntry(T40,"T1 template","f")
  legend.Draw()
  canvasSM.SaveAs("meinfo/plots/SM_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")

  canvasf05 = ROOT.TCanvas('canvasf05', '', 500, 500)
  f05.SetMinimum(0.001)
  f05.SetMaximum(1.5*f05.GetMaximum())
  f05.GetXaxis().SetTitle(""+Var+"")
  f05.Draw("hist")
  f05_Org.Draw("same e")
  legend = ROOT.TLegend(0.3,0.75,0.7,0.9)
  legend.AddEntry(f05_Org,"SM-BSM Mix MC ","l")
  legend.AddEntry(f05,"T1-T5 combination","f")
  legend.Draw()
  canvasf05.SaveAs("meinfo/plots/f05_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")

  canvas31 = ROOT.TCanvas('canvas31', '', 500, 500)
  T31.GetXaxis().SetTitle(""+Var+"")
  T31.Draw("hist")
  legend = ROOT.TLegend(0.3,0.8,0.7,0.9)
  legend.AddEntry(T31,"T2 template","f")
  legend.SetTextSize(.04)
  legend.Draw()
  canvas31.SaveAs("meinfo/plots/Int31_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")

  canvas22 = ROOT.TCanvas('canvas22', '', 500, 500)
  T22.GetXaxis().SetTitle(""+Var+"")
  T22.Draw("hist")
  legend = ROOT.TLegend(0.3,0.8,0.7,0.9)
  legend.AddEntry(T22,"T3 template","f")
  legend.SetTextSize(.04)
  legend.Draw()
  canvas22.SaveAs("meinfo/plots/Int22_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")

  canvas13 = ROOT.TCanvas('canvas13', '', 500, 500)
  T13.GetXaxis().SetTitle(""+Var+"")
  T13.Draw("hist")
  legend = ROOT.TLegend(0.3,0.8,0.7,0.9)
  legend.AddEntry(T13,"T4 template","f")
  legend.SetTextSize(.04)
  legend.Draw()
  canvas13.SaveAs("meinfo/plots/Int13_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")

 f.cd("hww2l2v_13TeV_"+Cat+"/"+Var+"/")
 T04.SetName("histo_"+Prod+"_"+AC+Sys+"")
 T31.SetName("histo_"+Prod+"_"+AC+"_M1"+Sys+"")
 T22.SetName("histo_"+Prod+"_"+AC+"_M2"+Sys+"")
 T13.SetName("histo_"+Prod+"_"+AC+"_M3"+Sys+"")
 T04.Write("",ROOT.TObject.kOverwrite)
 T31.Write("",ROOT.TObject.kOverwrite)
 T22.Write("",ROOT.TObject.kOverwrite)
 T13.Write("",ROOT.TObject.kOverwrite)

 f.Close()

##########################################################

VBFConfig = [ ("SRVBF", "kd_vbf_hm", "VBF", "H0M"),
              ("SRVBF", "kd_vbf_hp", "VBF", "H0PH"),
              ("SRVBF", "kd_vbf_hl", "VBF", "H0L1"),
              ("SRVBF", "kd_vbf_hm", "WH", "H0M"),
              ("SRVBF", "kd_vbf_hp", "WH", "H0PH"),
              ("SRVBF", "kd_vbf_hl", "WH", "H0L1"),
              ("SRVBF", "kd_vbf_hm", "ZH", "H0M"),
              ("SRVBF", "kd_vbf_hp", "ZH", "H0PH"),
              ("SRVBF", "kd_vbf_hl", "ZH", "H0L1")
]

VHConfig = [  ("SRVH", "kd_vh_hm", "VBF", "H0M"),
              ("SRVH", "kd_vh_hp", "VBF", "H0PH"),
              ("SRVH", "kd_vh_hl", "VBF", "H0L1"),
              ("SRVH", "kd_vh_hm", "WH", "H0M"),
              ("SRVH", "kd_vh_hp", "WH", "H0PH"),
              ("SRVH", "kd_vh_hl", "WH", "H0L1"),
              ("SRVH", "kd_vh_hm", "ZH", "H0M"),
              ("SRVH", "kd_vh_hp", "ZH", "H0PH"),
              ("SRVH", "kd_vh_hl", "ZH", "H0L1")
]
  
SigConfig = VBFConfig + VHConfig

Systematics = ["CMS_eff_mu", "CMS_eff_el"]

for cat, var, prod, sig in SigConfig :
 createIntTemplates(cat, var, prod, sig, "", True)
 for sys in Systematics :
  createIntTemplates(cat, var, prod, sig, "_"+sys+"Up", False)
  createIntTemplates(cat, var, prod, sig, "_"+sys+"Down", False)

