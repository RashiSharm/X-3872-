# This file was the first way to do sideband fitting, where I simply fit the humps in the Xmass, I thought I was doing the fit for upper and lower sidebands in X mass region. That is combined B Sideband.

import ROOT
import numpy as np
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

# current_directory = "/home/rsharm18/work/Rootfile/final/Simultaneous_sideband"
current_directory = "/home/rsharm18/work/Rootfile/Jan_25"
user_choice = input("Enter 0 for Data , 1 to cc MC and 2 for X MC ")
nL = nR = -100
alphaL = -100
alphaR = -100
if user_choice == "0":
    input = "subreso-Data"
    mass = 3872
    B_pos = 120
    file_name = "./../Data/subreso_Data.root"
    sigma_B = 5.68
    sigma_X = 4.70
    output = "Data"
    Lower = 3679
    Upper = 3695
elif user_choice == "1":
    input = "subreso-cc_MC"
    mass = 3872
    B_pos = 100
    file_name = "./../cc_MC/subreso_cc.root"
    sigma_B = 5.03
    sigma_X = 2.6
    output = "cc_MC"
    Lower = 3682
    Upper = 3692
elif user_choice == "2":
    input = "subreso-X_MC"
    mass = 3872
    B_pos = 11000
    file_name = "./../X_MC/subreso_X.root"
    sigma_B = 5.5
    sigma_X = 2.5
    output = "X_MC"
    Lower = 3864
    Upper = 3880
else:
    print("Invalid")        

file2 = ROOT.TFile.Open(f"{file_name}","READ")
def histo(file,particle):
    my_tree = file.Get("nTuple")

    Bp_Jpsi_B_M = my_tree.GetBranch("Bp_Jpsi_B_M")
    Bp_Jpsi_X_M = my_tree.GetBranch("Bp_Jpsi_X_M")
    nCandidate = my_tree.GetBranch("nCandidate")
    Bp_B_jpsi_pi2pi3 = my_tree.GetBranch("Bp_B_jpsi_pi2pi3")


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
        ## signal without reflections
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
 Fit_B_sig = CB.fit(histo_B_mass_signal,5100,5500,44,5279,6.44,-10,1.0,-10,1.0,2)
 Fit_X_sig = CB.fit(histo_X_mass_signal,3600,3940,9.1E3,3686,2.6,-10,1.0,-10.,1.0,44,3871.85,4.0,2)
 
 #fitting both sidebands simulatneously for psi2S
 Fit_psi2S_SB = CB.fit_SB(histo_X_mass_sideband_sub,3550,3850,44,-3671.428,-24.515,nL,alphaL,nR,alphaR,44,-3686.232,-2.544,-10.0,4.0,-10.0,1.0,2)
 #fitting both sidebands simulatneously for X 
#  Fit_X_SB = CB.fit_SB(histo_X_mass_sideband_sub,3750,3950,44,-3843.606,-14.994,nL,alphaL,nR,alphaR,44,-3871.901,-3.342,-10.0,4.0,-10.0,1.0,2)

elif user_choice == "1":
 #signal
 Fit_B_sig = CB.fit(histo_B_mass_signal,5100,5500,44,5279,6.44,-10,1.0,-10,1.0,2)
 Fit_X_sig = CB.fit(histo_X_mass_signal,3600,3940,9.1E3,3686,2.6,-10,1.0,-10.,1.0,0,3871.85,4.0,2)
 
#fitting both sidebands simulatneously 
 Fit_psi2S_SB = CB.fit_SB(histo_X_mass_sideband_sub,3550,3850,44,3660,9.0,nL,alphaL,nR,alphaR,44,3686,4.0,-10.0,4.0,-10.0,1.0,2)
 
elif user_choice == "2":
 # signal
 Fit_B_sig = CB.fit(histo_B_mass_signal,5100,5500,44,5279,6.44,-10,1.0,-10,1.0,2)
 Fit_X_sig = CB.fit(histo_X_mass_signal,3600,3940,0,3686,2.6,-10,1.0,-10.,1.0,44,3871.85,3.0,2)
 
