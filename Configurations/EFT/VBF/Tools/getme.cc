
#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "TFile.h"
#include "TString.h"
#include "TGraph.h"

#include <string>
#include <unordered_map>
#include <iostream>

#include "TLorentzVector.h"
#include <fstream>
#include <vector>
#include "TSpline.h"


class getme {
public:
  //! constructor
  getme();
  
  virtual ~getme() {}
  
  std::vector<float> CalcACMEs(string AC, float PMix, float PBSM, float PSM, float DMix, float DBSM, float DSM, std::string s);

  float CalcMEg1gi(float PMix, float PBSM, float PSM, float DMix, float DBSM, float DSM, float g1, float gi);

};


getme::getme() { 

}

float getme::CalcMEg1gi(float PMix, float PBSM, float PSM, float DMix, float DBSM, float DSM, float g1, float gi){

  float PME = 1;
  if(PMix!=-999) PME = (PMix-PSM-PBSM)*g1*gi + PSM*pow(g1,2) + PBSM*pow(gi,2);
  float DME = (DMix-DSM-DBSM)*g1*gi + DSM*pow(g1,2) + DBSM*pow(gi,2);

  float ME = PME*DME;

  return ME;

}

std::vector<float> getme::CalcACMEs(string AC, float PMix, float PBSM, float PSM, float DMix, float DBSM, float DSM, std::string s){

  std::vector<float> MixMEs;

  float g=1, scale = 1;

  if     (AC=="H0M"){ 
   if(s=="VBF")g = 0.29797;   
   if(s=="ZH") g = 0.14405; 
   if(s=="WH") g = 0.12361;  
   if(s=="ggH")g = 1.76132;
  }else if(AC=="H0PH"){
   if(s=="VBF")g = 0.27196;   
   if(s=="ZH") g = 0.11248; 
   if(s=="WH") g = 0.09989; 
   if(s=="ggH")g = 1.133582;
  }else if(AC=="H0L1"){ 
   if(s=="VBF")g = -2158.213;   
   if(s=="ZH") g = -517.788; 
   if(s=="WH") g = -525.274;
   if(s=="ggH")g = -13752.22;
   scale=-10000; 
  }

  // BSM Pure Sample ME
  float ME_PS = CalcMEg1gi(PMix, PBSM, PSM, DMix, DBSM, DSM, 0, 1);
  MixMEs.push_back(ME_PS);

  // Mixture MEs
  float ME_M0 = CalcMEg1gi(PMix, PBSM, PSM, DMix, DBSM, DSM, 0, 1*scale);
  MixMEs.push_back(ME_M0);

  float ME_M1 = CalcMEg1gi(PMix, PBSM, PSM, DMix, DBSM, DSM, 1, 0.25*scale);
  MixMEs.push_back(ME_M1);

  float ME_M2 = CalcMEg1gi(PMix, PBSM, PSM, DMix, DBSM, DSM, 1, 0.5*scale);
  MixMEs.push_back(ME_M2);

  float ME_M3 = CalcMEg1gi(PMix, PBSM, PSM, DMix, DBSM, DSM, 1, 0.75*scale);
  MixMEs.push_back(ME_M3);

  //f05 mixture MEs
  float ME_f05 = CalcMEg1gi(PMix, PBSM, PSM, DMix, DBSM, DSM, 1, g);
  MixMEs.push_back(ME_f05);

  return MixMEs; 

}


class GetME : public multidraw::TTreeFunction {
public:
  GetME(char const* name, char const* sig);

  char const* getName() const override { return "GetME"; }
  TTreeFunction* clone() const override { return new GetME(name_.c_str(), sig_.c_str()); }

  void beginEvent(long long) override;
  unsigned getNdata() override;
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  std::string name_;
  std::string sig_;
  std::string me_;
  unsigned vindex;

  // this is horrible
  static long long currentEntry;

