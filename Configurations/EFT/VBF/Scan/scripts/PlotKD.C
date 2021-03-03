
#include "setTDRStyle.C"
#include <map>

TH1F* getCombHist(TFile* file, TString sample, Int_t nbins);
TH1F* getOrigHist(TString sample, Int_t nbins);
double GetPoissError(double numberEvents, bool down, bool up);

void setStackStyle(THStack * hist, float r);
void setHistStyle(TH1 * hist, float r); 
void setTGraphStyle(TGraphAsymmErrors * h, float r);
void setBotStyle(TH1 * h, float r, bool fixRange, bool hideError);
void setTopPad(TCanvas * can, float r);
void setBotPad(TCanvas * can, float r);

const std::map<TString, TString> channels_hm = {
{"SRVBF1", "hww2l2v_13TeV_of2j_vbf_hmip"},
{"SRVBF2", "hww2l2v_13TeV_of2j_vbf_hmin"},
{"SRVH1",  "hww2l2v_13TeV_of2j_vh_hmip"},
{"SRVH2",  "hww2l2v_13TeV_of2j_vh_hmin"},
{"CRTop",  "hww2l2v_13TeV_top_of2j"},
{"CRDY",   "hww2l2v_13TeV_dytt_of2j"} };

const std::map<TString, TString> channels_hp = {
{"SRVBF1", "hww2l2v_13TeV_of2j_vbf_hpip"},
{"SRVBF2", "hww2l2v_13TeV_of2j_vbf_hpin"},
{"SRVH1",  "hww2l2v_13TeV_of2j_vh_hpip"},
{"SRVH2",  "hww2l2v_13TeV_of2j_vh_hpin"},
{"CRTop",  "hww2l2v_13TeV_top_of2j"},
{"CRDY",   "hww2l2v_13TeV_dytt_of2j"} };

const std::map<TString, TString> channels_hl = {
{"SRVBF", "hww2l2v_13TeV_of2j_vbf"},
{"SRVH",  "hww2l2v_13TeV_of2j_vh"},
{"CRTop", "hww2l2v_13TeV_top_of2j"},
{"CRDY",  "hww2l2v_13TeV_dytt_of2j"} };

TString ac, fit, reg, channel; 
Bool_t OrigBin = 1;

