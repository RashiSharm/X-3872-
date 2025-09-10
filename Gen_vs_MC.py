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
# ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/sumH.C')
# ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/debug_R_NDoubleDSCBFit.C')
# ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/debug_R_DSCB_BWFit.C')
# CB = ROOT.debug_R_NDoubleDSCBFit()
# CB2 = ROOT.debug_R_DSCB_BWFit()

current_directory = "/home/rsharm18/work/Rootfile/Sept_25/Kaon_excitations"

user_choice = input("Enter 0 for Data , 1 to cc MC and 2 for X MC ")

nL = nR = -100
alphaL = -100
alphaR = -100
if user_choice == "0":
    input = "subreso-Data"
    mass = 3872
    B_pos = 120
    file_name = "/home/rsharm18/work/Rootfile/Data/subreso_Data.root"
    sigma_B = 5.68
    sigma_X = 4.70
    output = "Data"
    Lower = 3679
    Upper = 3695
elif user_choice == "1":
    input = "subreso-cc_MC"
    mass = 3686
    B_pos = 100
    # file_name = "/home/rsharm18/work/Rootfile/cc_MC/subreso_cc.root"
    file_name = "/swdev/sharmar/X_analysis/Jul_25/Kaon_excitations/cc_MC/Kaon_excitations_with_cc_Kpp.root"
    file_name_w = "/swdev/sharmar/X_analysis/Jul_25/Kaon_excitations/weighted/cc_MC/Kaon_excitations_with_cc_Kpp.root"
    gen_file = "/swdev/sharmar/X_analysis/MC_gen/DVntuple_002-50000ev-20250815.root"
    particle = "cc"
    sigma_B = 5.03
    sigma_X = 2.6
    output = "cc_MC"
    Lower = 3682
    Upper = 3692
elif user_choice == "2":
    input = "subreso-X_MC"
    mass = 3872
    B_pos = 11000
    file_name = "/swdev/sharmar/X_analysis/Jul_25/Kaon_excitations/X_MC/Kaon_excitations_with_X_Kpp.root"
    file_name_w = "/swdev/sharmar/X_analysis/Jul_25/Kaon_excitations/weighted/X_MC/Kaon_excitations_with_X_Kpp.root"
    # file_name = "/home/rsharm18/work/Rootfile/X_MC/subreso_X.root"
    gen_file = "/swdev/sharmar/X_analysis/MC_gen/DVntuple_001-50000ev-20250815.root"
    particle = 'x'
    sigma_B = 5.5
    sigma_X = 2.5
    output = "X_MC"
    Lower = 3682
    Upper = 3692
else:
    print("Invalid")        

file = ROOT.TFile.Open(f"{file_name}","READ")
Gfile = ROOT.TFile.Open(f"{gen_file}", "READ")
file_w = ROOT.TFile.Open(f"{file_name_w}","READ")

def comp(file,Gfile,particle,lower,upper):
    my_hist = file.Get(f"h{particle}1")
    my_GenTree = Gfile.Get("MCDecayTreeTuple/MCDecayTree")

    # m_kpp = my_tree.GetBranch("m_kpp")
    m_kpp = my_GenTree.GetBranch("m_kpp")

    my_Genhisto = ROOT.TH1F(""," ",100, lower, upper)
    for entry in my_GenTree:
        m_kpp_val = m_kpp.GetLeaf("m_kpp").GetValue()
        my_Genhisto.Fill(m_kpp_val)

    c0 = ROOT.TCanvas()
    c0.cd()
    c0.SetFrameLineWidth(2)    
    
    legend = ROOT.TLegend(0.8, 0.75, 0.9, 0.85)
    legend.SetBorderSize(0)
    
    legend.AddEntry(my_hist,"Full MC")
    legend.AddEntry(my_Genhisto,"Gen MC")
    my_hist.Scale(1./my_hist.Integral())
    my_Genhisto.Scale(1./my_Genhisto.Integral())
    # my_hist.Scale(1./my_hist.GetEntries())
    # my_Genhisto.Scale(1./my_Genhisto.GetEntries())
    
    my_Genhisto.Rebin(2)
    my_hist.Rebin(2)
    my_hist.GetYaxis().SetTitle(f"Number Of Candidates/{my_hist.GetBinWidth(1)} MeV")
    my_hist.Draw("E")
    my_Genhisto.Draw("same")   
    legend.Draw("same")
    c0.SaveAs(f"/swdev/sharmar/X_analysis/Sept_25/Gen_vs_Full_MC/Gen_vs_FullMC_{particle}_norm_int.root")

    hi_R = ROOT.TH1D("weight","k",50, lower, upper)
    hi_R.GetYaxis().SetTitle(f"Number Of Candidates/{hi_R.GetBinWidth(1)} MeV")
    hi_R = my_hist/my_Genhisto
    # hi_R.Smooth()
    hi_R.Draw("E")
    c0.SaveAs(f"/swdev/sharmar/X_analysis/Sept_25/Gen_vs_Full_MC/Gen_vs_FullMC_{particle}_ratio_inte.root")
    return hi_R

