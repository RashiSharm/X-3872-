# This file was the first way to do sideband fitting, where I simply fit the humps in the Xmass, I thought I was doing the fit for upper and lower sidebands in X mass region. That is combined B Sideband.

import ROOT
import numpy as np
import sys
ROOT.gROOT.SetBatch(True)
lhcbFont = 132
lhcbWidth = 2.00
lhcbTSize = 0.06
ROOT.gStyle.SetTextFont(lhcbFont)
ROOT.gStyle.SetTextSize(lhcbTSize)

ROOT.gStyle.SetLabelFont(lhcbFont, "x")
ROOT.gStyle.SetLabelFont(lhcbFont, "y")
ROOT.gStyle.SetLabelFont(lhcbFont, "z")
ROOT.gStyle.SetLabelSize(lhcbTSize-0.02, "x")
ROOT.gStyle.SetLabelSize(lhcbTSize-0.02, "y")
ROOT.gStyle.SetLabelSize(lhcbTSize-0.02, "z")
ROOT.gStyle.SetTitleFont(lhcbFont)
ROOT.gStyle.SetTitleFont(lhcbFont, "x")
ROOT.gStyle.SetTitleFont(lhcbFont, "y")
ROOT.gStyle.SetTitleFont(lhcbFont, "z")
ROOT.gStyle.SetTitleSize(lhcbTSize, "x")
ROOT.gStyle.SetTitleSize(lhcbTSize, "y")
ROOT.gStyle.SetTitleSize(lhcbTSize, "z")
ROOT.gStyle.SetPaperSize(20, 26)
ROOT.gStyle.SetPadTopMargin(0.10)
ROOT.gStyle.SetPadRightMargin(0.05)
ROOT.gStyle.SetPadBottomMargin(0.16)
ROOT.gStyle.SetPadLeftMargin(0.14)
ROOT.gStyle.SetTitleOffset(0.95, "X")
ROOT.gStyle.SetTitleOffset(0.95, "Y")
ROOT.gStyle.SetTitleOffset(1.2, "Z")
ROOT.gStyle.SetTitleFillColor(0)
ROOT.gStyle.SetTitleStyle(0)
ROOT.gStyle.SetTitleBorderSize(0)
ROOT.gStyle.SetTitleFont(lhcbFont, "title")
ROOT.gStyle.SetTitleY(1.0)
ROOT.gStyle.SetTitleW(1.0)
ROOT.gStyle.SetTitleH(0.10)
ROOT.gStyle.SetHistMinimumZero(1)
ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/sumH.C')
ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/debug_R_NDoubleDSCBFit.C')
CB = ROOT.debug_R_NDoubleDSCBFit()

# current_directory = "/home/rsharm18/work/Rootfile/Mar_25/with_trigger_without_physDec"
current_directory = "/home/rsharm18/work/Rootfile/Apr_25/with_BDT_trained_on_X_MC"

user_choice = input("Enter 0 for Data , 1 to cc MC and 2 for X MC ")
nL = nR = -100
alphaL = -100
alphaR = -100
if user_choice == "0":
    input = "subreso-Data"
    mass = 3872
    B_pos = 120
    file_name = "/home/rsharm18/work/Rootfile/Data/subreso_Data.root"
    BDT_file = "/home/rsharm18/work/Rootfile/TMVA_Single_Entry_2_X_Data.root"
    sigma_B = 5.68
    sigma_X = 4.70
    output = "Data"
    Lower = 3679
    Upper = 3695
elif user_choice == "1":
    input = "subreso-cc_MC"
    mass = 3686
    B_pos = 100
    file_name = "/home/rsharm18/work/Rootfile/cc_MC/subreso_cc.root"
    BDT_file = "/home/rsharm18/work/Rootfile/TMVA_Single_Entry_2_X_cc_MC.root"
    sigma_B = 5.03
    sigma_X = 2.6
    output = "cc_MC"
    Lower = 3682
    Upper = 3692
elif user_choice == "2":
    input = "subreso-X_MC"
    mass = 3872
    B_pos = 11000
    file_name = "/home/rsharm18/work/Rootfile/X_MC/subreso_X.root"
    BDT_file = "/home/rsharm18/work/Rootfile/TMVA_Single_Entry_2_X_MC.root"
    sigma_B = 5.5
    sigma_X = 2.5
    output = "X_MC"
    Lower = 3682
    Upper = 3692
else:
    print("Invalid")        