void PlotKD(string acoup, string fittype, string region, Bool_t DrawSignal, Bool_t DrawData, Bool_t log){

 gSystem->Load("../../../../../../lib/slc7_amd64_gcc700/libHiggsAnalysisCombinedLimit.so");

 setTDRStyle();
 gStyle->SetHatchesSpacing(0.35); 

 ac  = ""+acoup;
 fit = ""+fittype; 
 reg = ""+region; 

 if(acoup=="H0M")      channel = channels_hm.find(""+reg+"")->second;
 else if(acoup=="H0PH")channel = channels_hp.find(""+reg+"")->second;
 else if(acoup=="H0L1")channel = channels_hl.find(""+reg+"")->second;

 std::cout<<"------------- Fit : "+fit+", Channel : "+reg+"("+channel+") ----------------"<<std::endl;

 TFile* procfile = TFile::Open("../Full2016/datacards_proc/"+channel+"/KD_"+ac+"/shapes/histos_"+channel+".root");  
 TH1F* hProc = (TH1F*) procfile->Get(""+channel+"/data_obs"); hProc->SetDirectory(0);
 Int_t nbins = hProc->GetXaxis()->GetNbins(); 
 procfile->Close();

 TFile* basefile = TFile::Open("../Full2016/datacards/"+channel+"/KD_"+ac+"/shapes/histos_"+channel+".root");  
 TH1F* hBase = (TH1F*) basefile->Get("histo_Data"); hBase->SetDirectory(0);
 Int_t nbins_base = hBase->GetXaxis()->GetNbins(); 
 basefile->Close();

 std::cout<<"Number of bins : "<< nbins_base <<" -> "<< nbins <<std::endl;

 TH1F* data        = getOrigHist("data_obs", nbins);
 TH1F* sig_sm      = getOrigHist("VBF_T1", nbins);  
 TH1F* sig_wh_sm   = getOrigHist("WH_T1", nbins);  
 TH1F* sig_zh_sm   = getOrigHist("ZH_T1", nbins);  
 TH1F* sig_ggh_sm  = getOrigHist("ggH_T1", nbins);  
 TH1F* sig_bsm     = getOrigHist("VBF_T5", nbins);  
 TH1F* sig_wh_bsm  = getOrigHist("WH_T5", nbins);  
 TH1F* sig_zh_bsm  = getOrigHist("ZH_T5", nbins);  
 TH1F* sig_ggh_bsm = getOrigHist("ggH_T3", nbins);

 sig_sm->Add(sig_wh_sm); sig_sm->Add(sig_zh_sm); //sig_sm->Add(sig_ggh_sm);
 sig_bsm->Add(sig_wh_bsm); sig_bsm->Add(sig_zh_bsm); //sig_bsm->Add(sig_ggh_bsm);
 // sig_bsm->Scale(sig_sm->Integral()/sig_bsm->Integral());

 TFile* combfit = TFile::Open("hists/fitDiagnostics"+ac+".root"); 
 TH1F* top     = getCombHist(combfit, "top", nbins);
 TH1F* DY      = getCombHist(combfit, "DY", nbins);
 TH1F* Dyemb   = getCombHist(combfit, "Dyemb", nbins);
 TH1F* WW      = getCombHist(combfit, "WW", nbins);
 TH1F* ggWW    = getCombHist(combfit, "ggWW", nbins);
 TH1F* WWewk   = getCombHist(combfit, "WWewk", nbins);
 TH1F* Fake_em = getCombHist(combfit, "Fake_em", nbins);
 TH1F* Fake_me = getCombHist(combfit, "Fake_me", nbins);
 TH1F* VZ      = getCombHist(combfit, "VZ", nbins);
 TH1F* VVV     = getCombHist(combfit, "VVV", nbins);
 TH1F* VgS_L   = getCombHist(combfit, "VgS_L", nbins);
 TH1F* VgS_H   = getCombHist(combfit, "VgS_H", nbins);
 TH1F* bck     = getCombHist(combfit, "total_background", nbins); 
 combfit->Close();

 DY->Add(Dyemb);
 WW->Add(WWewk);
 WW->Add(ggWW);
 Fake_em->Add(Fake_me);
 VZ->Add(VVV);
 VZ->Add(VgS_L);
 VZ->Add(VgS_H);

 Double_t binsize = 1;

 ///////// set tgraph with poisson errors /////////////////
 
 Double_t vx[nbins+1];
 Double_t evx[nbins+1];
 Double_t vy[nbins+1];
 Double_t evyh[nbins+1];
 Double_t evyl[nbins+1];

 for (Int_t i=0; i < nbins+1; i++){
   vx[i]   = data->GetBinCenter(i);
   evx[i]  = data->GetBinWidth(i)/2.;                  
   vy[i]   = data->GetBinContent(i)*binsize/data->GetBinWidth(i);
   evyh[i] = GetPoissError(data->GetBinContent(i), 0, 1)*binsize/data->GetBinWidth(i);
   evyl[i] = GetPoissError(data->GetBinContent(i), 1, 0)*binsize/data->GetBinWidth(i);
 }
 TGraphAsymmErrors *data_tgr = new TGraphAsymmErrors(nbins+1, vx, vy, evx, evx, evyl, evyh); 

 ///////////////////////////////

 TCanvas *canvas = new TCanvas("c","",0,0,600,600);
 canvas->Divide(1, 2);
 setTopPad(canvas, 3.5);
 setBotPad(canvas, 3.5);
 canvas->cd(1);

 gStyle->SetOptStat(0);
 gStyle->SetOptTitle(0);

 top->SetLineColor(400);
 top->SetFillColor(400); 
 WW->SetLineColor(851);
 WW->SetFillColor(851); 
 Fake_em->SetLineColor(921); 
 Fake_em->SetFillColor(921); 
 DY->SetLineColor(418);
 DY->SetFillColor(418); 
 VZ->SetLineColor(617);
 VZ->SetFillColor(617); 

 bck->SetFillStyle(3001); 
 bck->SetFillColor(12); 
 bck->SetLineColor(12); 
 bck->SetLineWidth(2); 
 bck->SetMarkerSize(0);

 sig_sm->SetLineColor(kBlack);
 sig_sm->SetLineWidth(2);
 sig_sm->SetLineStyle(1);

 sig_bsm->SetLineColor(kRed);
 sig_bsm->SetLineWidth(2);
 sig_bsm->SetLineStyle(1);

 top->Scale(binsize,"width");
 WW->Scale(binsize,"width");
 Fake_em->Scale(binsize,"width");
 DY->Scale(binsize,"width");
 VZ->Scale(binsize,"width");
 bck->Scale(binsize,"width");
 sig_sm->Scale(binsize,"width");
 sig_bsm->Scale(binsize,"width");
 data->Scale(binsize,"width");

 THStack *hs = new THStack("hs","");
 hs->Add(top);
 hs->Add(DY);
 hs->Add(VZ); 
 hs->Add(Fake_em); 
 hs->Add(WW);    
   
 Double_t Max = std::max(hs->GetMaximum(), data->GetMaximum());
 if(DrawSignal==1)Max = std::max(Max, sig_bsm->GetMaximum());
 Max *= 1.5;
 if(log==1)Max=Max*50;
 hs->SetMaximum(Max);
 hs->SetMinimum(0.05);

 data_tgr->SetMarkerSize(0.8);
 data_tgr->SetMarkerStyle(20);
 data_tgr->SetLineWidth(3);
 data_tgr->SetMarkerColor(kBlack);
 data_tgr->SetLineColor(kBlack);
 setTGraphStyle(data_tgr, 1.1);

 data->SetMarkerSize(0.8); 
 data->SetMarkerStyle(20);
 data->SetLineWidth(3);
 data->SetMarkerColor(kBlack);
 data->SetLineColor(kBlack);
 setHistStyle(data, 1.1); 

 hs->Draw("hist");  
 setStackStyle(hs, 0.95); 
 hs->GetHistogram()->GetXaxis()->SetLabelSize(0); 
 hs->GetHistogram()->GetXaxis()->SetLabelOffset(999);
 hs->GetYaxis()->SetTitle("Events/bin");

 bck->Draw("same E2 P2"); 

 if(DrawSignal==1){
   sig_sm->Draw("same hist");
   sig_bsm->Draw("same hist");
 } 
 if(DrawData==1)data_tgr->Draw("same P0"); 

 TLegend *leg = new TLegend(0.4, 0.7, 0.91, 0.91); 
 leg->SetNColumns(2);
 leg->SetBorderSize(0);
 leg->SetFillStyle(0);
 leg->SetTextSize(0.035); 
 leg->SetTextFont(42);   
 leg->SetFillColor(0);
 leg->AddEntry(data_tgr,"Data ","lep");
 leg->AddEntry(top,"tW and t#bar{t}","f");
 leg->AddEntry(DY,"DY","f");
 leg->AddEntry(Fake_em,"Nonprompt","f");
 leg->AddEntry(VZ,"Multiboson","f");
 leg->AddEntry(WW,"WW","f");
 leg->AddEntry(bck,"Background uncertainty","f");
 if(DrawSignal){ 
  leg->AddEntry(sig_sm,"SM h","L"); 
  leg->AddEntry(sig_bsm,"BSM h","L");
 }
 leg->SetBorderSize(0); 
 leg->SetFillStyle(0); 
 leg->Draw();

 if(OrigBin){

   Double_t M = hs->GetHistogram()->GetMaximum()/2;
   if(log==1)M = hs->GetHistogram()->GetMaximum()/30;
  
   for (Int_t i=1; i < (nbins_base/10); i++){
    Int_t N = i*10;
    TLine *line = new TLine(N, 0.01, N, M); 
    line->SetLineWidth(3); line->SetLineStyle(2); line->SetLineColor(kBlack); line->Draw();
  }
  for (Int_t i=1; i < (nbins_base/40); i++){
    Int_t N2 = i*40;
    TLine *line2 = new TLine(N2, 0.01, N2, M); 
    line2->SetLineWidth(3); line2->SetLineStyle(1); line2->SetLineColor(kBlue); line2->Draw();
  }
 }

 //// Ratio

  canvas->cd(2);

  TH1F* ratiod = (TH1F*) data->Clone(); ratiod->SetDirectory(0); ratiod->SetName("ratiod");
  TH1*  ratiob = (TH1*)  bck->Clone();  ratiob->SetDirectory(0); ratiob->SetName("ratiob");

  TH1F* bck0   = (TH1F*) bck->Clone();  bck0->SetDirectory(0);   bck0->SetName("bck0");
  for (Int_t i=0; i < bck0->GetXaxis()->GetNbins(); i++){
   bck0->SetBinError(i+1, 0);
  }

  ratiob->Divide(bck0);
  setBotStyle(ratiob,3.0,1,0);
  setHistStyle(ratiob,1.3); 

  ratiod->Divide(bck0);

  Double_t r_vy[nbins+1];
  Double_t r_evyh[nbins+1];
  Double_t r_evyl[nbins+1];

  for (Int_t i=0; i < nbins+1; i++){          
    Double_t n = bck0->GetBinContent(i);
    if(n==0){
     r_vy[i]   = 0;
     r_evyh[i] = 0;
     r_evyl[i] = 0;
    }else{  
     r_vy[i]   = vy[i]/n;
     r_evyh[i] = evyh[i]/n;
     r_evyl[i] = evyl[i]/n;
    }
  }
  TGraphAsymmErrors *ratiod_tgr = new TGraphAsymmErrors(nbins+1, vx, r_vy, evx, evx, r_evyl, r_evyh); 
  setTGraphStyle(ratiod_tgr,1.15);

  ratiob->SetFillStyle(3001); //fr 3004 12 12 2 0 
  ratiob->SetFillColor(12); 
  ratiob->SetLineColor(12); 
  ratiob->SetLineWidth(2); 
  ratiob->SetMarkerSize(0);

  ratiob->GetXaxis()->SetTitle("#lower[-0.15]{D_{BSM}} ");
  ratiod->GetXaxis()->SetTitle("#lower[-0.15]{D_{BSM}}");
  ratiob->GetYaxis()->SetTitle("Data/Bkg"); 
  ratiob->Draw("E2 E2");
  
  if(DrawData)ratiod_tgr->Draw("same P0");

  TLine *line = new TLine(0,1., nbins,1.); 
  line->SetLineColor(920);
  line->SetLineStyle(2);
  line->SetLineWidth(2);
  line->Draw();
 
  if(DrawData)ratiod_tgr->Draw("same P0");

  if(log==1){
    TPad *pad1 = (TPad *)(canvas->cd(1)); 
    pad1->SetLogy(); 
    canvas->Print("plots/"+ac+fit+"_"+reg+"_Log.png");
    canvas->Print("plots/"+ac+fit+"_"+reg+"_Log.pdf");
  }else{
    canvas->Print("plots/"+ac+fit+"_"+reg+".png");
    canvas->Print("plots/"+ac+fit+"_"+reg+".pdf");
  }

}

