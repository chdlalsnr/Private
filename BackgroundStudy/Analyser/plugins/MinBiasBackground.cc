#include "BackgroundStudy/Analyser/plugins/MinBiasBackground.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"


MinBiasBackground::MinBiasBackground(const edm::ParameterSet& pset) {

//  rechit_token_ = consumes<GEMRecHitCollection>(pset.getParameter<edm::InputTag>("gemRecHits"));
//  simhit_token_ = consumes<edm::PSimHitContainer>(pset.getParameter<edm::InputTag>("gemSimHits"));
//  geomToken_ = esConsumes<GEMGeometry, MuonGeometryRecord>();
//  geomTokenBeginRun_ = esConsumes<GEMGeometry, MuonGeometryRecord, edm::Transition::BeginRun>();

  rechit_token_ = consumes<ME0RecHitCollection>(pset.getParameter<edm::InputTag>("me0RecHits"));
  simhit_token_ = consumes<edm::PSimHitContainer>(pset.getParameter<edm::InputTag>("me0SimHits"));
  geomToken_ = esConsumes<ME0Geometry, MuonGeometryRecord>();
  geomTokenBeginRun_ = esConsumes<ME0Geometry, MuonGeometryRecord, edm::Transition::BeginRun>();
}

MinBiasBackground::~MinBiasBackground() {}

void MinBiasBackground::beginRun(const edm::Run& run, const edm::EventSetup& setup) {

  const ME0Geometry* gem = &setup.getData(geomTokenBeginRun_);

//  // GE1/1 binning
//  Double_t bp11_short[9];
//  Double_t bp11_long[9];
//  bp11_short[0] = 130.2;    bp11_long[0] = 128.136;
//  bp11_short[1] = 140.456;  bp11_long[1] = 139.320;
//  bp11_short[2] = 150.712;  bp11_long[2] = 150.489;
//  bp11_short[3] = 162.712;  bp11_long[3] = 163.79;
//  bp11_short[4] = 173.701;  bp11_long[4] = 177.070;
//  bp11_short[5] = 187.808;  bp11_long[5] = 192.981;
//  bp11_short[6] = 202.940;  bp11_long[6] = 208.868;
//  bp11_short[7] = 219.645;  bp11_long[7] = 228.027;
//  bp11_short[8] = 236.300;  bp11_long[8] = 247.432;

//  // GE2/1 binning
//  Double_t bp21_t1[9];
//  Double_t bp21_t2[9];
//  bp21_t1[0] = 127.8;    bp21_t2[0] = 124.763;
//  bp21_t1[1] = 147.325;  bp21_t2[1] = 146.313;
//  bp21_t1[2] = 168.895;  bp21_t2[2] = 165.857;
//  bp21_t1[3] = 193.995;  bp21_t2[3] = 188.933;
//  bp21_t1[4] = 215.565;  bp21_t2[4] = 208.477;
//  bp21_t1[5] = 240.665;  bp21_t2[5] = 233.578;
//  bp21_t1[6] = 262.235;  bp21_t2[6] = 257.173;
//  bp21_t1[7] = 287.335;  bp21_t2[7] = 284.298;
//  bp21_t1[8] = 308.905;  bp21_t2[8] = 307.893;

  // ME0 binning
  Double_t bp0[9];
  bp0[0] = 62.3442;
  bp0[1] = 69.9868;
  bp0[2] = 77.6794;
  bp0[3] = 87.0426;
  bp0[4] = 96.4058;
  bp0[5] = 108.148;
  bp0[6] = 119.891;
  bp0[7] = 134.701;
  bp0[8] = 149.512;

//  for (const auto& station : gem->regions()[0]->stations()) {
//
//    Int_t station_id = station->station();
    Int_t station_id = 0;

    hist_rechit_global_pos_x_[station_id] = fs_->make<TH1D>(Form("rechit_global_pos_x_st%d", station_id),"rechit_x",1000,0,1000);
    hist_rechit_global_pos_y_[station_id] = fs_->make<TH1D>(Form("rechit_global_pos_y_st%d", station_id),"rechit_y",1000,0,1000);
    hist_rechit_global_pos_z_[station_id] = fs_->make<TH1D>(Form("rechit_global_pos_z_st%d", station_id),"rechit_z",1000,0,1000);

    hist_simhit_global_pos_x_[station_id] = fs_->make<TH1D>(Form("simhit_global_pos_x_st%d", station_id),"simhit_x",1000,0,1000);
    hist_simhit_global_pos_y_[station_id] = fs_->make<TH1D>(Form("simhit_global_pos_y_st%d", station_id),"simhit_y",1000,0,1000);
    hist_simhit_global_pos_z_[station_id] = fs_->make<TH1D>(Form("simhit_global_pos_z_st%d", station_id),"simhit_z",1000,0,1000);

    rechit_r_odd = new TH1D("rechit_r_odd","RecHit Distribution in Global R_ME0", 8, bp0);
    hitrate_odd  = new TH1D("hitrate_odd","Hitrate Distribution per Eta-partition_ME0", 8, bp0);

//    rechit_r_even = new TH1D("rechit_r_even","RecHit Distribution in Global R_GE1/1", 8, bp11_long);
//    hitrate_even  = new TH1D("hitrate_even","Hitrate Distribution per Eta-partition_GE1/1", 8, bp11_long);
//  }
}

