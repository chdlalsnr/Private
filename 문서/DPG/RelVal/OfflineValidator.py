#!/usr/bin/python
from ROOT import *
import numpy as np
import sys

def main(release):

	path = '/cms/ldap_home/chdlalsnr/Validation/Samples/' + release
	if (release == 'CMSSW_11_2_0_pre1' or release == 'CMSSW_11_2_0_pre2' or release == 'CMSSW_11_2_0_pre3'):
		workflow = '/23211.0_TenMuExtendedE_0_200+TenMuExtendedE_0_200_pythia8_2026D49_GenSimHLBeamSpotFull+DigiFullTrigger_2026D49+RecoFullGlobal_2026D49+HARVESTFullGlobal_2026D49/'
	else:
		workflow = '/23211.0_TenMuExtendedE_0_200+2026D49+TenMuExtendedE_0_200_pythia8_GenSimHLBeamSpot+DigiTrigger+RecoGlobal+HARVESTGlobal/'
	path += workflow + 'step3.root'

	gSystem.Load('libFWCoreFWLite')
	FWLiteEnabler.enable()

	f = TFile(path, "read")
	event_num = 100

	gsh_re,gsh_st,gsh_ch,gsh_ro,gsh_hit_x,gsh_hit_y,gsh_hit_phi,gsh_hit_eta,gsh_mnt,gsh_eloss,gsh_tof = [],[],[],[],[],[],[],[],[],[],[]
	gsh_num_el,gsh_num_mu,gsh_num_a = 0,0,0
	msh_re,msh_st,msh_ch,msh_ro,msh_hit_x,msh_hit_y,msh_hit_phi,msh_hit_eta,msh_mnt,msh_eloss,msh_tof = [],[],[],[],[],[],[],[],[],[],[]
	#gdi_str,gdi_bx = [],[]
	grh_re,grh_st,grh_ch,grh_ro,grh_hit_x,grh_hit_y,grh_err_xx,grh_err_yy,grh_err_xy,grh_err,grh_bx,grh_cls = [],[],[],[],[],[],[],[],[],[],[],[]
	mrh_re,mrh_st,mrh_ch,mrh_ro,mrh_hit_x,mrh_hit_y,mrh_err_xx,mrh_err_yy,mrh_err_xy,mrh_err,mrh_tof = [],[],[],[],[],[],[],[],[],[],[]

	gsh_hit_xy,gsh_hit_ep,msh_hit_xy,msh_hit_ep,grh_hit_xy,mrh_hit_xy = [],[],[],[],[],[]

	for i in range(event_num):
		f.Events.GetEntry(i)

		temp_gsh = f.Events.PSimHits_g4SimHits_MuonGEMHits_SIM.product()
		temp_msh = f.Events.PSimHits_g4SimHits_MuonME0Hits_SIM.product()
		temp_digi = f.Events.GEMDetIdGEMDigiMuonDigiCollection_muonGEMDigis__RECO.product()
		temp_grh  = f.Events.GEMDetIdGEMRecHitsOwnedRangeMap_gemRecHits__RECO.product()
		temp_mrh  = f.Events.ME0DetIdME0RecHitsOwnedRangeMap_me0RecHits__RECO.product()

		for j in range(temp_gsh.size()):
			gsh_re.append(GEMDetId(temp_gsh[j].detUnitId()).region())
			gsh_st.append(GEMDetId(temp_gsh[j].detUnitId()).station())
			gsh_ch.append(GEMDetId(temp_gsh[j].detUnitId()).chamber())
			gsh_ro.append(GEMDetId(temp_gsh[j].detUnitId()).roll())

			gsh_hit_x.append(temp_gsh[j].localPosition().x())
			gsh_hit_y.append(temp_gsh[j].localPosition().y())
			double_xy = []
			double_xy.append(temp_gsh[j].localPosition().x())
			double_xy.append(temp_gsh[j].localPosition().y())
			gsh_hit_xy.append(double_xy)
			gsh_hit_eta.append(temp_gsh[j].localDirection().eta())
			gsh_hit_phi.append(temp_gsh[j].localDirection().phi())
			double_ep = []
			double_ep.append(temp_gsh[j].localDirection().eta())
			double_ep.append(temp_gsh[j].localDirection().phi())
			gsh_hit_ep.append(double_ep)

			gsh_mnt.append(temp_gsh[j].pabs())
			#gsh_seg.append(temp_gsh[j].exitPoint()-temp_gsh[j].entryPoint())
			gsh_eloss.append(temp_gsh[j].energyLoss())
			gsh_tof.append(temp_gsh[j].timeOfFlight())