////////////////////////////////////////////////////////////////////////////

TH1F* getOrigHist(TString sample, Int_t nbins){

 TFile* origfile = TFile::Open("../Full2016/datacards_proc/"+channel+"/KD_"+ac+"/shapes/histos_"+channel+".root");  
 TH1F* ohist = (TH1F*) origfile->Get(""+channel+"/"+sample+"")->Clone(); ohist->SetDirectory(0); 
 origfile->Close();

 if(OrigBin){ return ohist; }
 else{
  TH1F* hist = new TH1F(""+sample+"",""+sample+"", nbins, 0, nbins); hist->SetDirectory(0);
  Double_t N=0.,E=0.;
  for (Int_t i=0; i < hist->GetXaxis()->GetNbins(); i++){
   if(ohist!=NULL){ N = ohist->GetBinContent(i+1); E = ohist->GetBinError(i+1); }
   hist->SetBinContent(i+1, N);
   hist->SetBinError(i+1, E); //DM Check that data is TH1F (Normal errors) 
  }
 return hist;
 } 
 
}

TH1F* getCombHist(TFile* combfit, TString sample, Int_t nbins){

 TH1F* combhist = (TH1F*)combfit->Get("shapes_"+fit+"/hww2l2v_13TeV_"+reg+"/"+sample+""); 
 Double_t N=0.,E=0.;

 if(OrigBin){
  TFile* origfile = TFile::Open("../Full2016/datacards_proc/"+channel+"/KD_"+ac+"/shapes/histos_"+channel+".root");  
  TH1F* ohist = (TH1F*) origfile->Get(""+channel+"/data_obs")->Clone(); ohist->SetDirectory(0); //DM new name?
  origfile->Close();
  for (Int_t i=0; i < ohist->GetXaxis()->GetNbins(); i++){
   if(combhist!=NULL){N = combhist->GetBinContent(i+1); E = combhist->GetBinError(i+1); }
   ohist->SetBinContent(i+1, N);
   ohist->SetBinError(i+1, E);
  }
  return ohist;
 }else{
  TH1F* hist = new TH1F(""+sample+"",""+sample+"", nbins, 0, nbins); hist->SetDirectory(0);
  for (Int_t i=0; i < hist->GetXaxis()->GetNbins(); i++){
   if(combhist!=NULL){N = combhist->GetBinContent(i+1); E = combhist->GetBinError(i+1); }
   hist->SetBinContent(i+1, N);
   hist->SetBinError(i+1, E);
  }
  return hist;  
 }
 
}