void MinBiasBackground::endRun(const edm::Run& run, const edm::EventSetup& setup) {}

void MinBiasBackground::analyze(const edm::Event& event, const edm::EventSetup& setup) {

//  const GEMGeometry* gem = &setup.getData(geomToken_);
  const ME0Geometry* gem = &setup.getData(geomToken_);

//  edm::Handle<GEMRecHitCollection> rechit_collection;
//  event.getByToken(rechit_token_, rechit_collection);
  edm::Handle<ME0RecHitCollection> rechit_collection;
  event.getByToken(rechit_token_, rechit_collection);

  Int_t station_id = 0;
  for (const auto& rechit : *rechit_collection) {

    //GEMDetId gem_id{rechit.gemId()};
    ME0DetId gem_id{rechit.me0Id()};

    //Int_t region_id = gem_id.region();
    //Int_t station_id = gem_id.station();
    Int_t chamber_id = gem_id.chamber();
    //Int_t layer_id = gem_id.layer();
    //Int_t roll_id = gem_id.roll();

//    if (station_id == 1) {
      const BoundPlane& surface = gem->idToDet(gem_id)->surface();
      GlobalPoint&& rechit_global_pos = surface.toGlobal(rechit.localPosition());
  
      Float_t rechit_g_abs_x = std::fabs(rechit_global_pos.x());
      Float_t rechit_g_abs_y = std::fabs(rechit_global_pos.y());
      Float_t rechit_g_abs_z = std::fabs(rechit_global_pos.z());
  
      hist_rechit_global_pos_x_[station_id]->Fill(rechit_g_abs_x);
      hist_rechit_global_pos_y_[station_id]->Fill(rechit_g_abs_y);
      hist_rechit_global_pos_z_[station_id]->Fill(rechit_g_abs_z);
  
      Float_t rechit_g_r = pow((pow(rechit_g_abs_x,2.)+pow(rechit_g_abs_y,2.)),0.5);
  
//      if (chamber_id%2 == 0) rechit_r_even->Fill(rechit_g_r);
//      if (chamber_id%2 != 0) 
      rechit_r_odd->Fill(rechit_g_r); 
//    }
  }

  hitrate_odd->SetBinContent(1,(rechit_r_odd->GetBinContent(1))*SF/(EA_me0_eta8*18));
  hitrate_odd->SetBinContent(2,(rechit_r_odd->GetBinContent(2))*SF/(EA_me0_eta7*18));
  hitrate_odd->SetBinContent(3,(rechit_r_odd->GetBinContent(3))*SF/(EA_me0_eta6*18));
  hitrate_odd->SetBinContent(4,(rechit_r_odd->GetBinContent(4))*SF/(EA_me0_eta5*18));
  hitrate_odd->SetBinContent(5,(rechit_r_odd->GetBinContent(5))*SF/(EA_me0_eta4*18));
  hitrate_odd->SetBinContent(6,(rechit_r_odd->GetBinContent(6))*SF/(EA_me0_eta3*18));
  hitrate_odd->SetBinContent(7,(rechit_r_odd->GetBinContent(7))*SF/(EA_me0_eta2*18));
  hitrate_odd->SetBinContent(8,(rechit_r_odd->GetBinContent(8))*SF/(EA_me0_eta1*18));

//  hitrate_even->SetBinContent(1,(rechit_r_even->GetBinContent(1))*SF/(EA_long_eta8*18));
//  hitrate_even->SetBinContent(2,(rechit_r_even->GetBinContent(2))*SF/(EA_long_eta7*18));
//  hitrate_even->SetBinContent(3,(rechit_r_even->GetBinContent(3))*SF/(EA_long_eta6*18));
//  hitrate_even->SetBinContent(4,(rechit_r_even->GetBinContent(4))*SF/(EA_long_eta5*18));
//  hitrate_even->SetBinContent(5,(rechit_r_even->GetBinContent(5))*SF/(EA_long_eta4*18));
//  hitrate_even->SetBinContent(6,(rechit_r_even->GetBinContent(6))*SF/(EA_long_eta3*18));
//  hitrate_even->SetBinContent(7,(rechit_r_even->GetBinContent(7))*SF/(EA_long_eta2*18));
//  hitrate_even->SetBinContent(8,(rechit_r_even->GetBinContent(8))*SF/(EA_long_eta1*18));

  cvs->cd();
  hitrate_odd->GetXaxis()->SetTitle("Global R[cm]");
  hitrate_odd->GetYaxis()->SetTitle("Hitrate[Hz/cm2]");
  hitrate_odd->SetLineColor(kRed);
  hitrate_odd->SetLineWidth(1.0);
  hitrate_odd->Draw();
  
//  hitrate_even->SetLineColor(kBlue);
//  hitrate_even->SetLineWidth(1.0);
//  hitrate_even->Draw("same");

  cvs->SaveAs("hitrate_me0.png");

  // NOTE
  edm::Handle<edm::PSimHitContainer> simhit_container;
  event.getByToken(simhit_token_, simhit_container);

  for (const auto& simhit : *simhit_container.product()) {

    //GEMDetId simhit_gemid{simhit.detUnitId()};
    ME0DetId simhit_gemid{simhit.detUnitId()};
    const BoundPlane& surface = gem->idToDet(simhit_gemid)->surface();

    //Int_t region_id = simhit_gemid.region();
    //Int_t station_id = simhit_gemid.station();
    //Int_t layer_id = simhit_gemid.layer();
    //Int_t chamber_id = simhit_gemid.chamber();
    //Int_t roll_id = simhit_gemid.roll();

    const LocalPoint& simhit_local_pos = simhit.localPosition();
    const GlobalPoint& simhit_global_pos = surface.toGlobal(simhit_local_pos);

    Float_t simhit_g_abs_x = std::fabs(simhit_global_pos.x());
    Float_t simhit_g_abs_y = std::fabs(simhit_global_pos.y());
    Float_t simhit_g_abs_z = std::fabs(simhit_global_pos.z());

    hist_simhit_global_pos_x_[station_id]->Fill(simhit_g_abs_x);
    hist_simhit_global_pos_y_[station_id]->Fill(simhit_g_abs_y);
    hist_simhit_global_pos_z_[station_id]->Fill(simhit_g_abs_z);
  }
}

//define this as a plug-in
DEFINE_FWK_MODULE(MinBiasBackground);
