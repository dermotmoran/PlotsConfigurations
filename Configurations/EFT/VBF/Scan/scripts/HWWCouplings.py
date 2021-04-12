from HiggsAnalysis.CombinedLimit.PhysicsModel import *
 
### This is the base python class to study the VBF HWW AC
 
class HWWCouplings(PhysicsModel):
    def __init__(self):
        self.ACF = 'NA'
        self.NegList =  [ ("all", "H0PH", "WH_", "T2"), ("all", "H0PH", "ZH_", "T2"),
            ("all", "H0L1", "WH_", "T2"), ("all", "H0L1", "ZH_", "T2"), 
            ("all", "H0L1", "WH_", "T4"), ("all", "H0L1", "ZH_", "T4"),
            ("all", "H0L1", "VBF_", "T4"),("all", "H0LZg", "VBF_", "T2"),
            ("all", "H0L1", "ggH_", "T2"),
            ("of2j_vbf_hpin", "H0PH", "VBF_", "T2"), #DM These are just negative fluctuations
            ("of2j_vh", "H0L1", "VBF_","T3"),
            ("of2j_vbf_hmin","H0M","VBF_","T2"), #DM For H0M There are many as it is essentially 0 
            ("of2j_vbf_hmin","H0M","VBF_","T4"),
            ("top_of2j","H0M","VBF_","T2"),
            ("top_of2j","H0M","VBF_","T4"),
            ("dytt_of2j","H0M","VBF_","T2"),
            ("dytt_of2j","H0M","VBF_","T4"),
            ("of2j_vh_hmip","H0M","WH_","T4"),
            ("of2j_vh_hmin","H0M","WH_","T2"),
            ("of2j_vh_hmin","H0M","WH_","T4"),
            ("top_of2j","H0M","WH_","T2"),
            ("top_of2j","H0M","WH_","T4"),
            ("dytt_of2j","H0M","WH_","T2"),
            ("dytt_of2j","H0M","WH_","T4"),
            ("of2j_vbf_hmin","H0M","ZH_","T4"),
            ("of2j_vh_hmip","H0M","ZH_","T4"),
            ("of2j_vh_hmin","H0M","ZH_","T2"),
            ("of2j_vh_hmin","H0M","ZH_","T4"),
            ("top_of2j","H0M","ZH_","T4"),
            ("dytt_of2j","H0M","ZH_","T2"),
            ("of2j_vh_hmin","H0M","","T2"),
            ("of2j_ggh_thmin","H0M","GGHjj_","T2"),
            ("of2j_ggh_lhmin","H0M","GGHjj_","T2"),
            ("top_of2j","H0M","GGHjj_","T2") ]

    def setModelBuilder(self, modelBuilder):
        PhysicsModel.setModelBuilder(self,modelBuilder)
        self.modelBuilder.doModelBOnly = False

    def getYieldScale(self,bin,proc):
        scaling=1.

        signal = "NA" 
        temp = "NA" 

        if "VBF_T" in proc : 
         temp = proc[4:]
         signal = "Ewk"
        elif "WH_T" in proc or "ZH_T" in proc : 
         temp = proc[3:]
         signal = "Ewk"
        elif "ggH_T" in proc :                                   
         temp = proc[4:]
         signal = "ggH"

        if signal is not "NA" : 
         scaling = "scale_"+signal+"_"+temp
         for c, s, p, t in self.NegList :
          if (c in bin or c is "all") and p in proc and s in self.ACF and t in temp :
           scaling = scaling+"_Neg"
           break

        print "Will scale",proc,"in bin",bin,"by",scaling
        return scaling
         
    def setPhysicsOptions(self,physOptions):
        for po in physOptions:

         if po == "H0M":
          print "Will float Fa3"
          self.ACF = "H0M"
         elif po == "H0PH":
          print "Will float Fa2"
          self.ACF = "H0PH"
         elif po == "H0L1":
          print "Will float FL1"
          self.ACF = "H0L1"
         elif po == "H0LZg":
          print "Will float FLZg"
          self.ACF = "H0LZg"
  
    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""

        self.modelBuilder.doVar("muV[1.0,0.0,10.0]")
     #   self.modelBuilder.doVar("muF[1.0,0.0,10.0]")
        self.modelBuilder.doVar("Fai[0.0,-1.0,1.0]")

        poi='muV,Fai'

        self.modelBuilder.factory_( "expr::scale_Ewk_T1(\"pow(@0,2)*pow(1-abs(@1),2)\", muV, Fai)")
        self.modelBuilder.factory_( "expr::scale_Ewk_T2(\"pow(@0,2)*sign(@1)*pow(sqrt(1-abs(@1)),3)*sqrt(abs(@1))\", muV, Fai)")
        self.modelBuilder.factory_( "expr::scale_Ewk_T2_Neg(\"pow(@0,2)*sign(@1)*pow(sqrt(1-abs(@1)),3)*sqrt(abs(@1))*-1\", muV, Fai)")
        self.modelBuilder.factory_( "expr::scale_Ewk_T3(\"pow(@0,2)*(1-abs(@1))*abs(@1)\", muV, Fai)")
        self.modelBuilder.factory_( "expr::scale_Ewk_T3_Neg(\"pow(@0,2)*(1-abs(@1))*abs(@1)*-1\", muV, Fai)")
        self.modelBuilder.factory_( "expr::scale_Ewk_T4(\"pow(@0,2)*sign(@1)*sqrt(1-abs(@1))*pow(sqrt(abs(@1)),3)\", muV, Fai)")
        self.modelBuilder.factory_( "expr::scale_Ewk_T4_Neg(\"pow(@0,2)*sign(@1)*sqrt(1-abs(@1))*pow(sqrt(abs(@1)),3)*-1\", muV, Fai)")
        self.modelBuilder.factory_( "expr::scale_Ewk_T5(\"pow(@0,2)*pow(@1,2)\", muV, Fai)")

        self.modelBuilder.factory_( "expr::scale_ggH_T1(\"@0*(1-abs(@1))\", muV, Fai)")
        self.modelBuilder.factory_( "expr::scale_ggH_T2(\"@0*sign(@1)*sqrt(1-abs(@1))*sqrt(abs(@1))\", muV, Fai)")
        self.modelBuilder.factory_( "expr::scale_ggH_T2_Neg(\"@0*sign(@1)*sqrt(1-abs(@1))*sqrt(abs(@1))*-1\", muV, Fai)")
        self.modelBuilder.factory_( "expr::scale_ggH_T3(\"@0*abs(@1)\", muV, Fai)")
        
        self.modelBuilder.doSet("POI",poi)
       
HWWCouplings = HWWCouplings()