#fitting both sidebands simulatneously 
 Fit_X_SB = CB.fit_SB(histo_X_mass_sideband_sub,3750,3950,44,3850,9.0,nL,alphaL,nR,alphaR,44,3872,4.0,-10.0,4.0,-10.0,1.0,2)
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

t0 = text_B.AddText(f"N = {amp_B_S:.3f} #pm {amp_B_S_E:.3f}")
t1 = text_B.AddText(f"m = {mass_B_S:.3f} #pm {mass_B_S_E:.3f}")
t2 = text_B.AddText(f"#sigma = {sigma_B_S:.3f} #pm {sigma_B_S_E:.3f}")


histo_B_mass_signal.GetYaxis().SetTitle("Candidates/2.0 [MeV/c^{2}]")
histo_B_mass_signal.GetXaxis().SetTitle("m(J/#psi#pi^{+}#pi^{-}K^{+}#pi^{+}#pi^{-}) [MeV/c^{2}]")
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
Fit_B_sig.SetLineColor(8)
Fit_B_sig.SetLineStyle(2)
Fit_B_sig.DrawCopy("SAME")
Fit_B_sig.SetParameter(10,0)
Fit_B_sig.SetParameter(11,0)
Fit_B_sig.SetParameter(0,amp_B_S)
Fit_B_sig.SetLineColor(2)
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

x0 = text_X.AddText(f"N(#psi(2S)) = {amp_X_S:.3f} #pm {amp_X_S_E:.3f}")
x1 = text_X.AddText(f"m(#psi(2S)) = {mass_X_S:.3f} #pm {mass_X_S_E:.3f}")
x2 = text_X.AddText(f"#sigma(#psi(2S)) = {sigma_X_S:.3f} #pm {sigma_X_S_E:.3f}")
x3 = text_X.AddText(f"N(X(3872)) = {amp_X_S_1:.3f} #pm {amp_X_S_E_1:.3f}")
x4 = text_X.AddText(f"m(X(3872)) = {mass_X_S_1:.3f} #pm {mass_X_S_E_1:.3f}")
x5 = text_X.AddText(f"#sigma(X(3872)) = {sigma_X_S_1:.3f} #pm {sigma_X_S_E_1:.3f}")

histo_X_mass_signal.GetYaxis().SetTitle("Candidates/2.0 [MeV/c^{2}]")
histo_X_mass_signal.GetXaxis().SetTitle("m(J/#psi#pi^{+}#pi^{-}) [MeV/c^{2}]")
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

    sb0 = text.AddText(f"N(hump) = {amp1:.3f} #pm {ampE1:.3f}")
    sb1 = text.AddText(f"m(hump) = {mass1:.3f} #pm {massE1:.3f}") 
    sb2 = text.AddText(f"#sigma(hump) = {sigma1:.3f} #pm {sigmaE1:.3f}")
    if user_choice == "1":
      sb3 = text.AddText(f"N(#psi(2S)) = {amp2:.3f} #pm {ampE2:.3f}")
      sb4 = text.AddText(f"m(#psi(2S)) = {mass2:.3f} #pm {massE2:.3f}")
      sb5 = text.AddText(f"#sigma(#psi(2S)) = {sigma2:.3f} #pm {sigmaE2:.3f}")
    elif user_choice == "2" :
      sb3 = text.AddText(f"N(X(3872)) = {amp2:.3f} #pm {ampE2:.3f}")
      sb4 = text.AddText(f"m(X(3872)) = {mass2:.3f} #pm {massE2:.3f}")
      sb5 = text.AddText(f"#sigma(X(3872)) = {sigma2:.3f} #pm {sigmaE2:.3f}") 
    else:
      exit 

    histogram.GetYaxis().SetTitle("Candidates/2.0 MeV/c^{2}")
    histogram.GetXaxis().SetTitle("m(J/#psi#pi^{+}#pi^{-}) [MeV/c^{2}]")
    histogram.SetMarkerStyle(20)
    histogram.SetMarkerSize(0.1)
    # histo_X_mass_sideband_sub_sub.SetMarkerStyle(20)
    histogram.SetLineWidth(2)
    histogram.SetMarkerColor(1)
    histogram.SetLineColor(1)
    # if particle == 'X':
    #   histogram.GetXaxis().SetRangeUser(3650,4000)
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

  # X_Net_Yield = amp_X_S_1 - (1/3.0)*(peak_X)
  # X_Net_Yield_Error = np.sqrt(np.power(amp_X_S_E_1,2) + (1/9.0)*np.power(peak_err_X,2))
  # X_significance = X_Net_Yield/X_Net_Yield_Error

  print("#############################################################################################################")
  print("                B+ signal                B+ sideband              Net Yield                Significance")
  print(" Psi(2S)  ", round(amp_X_S,2) ,r"$\pm$", round(amp_X_S_E,2),"      ", round(peak_psi2S,2),r"$\pm$",round(peak_err_psi2S,2), "        ",round(Psi_2S_Net_Yield,2),r"$\pm$",round(Psi_2S_Net_Yield_Error,2),"       ",round(psi2S_significance,2) )
  print("                                                                                                                                                                                ")
  # print(" X(3872)   ",  round(amp_X_S_1,2) ,r"$\pm$", round(amp_X_S_E_1,2),"        ", round(peak_X,2),r"$\pm$",round(peak_err_X,2), "         ",round(X_Net_Yield,2),r"$\pm$",round(X_Net_Yield_Error,2),"         ",round(X_significance,2) )
  print("#############################################################################################################")

  print(psi2S_significance)
  # print(X_significance)

