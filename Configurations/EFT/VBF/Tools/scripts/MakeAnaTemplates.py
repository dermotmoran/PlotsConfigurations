
import sys
import ROOT 
import numpy as np
import shutil
import math
import os

from NegList import XHNegList, ggHNegList

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)

Verbose = False

############# Couplings of mixed HWW (g)

cons = {"VBF_H0M" : 0.29797901870, "VBF_H0PH" : 0.27196538, "VBF_H0L1" : -2158.21307286, "VBF_H0LZg" : -4091.051456694223,
        "WH_H0M"  : 0.1236136,     "WH_H0PH"  : 0.0998956,  "WH_H0L1"  : -525.274,      
        "ZH_H0M"  : 0.144057,      "ZH_H0PH"  : 0.112481,   "ZH_H0L1"  : -517.788,       "ZH_H0LZg"  : -642.9534550379002,
        "H0M"     : 1.76132,       "H0PH"     : 1.133582,   "H0L1"     : -13752.22,
        "EFTH0M"  : 1.76132,       "EFTH0PH"  : 1.133582,   "EFTH0L1"  : -13752.22,
        "ggHjj_H0M" : 1.0062 
       }

########## Split Scalings such that templates have a significant normalisation for combine 

cons_sc = {"H0M" : 10, "H0PH" : 10, "H0L1" : -10000, "H0LZg" : -10000, "EFTH0M" : 10, "EFTH0PH" : 10, "EFTH0L1" : -10000}

cons_zz = {"H0M" : .255052, "H0PH" : .165684, "H0L1" : 1.2100, "H0LZg" : 0.7613,  "ggHjj_H0M" : .10062,  
           "EFTH0M" : .255052, "EFTH0PH" : 0.039446, "EFTH0L1" : 0.4363}
 
############### Matrix of couplings for H(g1, gi) hypotheses - Ewk H (2 Vertices)

Gai = np.array(([1**4,0,0,0,0],  
                [0,0,0,0,1**4],  
                [1,.25,.25**2,.25**3,.25**4],  
                [1,.5,  .5**2, .5**3, .5**4],             
                [1,.75,.75**2,.75**3,.75**4]  )) 

l1s = -10000
Gl1 = np.array(([1**4,0,0,0,0],  # SM
                [0,0,0,0,(1*l1s)**4], # M0  
                [1,.25*l1s,(.25*l1s)**2,(.25*l1s)**3,(.25*l1s)**4], # M1  
                [1,.5*l1s, ( .5*l1s)**2,( .5*l1s)**3,( .5*l1s)**4], # M2            
                [1,.75*l1s,(.75*l1s)**2,(.75*l1s)**3,(.75*l1s)**4]  ))  # M3

Gl1Zg = np.array(([1**4,0,0], # SM  
                  [1,.25*l1s,(.25*l1s)**2], # M1 
                  [1,.75*l1s,(.75*l1s)**2] )) # M3

###### test params #####

MuSc  = 1.0
Scan = [-1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] 

######## Template forced positive for combine ################

print "- For each analysis channel we should check which templates are negative"
print "- They are added to lists (NegList.py) and forced positive -- Must be taken into account in Signal Model! "

###################################################################

src = "rootFileJJH/plots_JJH.root"
dst = "rootFileJJH/plots_JJH_AC.root"

#DM In the following logic htt is assumed to be suppressed - not treated as AC signal

othertemp_hvv = ['DATA','WW','WWewk','ggWW','top','DY','Dyemb','Vg','VgS_L','VgS_H','VZ','VVV','Fake_em','Fake_me','ggH_htt','qqH_htt','ZH_htt','WH_htt'] 

othertemp_hlzg = ['DATA','WW','WWewk','ggWW','top','DY','Dyemb','Vg','VgS_L','VgS_H','VZ','VVV','Fake_em','Fake_me','ggH_htt','qqH_htt','ZH_htt','WH_htt','WH_hww','ggH_hww'] #DM Should I use AC samples here for gghww and whww?

othertemp_hgg = ['DATA','WW','WWewk','ggWW','top','DY','Dyemb','Vg','VgS_L','VgS_H','VZ','VVV','Fake_em','Fake_me','ggH_htt','qqH_htt','ZH_htt','WH_htt','qqH_hww','WH_hww','ZH_hww']

if os.path.exists(dst):
    os.remove(dst)

print "- For Ewk HVV (2V) need templates : T1 -(4,0), T2 -(3,1), T3 -(2,2), T4 -(1,3), T5 -(0,4)" 
print "Get from SM-BSM mixture hypotheses : SM(1,0), M0(0,1), M1(1,.25), M2(1,.5), M3(1,.75) "
print "and G matrices Gai, Gl1, Gl1Zg"
print "- Will create new file : "+dst+" with HVV analysis templates"
print " " 
print "- For ggF HVV (1V) need templates T1 -(2,0), T2 -(1,1), T3 -(0,2)" 
print "Get from SM-BSM MC : SM(1,0), BSM(0,1), M1(1,gMix) "
print "- Will create new file : "+dst+" with HVV analysis templates"
print " "
print "- For ggH+2Jet HGG (1V) need templates T1 -(2,0), T2 -(1,1), T3 -(0,2)" 
print "Get from SM-BSM MC : SM(1,0), BSM(0,1), M1(1,gMix) "
print "- Will create new file : "+dst+" with HGG analysis templates"
print " "


###################################################

