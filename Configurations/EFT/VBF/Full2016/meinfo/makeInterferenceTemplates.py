
import sys
import ROOT 
import numpy as np
import shutil
import math
from os import path

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)

#########################################################

G2_HWW = 1.133582
G4_HWW = 1.76132
L1_HWW = -13752.22

G2_VBF = 0.27196538
G4_VBF = 0.29797901870
L1_VBF = -2158.21307286

JHUXSHWWa1 = 312.04019
JHUXSHWWa2 = 242.6283
JHUXSHWWa3 = 100.79135
JHUXSHWWL1 = 1.6475531e-06
JHUXSHWWa1a2 = 1149.9181
JHUXSHWWa1a3 = 624.7195
JHUXSHWWa1L1 = 5.3585509

JHUXSVBFa1 = 968.88143
JHUXSVBFa2 = 13097.831
JHUXSVBFa3 = 10910.237
JHUXSVBFL1 = 0.00020829261
JHUXSVBFa1a2 = 2207.6738
JHUXSVBFa1a3 = 1936.4327
JHUXSVBFa1L1 = 2861.7003

JHUXSHWWa1a2_I = (JHUXSHWWa1a2 - JHUXSHWWa1 - (G2_HWW**2)*JHUXSHWWa2)/G2_HWW
JHUXSHWWa1a3_I = (JHUXSHWWa1a3 - JHUXSHWWa1 - (G4_HWW**2)*JHUXSHWWa3)/G4_HWW
JHUXSHWWa1L1_I = (JHUXSHWWa1L1 - JHUXSHWWa1 - (L1_HWW**2)*JHUXSHWWL1)/L1_HWW

JHUXSVBFa1a2_I = (JHUXSVBFa1a2 - JHUXSVBFa1 - (G2_VBF**2)*JHUXSVBFa2)/G2_VBF
JHUXSVBFa1a3_I = (JHUXSVBFa1a3 - JHUXSVBFa1 - (G4_VBF**2)*JHUXSVBFa3)/G4_VBF
JHUXSVBFa1L1_I = (JHUXSVBFa1L1 - JHUXSVBFa1 - (L1_VBF**2)*JHUXSVBFL1)/L1_VBF

a1 = 1
ai = G4_VBF
print " " 
print " Test H0M for a1, ai = ", a1, ai
JHUXSVBFa1a3_ai = JHUXSVBFa1*a1**2 + JHUXSVBFa1a3_I*a1*ai + JHUXSVBFa3*ai**2
Fa3P = (JHUXSVBFa3*ai**2)/(JHUXSVBFa3*ai**2 + JHUXSVBFa1*a1**2)
Mu3P = (JHUXSVBFa3*ai**2 + JHUXSVBFa1*a1**2)/JHUXSVBFa1
print "PV F values : ", Fa3P ,", with Int : ", (JHUXSVBFa3*ai**2)/JHUXSVBFa1a3_ai
print "PV Mu values : ", Mu3P ,", with Int : ", JHUXSVBFa1a3_ai/JHUXSVBFa1
JHUXSHWWa1a3_ai = JHUXSHWWa1*a1**2 + JHUXSHWWa1a3_I*a1*ai + JHUXSHWWa3*(ai**2)
Fa3D = (JHUXSHWWa3*ai**2)/(JHUXSHWWa3*ai**2 + JHUXSHWWa1*a1**2)
Mu3D = (JHUXSHWWa3*ai**2 + JHUXSHWWa1*a1**2)/JHUXSHWWa1
print "DV F values : ", Fa3D,", with Int : ", (JHUXSHWWa3*ai**2)/JHUXSHWWa1a3_ai
print "DV Mu values : ", Mu3D,", with Int : ", JHUXSHWWa1a3_ai/JHUXSHWWa1
print " " 