file2 = ROOT.TFile.Open(f"{file_name}","READ")
def histo(file,particle):
    my_tree = file.Get("nTuple")
    my_tree.AddFriend("nTuple",f"{BDT_file}")

    Bp_Jpsi_B_M = my_tree.GetBranch("Bp_Jpsi_B_M")
    Bp_Jpsi_X_M = my_tree.GetBranch("Bp_Jpsi_X_M")
    nCandidate = my_tree.GetBranch("nCandidate")
    Bp_B_jpsi_pi2pi3 = my_tree.GetBranch("Bp_B_jpsi_pi2pi3")
    BDT = my_tree.GetBranch("BDT")

    Bp_L0DiMuonDecision_TOS = my_tree.GetBranch("Bp_L0DiMuonDecision_TOS")
    Bp_L0MuonDecision_TOS = my_tree.GetBranch("Bp_L0MuonDecision_TOS")
    Bp_Hlt1DiMuonHighMassDecision_TOS = my_tree.GetBranch("Bp_Hlt1DiMuonHighMassDecision_TOS")
    Bp_Hlt1TrackMuonDecision_TOS = my_tree.GetBranch("Bp_Hlt1TrackMuonDecision_TOS")
    Bp_Hlt1TrackMVADecision_TOS = my_tree.GetBranch("Bp_Hlt1TrackMVADecision_TOS")
    Bp_Hlt2DiMuonDetachedJPsiDecision_TOS = my_tree.GetBranch("Bp_Hlt2DiMuonDetachedJPsiDecision_TOS")
    Bp_Hlt2Phys_TOS = my_tree.GetBranch("Bp_Hlt2Phys_TOS")
    Bp_Hlt1Phys_TOS = my_tree.GetBranch("Bp_Hlt1Phys_TOS")
    
    ## Histograms    
    histo_B_mass_signal = ROOT.TH1F("B_mass_Jpsi_Constrained_sub"," ", 200, 5100, 5500)
    histo_X_mass_signal = ROOT.TH1F("X_mass_Jpsi_Constrained_sub"," ", 150, 3650, 3950)
    if input == '0':
      if particle == 'X':  
        histo_X_mass_sideband_sub = ROOT.TH1F("B_mass_Sideband_sub"," ", 275, 3700, 4000)  
      else: 
        histo_X_mass_sideband_sub = ROOT.TH1F("B_mass_Sideband_sub"," ", 275, 3400, 3950)      
    
    elif input == '1':
      histo_X_mass_sideband_sub = ROOT.TH1F("B_mass_Sideband_sub"," ", 275, 3400, 3950)
    elif input == '2':
      histo_X_mass_sideband_sub = ROOT.TH1F("B_mass_Sideband_sub"," ", 275, 3750, 4100)

    if particle == 'X':  
      histo_X_mass_sideband_sub = ROOT.TH1F("B_mass_Sideband_sub"," ", 100, 3700, 4000)  
    else: 
      histo_X_mass_sideband_sub = ROOT.TH1F("B_mass_Sideband_sub"," ", 275, 3400, 3950)     

    for entry in my_tree:
        branch_value_B = Bp_Jpsi_B_M.GetLeaf("Bp_Jpsi_B_M").GetValue()
        branch_value_cut = Bp_Jpsi_X_M.GetLeaf("Bp_Jpsi_X_M").GetValue()
        nCandidates_cut = nCandidate.GetLeaf("nCandidate").GetValue()
        branch_value_X = Bp_Jpsi_X_M.GetLeaf("Bp_Jpsi_X_M").GetValue()
        Jpsi_reflection = Bp_B_jpsi_pi2pi3.GetLeaf("Bp_B_jpsi_pi2pi3").GetValue()
        BDT_value = BDT.GetLeaf("BDT").GetValue()
        
        L01 = Bp_L0DiMuonDecision_TOS.GetLeaf("Bp_L0DiMuonDecision_TOS").GetValue()
        L02 = Bp_L0MuonDecision_TOS.GetLeaf("Bp_L0MuonDecision_TOS").GetValue()
        
        Hlt1_1 = Bp_Hlt1DiMuonHighMassDecision_TOS.GetLeaf("Bp_Hlt1DiMuonHighMassDecision_TOS").GetValue()

        Hlt1_3 = Bp_Hlt1TrackMuonDecision_TOS.GetLeaf("Bp_Hlt1TrackMuonDecision_TOS").GetValue()
        Hlt1_4 = Bp_Hlt1TrackMVADecision_TOS.GetLeaf("Bp_Hlt1TrackMVADecision_TOS").GetValue()

        Hlt2_1 = Bp_Hlt2DiMuonDetachedJPsiDecision_TOS.GetLeaf("Bp_Hlt2DiMuonDetachedJPsiDecision_TOS").GetValue()
       

        ## trigger requirements and (Hlt1_1 or Hlt1_2 or Hlt1_3 or Hlt1_4 ) and (Hlt2_1 or Hlt2_2)
        
        if (L01 or L02) and (Hlt1_1 or Hlt1_3 or Hlt1_4 ) and (Hlt2_1) and (BDT_value>0.0296) : 
          if (abs(branch_value_cut-mass) < 2.0*sigma_X) and (nCandidates_cut == 0) and  ((Lower>Jpsi_reflection or Jpsi_reflection>Upper)):
                histo_B_mass_signal.Fill(branch_value_B)
          if (abs(branch_value_B-5280) < 2.0*sigma_B) and (nCandidates_cut == 0) and ((Lower>Jpsi_reflection or Jpsi_reflection>Upper)):
                histo_X_mass_signal.Fill(branch_value_X)
          ## sideband without reflections
          if (abs(branch_value_B-5280) > 4.0*sigma_B) and (abs(branch_value_B-5280) < 10.0*sigma_B) and (nCandidates_cut == 0) and ((Lower>Jpsi_reflection or Jpsi_reflection>Upper)):
                  histo_X_mass_sideband_sub.Fill(branch_value_X)
      
    del my_tree  
    return  histo_B_mass_signal, histo_X_mass_signal, histo_X_mass_sideband_sub