#			gsh_num_el, gsh_num_mu, gsh_num_a = 0,0,0
#			if (temp_gsh[j].particleType() == 1):
#				gsh_num_el += 1
#			elif (temp_gsh[j].particleType() == 3):
#				gsh_num_a += 1
#			elif (temp_gsh[j].particleType() == 4):
#				gsh_num_mu += 1

        	for j in range(temp_msh.size()):
                	msh_re.append(GEMDetId(temp_msh[j].detUnitId()).region())
                	msh_st.append(GEMDetId(temp_msh[j].detUnitId()).station())
                	msh_ch.append(GEMDetId(temp_msh[j].detUnitId()).chamber())
                	msh_ro.append(GEMDetId(temp_msh[j].detUnitId()).roll())

                	msh_hit_x.append(temp_msh[j].localPosition().x())
                	msh_hit_y.append(temp_msh[j].localPosition().y())
			double_xy = []
			double_xy.append(temp_msh[j].localPosition().x())
			double_xy.append(temp_msh[j].localPosition().y())
			msh_hit_xy.append(double_xy)
                	msh_hit_eta.append(temp_msh[j].localDirection().eta())
                	msh_hit_phi.append(temp_msh[j].localDirection().phi())
			double_ep = []
			double_ep.append(temp_msh[j].localDirection().eta())
			double_ep.append(temp_msh[j].localDirection().phi())
			msh_hit_ep.append(double_ep)

                	msh_mnt.append(temp_msh[j].pabs())
                	#msh_seg.append(temp_msh[j].exitPoint()-temp_msh[j].entryPoint())
                	msh_eloss.append(temp_msh[j].energyLoss())
                	msh_tof.append(temp_msh[j].timeOfFlight())


