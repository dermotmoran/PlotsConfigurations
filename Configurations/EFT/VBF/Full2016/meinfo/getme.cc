
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
  
  std::vector<float> CalcACMEs(string AC, float PMix, float PBSM, float PSM, float DMix, float DBSM, float DSM);

  float CalcMEg1gi(float PMix, float PBSM, float PSM, float DMix, float DBSM, float DSM, float g1, float gi);

};


getme::getme() { 

}

float getme::CalcMEg1gi(float PMix, float PBSM, float PSM, float DMix, float DBSM, float DSM, float g1, float gi){

  float ME = ((PMix-PSM-PBSM)*g1*gi + PSM*pow(g1,2) + PBSM*pow(gi,2))*((DMix-DSM-DBSM)*g1*gi + DSM*pow(g1,2) + DBSM*pow(gi,2));

 return ME;

}

std::vector<float> getme::CalcACMEs(string AC, float PMix, float PBSM, float PSM, float DMix, float DBSM, float DSM){

  std::vector<float> MixMEs;

  float gVBF=1, gZH=1, gWH=1, scale = 1;

  if     (AC=="H0M"){  gVBF = 0.29797;   gZH = 0.14405;  gWH = 0.12361;  scale=1; }
  else if(AC=="H0PH"){ gVBF = 0.27196;   gZH = 0.11248;  gWH = 0.09989;  scale=1; }
  else if(AC=="H0L1"){ gVBF = -2158.213; gZH = -517.788; gWH = -525.274; scale=-10000; } 
  else{
     std::cout<<"This AC "+AC+" is not defined!! "<<std::endl;
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
  float ME_f05VBF = CalcMEg1gi(PMix, PBSM, PSM, DMix, DBSM, DSM, 1, gVBF);
  MixMEs.push_back(ME_f05VBF);

  float ME_f05ZH  = CalcMEg1gi(PMix, PBSM, PSM, DMix, DBSM, DSM, 1, gZH);
  MixMEs.push_back(ME_f05ZH);

  float ME_f05WH  = CalcMEg1gi(PMix, PBSM, PSM, DMix, DBSM, DSM, 1, gWH);
  MixMEs.push_back(ME_f05WH);

  // std::cout<<"eq "+AC+" "<< ME_f05VBF <<std::endl;

  return MixMEs; 

}


class GetME : public multidraw::TTreeFunction {
public:
  GetME(char const* name);

  char const* getName() const override { return "GetME"; }
  TTreeFunction* clone() const override { return new GetME(name_.c_str()); }

  void beginEvent(long long) override;
  unsigned getNdata() override;
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  std::string name_;
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

  static void setValues(long long);

  static getme worker;
  static std::vector<float> MEs;
};

long long GetME::currentEntry{-2};

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

GetME::GetME(char const* name) :
  TTreeFunction(),
  name_{name}
{
  if      (name_ == "MEH0PM")
    vindex = 0;
  else if (name_ == "MEH0M_PS")
    vindex = 1;
  else if (name_ == "MEH0M_M0")
    vindex = 2;
  else if (name_ == "MEH0M_M1")
    vindex = 3;
  else if (name_ == "MEH0M_M2")
    vindex = 4;
  else if (name_ == "MEH0M_M3")
    vindex = 5;
  else if (name_ == "MEH0M_f05VBF")
    vindex = 6;
  else if (name_ == "MEH0M_f05ZH")
    vindex = 7;
  else if (name_ == "MEH0M_f05WH")
    vindex = 8;
  else if (name_ == "MEH0PH_PS")
    vindex = 9;
  else if (name_ == "MEH0PH_M0")
    vindex = 10;
  else if (name_ == "MEH0PH_M1")
    vindex = 11;
  else if (name_ == "MEH0PH_M2")
    vindex = 12;
  else if (name_ == "MEH0PH_M3")
    vindex = 13;
  else if (name_ == "MEH0PH_f05VBF")
    vindex = 14;
  else if (name_ == "MEH0PH_f05ZH")
    vindex = 15;
  else if (name_ == "MEH0PH_f05WH")
    vindex = 16;
  else if (name_ == "MEH0L1_PS")
    vindex = 17;
  else if (name_ == "MEH0L1_M0")
    vindex = 18;
  else if (name_ == "MEH0L1_M1")
    vindex = 19;
  else if (name_ == "MEH0L1_M2")
    vindex = 20;
  else if (name_ == "MEH0L1_M3")
    vindex = 21;
  else if (name_ == "MEH0L1_f05VBF")
    vindex = 22;
  else if (name_ == "MEH0L1_f05ZH")
    vindex = 23;
  else if (name_ == "MEH0L1_f05WH")
    vindex = 24;
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

    _library.bindBranch(gen_dme_hsm,   "gen_dme_hsm");
    _library.bindBranch(gen_dme_hm,    "gen_dme_hm");
    _library.bindBranch(gen_dme_hp,    "gen_dme_hp");
    _library.bindBranch(gen_dme_hl,    "gen_dme_hl");
    _library.bindBranch(gen_dme_mixhm, "gen_dme_mixhm");
    _library.bindBranch(gen_dme_mixhp, "gen_dme_mixhp");
    _library.bindBranch(gen_dme_mixhl, "gen_dme_mixhl");
    _library.bindBranch(gen_pme_hsm,   "gen_pme_hsm");
    _library.bindBranch(gen_pme_hm,    "gen_pme_hm");
    _library.bindBranch(gen_pme_hp,    "gen_pme_hp");
    _library.bindBranch(gen_pme_hl,    "gen_pme_hl");
    _library.bindBranch(gen_pme_mixhm, "gen_pme_mixhm");
    _library.bindBranch(gen_pme_mixhp, "gen_pme_mixhp");
    _library.bindBranch(gen_pme_mixhl, "gen_pme_mixhl");

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
  float pme_hsm(*gen_pme_hsm ->Get());
  float pme_hm(*gen_pme_hm ->Get());
  float pme_hp(*gen_pme_hp ->Get());
  float pme_hl(*gen_pme_hl ->Get());
  float pme_mixhm(*gen_pme_mixhm ->Get());
  float pme_mixhp(*gen_pme_mixhp ->Get());
  float pme_mixhl(*gen_pme_mixhl ->Get());

  std::vector<float> result;

  float MEH0PM  = worker.CalcMEg1gi(pme_mixhm, pme_hm, pme_hsm, dme_mixhm, dme_hm, dme_hsm, 1, 0);
  result.push_back(MEH0PM);

  std::vector<float> MEH0M = worker.CalcACMEs("H0M", pme_mixhm, pme_hm, pme_hsm, dme_mixhm, dme_hm, dme_hsm);
  result.insert(result.end(), MEH0M.begin(), MEH0M.end());
 
  std::vector<float> MEH0PH = worker.CalcACMEs("H0PH", pme_mixhp, pme_hp, pme_hsm, dme_mixhp, dme_hp, dme_hsm);
  result.insert(result.end(), MEH0PH.begin(), MEH0PH.end());

  std::vector<float> MEH0L1 = worker.CalcACMEs("H0L1", pme_mixhl, pme_hl, pme_hsm, dme_mixhl, dme_hl, dme_hsm);
  result.insert(result.end(), MEH0L1.begin(), MEH0L1.end());

  MEs = result;

  //  std::cout<<"H0M "<< pme_mixhm*dme_mixhm <<" "<<  MEs.at(6) <<std::endl;
 
}