histo_B_mass_signal, histo_X_mass_signal, histo_X_mass_sideband_sub = histo(file2,'K')

c = ROOT.TCanvas()
c.cd()
c.SetFrameLineWidth(2)
t_B = ROOT.TLatex(5290,140,"B")

if user_choice == "0":
 #signal
 Fit_B_sig = CB.fit(histo_B_mass_signal,5100,5500,44,5279,3.22,-10,1.0,-10,1.0,2)
 Fit_X_sig = CB.fit_2(histo_X_mass_signal,3400,3940,9.1E3,3686,2.6,-10,-1.40,-10.,-1.6155,44,3871.85,4.0,-10,-1.61564,-10.,-1.87239,2)
 
 #fitting both sidebands simulatneously for psi2S
 Fit_X_SB = CB.fit(histo_X_mass_sideband_sub,3750,3950,44,-3871.852,-3.118,-10,-1.61564,-10,-1.87239,2)

 c3 = ROOT.TCanvas()
 c3.cd()
 c3.SetFrameLineWidth(2)
 
 amp2 = Fit_X_SB.GetParameter(0)
 mass2 = Fit_X_SB.GetParameter(1)
 sigma2 = Fit_X_SB.GetParameter(2)
 ampE2 = Fit_X_SB.GetParError(0)
 massE2 = Fit_X_SB.GetParError(1)
 sigmaE2 = Fit_X_SB.GetParError(2)
 text = ROOT.TPaveText(0.6, 0.6, 0.9, 0.9, "NDC")
 text.SetTextAlign(12)
 text.SetTextSize(0.03)
 text.SetFillStyle(0)
 text.SetBorderSize(0)
 sb0 = text.AddText(f"N = {(amp2):.2f} #pm {ampE2:.2f}")
 sb1 = text.AddText(f"m = {mass2:.2f} #pm {massE2:.2f}") 
 sb2 = text.AddText(f"#sigma = {sigma2:.2f} #pm {sigmaE2:.2f}")
   
 
 histo_X_mass_sideband_sub.GetXaxis().SetRangeUser(3750,3950)
 histo_X_mass_sideband_sub.GetYaxis().SetTitle(f"Number Of Candidates/{histo_X_mass_sideband_sub.GetXaxis().GetBinWidth(1)} MeV")
#  histo_X_mass_sideband_sub.GetYaxis().SetTitle(f"Number Of Candidates MeV")
 histo_X_mass_sideband_sub.GetXaxis().SetTitle("m(J/#psi#pi^{+}#pi^{-}) [MeV]")
 histo_X_mass_sideband_sub.SetMarkerStyle(20) 
 histo_X_mass_sideband_sub.SetLineWidth(2)
 histo_X_mass_sideband_sub.SetMarkerSize(0.1)
 histo_X_mass_sideband_sub.SetMarkerColor(1)
 histo_X_mass_sideband_sub.SetLineColor(1)
 histo_X_mass_sideband_sub.GetYaxis().SetRangeUser(0,120)