def AddOtherTemplates(Cat, Var, Prod, AC):

 if Verbose is True :  
  print " " 
  print " ", Cat, Var
  print " " 

 if Prod is "ggHjj_" :
  vertex = "HGG"
  othertemp = othertemp_hgg
 else :
  vertex = "HVV"
  othertemp = othertemp_hvv

 if AC is "H0LZg" : othertemp = othertemp_hlzg

 f = ROOT.TFile.Open(''+src+'', 'read')

 HistList = ROOT.TObjArray()
 HistNameList = []

 f.cd("hww2l2v_13TeV_"+Cat+"/"+Var+"/")
 d = ROOT.gDirectory
 for ih in d.GetListOfKeys():
    h = ih.ReadObj()
    if any(x in h.GetName() for x in othertemp) :

     QCDVar = False
     Sys    = False
     if "Up" in h.GetName() or "Down" in h.GetName(): Sys = True
     if Sys is False and "QCDscale" in h.GetName():  QCDVar = True

     if QCDVar is False and h.GetName() not in HistNameList :
      h.SetDirectory(0)
      if h.Integral() < 0 : #DM combine wont take negative pdfs (OK for jjH ana but should implement better fix for this!!)
       h.Scale(0)
       if Verbose is True : print "Setting to 0 : ", h.GetName(), Cat, Var 
      if AC is "H0LZg" :  #DM Set names such that templates are scaled by Mu*Fa1 in signal model
       if "WH_hww" in h.GetName() : 
        name = h.GetName() 
        name = name.replace("WH_hww","WH_T1")
        h.SetName(name)
       if "ggH_hww" in h.GetName() :
        name = h.GetName() 
        name = name.replace("ggH_hww","ggH_T1")
        h.SetName(name)
      HistList.Add(h)
      HistNameList.append(h.GetName())

 f.Close()

 fout = ROOT.TFile.Open(''+dst+'', 'update')
 fout.cd("hww2l2v_13TeV_"+Cat+"/"+vertex+"_"+AC+"/") 

 HistList.Write()

 if Verbose is True :  
  d = ROOT.gDirectory
  for ih in d.GetListOfKeys():
    h = ih.ReadObj()
    if "Up" not in h.GetName() and "Down" not in h.GetName() : 
     print h.GetName(), h.Integral()

 fout.Close()

############################################

def getSumOfRWHVVSamples(f, BaseN, Hyp, Sys): 

 if Hyp == "H0PM" : H1 = f.Get(''+BaseN+'H0PM'+Sys+'') 
 else             : H1 = f.Get(''+BaseN+'H0PM_'+Hyp+Sys+'') 
 if Hyp == "H0M" :  H2 = f.Get(''+BaseN+'H0M'+Sys+'') 
 else            :  H2 = f.Get(''+BaseN+'H0M_'+Hyp+Sys+'')
 if Hyp == "H0PH" : H3 = f.Get(''+BaseN+'H0PH'+Sys+'')
 else             : H3 = f.Get(''+BaseN+'H0PH_'+Hyp+Sys+'')
 if Hyp == "H0L1" : H4 = f.Get(''+BaseN+'H0L1'+Sys+'') 
 else             : H4 = f.Get(''+BaseN+'H0L1_'+Hyp+Sys+'') 
 if Hyp == "H0Mf05" :  H5 = f.Get(''+BaseN+'H0Mf05'+Sys+'') 
 else               :  H5 = f.Get(''+BaseN+'H0Mf05_'+Hyp+Sys+'') 
 if Hyp == "H0PHf05" : H6 = f.Get(''+BaseN+'H0PHf05'+Sys+'')
 else                : H6 = f.Get(''+BaseN+'H0PHf05_'+Hyp+Sys+'')
 if Hyp == "H0L1f05" : H7 = f.Get(''+BaseN+'H0L1f05'+Sys+'')
 else                : H7 = f.Get(''+BaseN+'H0L1f05_'+Hyp+Sys+'')

 H1.SetDirectory(0)
 H2.SetDirectory(0)
 H3.SetDirectory(0)
 H4.SetDirectory(0)
 H5.SetDirectory(0)
 H6.SetDirectory(0)
 H7.SetDirectory(0)

 Sum = H1.Clone()
 Sum.SetDirectory(0)

 H1.SetBit(ROOT.TH1.kIsAverage)
 H2.SetBit(ROOT.TH1.kIsAverage)
 H3.SetBit(ROOT.TH1.kIsAverage)
 H4.SetBit(ROOT.TH1.kIsAverage)
 H5.SetBit(ROOT.TH1.kIsAverage)
 H6.SetBit(ROOT.TH1.kIsAverage)
 H7.SetBit(ROOT.TH1.kIsAverage)
 
 H1.Add(H2,1)
 H1.Add(H3,1)
 H1.Add(H4,1)
 H1.Add(H5,1)
 H1.Add(H6,1)
 H1.Add(H7,1)

 for i in range(1, H1.GetXaxis().GetNbins()+1):
   n = H1.GetBinContent(i)
   e = H1.GetBinError(i)
   Sum.SetBinContent(i, n)
   Sum.SetBinError(i, e)

 return Sum

def getSumOfRWHGGSamples(f, BaseN, Hyp, Sys): 

 if Hyp == "H0PM" : H1 = f.Get(''+BaseN+'H0PM'+Sys+'') 
 else             : H1 = f.Get(''+BaseN+'H0PM_'+Hyp+Sys+'') 
 if Hyp == "H0M" :  H2 = f.Get(''+BaseN+'H0M'+Sys+'') 
 else            :  H2 = f.Get(''+BaseN+'H0M_'+Hyp+Sys+'')
 if Hyp == "H0Mf05" :  H3 = f.Get(''+BaseN+'H0Mf05'+Sys+'') 
 else               :  H3 = f.Get(''+BaseN+'H0Mf05_'+Hyp+Sys+'') 

 H1.SetDirectory(0)
 H2.SetDirectory(0)
 H3.SetDirectory(0)

 Sum = H1.Clone()
 Sum.SetDirectory(0)

 H1.SetBit(ROOT.TH1.kIsAverage)
 H2.SetBit(ROOT.TH1.kIsAverage)
 H3.SetBit(ROOT.TH1.kIsAverage)
 
 H1.Add(H2,1)
 H1.Add(H3,1)

 for i in range(1, H1.GetXaxis().GetNbins()+1):
   n = H1.GetBinContent(i)
   e = H1.GetBinError(i)
   Sum.SetBinContent(i, n)
   Sum.SetBinError(i, e)

 return Sum

