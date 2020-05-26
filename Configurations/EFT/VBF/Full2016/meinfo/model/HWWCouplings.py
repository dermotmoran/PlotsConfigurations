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
           if "VBFH" in n[0] and self.ACF not in n[0] and "H0PM" not in n[0] :
            print "removing nuisance", n[0]
            nuisancesToRemove.append(n[0])
        
        for nr in nuisancesToRemove:
          for n in nuisances:
            if n[0] == nr:
              nuisances.remove(n)
              break

    def getYieldScale(self,bin,process):
        scaling=1.

        if process=="VBFH0PM" : 
          scaling = "scale_ewk_sm"
        elif process=="VBF"+self.ACF+"" : 
          scaling = "scale_ewk_bsm"
        elif process=="VBF"+self.ACF+"_M1" : 
          scaling = "scale_ewk_int31"
        elif process=="VBF"+self.ACF+"_M2" : 
          scaling = "scale_ewk_int22"
        elif process=="VBF"+self.ACF+"_M3" : 
          scaling = "scale_ewk_int13"
        elif "VBFH" in process and self.ACF not in process and "H0PM" not in process :
          scaling = 0.
        else:
          scaling = 1.   

        print "Will scale",process,"in bin",bin,"by",scaling  
        return scaling
         
    def setPhysicsOptions(self,physOptions):
        for po in physOptions:
         if po == "FloatFa3":
          print "Will float Fa3 - Other AC set to 0"
          self.ACF = "H0M"
          self.G   = 2.55052
         if po == "FloatFa2":
          print "Will float Fa2 - Other AC set to 0"
          self.ACF = "H0PH"
          self.G   = 1.65684
         if po == "FloatFL1":
          print "Will float FL1 - Other AC set to 0"
          self.ACF = "H0L1"
          self.G   = 12100.42
  
    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""

        self.modelBuilder.doVar("muV[0.0,0.0,10.0]")
        self.modelBuilder.doVar("Fai[0.0,-1.0,1.0]")

      #  self.modelBuilder.doVar('expr::Fa2("@0*@1*%s**2", Fai, muV)'% self.G)
      #  self.modelBuilder.doVar('expr::Fa1("(1-abs(@0))*@1", Fai, muV)')

        poi='muV,Fai'

        self.modelBuilder.factory_( "expr::scale_ewk_sm(\"pow(@0,2)*pow(1-abs(@1),2)\", muV, Fai)")
        self.modelBuilder.factory_( "expr::scale_ewk_bsm(\"pow(@0,2)*pow(@1,2)*pow(%s,4)\", muV, Fai)"% self.G)
        self.modelBuilder.factory_( "expr::scale_ewk_int31(\"pow(@0,2)*sign(@1)*pow(sqrt(1-abs(@1)),3)*sqrt(abs(@1))*%s\", muV, Fai)"% self.G)
        self.modelBuilder.factory_( "expr::scale_ewk_int22(\"pow(@0,2)*(1-abs(@1))*abs(@1)*pow(%s,2)\", muV, Fai)"% self.G)
        self.modelBuilder.factory_( "expr::scale_ewk_int13(\"pow(@0,2)*sign(@1)*sqrt(1-abs(@1))*pow(sqrt(abs(@1)),3)*pow(%s,3)\", muV, Fai)"% self.G)
 
        self.modelBuilder.doSet("POI",poi)
       
HWWCouplings = HWWCouplings()