# histo_X_mass_sideband_sub_2.Draw()
# histo_X_mass_sideband_sub_2.SetLineColor(2)
 histo_X_mass_sideband_sub.Draw('E')
 text.Draw("same")

 c3.SaveAs(f"{current_directory}/{output}/sideband_fit_Data_X.pdf")
 c3.SaveAs(f"{current_directory}/{output}/sideband_fit_Data_X.root")
#  Fit_X_SB = CB.fit_2(histo_X_mass_sideband_sub,3750,3950,44,-3686,2.6,-10,4.0,-10.,1.0,44,3871.85,4.0,2)
 
 histo_X_mass_sideband_sub.GetXaxis().SetRangeUser(3400,3950)
 Fit_psi2S_SB = CB.fit_2(histo_X_mass_sideband_sub,3550,3950,44,-3671.428,24.515,nL,alphaL,nR,alphaR,44,-3686.197,-1.990,-10,-1.40,-10.,-1.6155,2)

elif user_choice == "1":
 #signal
 Fit_B_sig = CB.fit(histo_B_mass_signal,5100,5500,44,5279,3.22,-10,1.0,-10,1.0,2)
 Fit_X_sig = CB.fit(histo_X_mass_signal,3600,3940,9.1E3,3686,5.0,-10,1.0,-10.,1.0,2)
 
#fitting both sidebands simulatneously 
 Fit_psi2S_SB = CB.fit_2(histo_X_mass_sideband_sub,3550,3850,44,3660,9.0,nL,alphaL,nR,alphaR,44,-3686.197,-1.990,-10,-1.40,-10.,-1.6155,2)
 
elif user_choice == "2":
 # signal
 Fit_B_sig = CB.fit(histo_B_mass_signal,5100,5500,44,5279,3.22,-10,1.0,-10,1.0,2)
 Fit_X_sig = CB.fit(histo_X_mass_signal,3600,3940,44,3871.85,3.0,-10,1.0,-10.,1.0,2)
 
#fitting both sidebands simulatneously 
 Fit_X_SB = CB.fit_2(histo_X_mass_sideband_sub,3750,3950,44,3850,9.0,nL,alphaL,nR,alphaR,44,-3871.852,-3.118,-10,-1.61564,-10,-1.87239,2)
else:
    print("Invalid")     

amp_B_S = Fit_B_sig.GetParameter(0)
mass_B_S = Fit_B_sig.GetParameter(1)
sigma_B_S = Fit_B_sig.GetParameter(2)
amp_B_S_E = Fit_B_sig.GetParError(0)
mass_B_S_E = Fit_B_sig.GetParError(1)
sigma_B_S_E = Fit_B_sig.GetParError(2)

c0 = ROOT.TCanvas("c0","B signal")
c0.cd()
c0.SetFrameLineWidth(2)
t_B = ROOT.TLatex(5290,B_pos,"B")

text_B = ROOT.TPaveText(0.6, 0.7, 0.8, 0.9, "NDC")
text_B.SetTextAlign(12)
text_B.SetTextSize(0.03)
text_B.SetFillStyle(0)
text_B.SetBorderSize(0)

t0 = text_B.AddText(f"N = {amp_B_S:.2f} #pm {amp_B_S_E:.2f}")
t1 = text_B.AddText(f"m = {mass_B_S:.2f} #pm {mass_B_S_E:.2f}")
t2 = text_B.AddText(f"#sigma = {sigma_B_S:.2f} #pm {sigma_B_S_E:.2f}")


histo_B_mass_signal.GetYaxis().SetTitle(f"Candidates/{histo_B_mass_signal.GetBinWidth(1)} [MeV]")
histo_B_mass_signal.GetXaxis().SetTitle("m(J/#psi#pi^{+}#pi^{-}K^{+}#pi^{+}#pi^{-}) [MeV]")
histo_B_mass_signal.SetMarkerStyle(20)
histo_B_mass_signal.SetLineWidth(2)
histo_B_mass_signal.Draw('E')
t_B.Draw()
legendB = ROOT.TLegend(0.8, 0.75, 0.9, 0.85)
legendB.AddEntry(histo_B_mass_signal, "Data")
legendB.AddEntry(Fit_B_sig, "Fit")
legendB.SetBorderSize(0)
# legendB.Draw()
text_B.Draw()
c0.SaveAs(f"{current_directory}/{output}/B_mass-in_X_Signal_{input}.root")
c0.SaveAs(f"{current_directory}/{output}/B_mass-in_X_Signal_{input}.pdf")