ai = G2_VBF
print " Test H0PH for a1, ai = ", a1, ai
JHUXSVBFa1a2_ai = JHUXSVBFa1*a1**2 + JHUXSVBFa1a2_I*a1*ai + JHUXSVBFa2*ai**2
Fa2P = (JHUXSVBFa2*ai**2)/(JHUXSVBFa2*ai**2 + JHUXSVBFa1*a1**2)
Mu2P = (JHUXSVBFa2*ai**2 + JHUXSVBFa1*a1**2)/JHUXSVBFa1
print "PV F values : ", Fa2P ,", with Int : ", (JHUXSVBFa2*ai**2)/JHUXSVBFa1a2_ai
print "PV Mu values : ", Mu2P ,", with Int : ", JHUXSVBFa1a2_ai/JHUXSVBFa1
JHUXSHWWa1a2_ai = JHUXSHWWa1*a1**2 + JHUXSHWWa1a2_I*a1*ai + JHUXSHWWa2*(ai**2)
Fa2D = (JHUXSHWWa2*ai**2)/(JHUXSHWWa2*ai**2 + JHUXSHWWa1*a1**2)
Mu2D = (JHUXSHWWa2*ai**2 + JHUXSHWWa1*a1**2)/JHUXSHWWa1
print "DV F values : ", Fa2D,", with Int : ", (JHUXSHWWa2*ai**2)/JHUXSHWWa1a2_ai
print "DV Mu values : ", Mu2D,", with Int : ", JHUXSHWWa1a2_ai/JHUXSHWWa1
print " " 

ai = L1_VBF
print " Test H0L1 for a1, ai = ", a1, ai
JHUXSVBFa1L1_ai = JHUXSVBFa1*a1**2 + JHUXSVBFa1L1_I*a1*ai + JHUXSVBFL1*ai**2
FL1P  = np.sign(ai)*(JHUXSVBFL1*ai**2)/(JHUXSVBFL1*ai**2 + JHUXSVBFa1*a1**2)
MuL1P = (JHUXSVBFL1*ai**2 + JHUXSVBFa1*a1**2)/JHUXSVBFa1
print "PV F values : ", FL1P ,", with Int : ", (JHUXSVBFL1*ai**2)/JHUXSVBFa1L1_ai
print "PV Mu values : ", MuL1P ,", with Int : ", JHUXSVBFa1L1_ai/JHUXSVBFa1
JHUXSHWWa1L1_ai = JHUXSHWWa1*a1**2 + JHUXSHWWa1L1_I*a1*ai + JHUXSHWWL1*(ai**2)
FL1D = np.sign(ai)*(JHUXSHWWL1*ai**2)/(JHUXSHWWL1*ai**2 + JHUXSHWWa1*a1**2)
MuL1D = (JHUXSHWWL1*ai**2 + JHUXSHWWa1*a1**2)/JHUXSHWWa1
print "DV F values : ", FL1D,", with Int : ", (JHUXSHWWL1*ai**2)/JHUXSHWWa1L1_ai
print "DV Mu values : ", MuL1D,", with Int : ", JHUXSHWWa1L1_ai/JHUXSHWWa1
print " " 

###########################################################################

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

