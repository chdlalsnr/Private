#!/usr/bin/python
from ROOT import *
import numpy as np
import sys

def main(target, reference):

	path1 = '/cms/ldap_home/chdlalsnr/Validation/Samples/' + target #Target->kBlack
	path2 = '/cms/ldap_home/chdlalsnr/Validation/Samples/' + reference #Reference->kRed

	if (release == 'CMSSW_11_2_0_pre1' or release == 'CMSSW_11_2_0_pre2' or release == 'CMSSW_11_2_0_pre3'):
                workflow = '/23211.0_TenMuExtendedE_0_200+TenMuExtendedE_0_200_pythia8_2026D49_GenSimHLBeamSpotFull+DigiFullTrigger_2026D49+RecoFullGlobal_2026D49+HARVESTFullGlobal_2026D49/'
        else:
                workflow = '/23211.0_TenMuExtendedE_0_200+2026D49+TenMuExtendedE_0_200_pythia8_GenSimHLBeamSpot+DigiTrigger+RecoGlobal+HARVESTGlobal/'

	path1 += workflow + 'DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root'
	path2 += workflow + 'DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root'

	#histpath = 'DQMData/Run 1/MuonGEMDigisV/Run summary/GEMDigisTask/Strip/Occupancy/matched_strip_occ_eta_re1'
	#histpath = 'DQMData/Run 1/MuonGEMHitsV/Run summary/GEMHitsTask/TimeOfFlight/tof_muon_st1'
	#histpath = 'DQMData/Run 1/MuonGEMRecHitsV/Run summary/GEMRecHitsTask/Occupancy/muon_simhit_occ_phi_re1_st1'
	#histpath = 'DQMData/Run 1/MuonME0DigisV/Run summary/ME0DigisTask/me0_strip_dg_dx_local1_l1'
	#histpath = 'DQMData/Run 1/MuonME0HitsV/Run summary/ME0HitsTask/me0_sh_tofMuon_r1_l1'
	#histpath = 'DQMData/Run 1/MuonME0RecHitsV/Run summary/ME0RecHitsTask/me0_rh_PullX_r1_l1'
	#histpath = 'DQMData/Run 1/MuonME0RecHitsV/Run summary/ME0RecHitsTask/me0_rh_PullY_r1_l1'
	#histpath = 'DQMData/Run 1/MuonME0RecHitsV/Run summary/ME0RecHitsTask/me0_rh_DeltaX_r1_l1'
        histpath = 'DQMData/Run 1/MuonME0RecHitsV/Run summary/ME0RecHitsTask/me0_rh_DeltaY_r1_l1'

	root_file1 = TFile(path1, "READ")
	root_file2 = TFile(path2, "READ")
	hist1 = root_file1.Get(histpath)
	hist2 = root_file2.Get(histpath)
	hist3 = hist1 - hist2 #Residual = target - reference

	binmax1 = hist1.GetMaximumBin()
	mp1 = hist1.GetXaxis().GetBinCenter(binmax1)
	binmax2 = hist2.GetMaximumBin()
	mp2 = hist2.GetXaxis().GetBinCenter(binmax2)

	c1 = TCanvas('c1', '', 900, 600)
#	pad1 = TPad("pad1", "", 0.0, 0.3, 1.0, 1.0)
#	pad1.SetBottomMargin(0.1)
#	pad1.SetGridx()
#
#	pad2 = TPad("pad2", "", 0.0, 0.05, 1.0, 0.3)
#	pad2.SetTopMargin(0)
#	pad2.SetBottomMargin(0.2)
#	pad2.SetGridx()

	hist1.SetLineColor(kBlack)
	hist2.SetLineColor(kRed)

	if (mp1 < mp2):
		hist1.Draw()
		hist2.Draw('same')

	if (mp2 < mp1):
		hist2.Draw()
		hist1.Draw('same')

	c1.Draw()
	c1.SaveAs(hist1.GetName()+'.png')

	c2 = TCanvas('c2', '', 900, 600)
	hist3.Draw()
	hist3.SetLineColor(kBlue)
	if (hist3.GetXaxis().GetBinCenter(hist3.GetMaximumBin())!=0):
		hist3.SetLineColor(kRed)
	c2.Draw()
	c2.SaveAs(hist1.GetName()+'_residual.png')

	input("Press Enter to continue...")


if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])