# bkg deconstruction
Fit_B_sig.SetLineColor(4)
Fit_B_sig.DrawCopy("SAME")
Fit_B_sig.SetParameter(0,0)
Fit_B_sig.SetLineColor(6)
Fit_B_sig.SetLineStyle(2)
Fit_B_sig.DrawCopy("SAME")
Fit_B_sig.SetParameter(10,0)
Fit_B_sig.SetParameter(11,0)
Fit_B_sig.SetParameter(0,amp_B_S)
Fit_B_sig.SetLineColor(3)
Fit_B_sig.SetLineStyle(2)
Fit_B_sig.DrawCopy("SAME")

c0.SaveAs(f"{current_directory}/{output}/Separated_B_mass-in_X_Signal_{input}.pdf")



amp_X_S = Fit_X_sig.GetParameter(0)
mass_X_S = Fit_X_sig.GetParameter(1)
sigma_X_S = Fit_X_sig.GetParameter(2)
amp_X_S_E = Fit_X_sig.GetParError(0)
mass_X_S_E = Fit_X_sig.GetParError(1)
sigma_X_S_E = Fit_X_sig.GetParError(2)

amp_X_S_1 = Fit_X_sig.GetParameter(7)
mass_X_S_1 = Fit_X_sig.GetParameter(8)
sigma_X_S_1 = Fit_X_sig.GetParameter(9)
amp_X_S_E_1 = Fit_X_sig.GetParError(7)
mass_X_S_E_1 = Fit_X_sig.GetParError(8)
sigma_X_S_E_1 = Fit_X_sig.GetParError(9)

c1 = ROOT.TCanvas("c1","X Mass signal")
c1.cd()
c1.SetFrameLineWidth(2)
t_psi2S = ROOT.TLatex(3700,2200,"#psi(2S)")
t_X = ROOT.TLatex(3890,200,"X(3872)")

text_X = ROOT.TPaveText(0.6, 0.6, 0.8, 0.8, "NDC")
text_X.SetTextAlign(12)
text_X.SetTextSize(0.03)
text_X.SetFillStyle(0)
text_X.SetBorderSize(0)
if user_choice == "0":
  x0 = text_X.AddText(f"N(#psi(2S)) = {amp_X_S:.2f} #pm {amp_X_S_E:.2f}")
  x1 = text_X.AddText(f"m(#psi(2S)) = {mass_X_S:.2f} #pm {mass_X_S_E:.2f}")
  x2 = text_X.AddText(f"#sigma(#psi(2S)) = {sigma_X_S:.2f} #pm {sigma_X_S_E:.2f}")
  x3 = text_X.AddText(f"N(X(3872)) = {amp_X_S_1:.2f} #pm {amp_X_S_E_1:.2f}")
  x4 = text_X.AddText(f"m(X(3872)) = {mass_X_S_1:.2f} #pm {mass_X_S_E_1:.2f}")
  x5 = text_X.AddText(f"#sigma(X(3872)) = {sigma_X_S_1:.2f} #pm {sigma_X_S_E_1:.2f}")
elif user_choice == "1":
  x0 = text_X.AddText(f"N(#psi(2S)) = {amp_X_S:.2f} #pm {amp_X_S_E:.2f}")
  x1 = text_X.AddText(f"m(#psi(2S)) = {mass_X_S:.2f} #pm {mass_X_S_E:.2f}")
  x2 = text_X.AddText(f"#sigma(#psi(2S)) = {sigma_X_S:.2f} #pm {sigma_X_S_E:.2f}")
elif user_choice == "2":
  x3 = text_X.AddText(f"N(X(3872)) = {amp_X_S:.2f} #pm {amp_X_S_E:.2f}")
  x4 = text_X.AddText(f"m(X(3872)) = {mass_X_S:.2f} #pm {mass_X_S_E:.2f}")
  x5 = text_X.AddText(f"#sigma(X(3872)) = {sigma_X_S:.2f} #pm {sigma_X_S_E:.2f}")