elif user_choice == '1':
  hump_psi2S, hump_err_psi2S, peak_psi2S, peak_err_psi2S = sideband(histo_X_mass_sideband_sub,Fit_psi2S_SB, 'SB at psi2S MC','psi2S',user_choice)

  Psi_2S_Net_Yield = amp_X_S - (1/3.0)*(peak_psi2S)
  Psi_2S_Net_Yield_Error = np.sqrt(np.power(amp_X_S_E,2) + (1/9.0)*np.power(peak_err_psi2S,2))
  psi2S_significance = Psi_2S_Net_Yield/Psi_2S_Net_Yield_Error

  print("#############################################################################################################")
  print("                B+ signal                B+ sideband              Net Yield                Significance")
  print(" Psi(2S)  ", round(amp_X_S,2) ,r"$\pm$", round(amp_X_S_E,2),"      ", round(peak_psi2S,2),r"$\pm$",round(peak_err_psi2S,2), "        ",round(Psi_2S_Net_Yield,2),r"$\pm$",round(Psi_2S_Net_Yield_Error,2),"       ",round(psi2S_significance,2) )
  print("#############################################################################################################")
 
  print(psi2S_significance)

elif user_choice == '2':
  hump_X, hump_err_X, peak_X, peak_err_X = sideband(histo_X_mass_sideband_sub,Fit_X_SB, 'SB at X MC','X',user_choice)
 
  X_Net_Yield = amp_X_S_1 - (1/3.0)*(peak_X)
  X_Net_Yield_Error = np.sqrt(np.power(amp_X_S_E_1,2) + (1/9.0)*np.power(peak_err_X,2))
  X_significance = X_Net_Yield/X_Net_Yield_Error
    
  print("#############################################################################################################")
  print("                B+ signal                B+ sideband              Net Yield                Significance")
  print(" X(3872)   ",  round(amp_X_S_1,2) ,r"$\pm$", round(amp_X_S_E_1,2),"        ", round(peak_X,2),r"$\pm$",round(peak_err_X,2), "         ",round(X_Net_Yield,2),r"$\pm$",round(X_Net_Yield_Error,2),"         ",round(X_significance,2) )
  print("#############################################################################################################")
  print(X_significance) 

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