  static FloatValueReader* gen_dme_hsm;
  static FloatValueReader* gen_dme_hm;
  static FloatValueReader* gen_dme_hp;
  static FloatValueReader* gen_dme_hl;
  static FloatValueReader* gen_dme_mixhm;
  static FloatValueReader* gen_dme_mixhp;
  static FloatValueReader* gen_dme_mixhl;
  static FloatValueReader* gen_pme_hsm;
  static FloatValueReader* gen_pme_hm;
  static FloatValueReader* gen_pme_hp;
  static FloatValueReader* gen_pme_hl;
  static FloatValueReader* gen_pme_mixhm;
  static FloatValueReader* gen_pme_mixhp;
  static FloatValueReader* gen_pme_mixhl;

  static std::string readerSig;

  static void setValues(long long);

  static getme worker;
  static std::vector<float> MEs;
};

long long GetME::currentEntry{-2};

std::string GetME::readerSig{};

FloatValueReader* GetME::gen_dme_hsm{};
FloatValueReader* GetME::gen_dme_hm{};
FloatValueReader* GetME::gen_dme_hp{};
FloatValueReader* GetME::gen_dme_hl{};
FloatValueReader* GetME::gen_dme_mixhm{};
FloatValueReader* GetME::gen_dme_mixhp{};
FloatValueReader* GetME::gen_dme_mixhl{};
FloatValueReader* GetME::gen_pme_hsm{};
FloatValueReader* GetME::gen_pme_hm{};
FloatValueReader* GetME::gen_pme_hp{};
FloatValueReader* GetME::gen_pme_hl{};
FloatValueReader* GetME::gen_pme_mixhm{};
FloatValueReader* GetME::gen_pme_mixhp{};
FloatValueReader* GetME::gen_pme_mixhl{};

getme GetME::worker{};
std::vector<float> GetME::MEs{};

GetME::GetME(char const* name, char const* sig) :
  TTreeFunction(),
  name_{name},
  sig_{sig}
{

  me_ = "ME_"+sig_+"_"; 
  if(sig_ == "ggH") me_ = "ME_";

  if      (name_ == ""+me_+"H0PM")
    vindex = 0;
  else if (name_ == ""+me_+"H0M")
    vindex = 1;
  else if (name_ == ""+me_+"H0M_M0")
    vindex = 2;
  else if (name_ == ""+me_+"H0M_M1")
    vindex = 3;
  else if (name_ == ""+me_+"H0M_M2")
    vindex = 4;
  else if (name_ == ""+me_+"H0M_M3")
    vindex = 5;
  else if (name_ == ""+me_+"H0Mf05")
    vindex = 6;
  else if (name_ == ""+me_+"H0PH")
    vindex = 7;
  else if (name_ == ""+me_+"H0PH_M0")
    vindex = 8;
  else if (name_ == ""+me_+"H0PH_M1")
    vindex = 9;
  else if (name_ == ""+me_+"H0PH_M2")
    vindex = 10;
  else if (name_ == ""+me_+"H0PH_M3")
    vindex = 11;
  else if (name_ == ""+me_+"H0PHf05")
    vindex = 12;
  else if (name_ == ""+me_+"H0L1")
    vindex = 13;
  else if (name_ == ""+me_+"H0L1_M0")
    vindex = 14;
  else if (name_ == ""+me_+"H0L1_M1")
    vindex = 15;
  else if (name_ == ""+me_+"H0L1_M2")
    vindex = 16;
  else if (name_ == ""+me_+"H0L1_M3")
    vindex = 17;
  else if (name_ == ""+me_+"H0L1f05")
    vindex = 18;
}


void
GetME::beginEvent(long long _iEntry)
{
  setValues(_iEntry);
}

unsigned
GetME::getNdata()
{
  return 1;
}

double
GetME::evaluate(unsigned)
{
  return MEs.at(vindex);
}