hist_No_weight = comp(file,Gfile,particle,500,2000)

def comp_w(file_w,Gfile_w,particle,lower,upper):
    my_hist = file_w.Get(f"h{particle}1")
    my_GenTree = Gfile.Get("MCDecayTreeTuple/MCDecayTree")

    # m_kpp = my_tree.GetBranch("m_kpp")
    m_kpp = my_GenTree.GetBranch("m_kpp")
    weight = my_GenTree.GetBranch("weight")
    my_Genhisto = ROOT.TH1F(""," ",100, lower, upper)
    for entry in my_GenTree:
        m_kpp_val = m_kpp.GetLeaf("m_kpp").GetValue()
        w_val = weight.GetLeaf("weight").GetValue()
        my_Genhisto.Fill(m_kpp_val,w_val)

    c0 = ROOT.TCanvas()
    c0.cd()
    c0.SetFrameLineWidth(2)    
    
    legend = ROOT.TLegend(0.8, 0.75, 0.9, 0.85)
    legend.SetBorderSize(0)
    
    legend.AddEntry(my_hist,"Full MC")
    legend.AddEntry(my_Genhisto,"Gen MC")
    my_Genhisto.Rebin(2)
    my_hist.Rebin(2)
    my_hist.Scale(1./my_hist.Integral())
    my_Genhisto.Scale(1./my_Genhisto.Integral())  
    # my_hist.Scale(1./my_hist.GetEntries())
    # my_Genhisto.Scale(1./my_Genhisto.GetEntries())
    print(my_hist.GetBinWidth(1))
    my_hist.GetYaxis().SetTitle(f"Number Of Candidates/{my_hist.GetBinWidth(1)} MeV")
    my_hist.Draw("E")
    my_Genhisto.Draw("same")   
    legend.Draw("same")
    c0.SaveAs(f"/swdev/sharmar/X_analysis/Sept_25/Gen_vs_Full_MC/Gen_vs_FullMC_{particle}_norm_int_weighted.root")

    hi_R = ROOT.TH1D("weight","k",50, lower, upper)
    hi_R = my_hist/my_Genhisto
    # hi_R.Smooth()
    hi_R.GetYaxis().SetTitle(f"Number Of Candidates/{hi_R.GetBinWidth(1)} MeV")
    hi_R.Draw("E")
    c0.SaveAs(f"/swdev/sharmar/X_analysis/Sept_25/Gen_vs_Full_MC/Gen_vs_FullMC_{particle}_ratio_int_weighted.root")
    return hi_R

hist_weight = comp_w(file_w,Gfile,particle,500,2000)

c2 = ROOT.TCanvas()
c2.cd()
c2.SetFrameLineWidth(2)

Leg = ROOT.TLegend(0.8, 0.75, 0.9, 0.85)
Leg.SetBorderSize(0)

Leg.AddEntry(hist_weight,"Full/Gen for weighted")
Leg.AddEntry(hist_No_weight,"Full/Gen for Unweighted")
hist_weight.SetLineColor(1)
hist_No_weight.Draw()
hist_weight.Draw("same")
Leg.Draw("same")
c2.SaveAs(f"/swdev/sharmar/X_analysis/Sept_25/Gen_vs_Full_MC/Gen_vs_FullMC_{particle}_ratio_overlay.root")

# def histo(file,particle):
#     my_tree = file.Get("nTuple")
#     # my_tree.AddFriend("nTuple","/home/rsharm18/work/Rootfile/TMVA_Single_Entry_2_X.root")

