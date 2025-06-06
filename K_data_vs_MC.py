import ROOT
import numpy as np
from array import array
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
# ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/debug_R_NDoubleDSCBFit.C')
ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/debug_R_DSCB_BWFit.C')
# CB = ROOT.debug_R_NDoubleDSCBFit()
CB2 = ROOT.debug_R_DSCB_BWFit()

current_directory = "/home/rsharm18/work/Rootfile/May_25"

file_name_1 = "/home/rsharm18/work/Rootfile/Data/subreso_Data.root"
sigma_B = 5.68
sigma_X = 3.70
file_name_2 = "/home/rsharm18/work/Rootfile/cc_MC/subreso_cc.root"
file_name_3 = "/home/rsharm18/work/Rootfile/X_MC/subreso_X.root"
Lower = 3682
Upper = 3692

file = ROOT.TFile.Open(f"{file_name_1}","READ")
file2 = ROOT.TFile.Open(f"{file_name_2}","READ")
file3 = ROOT.TFile.Open(f"{file_name_3}","READ")

def histo(file,particle,state):
    my_tree = file.Get("nTuple")

    Bp_Jpsi_B_M = my_tree.GetBranch("Bp_Jpsi_B_M")
    Bp_Jpsi_X_M = my_tree.GetBranch("Bp_Jpsi_X_M")
    nCandidate = my_tree.GetBranch("nCandidate")
    Bp_B_jpsi_pi2pi3 = my_tree.GetBranch("Bp_B_jpsi_pi2pi3")

    Bp_L0DiMuonDecision_TOS = my_tree.GetBranch("Bp_L0DiMuonDecision_TOS")
    Bp_L0MuonDecision_TOS = my_tree.GetBranch("Bp_L0MuonDecision_TOS")
    Bp_Hlt1DiMuonHighMassDecision_TOS = my_tree.GetBranch("Bp_Hlt1DiMuonHighMassDecision_TOS")
    Bp_Hlt1TrackMuonDecision_TOS = my_tree.GetBranch("Bp_Hlt1TrackMuonDecision_TOS")
    Bp_Hlt1TrackMVADecision_TOS = my_tree.GetBranch("Bp_Hlt1TrackMVADecision_TOS")
    Bp_Hlt2DiMuonDetachedJPsiDecision_TOS = my_tree.GetBranch("Bp_Hlt2DiMuonDetachedJPsiDecision_TOS")
    Bp_Hlt2Phys_TOS = my_tree.GetBranch("Bp_Hlt2Phys_TOS")
    Bp_Hlt1Phys_TOS = my_tree.GetBranch("Bp_Hlt1Phys_TOS")
    K_PE = my_tree.GetBranch("K_PE")
    K_PX = my_tree.GetBranch("K_PX")
    K_PY = my_tree.GetBranch("K_PY")
    K_PZ = my_tree.GetBranch("K_PZ")
    Pi2_PE = my_tree.GetBranch("Pi2_PE")
    Pi2_PX = my_tree.GetBranch("Pi2_PX")
    Pi2_PY = my_tree.GetBranch("Pi2_PY")
    Pi2_PZ = my_tree.GetBranch("Pi2_PZ")
    Pi3_PE = my_tree.GetBranch("Pi3_PE")
    Pi3_PX = my_tree.GetBranch("Pi3_PX")
    Pi3_PY = my_tree.GetBranch("Pi3_PY")
    Pi3_PZ = my_tree.GetBranch("Pi3_PZ")
       

    histo_X  = ROOT.TH1D(f"X Constrained {particle} in {state}"," ", 100, 500, 2000)
    histo_cc = ROOT.TH1D(f"Psi(2S) Constrained {particle} in {state}"," ", 100, 500, 2000)
    histo_X_SB  = ROOT.TH1D(f"X gConstrained {particle} in {state}"," ", 100, 500, 2000)
    histo_cc_SB = ROOT.TH1D(f"Psi(2S) gConstrained {particle} in {state}"," ", 100, 500, 2000)
    histogram_S = ROOT.TH1D(f"Psi(2S) gkConstrained {particle} in {state}"," ", 100, 500, 2000)
    Jpsi_reflection = Bp_B_jpsi_pi2pi3.GetLeaf("Bp_B_jpsi_pi2pi3").GetValue()


    for entry in my_tree:
        branch_value_B = Bp_Jpsi_B_M.GetLeaf("Bp_Jpsi_B_M").GetValue()
        branch_value_X = Bp_Jpsi_X_M.GetLeaf("Bp_Jpsi_X_M").GetValue()
        nCandidates_cut = nCandidate.GetLeaf("nCandidate").GetValue()
        KPE = K_PE.GetLeaf("K_PE").GetValue()
        KPX = K_PX.GetLeaf("K_PX").GetValue()
        KPY = K_PY.GetLeaf("K_PY").GetValue()
        KPZ = K_PZ.GetLeaf("K_PZ").GetValue()
        Pi2PE = Pi2_PE.GetLeaf("Pi2_PE").GetValue()
        Pi2PX = Pi2_PX.GetLeaf("Pi2_PX").GetValue()
        Pi2PY = Pi2_PY.GetLeaf("Pi2_PY").GetValue()
        Pi2PZ = Pi2_PZ.GetLeaf("Pi2_PZ").GetValue()
        Pi3PE = Pi3_PE.GetLeaf("Pi3_PE").GetValue()
        Pi3PX = Pi3_PX.GetLeaf("Pi3_PX").GetValue()
        Pi3PY = Pi3_PY.GetLeaf("Pi3_PY").GetValue()
        Pi3PZ = Pi3_PZ.GetLeaf("Pi3_PZ").GetValue()
        PE = KPE+Pi2PE+Pi3PE
        PX = KPX+Pi2PX+Pi3PX
        PY = KPY+Pi2PY+Pi3PY
        PZ = KPZ+Pi2PZ+Pi3PZ
        L01 = Bp_L0DiMuonDecision_TOS.GetLeaf("Bp_L0DiMuonDecision_TOS").GetValue()
        L02 = Bp_L0MuonDecision_TOS.GetLeaf("Bp_L0MuonDecision_TOS").GetValue()
        
        Hlt1_1 = Bp_Hlt1DiMuonHighMassDecision_TOS.GetLeaf("Bp_Hlt1DiMuonHighMassDecision_TOS").GetValue()

        Hlt1_3 = Bp_Hlt1TrackMuonDecision_TOS.GetLeaf("Bp_Hlt1TrackMuonDecision_TOS").GetValue()
        Hlt1_4 = Bp_Hlt1TrackMVADecision_TOS.GetLeaf("Bp_Hlt1TrackMVADecision_TOS").GetValue()

        Hlt2_1 = Bp_Hlt2DiMuonDetachedJPsiDecision_TOS.GetLeaf("Bp_Hlt2DiMuonDetachedJPsiDecision_TOS").GetValue()
       
        K_exct= np.sqrt(np.power(PE,2) - np.power(PX,2) - np.power(PY,2) - np.power(PZ,2))    
        if (L01 or L02) and (Hlt1_1 or Hlt1_3 or Hlt1_4 ) and (Hlt2_1) and (nCandidates_cut==0) and ((Lower>Jpsi_reflection or Jpsi_reflection>Upper)):  
         if (abs(branch_value_B-5279.92) < 2.0*sigma_B) :        
            if(particle=='X'and abs(branch_value_X-3872.)<2.0*sigma_X ):
             histo_X.Fill(K_exct)            
            elif (particle=='cc' and abs(branch_value_X-3686.)<2.0*sigma_X):  
             histo_cc.Fill(K_exct)   
         if (abs(branch_value_B-5279.90) > 4.0*sigma_B) and (abs(branch_value_B-5279.90) < 10.0*sigma_B) :     
          if (particle =="X" and abs(branch_value_X-3872.) > 4.0*sigma_X) and (abs(branch_value_X-3872.) < 10.0*sigma_X) :    
            histo_X_SB.Fill(K_exct)        
          elif(particle == "cc" and abs(branch_value_X-3872.) > 4.0*sigma_X) and (abs(branch_value_X-3872.) < 10.0*sigma_X) : 
            histo_cc_SB.Fill(K_exct)   
    
    del my_tree  
    return  histo_X,histo_cc,histo_X_SB,histo_cc_SB