void
GetME::bindTree_(multidraw::FunctionLibrary& _library)
{
  if (currentEntry == -2) {
    currentEntry = -1;

    readerSig = sig_;
   
    _library.bindBranch(gen_dme_hsm,   "gen_dme_hsm");
    _library.bindBranch(gen_dme_hm,    "gen_dme_hm");
    _library.bindBranch(gen_dme_hp,    "gen_dme_hp");
    _library.bindBranch(gen_dme_hl,    "gen_dme_hl");
    _library.bindBranch(gen_dme_mixhm, "gen_dme_mixhm");
    _library.bindBranch(gen_dme_mixhp, "gen_dme_mixhp");
    _library.bindBranch(gen_dme_mixhl, "gen_dme_mixhl");

    if (readerSig != "ggH"){
     _library.bindBranch(gen_pme_hsm,   "gen_pme_hsm");
     _library.bindBranch(gen_pme_hm,    "gen_pme_hm");
     _library.bindBranch(gen_pme_hp,    "gen_pme_hp");
     _library.bindBranch(gen_pme_hl,    "gen_pme_hl");
     _library.bindBranch(gen_pme_mixhm, "gen_pme_mixhm");
     _library.bindBranch(gen_pme_mixhp, "gen_pme_mixhp");
     _library.bindBranch(gen_pme_mixhl, "gen_pme_mixhl");
    }

    _library.addDestructorCallback([]() {
        currentEntry = -2;

        gen_dme_hsm   = nullptr;
        gen_dme_hm    = nullptr;
        gen_dme_hp    = nullptr;
        gen_dme_hl    = nullptr;
        gen_dme_mixhm = nullptr;
        gen_dme_mixhp = nullptr;
        gen_dme_mixhl = nullptr;
        gen_pme_hsm   = nullptr;
        gen_pme_hm    = nullptr;
        gen_pme_hp    = nullptr;
        gen_pme_hl    = nullptr;
        gen_pme_mixhm = nullptr;
        gen_pme_mixhp = nullptr;
        gen_pme_mixhl = nullptr;
      });
  }
}

void
GetME::setValues(long long _iEntry)
{
  if (_iEntry == currentEntry)
    return;

  currentEntry = _iEntry;

  float dme_hsm(*gen_dme_hsm ->Get());
  float dme_hm(*gen_dme_hm ->Get());
  float dme_hp(*gen_dme_hp ->Get());
  float dme_hl(*gen_dme_hl ->Get());
  float dme_mixhm(*gen_dme_mixhm ->Get());
  float dme_mixhp(*gen_dme_mixhp ->Get());
  float dme_mixhl(*gen_dme_mixhl ->Get());
 
  float pme_hsm = -999;
  float pme_hm = -999;
  float pme_hp = -999;
  float pme_hl = -999;
  float pme_mixhm = -999;
  float pme_mixhp = -999;
  float pme_mixhl = -999;

  if (readerSig != "ggH"){
   pme_hsm = *gen_pme_hsm->Get();
   pme_hm = *gen_pme_hm->Get();
   pme_hp = *gen_pme_hp->Get();
   pme_hl = *gen_pme_hl->Get();
   pme_mixhm = *gen_pme_mixhm->Get();
   pme_mixhp = *gen_pme_mixhp->Get();
   pme_mixhl = *gen_pme_mixhl->Get();
  }

  std::vector<float> result;

  float MEH0PM  = worker.CalcMEg1gi(pme_mixhm, pme_hm, pme_hsm, dme_mixhm, dme_hm, dme_hsm, 1, 0);
  result.push_back(MEH0PM);

  std::vector<float> MEH0M = worker.CalcACMEs("H0M", pme_mixhm, pme_hm, pme_hsm, dme_mixhm, dme_hm, dme_hsm, readerSig);
  result.insert(result.end(), MEH0M.begin(), MEH0M.end());

  std::vector<float> MEH0PH = worker.CalcACMEs("H0PH", pme_mixhp, pme_hp, pme_hsm, dme_mixhp, dme_hp, dme_hsm, readerSig);
  result.insert(result.end(), MEH0PH.begin(), MEH0PH.end());

  std::vector<float> MEH0L1 = worker.CalcACMEs("H0L1", pme_mixhl, pme_hl, pme_hsm, dme_mixhl, dme_hl, dme_hsm, readerSig);
  result.insert(result.end(), MEH0L1.begin(), MEH0L1.end());

  MEs = result;
  
  if(isnan(MEH0PM)){ 
   std::cout<<"ME is nan? - Should check this! "<< std::endl;
   std::fill(MEs.begin(), MEs.end(), 1);
  }

}