def createIntTemplates(Cat, Var, AC, Sys, Test):

 print " " 
 print Cat, Var, AC, Sys, Test
 print " " 

 f = ROOT.TFile.Open(''+dst+'', 'update')

 SM = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_VBFH0PM'+Sys+'')
 M0 = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_VBF'+AC+Sys+'')
 M1 = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_VBF'+AC+'_M1'+Sys+'')
 M2 = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_VBF'+AC+'_M2'+Sys+'')
 M3 = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_VBF'+AC+'_M3'+Sys+'')

 SM_Org  = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_VBFH0PM_Org'+Sys+'')
 BSM_Org = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_VBF'+AC+'_Org'+Sys+'')
 f05_Org = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_VBF'+AC+'f05_Org'+Sys+'')

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
 if AC == "H0L1" : 
  InvG = np.linalg.inv(Gl1)

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
          
 if AC == "H0M"  :
   Fai = Fa3P
   Mu  = Mu3P
   G   = G4_VBF
 if AC == "H0PH" : 
   Fai = Fa2P
   Mu  = Mu2P
   G   = G2_VBF
 if AC == "H0L1" : 
   Fai = FL1P
   Mu  = MuL1P
   G   = abs(L1_VBF)

 Fa1 = 1-abs(Fai)

 print "Fai, Fa1, and Mu = ", Fai, Fa1, Mu
 
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

 if Test == True :

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

  canvasBSM = ROOT.TCanvas('canvasBSM', '', 500, 500)
  T04.SetMinimum(0.1)
  T04.SetMaximum(1.5*T04.GetMaximum())
  T04.GetXaxis().SetTitle(""+Var+"")
  T04.Draw("hist")
  BSM_Org.Draw("same e")
  legend = ROOT.TLegend(0.3,0.75,0.7,0.9)
  legend.AddEntry(BSM_Org,"pure BSM MC","l")
  legend.AddEntry(T04,"T5 template","f")
  legend.Draw()
  canvasBSM.SaveAs("meinfo/plots/BSM_"+Cat+"_"+Var+"_"+AC+Sys+".pdf")

  canvasSM = ROOT.TCanvas('canvasSM', '', 500, 500)
  T40.SetMinimum(0.1)
  T40.SetMaximum(1.5*T40.GetMaximum())
  T40.GetXaxis().SetTitle(""+Var+"")
  T40.Draw("hist")
  SM_Org.Draw("same e")
  legend = ROOT.TLegend(0.3,0.75,0.7,0.9)
  legend.AddEntry(SM_Org,"pure SM MC","l")
  legend.AddEntry(T40,"T1 template","f")
  legend.Draw()
  canvasSM.SaveAs("meinfo/plots/SM_"+Cat+"_"+Var+"_"+AC+Sys+".pdf")

  canvasf05 = ROOT.TCanvas('canvasf05', '', 500, 500)
  f05.SetMinimum(0.1)
  f05.SetMaximum(1.5*f05.GetMaximum())
  f05.GetXaxis().SetTitle(""+Var+"")
  f05.Draw("hist")
  f05_Org.Draw("same e")
  legend = ROOT.TLegend(0.3,0.75,0.7,0.9)
  legend.AddEntry(f05_Org,"SM-BSM Mix MC ","l")
  legend.AddEntry(f05,"T1-T5 combination","f")
  legend.Draw()
  canvasf05.SaveAs("meinfo/plots/f05_"+Cat+"_"+Var+"_"+AC+Sys+".pdf")

  canvas31 = ROOT.TCanvas('canvas31', '', 500, 500)
  T31.GetXaxis().SetTitle(""+Var+"")
  T31.Draw("hist")
  legend = ROOT.TLegend(0.3,0.8,0.7,0.9)
  legend.AddEntry(T31,"T2 template","f")
  legend.SetTextSize(.04)
  legend.Draw()
  canvas31.SaveAs("meinfo/plots/Int31_"+Cat+"_"+Var+"_"+AC+Sys+".pdf")

  canvas22 = ROOT.TCanvas('canvas22', '', 500, 500)
  T22.GetXaxis().SetTitle(""+Var+"")
  T22.Draw("hist")
  legend = ROOT.TLegend(0.3,0.8,0.7,0.9)
  legend.AddEntry(T22,"T3 template","f")
  legend.SetTextSize(.04)
  legend.Draw()
  canvas22.SaveAs("meinfo/plots/Int22_"+Cat+"_"+Var+"_"+AC+Sys+".pdf")

  canvas13 = ROOT.TCanvas('canvas13', '', 500, 500)
  T13.GetXaxis().SetTitle(""+Var+"")
  T13.Draw("hist")
  legend = ROOT.TLegend(0.3,0.8,0.7,0.9)
  legend.AddEntry(T13,"T4 template","f")
  legend.SetTextSize(.04)
  legend.Draw()
  canvas13.SaveAs("meinfo/plots/Int13_"+Cat+"_"+Var+"_"+AC+Sys+".pdf")


 f.cd("hww2l2v_13TeV_"+Cat+"/"+Var+"/")
 T04.SetName("histo_VBF"+AC+Sys+"")
 T31.SetName("histo_VBF"+AC+"_M1"+Sys+"")
 T22.SetName("histo_VBF"+AC+"_M2"+Sys+"")
 T13.SetName("histo_VBF"+AC+"_M3"+Sys+"")
 T04.Write("",ROOT.TObject.kOverwrite)
 T31.Write("",ROOT.TObject.kOverwrite)
 T22.Write("",ROOT.TObject.kOverwrite)
 T13.Write("",ROOT.TObject.kOverwrite)

 f.Close()

##########################################################


SigConfig = [ ("SRVBF", "kd_vbf_hm", "H0M"),
              ("SRVBF", "kd_vbf_hp", "H0PH"),
              ("SRVBF", "kd_vbf_hl", "H0L1")]
  
Systematics = ["CMS_eff_mu", "CMS_eff_el"]

for cat, var, sig in SigConfig :
 createIntTemplates(cat, var, sig, "", False)
 for sys in Systematics :
  createIntTemplates(cat, var, sig, "_"+sys+"Up", False)
  createIntTemplates(cat, var, sig, "_"+sys+"Down", False)