#########################################################

def checkForBadSys(Cat, Var, Prod, AC, Sys, Temp):

 if Prod is "ggHjj_" : vertex = "HGG"
 else :                vertex = "HVV"

 fout = ROOT.TFile.Open(''+dst+'', 'update')

 Nom = fout.Get("hww2l2v_13TeV_"+Cat+"/"+vertex+"_"+AC+"/histo_"+Prod+Temp+"")
 Up = fout.Get("hww2l2v_13TeV_"+Cat+"/"+vertex+"_"+AC+"/histo_"+Prod+Temp+Sys+"Up") 
 Dn = fout.Get("hww2l2v_13TeV_"+Cat+"/"+vertex+"_"+AC+"/histo_"+Prod+Temp+Sys+"Down")

 Err = ROOT.Double(0.)
 N = Nom.IntegralAndError(0,Nom.GetNbinsX(),Err)
 U = Up.Integral()
 D = Dn.Integral()

 fout.cd("hww2l2v_13TeV_"+Cat+"/"+vertex+"_"+AC+"/") 

 if N == 0 :
  Up.Scale(0)
  Dn.Scale(0)
  Up.SetName("histo_"+Prod+Temp+Sys+"Up")
  Dn.SetName("histo_"+Prod+Temp+Sys+"Down")
  Up.Write("",ROOT.TObject.kOverwrite)
  Dn.Write("",ROOT.TObject.kOverwrite)
  
 else : # Assuming then that N is positive (Should be the case!)

  BadShapeSys = False
  if U<0 or D<0 or (U<N and D<N) or (U>N and D>N) : BadShapeSys = True 
  if Err/N > 1.0 : BadShapeSys = True 

  if BadShapeSys is True : # Treat as symmetric norm uncertainty (Assuming MC stat uncertinty is too big to treat this as shape sys)

    Up = Nom.Clone() 
    Dn = Nom.Clone()
    NErr = max(abs(D-N),abs(U-N))
    Up.Scale((N+NErr)/N)
    if(N-NErr)>0: Dn.Scale((N-NErr)/N)
    else        : Dn.Scale(0.0001)
    Up.SetName("histo_"+Prod+Temp+Sys+"Up")
    Dn.SetName("histo_"+Prod+Temp+Sys+"Down")
    Up.Write("",ROOT.TObject.kOverwrite)
    Dn.Write("",ROOT.TObject.kOverwrite)

 fout.Close()
    

#########################################################

