
import sys
import ROOT 
import numpy as np
import shutil
import math
from os import path

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)

############# Couplings of mixed samples

G2_HWW = 1.133582
G4_HWW = 1.76132
L1_HWW = -13752.22

G2_VBF = 0.27196538
G4_VBF = 0.29797901870
L1_VBF = -2158.21307286

G2_WH = 0.0998956
G4_WH = 0.1236136
L1_WH = -525.274

G2_ZH = 0.112481
G4_ZH = 0.144057
L1_ZH = -517.788
 
############### Matrix of couplings for H(g1, gi) hypotheses - Ewk H (2 Vertices)

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

print "- For Ewk H (2V) need templates : T1 -(4,0), T2 -(3,1), T3 -(2,2), T4 -(1,3), T5 -(0,4)" 
print "Get from SM-BSM mixture hypotheses : SM(1,0), M0(0,1), M1(1,.25), M2(1,.5), M3(1,.75) "
print "and G matrices ", Gai, Gl1
print "- Will create new file : "+dst+""
print "with hists M0(0,1), M1(1,.25), M2(1,.5), M3(1,.75) replaced by hists T2, T3, T4, T5"
print " " 
print "- For ggH (1V) need templates T1 -(2,0), T2 -(1,1), T3 -(0,2)" 
print "Get from SM-BSM MC : SM(1,0), BSM(0,1), M1(1,gMix) "
print "- Will create new file : "+dst+""
print "with hist M1(1,gMix) replaced hist T2"
print " "

#########################################################