void setStackStyle(THStack * hist, float r) {
    hist->GetXaxis()->SetTitleSize(hist->GetXaxis()->GetTitleSize()*r*r);
    hist->GetYaxis()->SetTitleSize(hist->GetYaxis()->GetTitleSize()*r*r*1.1);
    hist->GetXaxis()->SetLabelSize(hist->GetXaxis()->GetLabelSize()*r);
    hist->GetYaxis()->SetLabelSize(hist->GetYaxis()->GetLabelSize()*r); //0.9
    hist->GetXaxis()->SetLabelOffset(hist->GetXaxis()->GetLabelOffset()*r*r*r*r);
    hist->GetXaxis()->SetTitleOffset(hist->GetXaxis()->GetTitleOffset()*r);
    hist->GetYaxis()->SetTitleOffset(hist->GetYaxis()->GetTitleOffset()); //1.15

    TLatex *   tex = new TLatex(0.95,0.98,"35.9 fb^{-1}  (13 TeV)");//fr 0.9,0.98
    tex->SetNDC();
    tex->SetTextAlign(33);
    tex->SetTextFont(42);
    tex->SetTextSize(0.04);
    tex->SetLineWidth(2);
    tex->Draw();
    
    tex = new TLatex(0.158,0.94,"#bf{CMS Preliminary}"); //fr 0.2,0.94
    tex->SetNDC();
    tex->SetTextFont(42);
    tex->SetTextSize(0.04);
    tex->SetLineWidth(2);
    tex->Draw();
}

