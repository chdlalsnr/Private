#!/usr/bin/python
from ROOT import *
import numpy as np
import sys

def main(target, reference):

	path1 = '/cms/ldap_home/chdlalsnr/' + target #Target->kBlack
        path2 = '/cms/ldap_home/chdlalsnr/Validation/Samples/' + reference #Reference->kRed

        if (target == 'CMSSW_11_2_0_pre1' or target == 'CMSSW_11_2_0_pre2' or target == 'CMSSW_11_2_0_pre3'):
                workflow1 = '/src/23211.0_TenMuExtendedE_0_200+TenMuExtendedE_0_200_pythia8_2026D49_GenSimHLBeamSpotFull+DigiFullTrigger_2026D49+RecoFullGlobal_2026D49+HARVESTFullGlobal_2026D49/'
        else:
                workflow1 = '/src/23211.0_TenMuExtendedE_0_200+2026D49+TenMuExtendedE_0_200_pythia8_GenSimHLBeamSpot+DigiTrigger+RecoGlobal+HARVESTGlobal/'

	if (reference == 'CMSSW_11_2_0_pre1' or reference == 'CMSSW_11_2_0_pre2' or reference == 'CMSSW_11_2_0_pre3'):
                workflow2 = '/23211.0_TenMuExtendedE_0_200+TenMuExtendedE_0_200_pythia8_2026D49_GenSimHLBeamSpotFull+DigiFullTrigger_2026D49+RecoFullGlobal_2026D49+HARVESTFullGlobal_2026D49/'
        else:
                workflow2 = '/23211.0_TenMuExtendedE_0_200+2026D49+TenMuExtendedE_0_200_pythia8_GenSimHLBeamSpot+DigiTrigger+RecoGlobal+HARVESTGlobal/'

        path1 += workflow1 + 'step3.root'
        path2 += workflow2 + 'step3.root'

	f1 = TFile(path1, "READ")
	f2 = TFile(path2, "READ")

	gem_sh1,gem_dg1,gem_rh1 = [],[],[]
	gem_sh2,gem_dg2,gem_rh2 = [],[],[]

	evt_num = 10
	for i in range(evt_num):
		f1.Events.GetEntry(i)

		temp_gsh = f1.Events.PSimHits_g4SimHits_MuonGEMHits_SIM.product()
#		temp_gdg = f1.Events.GEMDetIdGEMDigiMuonDigiCollection_muonGEMDigis__RECO.product()
		temp_grh = f1.Events.GEMDetIdGEMRecHitsOwnedRangeMap_gemRecHits__RECO.product()

		for j in range(temp_gsh.size()):
			gem_sh1.append(temp_gsh[j].localPosition().x())
#		for j in range(temp_gdg.__sizeof__()):
#			gem_dg1.append(temp_gdg.get(j))
		for j in range(temp_grh.size()):
			gem_rh1.append(temp_grh[j].hit().localPosition().x())

	for i in range(evt_num):
		f2.Events.GetEntry(i)

		temp_gsh = f2.Events.PSimHits_g4SimHits_MuonGEMHits_SIM.product()
#               temp_gdg = f2.Events.GEMDetIdGEMDigiMuonDigiCollection_muonGEMDigis__RECO.product()
                temp_grh = f2.Events.GEMDetIdGEMRecHitsOwnedRangeMap_gemRecHits__RECO.product()

		for j in range(temp_gsh.size()):
                        gem_sh2.append(temp_gsh[j].localPosition().x())
#                for j in range(temp_gdg.__sizeof__()):
#                        gem_dg2.append(temp_gdg)
                for j in range(temp_grh.size()):
                        gem_rh2.append(temp_grh[j].hit().localPosition().x())



	# SIMHIT
	hist_sh1 = TH1D("hist_sh1", "", 100, -50, 50)
	for i in range(len(gem_sh1)): hist_sh1.Fill(gem_sh1[i])
	hist_sh2 = TH1D("hist_sh2", "", 100, -50, 50)
	for i in range(len(gem_sh2)): hist_sh2.Fill(gem_sh2[i])

	crt_sh = 0.00001*hist_sh1.GetXaxis().GetBinCenter(hist_sh1.GetMaximumBin())
	hist_sh = hist_sh1 - hist_sh2
	bm_sh = hist_sh.GetMaximumBin()
	mp_sh = hist_sh.GetXaxis().GetBinCenter(bm_sh)
	if mp_sh >= crt_sh:
		print("*** Discrepancy occurred at SIMHIT step ***")
		sys.exit(0)
	elif mp_sh < crt_sh:
		print("*** There is no discrepancy at SIMHIT step ***")

#	# DIGI
#	hist_dg1 = TH1D("hist_dg1", "", 400, 0, 400)
#	for i in range(len(gem_dg1)): hist_dg1.Fill(gem_dg1[i])
#	hist_dg2 = TH1D("hist_dg2", "", 400, 0, 400)
#	for i in range(len(gem_dg2)): hist_dg2.Fill(gem_dg2[i])
#
#	hist_dg = hist_dg1 - hist_dg2
#	bm_dg = hist_dg.GetMaximumBin()
#	mp_dg = hist_dg.GetXaxis().GetBinCenter(bm_dg)
#	if mp_dg > 0.:
#		print("*** Discrepancy occurred at DIGI step ***")
#		return

	# RECHIT
	hist_rh1 = TH1D("hist_rh1", "", 100, -50, 50)
	for i in range(len(gem_rh1)): hist_rh1.Fill(gem_rh1[i])
	hist_rh2 = TH1D("hist_rh2", "", 100, -50, 50)
	for i in range(len(gem_rh2)): hist_rh2.Fill(gem_rh2[i])

	crt_rh = 0.00001*hist_rh1.GetXaxis().GetBinCenter(hist_rh1.GetMaximumBin())
	hist_rh = hist_rh1 - hist_rh2
	bm_rh = hist_rh.GetMaximumBin()
	mp_rh = hist_rh.GetXaxis().GetBinCenter(bm_rh)
	if mp_rh >= crt_rh:
		print("*** Discrepancy occurred at RECHIT step ***")
		sys.exit(0)
	elif mp_rh < crt_rh:
                print("*** There is no discrepancy at RECHIT step ***")


if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