histo_X_mass_signal.GetYaxis().SetTitle(f"Candidates/{histo_X_mass_signal.GetXaxis().GetBinWidth(1)} [MeV]")
histo_X_mass_signal.GetXaxis().SetTitle("m(J/#psi#pi^{+}#pi^{-}) [MeV]")
histo_X_mass_signal.SetMarkerStyle(20)
histo_X_mass_signal.SetLineWidth(2)
histo_X_mass_signal.Draw('E')
t_psi2S.Draw()
legendX = ROOT.TLegend(0.8, 0.75, 0.9, 0.85)
legendX.AddEntry(histo_X_mass_signal, "Data")
legendX.AddEntry(Fit_X_sig, "Fit")
legendX.SetBorderSize(0)
# legendX.Draw()
t_X.Draw()
text_X.Draw()
c1.SaveAs(f"{current_directory}/{output}/X_mass-in_B_Signal_{input}.root")
c1.SaveAs(f"{current_directory}/{output}/X_mass-in_B_Signal_{input}.pdf")


Fit_X_sig.SetLineColor(4)
Fit_X_sig.DrawCopy("SAME")
Fit_X_sig.SetParameter(0,0)
Fit_X_sig.SetParameter(7,0)
Fit_X_sig.SetLineColor(6)
Fit_X_sig.SetLineStyle(2)
Fit_X_sig.DrawCopy("SAME")
# Fit_X_sig.SetParameter(0,amp_X_S)
# Fit_X_sig.SetParameter(7,0)
# Fit_X_sig.SetLineColor(4)
# Fit_X_sig.SetLineStyle(1)
# Fit_X_sig.DrawCopy("SAME")

Fit_X_sig.SetParameter(10,0)
Fit_X_sig.SetParameter(11,0)
Fit_X_sig.SetParameter(12,0)
Fit_X_sig.SetParameter(0,amp_X_S)
Fit_X_sig.SetParameter(7,amp_X_S_1)
Fit_X_sig.SetLineColor(3)
Fit_X_sig.SetLineStyle(2)
Fit_X_sig.DrawCopy("SAME")
# Fit_X_sig.SetParameter(7,amp_X_S_1)
# Fit_X_sig.SetParameter(0,amp_X_S)
# Fit_X_sig.SetLineColor(2)
# Fit_X_sig.SetLineStyle(1)
# Fit_X_sig.DrawCopy("SAME")
# Fit_X_sig.SetParameter(10,0)
# Fit_X_sig.SetParameter(11,0)
# Fit_X_sig.SetLineColor(2)
# Fit_X_sig.SetLineStyle(2)
# Fit_X_sig.DrawCopy("SAME")

c1.SaveAs(f"{current_directory}/{output}/Separated_X_mass-in_B_Signal_{input}.pdf")
if (user_choice == "0"):
  histo_X_mass_signal.GetXaxis().SetRangeUser(3840,3940)
  c1.SaveAs(f"{current_directory}/{output}/Zoomed_Separated_X_mass-in_B_Signal_{input}.pdf")

ROOT.gPad.WaitPrimitive()

