#ifndef MinBiasBackground_h
#define MinBiasBackground_h

#include "FWCore/PluginManager/interface/ModuleDef.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Framework/interface/Event.h"

#include "Geometry/GEMGeometry/interface/GEMGeometry.h"
#include "Geometry/Records/interface/MuonGeometryRecord.h"
#include "DataFormats/GEMRecHit/interface/GEMRecHitCollection.h"
#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"
#include "Geometry/GEMGeometry/interface/ME0Geometry.h"
#include "DataFormats/GEMRecHit/interface/ME0RecHitCollection.h"

#include "TH1D.h"
#include "TCanvas.h"

#include <cmath>


class MinBiasBackground : public edm::EDAnalyzer {

public:
  explicit MinBiasBackground(const edm::ParameterSet&);
  ~MinBiasBackground();

private:
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void beginRun(const edm::Run&, const edm::EventSetup&) override;
  virtual void endRun(const edm::Run&, const edm::EventSetup&) override;

  // Parameter
//  edm::EDGetTokenT<GEMRecHitCollection> rechit_token_;
  edm::EDGetTokenT<edm::PSimHitContainer> simhit_token_;
//  edm::ESGetToken<GEMGeometry, MuonGeometryRecord> geomToken_;
//  edm::ESGetToken<GEMGeometry, MuonGeometryRecord> geomTokenBeginRun_;
  edm::EDGetTokenT<ME0RecHitCollection> rechit_token_;
  edm::ESGetToken<ME0Geometry, MuonGeometryRecord> geomToken_;
  edm::ESGetToken<ME0Geometry, MuonGeometryRecord> geomTokenBeginRun_;

//  // Variables
//  // GE1/1 Effective Area_Long[cm2]
//  Double_t EA_long_eta1 = 831.75;
//  Double_t EA_long_eta2 = 764.72;
//  Double_t EA_long_eta3 = 583.82;
//  Double_t EA_long_eta4 = 537.61;
//  Double_t EA_long_eta5 = 413.69;
//  Double_t EA_long_eta6 = 381.42;
//  Double_t EA_long_eta7 = 295.55;
//  Double_t EA_long_eta8 = 272.75;
//  // GE1/1 Effective Area_Short[cm2]
//  Double_t EA_short_eta1 = 674.18;
//  Double_t EA_short_eta2 = 624.78;
//  Double_t EA_short_eta3 = 488.86;
//  Double_t EA_short_eta4 = 453.65;
//  Double_t EA_short_eta5 = 358.16;
//  Double_t EA_short_eta6 = 332.67;
//  Double_t EA_short_eta7 = 263.78;
//  Double_t EA_short_eta8 = 245.19;

//  // GE2/1 Effective Area_Type I[cm2]
//  Double_t EA_t1_eta1 = 2665.571;
//  Double_t EA_t1_eta2 = 2461.298;
//  Double_t EA_t1_eta3 = 2226.463;
//  Double_t EA_t1_eta4 = 2022.190;
//  Double_t EA_t1_eta5 = 1494.824;
//  Double_t EA_t1_eta6 = 1354.682;
//  Double_t EA_t1_eta7 = 1189.231;
//  Double_t EA_t1_eta8 = 1049.088;
//  // GE2/1 Effective Area_Type II[cm2]
//  Double_t EA_t2_eta1 = 2444.621;
//  Double_t EA_t2_eta2 = 2273.919;
//  Double_t EA_t2_eta3 = 2075.284;
//  Double_t EA_t2_eta4 = 1904.583;
//  Double_t EA_t2_eta5 = 1705.943;
//  Double_t EA_t2_eta6 = 1535.244;
//  Double_t EA_t2_eta7 = 1336.606;
//  Double_t EA_t2_eta8 = 1165.905;

  // ME0 Effective Area[cm2]
  Double_t EA_me0_eta1 = 739.850;
  Double_t EA_me0_eta2 = 662.755;
  Double_t EA_me0_eta3 = 470.256;
  Double_t EA_me0_eta4 = 421.837;
  Double_t EA_me0_eta5 = 301.335;
  Double_t EA_me0_eta6 = 270.584;
  Double_t EA_me0_eta7 = 199.062;
  Double_t EA_me0_eta8 = 178.329;

//  Double_t SF = 8351.51; // for GE1/1
  Double_t SF = 12562.96; // for GE2/1 & ME0

  // output definitions
  edm::Service<TFileService> fs_;
  TCanvas* cvs = new TCanvas("c","c", 900, 600);

  std::map<Int_t, TH1D*> hist_rechit_global_pos_x_;
  std::map<Int_t, TH1D*> hist_rechit_global_pos_y_;
  std::map<Int_t, TH1D*> hist_rechit_global_pos_z_;

  std::map<Int_t, TH1D*> hist_simhit_global_pos_x_;
  std::map<Int_t, TH1D*> hist_simhit_global_pos_y_;
  std::map<Int_t, TH1D*> hist_simhit_global_pos_z_;

  TH1D* rechit_r_odd;
  TH1D* rechit_r_even;
  TH1D* hitrate_odd;
  TH1D* hitrate_even;
};

#endif  // MinBiasBackground_h