#     Bp_Jpsi_B_M = my_tree.GetBranch("Bp_Jpsi_B_M")
#     Bp_Jpsi_X_M = my_tree.GetBranch("Bp_Jpsi_X_M")
#     nCandidate = my_tree.GetBranch("nCandidate")
#     K_PE = my_tree.GetBranch("K_PE")
#     K_PX = my_tree.GetBranch("K_PX")
#     K_PY = my_tree.GetBranch("K_PY")
#     K_PZ = my_tree.GetBranch("K_PZ")
#     Pi2_PE = my_tree.GetBranch("Pi2_PE")
#     Pi2_PX = my_tree.GetBranch("Pi2_PX")
#     Pi2_PY = my_tree.GetBranch("Pi2_PY")
#     Pi2_PZ = my_tree.GetBranch("Pi2_PZ")
#     Pi3_PE = my_tree.GetBranch("Pi3_PE")
#     Pi3_PX = my_tree.GetBranch("Pi3_PX")
#     Pi3_PY = my_tree.GetBranch("Pi3_PY")
#     Pi3_PZ = my_tree.GetBranch("Pi3_PZ")
#     # BDT = my_tree.GetBranch("BDT")

#     histo_X  = ROOT.TH1F("X Constrained K*"," ", 100, 500, 2000)
#     histo_cc = ROOT.TH1F("Psi(2S) Constrained K*"," ", 100, 500, 2000)

#     for entry in my_tree:
#         branch_value_B = Bp_Jpsi_B_M.GetLeaf("Bp_Jpsi_B_M").GetValue()
#         branch_value_X = Bp_Jpsi_X_M.GetLeaf("Bp_Jpsi_X_M").GetValue()
#         nCandidates_cut = nCandidate.GetLeaf("nCandidate").GetValue()
#         KPE = K_PE.GetLeaf("K_PE").GetValue()
#         KPX = K_PX.GetLeaf("K_PX").GetValue()
#         KPY = K_PY.GetLeaf("K_PY").GetValue()
#         KPZ = K_PZ.GetLeaf("K_PZ").GetValue()
#         Pi2PE = Pi2_PE.GetLeaf("Pi2_PE").GetValue()
#         Pi2PX = Pi2_PX.GetLeaf("Pi2_PX").GetValue()
#         Pi2PY = Pi2_PY.GetLeaf("Pi2_PY").GetValue()
#         Pi2PZ = Pi2_PZ.GetLeaf("Pi2_PZ").GetValue()
#         Pi3PE = Pi3_PE.GetLeaf("Pi3_PE").GetValue()
#         Pi3PX = Pi3_PX.GetLeaf("Pi3_PX").GetValue()
#         Pi3PY = Pi3_PY.GetLeaf("Pi3_PY").GetValue()
#         Pi3PZ = Pi3_PZ.GetLeaf("Pi3_PZ").GetValue()
#         # BDT_X = BDT.GetLeaf("BDT").GetValue()
#         PE = KPE+Pi2PE+Pi3PE
#         PX = KPX+Pi2PX+Pi3PX
#         PY = KPY+Pi2PY+Pi3PY
        # PZ = KPZ+Pi2PZ+Pi3PZ
# defining the Kaon excitation variable        
#         K_exct= np.sqrt(np.power(PE,2) - np.power(PX,2) - np.power(PY,2) - np.power(PZ,2))
           
#         if (user_choice=="0"):
#         #  if (abs(branch_value_B-5279)<11.4 and abs(branch_value_X-3872)<4.9 and (nCandidates_cut==0)):
#          if (abs(branch_value_B-5279)<11.4 and abs(branch_value_X-3872)<4.9 and (nCandidates_cut==0)):
#             histo_X.Fill(K_exct)
#          elif (abs(branch_value_B-5279)<11.4 and abs(branch_value_X-3686)<4.9 and (nCandidates_cut==0)): 
#             histo_cc.Fill(K_exct) 
#         elif (user_choice=="1"):
#            if (abs(branch_value_B-5279)<11.4 and abs(branch_value_X-3686)<4.9 and (nCandidates_cut==0)): 
#             histo_cc.Fill(K_exct)
#         elif (user_choice=="2"):
#            if (abs(branch_value_B-5279)<11.4 and abs(branch_value_X-3872)<4.9 and (nCandidates_cut==0)):
#             histo_X.Fill(K_exct)
# # sqrt((K_PE+Pi2_PE+Pi3_PE)^2-(K_PX+Pi2_PX+Pi3_PY)^2-(K_PY+Pi2_PY+Pi3_PY)^2-(K_PZ+Pi2_PZ+Pi3_PZ)^2)>>h3X(100,500,2000)","fabs(Bp_Jpsi_B_M-5279)<11.4 && fabs(Bp_B_X_M-3686)<4.9&&BDT>-0.113

#     del my_tree  
#     return  histo_X, histo_cc


# c2 = ROOT.TCanvas()
# c2.cd()
# c2.SetFrameLineWidth(2)
# histogram_cc, histogram_X = histo(file,'K')  
    