def create2VIntTemplates(Cat, Var, Prod, AC, Sys, Test):

 if Verbose is True :  
  print " " 
  print " ", Cat, Var, Prod, AC, Sys, Test
  print " " 

 f = ROOT.TFile.Open(''+src+'', 'read')
 BaseN = "hww2l2v_13TeV_"+Cat+"/"+Var+"/histo_"+Prod+""

 MCForThisAC = True
 if "H0LZg" in AC or "EFT" in AC : MCForThisAC = False

 SM = getSumOfRWHVVSamples(f, BaseN, "H0PM",  Sys)
 M0 = getSumOfRWHVVSamples(f, BaseN, AC+"_M0",Sys)
 M1 = getSumOfRWHVVSamples(f, BaseN, AC+"_M1",Sys)
 M2 = getSumOfRWHVVSamples(f, BaseN, AC+"_M2",Sys)
 M3 = getSumOfRWHVVSamples(f, BaseN, AC+"_M3",Sys)
 
 if MCForThisAC is True :
  SM_Org  = f.Get(''+BaseN+'H0PM'+Sys+'')
  BSM_Org = f.Get(''+BaseN+AC+Sys+'')
  f05_Org = f.Get(''+BaseN+AC+'f05'+Sys+'')
  SM_Org.SetDirectory(0)
  BSM_Org.SetDirectory(0)
  f05_Org.SetDirectory(0)
  SM_Org.SetLineColor(ROOT.kBlack)
  BSM_Org.SetLineColor(ROOT.kBlack) 
  f05_Org.SetLineColor(ROOT.kBlack) 
  SM_Org.SetLineWidth(2)
  BSM_Org.SetLineWidth(2)
  f05_Org.SetLineWidth(2)

 f.Close()

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

 if AC is "H0LZg" :
 
  InvG = np.linalg.inv(Gl1Zg)

  T1.Scale( InvG[0][0])
  T1.Add(M1,InvG[0][1])
  T1.Add(M3,InvG[0][2])

  T2.Scale( InvG[1][0])
  T2.Add(M1,InvG[1][1])
  T2.Add(M3,InvG[1][2])

  T3.Scale( InvG[2][0])
  T3.Add(M1,InvG[2][1])
  T3.Add(M3,InvG[2][2])

  T4.Scale(0)
  T5.Scale(0)

 else :

  InvG = np.linalg.inv(Gai)
  if "H0L1" in AC  : InvG = np.linalg.inv(Gl1)

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
 
 ####################################
 
 if Test == True :

  T1.SetLineColor(ROOT.kRed)
  T2.SetLineColor(ROOT.kOrange)
  T3.SetLineColor(ROOT.kCyan)
  T4.SetLineColor(ROOT.kBlue)
  T5.SetLineColor(ROOT.kGreen)
  T1.SetFillColor(ROOT.kRed)
  T2.SetFillColor(ROOT.kOrange)
  T3.SetFillColor(ROOT.kCyan)
  T4.SetFillColor(ROOT.kBlue)
  T5.SetFillColor(ROOT.kGreen)
  T1.SetLineWidth(2)
  T2.SetLineWidth(2)
  T3.SetLineWidth(2)
  T4.SetLineWidth(2)
  T5.SetLineWidth(2)

  if MCForThisAC is True :

   G = cons[Prod+AC]
   f05T = T1.Clone()
   f05T.SetDirectory(0)
   f05T.Add(T2, G)
   f05T.Add(T3, G**2)
   f05T.Add(T4, G**3)
   f05T.Add(T5, G**4)
   f05T.SetLineColor(ROOT.kRed)
   f05T.SetFillColor(ROOT.kRed)

   canvasf05 = ROOT.TCanvas('canvasf05', '', 500, 500)
   f05T.SetMinimum(0.001)
   f05T.SetMaximum(1.5*f05T.GetMaximum())
   f05T.GetXaxis().SetTitle(""+Var+"")
   f05T.Draw("hist")
   f05_Org.Draw("same e")
   legend = ROOT.TLegend(0.3,0.75,0.7,0.9)
   legend.AddEntry(f05_Org,"SM-BSM Mix MC ","l")
   legend.AddEntry(f05T,"T1-T5 combination","f")
   legend.Draw()
   canvasf05.SaveAs("plotJJH/Temps/f05_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")
   canvasf05.SaveAs("plotJJH/Temps/f05_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

  canvasInitial = ROOT.TCanvas('canvasInitial', '', 500, 500)
  canvasInitial.Divide(3,2)
    
  canvasInitial.cd(1)
  T1.SetMaximum(1.5*T1.GetMaximum())
  T1.Draw("hist")
  if MCForThisAC is True : SM_Org.Draw("same e")
  canvasInitial.cd(2)
  T2.Draw("hist")
  canvasInitial.cd(3)
  T3.Draw("hist")
  canvasInitial.cd(4)
  T4.Draw("hist")
  canvasInitial.cd(5)
  T5.SetMaximum(1.5*T5.GetMaximum())
  T5.Draw("hist")
  if MCForThisAC is True : BSM_Org.Draw("same e")
  canvasInitial.cd(6)

  legend = ROOT.TLegend(0.2,0.2,1.0,1.0)
  legend.AddEntry(T1,"T1","f")
  legend.AddEntry(T2,"T2","f")
  legend.AddEntry(T3,"T3","f")
  legend.AddEntry(T4,"T4","f")
  legend.AddEntry(T5,"T5","f")
  legend.Draw()

  canvasInitial.SaveAs("plotJJH/Temps/InitialT_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")
  canvasInitial.SaveAs("plotJJH/Temps/InitialT_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

 ######### Template tricks for combine #######

 Gsc = cons_sc[AC] 

 T2.Scale(Gsc) 
 T3.Scale(Gsc**2) 
 T4.Scale(Gsc**3) 
 T5.Scale(Gsc**4)

 NegList = XHNegList[AC]

 for c, s, p, t in NegList :
  if (c in Cat or c is "all") and p is Prod and s is AC :
   if Verbose is True : print "--------- Force Template positive (Compensate in model!)", c, s, p, t
   if   t is "T2" :  T2.Scale(-1)  
   elif t is "T3" :  T3.Scale(-1)  
   elif t is "T4" :  T4.Scale(-1)  

 ## Test for negative interference terms

 if Sys is "" : 
  if T2.Integral() < 0 : print ""+Sys+" (\""+Cat+"\",\""+AC+"\",\""+Prod+"\",\"T2\"),"
  if T3.Integral() < 0 : print ""+Sys+" (\""+Cat+"\",\""+AC+"\",\""+Prod+"\",\"T3\"),"
  if T4.Integral() < 0 : print ""+Sys+" (\""+Cat+"\",\""+AC+"\",\""+Prod+"\",\"T4\"),"

 if Test == True :

  gr = ROOT.TGraph(len(Scan))
  gr.SetLineColor(ROOT.kRed)
  gr.SetLineWidth(2)

  ScanH = []

  for i in range(len(Scan)): 

   FaiSc = Scan[i]
   Fa1Sc = 1-abs(FaiSc)
   GSc   = cons_zz[AC] 

   N1Sc = MuSc**2*Fa1Sc**2    
   N2Sc = MuSc**2*np.sign(FaiSc)*math.sqrt(abs(FaiSc))*(math.sqrt(Fa1Sc)**3)*GSc
   N3Sc = MuSc**2*abs(FaiSc)*Fa1Sc*(GSc**2)
   N4Sc = MuSc**2*np.sign(FaiSc)*(math.sqrt(abs(FaiSc))**3)*math.sqrt(Fa1Sc)*(GSc**3)
   N5Sc = MuSc**2*FaiSc**2*(GSc**4)

   for c, s, p, t in NegList :
    if (c in Cat or c is "all") and p is Prod and s is AC :
     if   t is "T2" :  N2Sc = N2Sc*-1 
     elif t is "T3" :  N3Sc = N3Sc*-1 
     elif t is "T4" :  N4Sc = N4Sc*-1 
          
   f05TSc = T1.Clone()
   f05TSc.SetDirectory(0)
   f05TSc.Scale(  N1Sc)
   f05TSc.Add(T2, N2Sc)
   f05TSc.Add(T3, N3Sc)
   f05TSc.Add(T4, N4Sc)
   f05TSc.Add(T5, N5Sc)
  
   ScanH.append(f05TSc)

   gr.SetPoint(i, Scan[i], f05TSc.Integral())

  canvasFinal = ROOT.TCanvas('canvasFinal', '', 500, 500)
  canvasFinal.Divide(3,2)    
  canvasFinal.cd(1)
  T1.Draw("hist")
  canvasFinal.cd(2)
  T2.Draw("hist")
  canvasFinal.cd(3)
  T3.Draw("hist")
  canvasFinal.cd(4)
  T4.Draw("hist")
  canvasFinal.cd(5)
  T5.Draw("hist")
  canvasFinal.cd(6)
  legend = ROOT.TLegend(0.2,0.2,1.0,1.0)
  legend.AddEntry(T1,"T1","f")
  legend.AddEntry(T2,"T2","f")
  legend.AddEntry(T3,"T3","f")
  legend.AddEntry(T4,"T4","f")
  legend.AddEntry(T5,"T5","f")
  legend.Draw()
  canvasFinal.SaveAs("plotJJH/Temps/FinalT_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")
  canvasFinal.SaveAs("plotJJH/Temps/FinalT_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

  canvasScan = ROOT.TCanvas('canvasScan', '', 500, 500)
  gr.Draw("ALP")
  canvasScan.SaveAs("plotJJH/Temps/FinalS_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")
  canvasScan.SaveAs("plotJJH/Temps/FinalS_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

  canvasScanSh = ROOT.TCanvas('canvasScanSh', '', 500, 500)
  canvasScanSh.Divide(2,1)
  canvasScanSh.cd(1)

  PlotSc = [0,0.1,0.2,0.5,0.7,1]
  Count = 0 
  canvasScanSh.cd(1)
  for i in range(len(PlotSc)):
   for j in range(len(Scan)):
    if -1*PlotSc[i] == Scan[j]:
     h = ScanH[j]
     if h.Integral() != 0 : h.Scale(1.0/h.Integral())
     h.SetLineColor(Count+1)
     h.SetMaximum(1.0)
     if Count is 0 : h.Draw("hist")
     else          : h.Draw("same hist")
     Count = Count+1

  legend = ROOT.TLegend(0.3,0.5,0.7,0.9)
  Count = 0 
  canvasScanSh.cd(2)
  for i in range(len(PlotSc)):
   for j in range(len(Scan)):
    if PlotSc[i] == Scan[j]:
     h = ScanH[j]
     if h.Integral() != 0 : h.Scale(1.0/h.Integral())
     h.SetLineColor(Count+1)
     h.SetMaximum(1.0)
     legend.AddEntry(h,""+str(PlotSc[i]),"l")
     if Count is 0 : h.Draw("hist")
     else          : h.Draw("same hist")
     Count = Count+1
  legend.Draw()

  canvasScanSh.SaveAs("plotJJH/Temps/FinalSH_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")
  canvasScanSh.SaveAs("plotJJH/Temps/FinalSH_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

 fout = ROOT.TFile.Open(''+dst+'', 'update')
 ROOT.gDirectory.mkdir("hww2l2v_13TeV_"+Cat+"/HVV_"+AC+"/")
 fout.cd("hww2l2v_13TeV_"+Cat+"/HVV_"+AC+"/")

 T1.SetName("histo_"+Prod+"T1"+Sys+"") 
 T2.SetName("histo_"+Prod+"T2"+Sys+"")
 T3.SetName("histo_"+Prod+"T3"+Sys+"")
 T4.SetName("histo_"+Prod+"T4"+Sys+"")
 T5.SetName("histo_"+Prod+"T5"+Sys+"")

 T1.Write()
 T2.Write()
 T3.Write()
 T4.Write()
 T5.Write()

 fout.Close()

##########################################################

def create1VIntTemplates(Cat, Var, Prod, AC, Sys, Test): 

 if Verbose is True : 
  print " " 
  print " ", Cat, Var, Prod, AC, Sys, Test
  print " " 

 f = ROOT.TFile.Open(''+src+'', 'read')

 MCForThisAC = True
 if "EFT" in AC : MCForThisAC = False

 if Prod is "ggHjj_" :
  vertex = "HGG"
  BaseN = "hww2l2v_13TeV_"+Cat+"/"+Var+"/histo_GGHjj_"
  SM  = getSumOfRWHGGSamples(f, BaseN, "H0PM",  Sys)
  BSM = getSumOfRWHGGSamples(f, BaseN, AC,      Sys)
  f05 = getSumOfRWHGGSamples(f, BaseN, AC+"f05",Sys)
 else :
  vertex = "HVV"
  BaseN = "hww2l2v_13TeV_"+Cat+"/"+Var+"/histo_"
  SM  = getSumOfRWHVVSamples(f, BaseN, "H0PM",  Sys)
  BSM = getSumOfRWHVVSamples(f, BaseN, AC,      Sys)
  f05 = getSumOfRWHVVSamples(f, BaseN, AC+"f05",Sys)
            
 if MCForThisAC is True :
  SM_Org  = f.Get(''+BaseN+'H0PM'+Sys+'')
  BSM_Org = f.Get(''+BaseN+AC+Sys+'')
  f05_Org = f.Get(''+BaseN+AC+'f05'+Sys+'')
  SM_Org.SetDirectory(0)
  BSM_Org.SetDirectory(0)
  f05_Org.SetDirectory(0)
  SM_Org.SetLineColor(ROOT.kBlack)
  BSM_Org.SetLineColor(ROOT.kBlack) 
  f05_Org.SetLineColor(ROOT.kBlack) 
  SM_Org.SetLineWidth(2)
  BSM_Org.SetLineWidth(2)
  f05_Org.SetLineWidth(2)

 f.Close()

 if Prod is "ggHjj_": G = cons[Prod+AC]
 else :               G = cons[AC]

 T1 = SM.Clone()  # 2,0
 T2 = SM.Clone()  # 1,1
 T3 = BSM.Clone() # 0,2

 T1.SetDirectory(0)
 T2.SetDirectory(0)
 T3.SetDirectory(0)

 T2.Scale(-1/G)
 T2.Add(BSM, -G)
 T2.Add(f05, 1/G)
 
 if Test == True :

  T1.SetLineColor(ROOT.kRed)
  T1.SetFillColor(ROOT.kRed)
  T2.SetLineColor(ROOT.kBlue)
  T2.SetFillColor(ROOT.kBlue)
  T3.SetLineColor(ROOT.kGreen)
  T3.SetFillColor(ROOT.kGreen)
  T1.SetLineWidth(3)
  T2.SetLineWidth(3)
  T3.SetLineWidth(3)

  if MCForThisAC is True :

   f05T = T1.Clone()
   f05T.SetDirectory(0)
   f05T.Add(T2, G)
   f05T.Add(T3, G**2)
   f05T.SetLineColor(ROOT.kRed)
   f05T.SetFillColor(ROOT.kRed)
   f05T.SetLineWidth(2)

   canvasf05 = ROOT.TCanvas('canvasf05', '', 500, 500)
   f05T.SetMinimum(0.001)
   f05T.SetMaximum(1.5*f05T.GetMaximum())
   f05T.GetXaxis().SetTitle(""+Var+"")
   f05T.Draw("hist")
   f05_Org.Draw("same e")
   legend = ROOT.TLegend(0.3,0.75,0.7,0.9)
   legend.AddEntry(f05_Org,"SM-BSM Mix MC ","l")
   legend.AddEntry(f05T,"T1-T3 combination","f")
   legend.Draw()
   canvasf05.SaveAs("plotJJH/Temps/f05_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")
   canvasf05.SaveAs("plotJJH/Temps/f05_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

  canvasInitial = ROOT.TCanvas('canvasInitial', '', 500, 500)
  canvasInitial.Divide(2,2)
  canvasInitial.cd(1)
  T1.SetMaximum(1.5*T1.GetMaximum())
  T1.Draw("hist")
  if MCForThisAC is True : SM_Org.Draw("same e")
  canvasInitial.cd(2)
  T2.Draw("hist")
  canvasInitial.cd(3)
  T3.SetMaximum(1.5*T3.GetMaximum())
  T3.Draw("hist")
  if MCForThisAC is True : BSM_Org.Draw("same e")
  canvasInitial.cd(4)
  legend = ROOT.TLegend(0.2,0.2,1.0,1.0)
  legend.AddEntry(T1,"T1","f")
  legend.AddEntry(T2,"T2","f")
  legend.AddEntry(T3,"T3","f")
  legend.Draw() 
  canvasInitial.SaveAs("plotJJH/Temps/InitialT_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf") 
  canvasInitial.SaveAs("plotJJH/Temps/InitialT_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

 ######### Template tricks for combine #######

 Gsc = cons_sc[AC]

 T2.Scale(Gsc) 
 T3.Scale(Gsc**2) 

 for c, s, p, t in ggHNegList :
  if (c in Cat or c is "all") and p is Prod and s is AC :
   if Verbose is True : print "--------- Force Template positive (Compensate in model!) ", c, s, p, t
   if t is "T2" :  T2.Scale(-1)  

 if Prod is not "ggHjj_" and AC is "H0M" :  T2.Scale(0) #DM 

 ## Test for negative interference terms 

 if Sys is "" : 
  if T2.Integral() < 0 : print ""+Sys+" (\""+Cat+"\",\""+AC+"\",\""+Prod+"\",\"T2\"),"

 if Test == True :

  gr = ROOT.TGraph(len(Scan))
  gr.SetLineColor(ROOT.kRed)
  gr.SetLineWidth(2)

  for i in range(len(Scan)): 

   FaiSc = Scan[i]
   Fa1Sc = 1-abs(FaiSc)

   if Prod is "ggHjj_": GSc = cons_zz[Prod+AC] 
   else :               GSc = cons_zz[AC]

   N1Sc = MuSc*Fa1Sc                       
   N2Sc = MuSc*np.sign(FaiSc)*math.sqrt(abs(FaiSc)*Fa1Sc)*GSc
   N3Sc = MuSc*abs(FaiSc)*(GSc**2)

   for c, s, p, t in ggHNegList :
    if (c in Cat or c is "all") and p is Prod and s is AC :
     if   t is "T2" :  N2Sc = N2Sc*-1 
          
   f05TSc = T1.Clone()
   f05TSc.SetDirectory(0)
   f05TSc.Scale(  N1Sc)
   f05TSc.Add(T2, N2Sc)
   f05TSc.Add(T3, N3Sc)
  
   gr.SetPoint(i, Scan[i], f05TSc.Integral())

  canvasFinal = ROOT.TCanvas('canvasFinal', '', 500, 500)
  canvasFinal.Divide(2,2)
  canvasFinal.cd(1)
  T1.Draw("hist")
  canvasFinal.cd(2)
  T2.Draw("hist")
  canvasFinal.cd(3)
  T3.Draw("hist")
  canvasFinal.cd(4)
  legend = ROOT.TLegend(0.2,0.2,1.0,1.0)
  legend.AddEntry(T1,"T1","f")
  legend.AddEntry(T2,"T2","f")
  legend.AddEntry(T3,"T3","f")
  legend.Draw() 
  canvasFinal.SaveAs("plotJJH/Temps/FinalT_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf") 
  canvasFinal.SaveAs("plotJJH/Temps/FinalT_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

  canvasScan = ROOT.TCanvas('canvasScan', '', 500, 500)
  gr.Draw("ALP")
  canvasScan.SaveAs("plotJJH/Temps/FinalS_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".pdf")
  canvasScan.SaveAs("plotJJH/Temps/FinalS_"+Cat+"_"+Var+"_"+Prod+AC+Sys+".png")

 fout = ROOT.TFile.Open(''+dst+'', 'update')
 ROOT.gDirectory.mkdir("hww2l2v_13TeV_"+Cat+"/"+vertex+"_"+AC+"/")
 fout.cd("hww2l2v_13TeV_"+Cat+"/"+vertex+"_"+AC+"/")

 T1.SetName("histo_"+Prod+"T1"+Sys+"") 
 T2.SetName("histo_"+Prod+"T2"+Sys+"")
 T3.SetName("histo_"+Prod+"T3"+Sys+"")

 T1.Write() 
 T2.Write()
 T3.Write()

 fout.Close()

################### AC Signal Shape Sys #######################################

DoSys=False
DoTest=True
AddOtherTemps=False

Yr="_2016"

Sys = [ "CMS_scale_e"+Yr, "CMS_scale_m"+Yr, "CMS_eff_m"+Yr, "CMS_eff_e"+Yr, 
"CMS_scale_JESHF"+Yr, "CMS_scale_JESBBEC1","CMS_scale_JESRelativeSample"+Yr, "CMS_scale_JESEC2","CMS_scale_JESFlavorQCD","CMS_scale_JESBBEC1"+Yr,"CMS_scale_JESAbsolute", "CMS_scale_JESHF","CMS_scale_JESEC2"+Yr,"CMS_scale_JESAbsolute"+Yr,"CMS_scale_JESRelativeBal",
"CMS_btag_jes","CMS_btag_lf","CMS_btag_lfstats1"+Yr, "CMS_btag_lfstats2"+Yr,"CMS_btag_hfstats1"+Yr, "CMS_btag_hfstats2"+Yr,"CMS_btag_cferr1","CMS_btag_cferr2",
"CMS_PUID"+Yr,"CMS_scale_met"+Yr,
"CMS_eff_prefiring"+Yr,"CMS_eff_hwwtrigger"+Yr,
"PS_ISR", "PS_FSR" ] 

Sys_ggh = [ "THU_ggH_Mu","THU_ggH_Res","THU_ggH_Mig01","THU_ggH_Mig12", "THU_ggH_VBF2j","THU_ggH_VBF3j", "THU_ggH_PT60", "THU_ggH_PT120", "THU_ggH_qmtop","CMS_PU"+Yr ]

Sys_VBF = [ "THU_qqH_YIELD","THU_qqH_PTH200","THU_qqH_Mjj60","THU_qqH_Mjj120","THU_qqH_Mjj350","THU_qqH_Mjj700","THU_qqH_Mjj1000","THU_qqH_Mjj1500","THU_qqH_PTH25","THU_qqH_JET01","THU_qqH_EWK","CMS_PU"+Yr ] 

####################################################################################

####### HVV setup  ######

XHProd = ["VBF_","ZH_","WH_"]

ACConfig  = [ ("of2j_vbf_hmip", "kd3d_vbf_hm", "H0M"),
              ("of2j_vbf_hmin", "kd3d_vbf_hm", "H0M"),
              ("of2j_vh_hmip",  "kd2d_vh_hm",  "H0M"),
              ("of2j_vh_hmin",  "kd2d_vh_hm",  "H0M"),
              ("top_of2j",      "events",      "H0M"),
              ("dytt_of2j",     "events",      "H0M"),
              ("of2j_vbf_hpip", "kd3d_vbf_hp", "H0PH"),
              ("of2j_vbf_hpin", "kd3d_vbf_hp", "H0PH"),
              ("of2j_vh_hpip",  "kd2d_vh_hp",  "H0PH"),
              ("of2j_vh_hpin",  "kd2d_vh_hp",  "H0PH"),
              ("top_of2j",      "events",      "H0PH"),
              ("dytt_of2j",     "events",      "H0PH"),
              ("of2j_vbf",      "kd3d_vbf_hl", "H0L1"),
              ("of2j_vh",       "kd2d_vh_hl",  "H0L1"), 
              ("top_of2j",      "events",      "H0L1"),
              ("dytt_of2j",     "events",      "H0L1"),  
]

LZGConfig = [ ("of2j_vbf",  "kd3d_vbf_hlzg","H0LZg"),
              ("of2j_vh",   "kd2d_vh_hlzg", "H0LZg"),
              ("top_of2j",  "events",       "H0LZg"),
              ("dytt_of2j", "events",       "H0LZg"),
]

EFTConfig = [ ("of2j_vbf_hmip", "kd3d_vbf_hm", "EFTH0M"),
              ("of2j_vbf_hmin", "kd3d_vbf_hm", "EFTH0M"),
              ("of2j_vh_hmip",  "kd2d_vh_hm",  "EFTH0M"),
              ("of2j_vh_hmin",  "kd2d_vh_hm",  "EFTH0M"),
              ("top_of2j",      "events",      "EFTH0M"),
              ("dytt_of2j",     "events",      "EFTH0M"),
              ("of2j_vbf_hpip", "kd3d_vbf_hp", "EFTH0PH"),
              ("of2j_vbf_hpin", "kd3d_vbf_hp", "EFTH0PH"),
              ("of2j_vh_hpip",  "kd2d_vh_hp",  "EFTH0PH"),
              ("of2j_vh_hpin",  "kd2d_vh_hp",  "EFTH0PH"),
              ("top_of2j",      "events",      "EFTH0PH"),
              ("dytt_of2j",     "events",      "EFTH0PH"),
              ("of2j_vbf",      "kd3d_vbf_hl", "EFTH0L1"),
              ("of2j_vh",       "kd2d_vh_hl",  "EFTH0L1"), 
              ("top_of2j",      "events",      "EFTH0L1"),
              ("dytt_of2j",     "events",      "EFTH0L1"),  
]

for prod in XHProd :

 print "------------------------------------", prod
 if prod is "ZH_" or prod is "VBF_" : SigConfig = ACConfig + LZGConfig + EFTConfig
 else : SigConfig = ACConfig + EFTConfig

 for cat, var, sig in SigConfig :
  create2VIntTemplates(cat, var, prod, sig, "", DoTest)
  if DoSys is True :
   for sys in Sys :
    create2VIntTemplates(cat, var, prod, sig, "_"+sys+"Up", False)
    create2VIntTemplates(cat, var, prod, sig, "_"+sys+"Down", False)
    checkForBadSys(cat, var, prod, sig, "_"+sys+"","T1")
    checkForBadSys(cat, var, prod, sig, "_"+sys+"","T2")
    checkForBadSys(cat, var, prod, sig, "_"+sys+"","T3")
    checkForBadSys(cat, var, prod, sig, "_"+sys+"","T4")
    checkForBadSys(cat, var, prod, sig, "_"+sys+"","T5")
   if "VBF_" in prod :
    for sys in Sys_VBF :
     create2VIntTemplates(cat, var, prod, sig, "_"+sys+"Up", False)
     create2VIntTemplates(cat, var, prod, sig, "_"+sys+"Down", False)  
     checkForBadSys(cat, var, prod, sig, "_"+sys+"","T1")
     checkForBadSys(cat, var, prod, sig, "_"+sys+"","T2")
     checkForBadSys(cat, var, prod, sig, "_"+sys+"","T3")
     checkForBadSys(cat, var, prod, sig, "_"+sys+"","T4")
     checkForBadSys(cat, var, prod, sig, "_"+sys+"","T5")


prod = "ggH_" 
print "------------------------------------", prod
SigConfig = ACConfig + EFTConfig

for cat, var, sig in SigConfig :
 create1VIntTemplates(cat, var, prod, sig, "", DoTest)
 if DoSys is True :
  for sys in Sys :
   create1VIntTemplates(cat, var, prod, sig, "_"+sys+"Up", False)
   create1VIntTemplates(cat, var, prod, sig, "_"+sys+"Down", False) 
   checkForBadSys(cat, var, prod, sig, "_"+sys+"","T1")
   checkForBadSys(cat, var, prod, sig, "_"+sys+"","T2")
   checkForBadSys(cat, var, prod, sig, "_"+sys+"","T3")
  for sys in Sys_ggh :
   create1VIntTemplates(cat, var, prod, sig, "_"+sys+"Up", False)
   create1VIntTemplates(cat, var, prod, sig, "_"+sys+"Down", False)    
   checkForBadSys(cat, var, prod, sig, "_"+sys+"","T1")
   checkForBadSys(cat, var, prod, sig, "_"+sys+"","T2")
   checkForBadSys(cat, var, prod, sig, "_"+sys+"","T3")
 
SigConfig = ACConfig + LZGConfig + EFTConfig

if AddOtherTemps is True :
 for cat, var, sig in SigConfig :
  AddOtherTemplates(cat, var, prod, sig)

####### ggH+2Jet setup  ######

GGHJJConfig = [ ("of2j_ggh_thmip", "kd3d_ggh_hm", "H0M"),
                ("of2j_ggh_thmin", "kd3d_ggh_hm", "H0M"),
                ("of2j_ggh_lhmip", "kd2d_ggh_hm", "H0M"),
                ("of2j_ggh_lhmin", "kd2d_ggh_hm", "H0M"),
                ("top_of2j",       "events",      "H0M"),
                ("dytt_of2j",      "events",      "H0M"),
]  

prod = "ggHjj_"
print "------------------------------------", prod

for cat, var, sig in GGHJJConfig :
 create1VIntTemplates(cat, var, prod, sig, "", DoTest)
 if DoSys is True :
  for sys in Sys :
   create1VIntTemplates(cat, var, prod, sig, "_"+sys+"Up", False)
   create1VIntTemplates(cat, var, prod, sig, "_"+sys+"Down", False)  
   checkForBadSys(cat, var, prod, sig, "_"+sys+"","T1")
   checkForBadSys(cat, var, prod, sig, "_"+sys+"","T2")
   checkForBadSys(cat, var, prod, sig, "_"+sys+"","T3")
  for sys in Sys_ggh :
   create1VIntTemplates(cat, var, prod, sig, "_"+sys+"Up", False)
   create1VIntTemplates(cat, var, prod, sig, "_"+sys+"Down", False)    
   checkForBadSys(cat, var, prod, sig, "_"+sys+"","T1")
   checkForBadSys(cat, var, prod, sig, "_"+sys+"","T2")
   checkForBadSys(cat, var, prod, sig, "_"+sys+"","T3")

if AddOtherTemps is True :
 for cat, var, sig in GGHJJConfig :
  AddOtherTemplates(cat, var, prod, sig)

print "Its done!!!"
