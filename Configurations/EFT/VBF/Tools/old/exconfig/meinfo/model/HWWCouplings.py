from HiggsAnalysis.CombinedLimit.PhysicsModel import *
 
### This is the base python class to study the VBF HWW AC
 
class HWWCouplings(PhysicsModel):
    def __init__(self):
        self.ACF = 'NA'

    def setModelBuilder(self, modelBuilder):
        PhysicsModel.setModelBuilder(self,modelBuilder)
        self.modelBuilder.doModelBOnly = False

    def preProcessNuisances(self,nuisances):
        nuisancesToRemove = []
        for n in nuisances:
          if "stat" in n[0] :
           if "VBF_" in n[0] or "WH_" in n[0] or "ZH_" in n[0] : # fix to inclsde ggF and Org hists
            if self.ACF not in n[0] and "H0PM" not in n[0] :
             print "removing nuisance", n[0]
             nuisancesToRemove.append(n[0])
        
        for nr in nuisancesToRemove:
          for n in nuisances:
            if n[0] == nr:
              nuisances.remove(n)
              break

    def getYieldScale(self,bin,proc):
        scaling=1.

        ewkH = 0
        ggH  = 0

        if "VBF_H0" in proc or "WH_H0" in proc or "ZH_H0" in proc : ewkH = 1 
        elif "H0" in proc : ggH = 1

        if ewkH is 1 :
         if "H0PM" in proc : 
          scaling = "scale_ewk_sm"
         elif self.ACF+"_M1" in proc : 
          scaling = "scale_ewk_int31"
         elif self.ACF+"_M2" in proc : 
          scaling = "scale_ewk_int22"
         elif self.ACF+"_M3" in proc : 
          scaling = "scale_ewk_int13"
         elif self.ACF in proc : 
          scaling = "scale_ewk_bsm"
         elif self.ACF not in proc and "H0PM" not in proc :
          scaling = 0.

        elif ggH is 1 :      
         if "H0PM" in proc : 
          scaling = "scale_sm"
         elif self.ACF+"_M1" in proc : 
          scaling = "scale_int11"
         elif self.ACF in proc : 
          scaling = "scale_bsm"
         elif self.ACF not in proc and "H0PM" not in proc :
          scaling = 0. 
       
        else:
         scaling = 1.  

        if "_Org" in proc :
         scaling = 0.

        if self.ACF is "H0PH" :
         if "WH_H0PH_M1" in proc or "ZH_H0PH_M1" in proc : 
          scaling = "scale_ewk_int31n"
        if self.ACF is "H0L1" :
         if "VBF_H0L1_M1" in proc : 
          scaling = "scale_ewk_int31n"

        if scaling is not 0. : 
         print "Will scale",proc,"in bin",bin,"by",scaling  
        return scaling
         
    def setPhysicsOptions(self,physOptions):
        for po in physOptions:

         if po == "Float_hm":
          print "Will float Fa3 (H0M) - Other AC set to 0"
          self.ACF = "H0M"
          self.G   = 2.55052

         if po == "Float_hp":
          print "Will float Fa2 (H0PH) - Other AC set to 0"
          self.ACF = "H0PH"
          self.G   = 1.65684

         if po == "Float_hl":
          print "Will float FL1 (H0L1) - Other AC set to 0"
          self.ACF = "H0L1"
          self.G   = -12100.42
  
    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""

        self.modelBuilder.doVar("muV[1.0,0.0,10.0]")
    #    self.modelBuilder.doVar("muF[0.0,0.0,10.0]")
        self.modelBuilder.doVar("Fai[0.0,-1.0,1.0]")

        poi='muV,Fai'

        self.modelBuilder.factory_( "expr::scale_ewk_sm(\"pow(@0,2)*pow(1-abs(@1),2)\", muV, Fai)")
        self.modelBuilder.factory_( "expr::scale_ewk_bsm(\"pow(@0,2)*pow(@1,2)*pow(%s,4)\", muV, Fai)"% self.G)
        self.modelBuilder.factory_( "expr::scale_ewk_int31(\"pow(@0,2)*sign(@1)*pow(sqrt(1-abs(@1)),3)*sqrt(abs(@1))*%s\", muV, Fai)"% self.G)
        self.modelBuilder.factory_( "expr::scale_ewk_int31n(\"pow(@0,2)*sign(@1)*pow(sqrt(1-abs(@1)),3)*sqrt(abs(@1))*%s*-1\", muV, Fai)"% self.G)
        self.modelBuilder.factory_( "expr::scale_ewk_int22(\"pow(@0,2)*(1-abs(@1))*abs(@1)*pow(%s,2)\", muV, Fai)"% self.G)
        self.modelBuilder.factory_( "expr::scale_ewk_int13(\"pow(@0,2)*sign(@1)*sqrt(1-abs(@1))*pow(sqrt(abs(@1)),3)*pow(%s,3)\", muV, Fai)"% self.G)

        self.modelBuilder.factory_( "expr::scale_sm(\"@0*(1-abs(@1))\", muV, Fai)")
        self.modelBuilder.factory_( "expr::scale_bsm(\"@0*abs(@1)*pow(%s,2)\", muV, Fai)"% self.G)
        self.modelBuilder.factory_( "expr::scale_int11(\"@0*sign(@1)*sqrt(1-abs(@1))*sqrt(abs(@1))*%s\", muV, Fai)"% self.G)
        
        self.modelBuilder.doSet("POI",poi)
       
HWWCouplings = HWWCouplings()