def sideband(histogram, fit, canvas_name, particle,user_choice):
    print(fit.GetParameter(0))
    print(fit.GetParError(0))
    c2 = ROOT.TCanvas("c2",f"{canvas_name}")
    c2.cd()
    c2.SetFrameLineWidth(2)

    if user_choice == "1":
      text = ROOT.TPaveText(0.6, 0.6, 0.9, 0.9, "NDC")
    elif user_choice == "2":
      text = ROOT.TPaveText(0.3, 0.6, 0.6, 0.9, "NDC")
    else:
      text = ROOT.TPaveText(0.6, 0.6, 0.9, 0.9, "NDC")

    text.SetTextAlign(12)
    text.SetTextSize(0.03)
    text.SetFillStyle(0)
    text.SetBorderSize(0)

    amp1 = fit.GetParameter(0)
    mass1 = fit.GetParameter(1)
    sigma1 = fit.GetParameter(2)
    ampE1 = fit.GetParError(0)
    massE1 = fit.GetParError(1)
    sigmaE1 = fit.GetParError(2)

    amp2 = fit.GetParameter(7)
    mass2 = fit.GetParameter(8)
    sigma2 = fit.GetParameter(9)
    ampE2 = fit.GetParError(7)
    massE2 = fit.GetParError(8)
    sigmaE2 = fit.GetParError(9)

    if user_choice == "0":
      sb0 = text.AddText(f"N = {(amp2):.2f} #pm {ampE2:.2f}")
      sb1 = text.AddText(f"m = {mass2:.2f} #pm {massE2:.2f}") 
      sb2 = text.AddText(f"#sigma = {sigma2:.2f} #pm {sigmaE2:.2f}")
    if user_choice == "1":
      sb3 = text.AddText(f"N(#psi(2S)) = {amp2:.2f} #pm {ampE2:.2f}")
      sb4 = text.AddText(f"m(#psi(2S)) = {mass2:.2f} #pm {massE2:.2f}")
      sb5 = text.AddText(f"#sigma(#psi(2S)) = {sigma2:.2f} #pm {sigmaE2:.2f}")
    elif user_choice == "2" :
      sb3 = text.AddText(f"N(X(3872)) = {amp2:.2f} #pm {ampE2:.2f}")
      sb4 = text.AddText(f"m(X(3872)) = {mass2:.2f} #pm {massE2:.2f}")
      sb5 = text.AddText(f"#sigma(X(3872)) = {sigma2:.2f} #pm {sigmaE2:.2f}") 
    else:
      exit 

    histogram.GetYaxis().SetTitle(f"Candidates/{histogram.GetXaxis().GetBinWidth(1)}MeV")
    histogram.GetXaxis().SetTitle("m(J/#psi#pi^{+}#pi^{-}) [MeV]")
    histogram.SetMarkerStyle(20)
    histogram.SetMarkerSize(0.1)
    # histo_X_mass_sideband_sub_sub.SetMarkerStyle(20)
    histogram.SetLineWidth(2)
    histogram.SetMarkerColor(1)
    histogram.SetLineColor(1)
    histogram.Draw('E')
    text.Draw("same")
    c2.SaveAs(f"{current_directory}/{output}/sideband_fit_{input}_{particle}.root")
    
    fitval_0 = fit.GetParameter(0)
    fitval_7 = fit.GetParameter(7)
    fit.SetLineColor(4)
    fit.DrawCopy("SAME")
    fit.SetParameter(0,0)
    fit.SetParameter(7,0)
    fit.SetParameter(10,fit.GetParameter(10))
    fit.SetParameter(11,fit.GetParameter(11))
    fit.SetLineColor(7)
    fit.SetLineStyle(2)
    fit.DrawCopy("SAME")
    fit.SetParameter(0,fitval_0)
    fit.SetParameter(10,0)
    fit.SetParameter(11,0)
    fit.SetParameter(12,0)
    fit.SetLineColor(8)
    fit.SetLineStyle(2)
    fit.DrawCopy("SAME")
    fit.SetParameter(0,0)
    fit.SetParameter(7,fitval_7)
    fit.SetLineColor(6)
    fit.SetLineStyle(2)
    fit.DrawCopy("SAME")
    # ROOT.gPad.WaitPrimitive()
    # t_psi2S.Draw()
    # t_X.Draw()
    # legendX.Draw()
    histogram.GetYaxis().SetRangeUser(0,2700)
    histogram.GetXaxis().SetRangeUser(3650,3950)
    c2.SaveAs(f"{current_directory}/{output}/sideband_fit_{input}_{particle}.pdf")
    if user_choice == "1":
      histogram.GetXaxis().SetRangeUser(3500,3900)
      c2.SaveAs(f"{current_directory}/{output}/Zoomed_sideband_fit_{input}_{particle}.pdf")
    elif user_choice == "2":  
      histogram.GetXaxis().SetRangeUser(3750,3950)
      c2.SaveAs(f"{current_directory}/{output}/Zoomed_sideband_fit_{input}_{particle}.pdf")
    else:
      exit
    ROOT.gPad.WaitPrimitive()

    hump = amp1
    hump_err = ampE1
    peak = amp2
    peak_err = ampE2
    del histogram
    del text
    del c2
    return hump, hump_err, peak, peak_err