void setHistStyle(TH1 * hist, float r) {
    hist->GetXaxis()->SetTitleSize(hist->GetXaxis()->GetTitleSize()*r*r);
    hist->GetYaxis()->SetTitleSize(hist->GetYaxis()->GetTitleSize()*r*r);
    hist->GetXaxis()->SetLabelSize(hist->GetXaxis()->GetLabelSize()*r);
    hist->GetYaxis()->SetLabelSize(hist->GetYaxis()->GetLabelSize()*r);
    hist->GetXaxis()->SetLabelOffset(hist->GetXaxis()->GetLabelOffset()*r*r*r*r);
    hist->GetXaxis()->SetTitleOffset(hist->GetXaxis()->GetTitleOffset()*r);
    hist->GetYaxis()->SetTitleOffset(hist->GetYaxis()->GetTitleOffset());
    hist->SetLineWidth(1);
    hist->SetLineColor(1);
    hist->SetMarkerStyle(20);
    hist->SetMarkerColor(1);
    hist->SetMarkerSize(0.825);
}


void setTGraphStyle(TGraphAsymmErrors * hist, float r) {
    hist->GetXaxis()->SetTitleSize(hist->GetXaxis()->GetTitleSize()*r*r);
    hist->GetYaxis()->SetTitleSize(hist->GetYaxis()->GetTitleSize()*r*r);
    hist->GetXaxis()->SetLabelSize(hist->GetXaxis()->GetLabelSize()*r);
    hist->GetYaxis()->SetLabelSize(hist->GetYaxis()->GetLabelSize()*r);
    hist->GetXaxis()->SetLabelOffset(hist->GetXaxis()->GetLabelOffset()*r*r*r*r);
    hist->GetXaxis()->SetTitleOffset(hist->GetXaxis()->GetTitleOffset()*r);
    hist->GetYaxis()->SetTitleOffset(hist->GetYaxis()->GetTitleOffset());
    hist->SetLineWidth(1);
    hist->SetLineColor(1);
    hist->SetMarkerStyle(20);
    hist->SetMarkerColor(1);
    hist->SetMarkerSize(0.825);
}