def create2VIntTemplates(Cat, Var, Prod, AC, Sys, Test):

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

 T1 = SM.Clone() # 4,0
 T2 = SM.Clone() # 3,1
 T3 = SM.Clone() # 2,2
 T4 = SM.Clone() # 1,3
 T5 = SM.Clone() # 0,4

 T1.SetDirectory(0)
 T2.SetDirectory(0)
 T3.SetDirectory(0)
 T4.SetDirectory(0)
 T5.SetDirectory(0)

 InvG = np.linalg.inv(Gai)
 if AC == "H0L1" : InvG = np.linalg.inv(Gl1)

 T1.Scale( InvG[0][0])
 T1.Add(M0,InvG[0][1])
 T1.Add(M1,InvG[0][2])
 T1.Add(M2,InvG[0][3])
 T1.Add(M3,InvG[0][4])

 T2.Scale( InvG[1][0])
 T2.Add(M0,InvG[1][1])
 T2.Add(M1,InvG[1][2])
 T2.Add(M2,InvG[1][3])
 T2.Add(M3,InvG[1][4])

 T3.Scale( InvG[2][0])
 T3.Add(M0,InvG[2][1])
 T3.Add(M1,InvG[2][2])
 T3.Add(M2,InvG[2][3])
 T3.Add(M3,InvG[2][4])

 T4.Scale( InvG[3][0])
 T4.Add(M0,InvG[3][1])
 T4.Add(M1,InvG[3][2])
 T4.Add(M2,InvG[3][3])
 T4.Add(M3,InvG[3][4])

 T5.Scale( InvG[4][0])
 T5.Add(M0,InvG[4][1])
 T5.Add(M1,InvG[4][2])
 T5.Add(M2,InvG[4][3])
 T5.Add(M3,InvG[4][4])
 
 ######### Tricks for combine #######
 
 T2Neg = False 

 if AC == "H0M" :
  print "--------- Force T2 and T4 = 0"
  T2.Scale(0)  
  T4.Scale(0)  

 if T2.Integral() < 0 :
  print "--------- Force T2 positive - Compensate in model! "
  T2.Scale(-1)  
  T2Neg = True

 ####################################
 
 if Test == True :

  Fai = 0.5
  Mu  = 2.0
 
  if Prod=="VBF" :      
   if AC == "H0M"  : G = G4_VBF
   if AC == "H0PH" : G = G2_VBF
   if AC == "H0L1" : G = L1_VBF
  if Prod=="WH" :      
   if AC == "H0M"  : G = G4_WH
   if AC == "H0PH" : G = G2_WH
   if AC == "H0L1" : G = L1_WH
  if Prod=="ZH" :      
   if AC == "H0M"  : G = G4_ZH
   if AC == "H0PH" : G = G2_ZH
   if AC == "H0L1" : G = L1_ZH

  Fa1 = 1-abs(Fai)

  print "Fai, Fa1, Mu and G = ", Fai, Fa1, Mu, G
 
  N1 = Mu**2*Fa1**2    # 4,0
  N2 = Mu**2*np.sign(Fai)*math.sqrt(abs(Fai))*(math.sqrt(Fa1)**3)*G # 3,1
  N3 = Mu**2*abs(Fai)*Fa1*G**2 # 2,2
  N4 = Mu**2*np.sign(Fai)*(math.sqrt(abs(Fai))**3)*math.sqrt(Fa1)*G**3 # 1,3
  N5 = Mu**2*Fai**2*G**4 # 0,4
 
  if T2Neg is True : N2 = N2*-1
          
  f05 = T1.Clone()
  f05.SetDirectory(0)
  f05.Scale(  N1)
  f05.Add(T2, N2)
  f05.Add(T3, N3)
  f05.Add(T4, N4)
  f05.Add(T5, N5)

  print "BSM Intergal R :", BSM_Org.Integral()/T5.Integral()
  print "SM Intergal R :", SM_Org.Integral()/T1.Integral()
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

  T1.SetLineColor(ROOT.kRed)
  T1.SetFillColor(ROOT.kRed)
  T2.SetLineColor(ROOT.kOrange)
  T2.SetFillColor(ROOT.kOrange)
  T3.SetLineColor(ROOT.kCyan)
  T3.SetFillColor(ROOT.kCyan)
  T4.SetLineColor(ROOT.kBlue)
  T4.SetFillColor(ROOT.kBlue)
  T5.SetLineColor(ROOT.kGreen)
  T5.SetFillColor(ROOT.kGreen)
  T1.SetLineWidth(2)
  T2.SetLineWidth(2)
  T3.SetLineWidth(2)
  T4.SetLineWidth(2)
  T5.SetLineWidth(2)

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
  canvasH.SaveAs("meinfo/plots/H_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

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
  canvasf05.SaveAs("meinfo/plots/f05_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

  canvasT1 = ROOT.TCanvas('canvasT1', '', 500, 500)
  T1.SetMinimum(0.001)
  T1.SetMaximum(1.5*T1.GetMaximum())
  T1.GetXaxis().SetTitle(""+Var+"")
  T1.Draw("hist")
  SM_Org.Draw("same e")
  legend = ROOT.TLegend(0.3,0.75,0.7,0.9)
  legend.AddEntry(SM_Org,"pure SM MC","l")
  legend.AddEntry(T1,"T1 template","f")
  legend.Draw()
  canvasT1.SaveAs("meinfo/plots/T1_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")
  canvasT1.SaveAs("meinfo/plots/T1_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

  canvasT2 = ROOT.TCanvas('canvasT2', '', 500, 500)
  T2.GetXaxis().SetTitle(""+Var+"")
  T2.Draw("hist")
  legend = ROOT.TLegend(0.3,0.8,0.7,0.9)
  legend.AddEntry(T2,"T2 template","f")
  legend.SetTextSize(.04)
  legend.Draw()
  canvasT2.SaveAs("meinfo/plots/T2_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")
  canvasT2.SaveAs("meinfo/plots/T2_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

  canvasT3 = ROOT.TCanvas('canvasT3', '', 500, 500)
  T3.GetXaxis().SetTitle(""+Var+"")
  T3.Draw("hist")
  legend = ROOT.TLegend(0.3,0.8,0.7,0.9)
  legend.AddEntry(T3,"T3 template","f")
  legend.SetTextSize(.04)
  legend.Draw()
  canvasT3.SaveAs("meinfo/plots/T3_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")
  canvasT3.SaveAs("meinfo/plots/T3_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

  canvasT4 = ROOT.TCanvas('canvasT4', '', 500, 500)
  T4.GetXaxis().SetTitle(""+Var+"")
  T4.Draw("hist")
  legend = ROOT.TLegend(0.3,0.8,0.7,0.9)
  legend.AddEntry(T4,"T4 template","f")
  legend.SetTextSize(.04)
  legend.Draw()
  canvasT4.SaveAs("meinfo/plots/T4_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")
  canvasT4.SaveAs("meinfo/plots/T4_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

  canvasT5 = ROOT.TCanvas('canvasT5', '', 500, 500)
  T5.SetMinimum(0.001)
  T5.SetMaximum(1.5*T5.GetMaximum())
  T5.GetXaxis().SetTitle(""+Var+"")
  T5.Draw("hist")
  BSM_Org.Draw("same e")
  legend = ROOT.TLegend(0.3,0.75,0.7,0.9)
  legend.AddEntry(BSM_Org,"pure BSM MC","l")
  legend.AddEntry(T5,"T5 template","f")
  legend.Draw()
  canvasT5.SaveAs("meinfo/plots/T5_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")
  canvasT5.SaveAs("meinfo/plots/T5_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

 f.cd("hww2l2v_13TeV_"+Cat+"/"+Var+"/")

 T2.SetName("histo_"+Prod+"_"+AC+"_M1"+Sys+"")
 T3.SetName("histo_"+Prod+"_"+AC+"_M2"+Sys+"")
 T4.SetName("histo_"+Prod+"_"+AC+"_M3"+Sys+"")
 T5.SetName("histo_"+Prod+"_"+AC+Sys+"")

 T2.Write("",ROOT.TObject.kOverwrite)
 T3.Write("",ROOT.TObject.kOverwrite)
 T4.Write("",ROOT.TObject.kOverwrite)
 T5.Write("",ROOT.TObject.kOverwrite)

 f.Close()

##########################################################

def create1VIntTemplates(Cat, Var, AC, Sys, Test):

 print " " 
 print " ", Cat, Var, AC, Sys, Test
 print " " 

 f = ROOT.TFile.Open(''+dst+'', 'update')

 BSMO = True
 if AC == "H0L1" : BSMO = False

 SM  = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_H0PM'+Sys+'')
 BSM = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+AC+Sys+'')
 Mix = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+AC+'_M1'+Sys+'')

 SM_Org  = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_H0PM_Org'+Sys+'')
 if BSMO : BSM_Org = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+AC+'_Org'+Sys+'')
 Mix_Org = f.Get('hww2l2v_13TeV_'+Cat+'/'+Var+'/histo_'+AC+'f05_Org'+Sys+'')

 if AC == "H0M"  : G = G4_HWW
 if AC == "H0PH" : G = G2_HWW
 if AC == "H0L1" : G = L1_HWW

 T2 = SM.Clone()
 T2.SetDirectory(0)
 T2.Scale(-1/G)
 T2.Add(BSM, -G)
 T2.Add(Mix, 1/G)

 if BSMO : print "BSM Intergal R :", BSM_Org.Integral()/BSM.Integral()
 print "SM Intergal R :", SM_Org.Integral()/SM.Integral()
 print "Mix Intergal R :", Mix_Org.Integral()/Mix.Integral()

 ######### Tricks for combine #######
 
 if AC == "H0M" :
  print "--------- Force T2 = 0"
  T2.Scale(0)  

 #################
 
 if Test == True :

  Fai = 0.5
  Mu  = 2.0
  Fa1 = 1-abs(Fai)
 
  N1 = Mu*Fa1                       # 2,0
  N2 = Mu*math.sqrt(abs(Fai)*Fa1)*G # 1,1
  N3 = Mu*Fai*G**2                  # 0,2
           
  f05 = SM.Clone()
  f05.SetDirectory(0)
  f05.Scale(   N1)
  f05.Add(T2,  N2)
  f05.Add(BSM, N3)
  
  print "f05 Intergal R :", Mix_Org.Integral()/f05.Integral()

  ###############

  SM.SetLineColor(ROOT.kRed)
  SM.SetFillColor(ROOT.kRed)
  BSM.SetLineColor(ROOT.kGreen)
  BSM.SetFillColor(ROOT.kGreen)
  Mix.SetLineColor(ROOT.kCyan)
  Mix.SetFillColor(ROOT.kCyan)
  SM.SetLineWidth(3)
  BSM.SetLineWidth(3)
  Mix.SetLineWidth(3)

  SM_Org.SetLineColor(ROOT.kBlack)
  if BSMO : BSM_Org.SetLineColor(ROOT.kBlack) 
  Mix_Org.SetLineColor(ROOT.kBlack) 
  SM_Org.SetLineWidth(2)
  if BSMO : BSM_Org.SetLineWidth(2)
  Mix_Org.SetLineWidth(2)

  T2.SetLineColor(ROOT.kBlue)
  T2.SetFillColor(ROOT.kBlue)

  f05.SetLineColor(ROOT.kRed)
  f05.SetFillColor(ROOT.kRed)
  f05.SetLineWidth(2)

  canvasf05 = ROOT.TCanvas('canvasf05', '', 500, 500)
  f05.SetMinimum(0.001)
  f05.SetMaximum(1.5*f05.GetMaximum())
  f05.GetXaxis().SetTitle(""+Var+"")
  f05.Draw("hist")
  Mix_Org.Draw("same e")
  Mix.Draw("same e")
  legend = ROOT.TLegend(0.3,0.75,0.7,0.9)
  legend.AddEntry(Mix_Org,"SM-BSM Mix MC ","l")
  legend.AddEntry(f05,"T1-T3 combination","f")
  legend.Draw()
  canvasf05.SaveAs("meinfo/plots/f05_"+Cat+"_"+Var+"_"+AC+Sys+".pdf")
  canvasf05.SaveAs("meinfo/plots/f05_"+Cat+"_"+Var+"_"+AC+Sys+".png")

  canvasT1 = ROOT.TCanvas('canvasT1', '', 500, 500)
  SM.SetMinimum(0.001)
  SM.SetMaximum(1.5*SM.GetMaximum())
  SM.GetXaxis().SetTitle(""+Var+"")
  SM.Draw("hist")
  SM_Org.Draw("same e")
  legend = ROOT.TLegend(0.3,0.75,0.7,0.9)
  legend.AddEntry(SM_Org,"pure SM MC","l")
  legend.AddEntry(SM,"T1 template","f")
  legend.Draw()
  canvasT1.SaveAs("meinfo/plots/T1_"+Cat+"_"+Var+"_"+AC+Sys+".pdf")
  canvasT1.SaveAs("meinfo/plots/T1_"+Cat+"_"+Var+"_"+AC+Sys+".png")

  canvasT2 = ROOT.TCanvas('canvasT2', '', 500, 500)
  T2.GetXaxis().SetTitle(""+Var+"")
  T2.Draw("hist")
  legend = ROOT.TLegend(0.3,0.8,0.7,0.9)
  legend.AddEntry(T2,"T2 template","f")
  legend.SetTextSize(.04)
  legend.Draw()
  canvasT2.SaveAs("meinfo/plots/T2_"+Cat+"_"+Var+"_"+AC+Sys+".pdf")
  canvasT2.SaveAs("meinfo/plots/T2_"+Cat+"_"+Var+"_"+AC+Sys+".png")

  canvasT3 = ROOT.TCanvas('canvasT3', '', 500, 500)
  BSM.SetMinimum(0.001)
  BSM.SetMaximum(1.5*BSM.GetMaximum())
  BSM.GetXaxis().SetTitle(""+Var+"")
  BSM.Draw("hist")
  if BSMO : BSM_Org.Draw("same e")
  legend = ROOT.TLegend(0.3,0.75,0.7,0.9)
  if BSMO : legend.AddEntry(BSM_Org,"pure BSM MC","l")
  legend.AddEntry(BSM,"T3 template","f")
  legend.Draw()
  canvasT3.SaveAs("meinfo/plots/T3_"+Cat+"_"+Var+"_"+AC+Sys+".pdf")
  canvasT3.SaveAs("meinfo/plots/T3_"+Cat+"_"+Var+"_"+AC+Sys+".png")

 f.cd("hww2l2v_13TeV_"+Cat+"/"+Var+"/")
 T2.SetName("histo_"+AC+"_M1"+Sys+"")
 T2.Write("",ROOT.TObject.kOverwrite)

 f.Close()

##########################################################

Systematics = ["CMS_eff_mu", "CMS_eff_el"]

VBFConfig = [ ("SRVBF", "kd_vbf_hm", "VBF", "H0M"),
              ("SRVBF", "kd_vbf_hp", "VBF", "H0PH"),
              ("SRVBF", "kd_vbf_hl", "VBF", "H0L1"),
              ("SRVH",  "kd_vh_hm",  "VBF", "H0M"),
              ("SRVH",  "kd_vh_hp",  "VBF", "H0PH"),
              ("SRVH",  "kd_vh_hl",  "VBF", "H0L1"),             
]

WHConfig = [  ("SRVBF", "kd_vbf_hm", "WH", "H0M"),
              ("SRVBF", "kd_vbf_hp", "WH", "H0PH"),
              ("SRVBF", "kd_vbf_hl", "WH", "H0L1"),
              ("SRVH",  "kd_vh_hm",  "WH", "H0M"),
              ("SRVH",  "kd_vh_hp",  "WH", "H0PH"),
              ("SRVH",  "kd_vh_hl",  "WH", "H0L1"),            
]

ZHConfig = [  ("SRVBF", "kd_vbf_hm", "ZH", "H0M"),
              ("SRVBF", "kd_vbf_hp", "ZH", "H0PH"),
              ("SRVBF", "kd_vbf_hl", "ZH", "H0L1"),
              ("SRVH",  "kd_vh_hm",  "ZH", "H0M"),
              ("SRVH",  "kd_vh_hp",  "ZH", "H0PH"),
              ("SRVH",  "kd_vh_hl",  "ZH", "H0L1"),            
]
  
SigConfig2V = VBFConfig + WHConfig + ZHConfig 

for cat, var, prod, sig in SigConfig2V :
 create2VIntTemplates(cat, var, prod, sig, "", True)
 for sys in Systematics :
  create2VIntTemplates(cat, var, prod, sig, "_"+sys+"Up", False)
  create2VIntTemplates(cat, var, prod, sig, "_"+sys+"Down", False)



ggHConfig = [ ("SRVBF", "kd_vbf_hm", "H0M"),
              ("SRVBF", "kd_vbf_hp", "H0PH"),
              ("SRVBF", "kd_vbf_hl", "H0L1"),
              ("SRVH",  "kd_vh_hm",  "H0M"),
              ("SRVH",  "kd_vh_hp",  "H0PH"),
              ("SRVH",  "kd_vh_hl",  "H0L1"),            
]

for cat, var, sig in ggHConfig :
 create1VIntTemplates(cat, var, sig, "", True)
 for sys in Systematics :
  create1VIntTemplates(cat, var, sig, "_"+sys+"Up", False)
  create1VIntTemplates(cat, var, sig, "_"+sys+"Down", False)