if user_choice == '0':
  hump_psi2S, hump_err_psi2S, peak_psi2S, peak_err_psi2S = sideband(histo_X_mass_sideband_sub,Fit_psi2S_SB, 'SB at psi2S','psi2S',user_choice)
  # hump_X, hump_err_X, peak_X, peak_err_X = sideband(histo_X_mass_sideband_sub,Fit_X_SB, 'SB at X','X')

  Psi_2S_Net_Yield = amp_X_S - (1/3.0)*(peak_psi2S)
  Psi_2S_Net_Yield_Error = np.sqrt(np.power(amp_X_S_E,2) + (1/9.0)*np.power(peak_err_psi2S,2))
  psi2S_significance = Psi_2S_Net_Yield/Psi_2S_Net_Yield_Error

  X_Net_Yield = amp_X_S_1 - (1/3.0)*(amp2)
  X_Net_Yield_Error = np.sqrt(np.power(amp_X_S_E_1,2) + (1/9.0)*np.power(ampE2,2))
  X_significance = X_Net_Yield/X_Net_Yield_Error

  f = open(f"{current_directory}/{output}/Data_significance.txt",'w')
  original_stdout = sys.stdout
  sys.stdout = f
  print("#############################################################################################################", file=f)
  print("                B+ signal         B+ sideband              Net Yield                Significance", file=f)
  print(" Psi(2S)  ", round(amp_X_S,2) ,u"\u00B1", round(amp_X_S_E,2),"      ", round(peak_psi2S,2),u"\u00B1",round(peak_err_psi2S,2), "        ",round(Psi_2S_Net_Yield,2),u"\u00B1",round(Psi_2S_Net_Yield_Error,2),"       ",round(psi2S_significance,2), file=f)
  print("                                                                                                                                                                                ", file=f)
  print(" X(3872)   ",  round(amp_X_S_1,2) ,u"\u00B1", round(amp_X_S_E_1,2),"        ", round(amp2,2),u"\u00B1",round(ampE2,2), "         ",round(X_Net_Yield,2),u"\u00B1",round(X_Net_Yield_Error,2),"         ",round(X_significance,2), file=f )
  print("#############################################################################################################", file=f)

  print("psi2S significance = ",psi2S_significance, file=f)
  print("X significance = ",X_significance,file=f)
  print("Rate = ", (X_Net_Yield/Psi_2S_Net_Yield)*0.802*0.98, u"\u00B1" , ((X_Net_Yield/Psi_2S_Net_Yield)*0.802*0.98)*np.sqrt(np.power(X_Net_Yield_Error/X_Net_Yield,2)+np.power(Psi_2S_Net_Yield_Error/Psi_2S_Net_Yield,2)))
  sys.stdout = original_stdout
  f.close()


elif user_choice == '1':
  hump_psi2S, hump_err_psi2S, peak_psi2S, peak_err_psi2S = sideband(histo_X_mass_sideband_sub,Fit_psi2S_SB, 'SB at psi2S MC','psi2S',user_choice)

  Psi_2S_Net_Yield = amp_X_S - (1/3.0)*(peak_psi2S)
  Psi_2S_Net_Yield_Error = np.sqrt(np.power(amp_X_S_E,2) + (1/9.0)*np.power(peak_err_psi2S,2))
  psi2S_significance = Psi_2S_Net_Yield/Psi_2S_Net_Yield_Error

  f = open(f"{current_directory}/{output}/cc_MC_significance.txt",'w')
  original_stdout = sys.stdout
  sys.stdout = f
  print("#############################################################################################################",file=f)
  print("                B+ signal                B+ sideband              Net Yield                Significance",file=f)
  print(" Psi(2S)  ", round(amp_X_S,2) ,u"\u00B1", round(amp_X_S_E,2),"      ", round(peak_psi2S,2),u"\u00B1",round(peak_err_psi2S,2), "        ",round(Psi_2S_Net_Yield,2),u"\u00B1",round(Psi_2S_Net_Yield_Error,2),"       ",round(psi2S_significance,2) ,file=f)
  print("#############################################################################################################",file=f)
 
  print(psi2S_significance,file=f)
  sys.stdout = original_stdout
  f.close()

elif user_choice == '2':
  hump_X, hump_err_X, peak_X, peak_err_X = sideband(histo_X_mass_sideband_sub,Fit_X_SB, 'SB at X MC','X',user_choice)
 
  X_Net_Yield = amp_X_S - (1/3.0)*(peak_X)
  X_Net_Yield_Error = np.sqrt(np.power(amp_X_S_E,2) + (1/9.0)*np.power(peak_err_X,2))
  X_significance = X_Net_Yield/X_Net_Yield_Error

  f = open(f"{current_directory}/{output}/X_MC_significance.txt",'w')
  original_stdout = sys.stdout
  sys.stdout = f    
  print("#############################################################################################################",file=f)
  print("                B+ signal                B+ sideband              Net Yield                Significance",file=f)
  print(" X(3872)   ",  round(amp_X_S,2) ,u"\u00B1", round(amp_X_S_E,2),"        ", round(peak_X,2),u"\u00B1",round(peak_err_X,2), "         ",round(X_Net_Yield,2),u"\u00B1",round(X_Net_Yield_Error,2),"         ",round(X_significance,2) ,file=f)
  print("#############################################################################################################",file=f)
  print(X_significance,file=f) 
  sys.stdout = original_stdout
  f.close()

del histo_B_mass_signal
del histo_X_mass_signal
del histo_X_mass_sideband_sub
del legendX
del legendB
del text_X
del text_B
del c1
del c0
del t_X
del t_B
del t_psi2S
del c
del file2
del CB