# print("#############################################################################################################")
# print("                B+ signal                B+ sideband              Net Yield                Significance")
# print(" Psi(2S)  ", round(amp_X_S,2) ,r"$\pm$", round(amp_X_S_E,2),"      ", round(peak_psi2S,2),r"$\pm$",round(peak_err_psi2S,2), "        ",round(Psi_2S_Net_Yield,2),r"$\pm$",round(Psi_2S_Net_Yield_Error,2),"       ",round(psi2S_significance,2) )
# print("                                                                                                                                                                                ")
# print(" X(3872)   ",  round(amp_X_S_1,2) ,r"$\pm$", round(amp_X_S_E_1,2),"        ", round(peak_X,2),r"$\pm$",round(peak_err_X,2), "         ",round(X_Net_Yield,2),r"$\pm$",round(X_Net_Yield_Error,2),"         ",round(X_significance,2) )
# print("#############################################################################################################")
# print("Psi 2S Significance after sideband reduction ", Psi_2S_Net_Yield/Psi_2S_Net_Yield_Error)
# print("X (3872) Significance after sideband reduction ", X_Net_Yield/X_Net_Yield_Error)


# ROOT.gPad.WaitPrimitive()
# ROOT.gPad.WaitPrimitive()
# print(Fit_X_SB.GetParError(0))

# Psi_2S_Sideband = Fit_X_SB.GetParameter(0)
# Psi_2S_Sideband_Error = Fit_X_SB.GetParError(0)
# X_Sideband = Fit_X_SB.GetParameter(7)
# X_Sideband_Error = Fit_X_SB.GetParError(0)


# Psi_2S_Net_Yield = Psi_2S_Signal - (1/3.0)*Psi_2S_Sideband
# Psi_2S_Net_Yield_Error = (Psi_2S_Signal_Error*Psi_2S_Signal_Error + (1/9.0)*Psi_2S_Sideband_Error*Psi_2S_Sideband_Error)**(0.5)
# X_Net_Yield = X_Signal - (1/3.0)*X_Sideband
# X_Net_Yield_Error = (X_Signal_Error*X_Signal_Error + (1/9.0)*X_Sideband_Error*X_Sideband_Error)**(0.5)
# # # print(" Psi_2S_Signal ",Psi_2S_Signal, " Psi_2S_Sideband ", Psi_2S_Sideband," Psi_2S_Net_Yield ",Psi_2S_Net_Yield, " +/- ", Psi_2S_Net_Yield_Error)
# # # print(" X_Signal ",X_Signal, " X_Sideband ", X_Sideband," X_Net_Yield ",X_Net_Yield, " +/- ", X_Net_Yield_Error)
# Psi_2S_Significance = Psi_2S_Net_Yield/(Psi_2S_Net_Yield_Error+0.1)
# X_Significance = X_Net_Yield/X_Net_Yield_Error
# print("#############################################################################################################")
# print("                B+ signal                B+ sideband              Net Yield                Significance")
# print(" Psi(2S)  ", round(Psi_2S_Signal,2) ,r"$\pm$", round(Psi_2S_Signal_Error,2),"      ", round(Psi_2S_Sideband,2),r"$\pm$",round(Psi_2S_Sideband_Error,2), "        ",round(Psi_2S_Net_Yield,2),r"$\pm$",round(Psi_2S_Net_Yield_Error,2),"       ",round(Psi_2S_Significance,2) )
# # print("                                                                                                                                                                                ")
# print(" X(3872)   ",  round(X_Signal,2) ,r"$\pm$", round(X_Signal_Error,2),"        ", round(X_Sideband,2),r"$\pm$",round(X_Sideband_Error,2), "         ",round(X_Net_Yield,2),r"$\pm$",round(X_Net_Yield_Error,2),"         ",round(X_Significance,2) )
# print("#############################################################################################################")
# # print("Psi 2S Significance after sideband reduction ", Psi_2S_Net_Yield/Psi_2S_Net_Yield_Error)
# # print("X (3872) Significance after sideband reduction ", X_Net_Yield/X_Net_Yield_Error)
# # ROOT.gPad.WaitPrimitive()
# # ROOT.gPad.WaitPrimitive()
# # ROOT.gPad.WaitPrimitive()
# # ROOT.gPad.WaitPrimitive()
# # ROOT.gPad.WaitPrimitive()
# # ROOT.gPad.WaitPrimitive()
# # file.Close()