# # data histograms
histogram_X,h_cc,h_X_SB,h_ccsb = histo(file,"X","data")  
h_X,histogram_cc,h_xsb,h_cc_SB = histo(file,"cc","data")
histogram_X_MC,h_cc_MC,h_X_SB_MC,h_ccsb_MC = histo(file2,"X","MC")  
h_X_MC,histogram_cc_MC,h_xsb_MC,h_cc_SB_MC = histo(file3,"cc","MC")


def hist_comp(hist1,hist1_SB,hist2,hist2_SB,state):

    c0 = ROOT.TCanvas()
    c0.cd()
    c0.SetFrameLineWidth(2)


    hist1.GetXaxis().SetTitle("m(K^{+}#pi^{+}#pi^{-}) [MeV]")
    hist1.GetYaxis().SetTitle(f"Number Of Candidates/{hist1.GetBinWidth(1)} MeV")
    hist1.SetMarkerStyle(20) 
    hist1.SetLineWidth(2)
    hist1.SetMarkerSize(0.1)
    hist1.SetMarkerColor(1)
    hist1.SetLineColor(1)
    

    for bin in range(1,hist1.GetNbinsX()+1):
        error1 = hist1.GetBinError(bin)
        error2 = hist2.GetBinError(bin)
        error1_MC = hist1_SB.GetBinError(bin)
        error2_MC = hist2_SB.GetBinError(bin)
        if (error1== 0):
            hist1.SetBinError(bin,1)
        elif(error2== 0):
            hist2.SetBinError(bin,1)
        elif(error1_MC== 0):
            hist1_SB.SetBinError(bin,1) 
        elif(error2_MC== 0):
            hist2_SB.SetBinError(bin,1)

    hist1_SB.Scale(1/3.0)
    hist1.Add(hist1_SB,-1)

    hist2_SB.Scale(1/3.0)
    hist2.Add(hist2_SB,-1)
   
    
    for bin in range(1,hist1.GetNbinsX()+1):
        val_1 = hist1.GetBinContent(bin)
        val_2 = hist2.GetBinContent(bin)
        if (val_1 < 0):
            hist1.SetBinError(bin,abs(val_1))
        elif(val_2 < 0):
            hist2.SetBinError(bin,abs(val_2))
    line = ROOT.TLine(700,0,1600,0)
    line.SetLineColor(36)
    
    hist1.Scale(1./hist1.GetEntries())
    hist2.Scale(1./hist2.GetEntries())
    hist1.SetLineColor(1)
    hist2.SetLineColor(2)
    hist1.Draw('E')
    line.Draw('same')
    hist2.Draw('same')