void setTopPad(TCanvas * can, float r) {
   can->GetPad(1)->SetPad("TopPad", "", 0., 1./r, 1.0, 1.0, 0, -1, 0);
   can->GetPad(1)->SetTopMargin(0.24/r);
   can->GetPad(1)->SetBottomMargin(0.04/r);
   can->GetPad(1)->SetRightMargin(0.05);
   can->GetPad(1)->SetTicks(1, 1);
}

void setBotPad(TCanvas * can, float r) {
   can->GetPad(2)->SetPad("BotPad", "", 0., 0., 1.0, 1./r, 0, -1, 0);
   can->GetPad(2)->SetTopMargin(r/100.);
   can->GetPad(2)->SetBottomMargin(r/10.);
   can->GetPad(2)->SetRightMargin(0.05);
   can->GetPad(2)->SetTicks(1, 1);
}

void setBotStyle(TH1 * h, float r, bool fixRange, bool hideError){
    h->GetXaxis()->SetLabelSize(h->GetXaxis()->GetLabelSize()*(r-1));
    h->GetXaxis()->SetLabelOffset(h->GetXaxis()->GetLabelOffset()*(r-1));
    h->GetXaxis()->SetTitleSize(h->GetXaxis()->GetTitleSize()*(r-1));
    h->GetYaxis()->SetLabelSize(h->GetYaxis()->GetLabelSize()*(r-1));
    h->GetYaxis()->SetNdivisions(505);
    h->GetYaxis()->SetTitleSize(h->GetYaxis()->GetTitleSize()*(r-1));
    h->GetYaxis()->SetTitleOffset(h->GetYaxis()->GetTitleOffset()/(r-0.7));
    if (fixRange){
      h->GetYaxis()->SetRangeUser(0.5, 1.5);  
        for ( int i =1 ; i< h->GetNbinsX()+1; ++i){
            if (h->GetBinContent(i)<1.e-6) h->SetBinContent(i, -1.e-6);
        }
    }
    if (hideError){
        for ( int i =1 ; i< h->GetNbinsX()+1; ++i){
              h->SetBinError(i, 0);
         }
   }
}


double GetPoissError(double numberEvents, bool down, bool up){

  double alpha = (1-0.6827);
  double L = 0, U = 0;

  if(numberEvents!=0) L = ROOT::Math::gamma_quantile(alpha/2,numberEvents,1.);
   
  if(numberEvents==0) U = ROOT::Math::gamma_quantile_c(alpha/2,numberEvents+1,1.); 
  else                U = ROOT::Math::gamma_quantile_c(alpha/2,numberEvents+1,1.);
          
  L = numberEvents - L;
  if(numberEvents>0) U = U - numberEvents;
        
  if     (up   && !down)  return U;
  else if(down && !up)    return L;
  else                    return 0;
 
}