#		for j in range(temp_digi.size()):
#			gdi_str.append(temp_digi[j].strip()
#			gdi_bx   .append(temp_digi[j].bx()


		for j in range(temp_grh.size()):
			grh_re.append(temp_grh[j].gemId().region())
			grh_st.append(temp_grh[j].gemId().station())
			grh_ch.append(temp_grh[j].gemId().chamber())
			grh_ro.append(temp_grh[j].gemId().roll())

			grh_hit_x.append(temp_grh[j].hit().localPosition().x())
			grh_hit_y.append(temp_grh[j].hit().localPosition().y())
			double_xy = []
			double_xy.append(temp_grh[j].hit().localPosition().x())
			double_xy.append(temp_grh[j].hit().localPosition().y())
			grh_hit_xy.append(double_xy)
			grh_err_xx = temp_grh[j].hit().localPositionError().xx()
			grh_err_yy = temp_grh[j].hit().localPositionError().yy()
			grh_err_xy = temp_grh[j].hit().localPositionError().xy()
			grh_err.append(np.sqrt(grh_err_xx**2 + grh_err_yy**2))

			grh_bx.append(temp_grh[j].BunchX())
			grh_cls.append(temp_grh[j].clusterSize())

        	for j in range(temp_mrh.size()):
                	mrh_re.append(temp_mrh[j].me0Id().region())
                	mrh_st.append(temp_mrh[j].me0Id().station())
                	mrh_ch.append(temp_mrh[j].me0Id().chamber())
                	mrh_ro.append(temp_mrh[j].me0Id().roll())

                	mrh_hit_x.append(temp_mrh[j].hit().localPosition().x())
                	mrh_hit_y.append(temp_mrh[j].hit().localPosition().y())
			double_xy = []
			double_xy.append(temp_mrh[j].hit().localPosition().x())
			double_xy.append(temp_mrh[j].hit().localPosition().y())
			mrh_hit_xy.append(double_xy)
                	mrh_err_xx = temp_mrh[j].hit().localPositionError().xx()
                	mrh_err_yy = temp_mrh[j].hit().localPositionError().yy()
                	mrh_err_xy = temp_mrh[j].hit().localPositionError().xy()
                	mrh_err.append(np.sqrt(mrh_err_xx**2 + mrh_err_yy**2))

                	mrh_tof.append(temp_mrh[j].tof())


	canvas = TCanvas('c', '', 1800, 900)
	canvas.Divide(4,2)

	canvas.cd(1)
	h2_gsh_xy = TH2D("h2_gsh_xy","2D Distribution on SimHits (ch,eta)", 36, 1, 36, 8, 1, 9)
	for i in range(len(gsh_ch)): h2_gsh_xy.Fill(gsh_ch[i],gsh_ro[i])
	h2_gsh_xy.GetXaxis().SetTitle("Chamber Number")
	h2_gsh_xy.GetYaxis().SetTitle("Eta-partition Number")
	h2_gsh_xy.Draw("colz")

	canvas.cd(2)
	h2_msh_xy = TH2D("h2_msh_xy","2D Distribution on SimHits (ch,eta)", 18, 1, 18, 8, 1, 9)
	for i in range(len(msh_ch)): h2_msh_xy.Fill(msh_ch[i],msh_ro[i])
	h2_msh_xy.GetXaxis().SetTitle("Chamber Number")
	h2_msh_xy.GetYaxis().SetTitle("Eta-partition Number")
	h2_msh_xy.Draw("colz")

	canvas.cd(3)
	h_gsh_tof = TH1D("h_gsh_tof","TimeOfFlight Distribution of GEM SimHits", 10, 15, 35)
	for i in range(len(gsh_tof)): h_gsh_tof.Fill(gsh_tof[i])
	h_gsh_tof.GetXaxis().SetTitle("TimeOfFlight [ns]")
	h_gsh_tof.GetYaxis().SetTitle("Entry")
	h_gsh_tof.Draw()

	canvas.cd(4)
	h_msh_tof = TH1D("h_msh_tof","TimeOfFlight Distribution of ME0 SimHits", 10, 15, 35)
	for i in range(len(msh_tof)): h_msh_tof.Fill(msh_tof[i])
	h_msh_tof.GetXaxis().SetTitle("TimeOfFlight [ns]")
	h_msh_tof.GetYaxis().SetTitle("Entry")
	h_msh_tof.Draw()

	canvas.cd(5)
	h2_grh_xy = TH2D("h2_grh_xy","2D Distribution on RecHits (ch,eta)", 36, 1, 36, 8, 1, 9)
	for i in range(len(grh_ch)): h2_grh_xy.Fill(grh_ch[i],grh_ro[i])
	h2_grh_xy.GetXaxis().SetTitle("Chamber Number")
	h2_grh_xy.GetYaxis().SetTitle("Eta-partition Number")
	h2_grh_xy.Draw("colz")

	canvas.cd(6)
	h2_mrh_xy = TH2D("h2_mrh_xy","2D Distribution on RecHits (ch,eta)", 18, 1, 18, 8, 1, 9)
	for i in range(len(mrh_ch)): h2_mrh_xy.Fill(mrh_ch[i],mrh_ro[i])
	h2_mrh_xy.GetXaxis().SetTitle("Chamber Number")
	h2_mrh_xy.GetYaxis().SetTitle("Eta-partion Number")
	h2_mrh_xy.Draw("colz")

	canvas.cd(7)
	h_grh_err = TH1D("h_grh_err","Error Distribution of GEM RecHits", 10, 0., 50.)
	for i in range(len(grh_err)): h_grh_err.Fill(grh_err[i])
	h_grh_err.GetXaxis().SetTitle("Error [cm]")
	h_grh_err.GetYaxis().SetTitle("Entry")
	h_grh_err.Draw()

	canvas.cd(8)
	h_mrh_err = TH1D("h_mrh_err","Error Distribution of ME0 RecHits", 10, 0., 50.)
	for i in range(len(mrh_err)): h_mrh_err.Fill(mrh_err[i])
	h_mrh_err.GetXaxis().SetTitle("Error [cm]")
	h_mrh_err.GetYaxis().SetTitle("Entry")
	h_mrh_err.Draw()

	canvas.SaveAs("Offline_Validation.png")
	input("Press Enter to continue...")


if __name__ == '__main__':
        main(sys.argv[1])