# if user_choice == "0":
#     # Fit_K = CB.fit_2(histogram_X,800,1600,44,-1270,-273,-0.3,0.01,-3.,0.5,44,-1460,-300,-0.3,0.01,-3.,0.5,3) # no this is fitting two DSCB to the data, whereas this is one BW and one DSCB.
#     print("fit")
#     # Fit_K2 = CB2.fit(histogram_X,800,1600,44,-1270,-273,-0.3,0.01,-3.,0.5,44,1460,300,3) # no this is fitting two DSCB to the data, whereas this is one BW and one DSCB.

#     Fit_K2 = CB2.fit(histogram_X,800,1600,44,-1471.23,-999,-0.3,-0.01,-3.0,0.5,44,-1270,30,3) # no this is fitting two DSCB to the data, whereas this is one BW and one DSCB.

# elif user_choice == "1":
#     Fit_K = CB.fit(histogram_cc,805,1600,44,1460,300,-0.3,0.01,-3.,0.5,3)
#     # Fit_K = CB.fit(histogram_X,800,1600,44,1440,300,-10.,1.0,-40.,0.01,1)
# elif user_choice == "2":
#     Fit_K = CB.fit(histogram_X,800,1400,44,1240,100,-0.3,0.01,-3.,0.5,3)    
    
# histogram_X.GetXaxis().SetTitle("m(K^{+}#pi^{+}#pi^{-}) [MeV]")
# histogram_X.SetMarkerStyle(20) 
# histogram_X.SetLineWidth(2)
# histogram_X.SetMarkerSize(0.1)
# histogram_X.SetMarkerColor(1)
# histogram_X.SetLineColor(1)
# # histogram_X.GetYaxis().SetRangeUser(0,120)
# histogram_X.Draw('E')
# Fit_K2.Draw('same')


# c2.SaveAs(f"{current_directory}/{output}/old/Kaon_excitations_with_X_constraint2.pdf")
# c2.SaveAs(f"{current_directory}/{output}/old/Kaon_excitations_with_X_constraint2.root")

# amp_DSCB = Fit_K2.GetParameter(0)
# amp_BW = Fit_K2.GetParameter(7)

# # Fit_K2.SetLineColor(4)
# # Fit_K2.DrawCopy("SAME")
# # Fit_K2.SetParameter(0,0)
# # Fit_K2.SetParameter(7,0)
# # Fit_K2.SetParameter(10,Fit_K2.GetParameter(10))
# # Fit_K2.SetParameter(11,Fit_K2.GetParameter(11))
# # Fit_K2.SetParameter(12,Fit_K2.GetParameter(12))
# # Fit_K2.SetParameter(13,Fit_K2.GetParameter(13))
# # Fit_K2.SetLineColor(7)
# # Fit_K2.SetLineStyle(2)
# # Fit_K2.DrawCopy("SAME")
# # print("line")
# # Fit_K2.SetParameter(0,amp_DSCB)
# # Fit_K2.SetParameter(10,0)
# # Fit_K2.SetParameter(11,0)
# # Fit_K2.SetParameter(12,0)
# # Fit_K2.SetParameter(13,0)
# # Fit_K2.SetLineColor(8)
# # Fit_K2.SetLineStyle(2)
# # Fit_K2.DrawCopy("SAME")
# # print("DSCB")
# # Fit_K2.SetParameter(0,0)
# # Fit_K2.SetParameter(7,amp_BW_7)
# # Fit_K2.SetLineColor(6)
# # Fit_K2.SetLineStyle(2)
# # Fit_K2.DrawCopy("SAME")
# # print("BW")

# c2.SaveAs(f"{current_directory}/{output}/old/Separated_Kaon_excitations_with_X_constraint2.pdf")

# # c3 = ROOT.TCanvas()
# # c3.cd()
# # c3.SetFrameLineWidth(2)
# # histogram_cc.GetXaxis().SetTitle("m(K^{+}#pi^{+}#pi^{-}) [MeV]")
# # histogram_cc.SetMarkerStyle(20) 
# # histogram_cc.SetLineWidth(2)
# # histogram_cc.SetMarkerSize(0.1)
# # histogram_cc.SetMarkerColor(1)
# # histogram_cc.SetLineColor(1)
# # # histogram_cc.GetYaxis().SetRangeUser(0,120)
# # histogram_cc.Draw('E')

# # c3.SaveAs(f"{current_directory}/{output}/Kaon_excitations_with_cc_constraint.pdf")
# # c3.SaveAs(f"{current_directory}/{output}/Kaon_excitations_with_cc_constraint.root")
# del histogram_cc
# del histogram_X