#     legend.Draw('same')
#     # histog.Draw('same')
    
    # c0.SaveAs(f"{current_directory}/Kaon_excitations_with_{state}.root")
    # c0.SaveAs(f"{current_directory}/Kaon_excitations_with_{state}.pdf")
    

    c1 = ROOT.TCanvas()
    c1.cd()
    c1.SetFrameLineWidth(2)
    hi_W = ROOT.TH1D("weight","k", 100, 500, 2000)
    hi_W = hist1/hist2
    hi_W.Draw('E')
    
    # hi_W.SaveAs(f"{current_directory}/weights_for_{state}_Jpsi_refl.root")
    output_file = ROOT.TFile(f"{current_directory}/weightfile_{state}.root", "RECREATE")
    tree_w = ROOT.TTree("histogram_data", "Values from the histogram bins")
    val = array('d', [0.0])
    bin_center = array('d', [0.])
    bin_index = array('i', [0]) 
    tree_w.Branch("weight", val, "weight/D")
    tree_w.Branch("bin_center", bin_center, 'bin_center/D')
    tree_w.Branch("bin_index", bin_index, 'bin_index/I')

    n_bins = hi_W.GetNbinsX()
    for i in range(1, n_bins + 1):
        val[0] = hi_W.GetBinContent(i)
        bin_center[0] = hi_W.GetXaxis().GetBinCenter(i)
        bin_index[0] = i
        tree_w.Fill()    

    output_file.cd()
    tree_w.Write()
    output_file.Close()    
    

    


hist_cc_W = hist_comp(histogram_cc,h_cc_SB,histogram_cc_MC,h_cc_SB_MC,"cc")    
# hist_x_W = hist_comp(histogram_X,h_X_SB,histogram_X_MC,h_X_SB_MC,"X")








# file2.1 = ROOT.TFile(f"{file_name_2.1}","RECREATE")
# file3.1 = ROOT.TFile(f"{file_name_3.1}","RECREATE")
# def MC_weighting(file,hist_weight):
#     my_tree = file.Get("nTuple")

#     n_bins = hist_weight.GetNbinsX()
#     bin_contents = array('f',[0.0])
#     # bin_contents = ROOT.std.vector('float')()
#     weight_branch = my_tree.Branch("weight", bin_contents,"weight/F")

#     for entry in range(my_tree.GetEntries()):
#         my_tree.GetEntry(entry)
#         bin_index = entry + 1
#         if bin_index <= n_bins:
#             bin_value = hist_weight.GetBinContent(bin_index)
#             bin_contents.push_back(bin_value)
#         else:
#             bin_contents.push_back(1.0)    

#         weight_branch.Fill()

#     file_out = ROOT.TFile(f"{current_directory}","RECREATE")
#     file_out.cd()
#     my_tree.Write()
#     file_out.Close()
    # file.Close()

#     return 1

# MC_weighting(file2,hist_cc_W)
# MC_weighting(file3,hist_x_W)   
