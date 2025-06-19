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
ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/FitMyPoly.C')
ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/NDoubleDSCBFit.C')
# ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/debug_R_DSCB_BWFit.C')
poly = ROOT.FitMyPoly()
DSCB = ROOT.NDoubleDSCBFit()

mc_dir = "/home/rsharm18/work/Rootfile/"
current_directory = "/home/rsharm18/work/Rootfile/June_25/Kaon_excitations/compared"
hist_dir = "/home/rsharm18/work/Rootfile/June_25/Kaon_excitations/hist_files"

file_XK = f"{hist_dir}/Data/Kaon_excitations_with_X_XK.root"
file_XK_MC = f"{hist_dir}/X_MC/Kaon_excitations_with_X_XK.root"
file_XKpim = f"{hist_dir}/Data/Kaon_excitations_with_X_XPimK.root"
file_XKpim_MC = f"{hist_dir}/X_MC/Kaon_excitations_with_X_XPimK.root"
file_Xpip = f"{hist_dir}/Data/Kaon_excitations_with_X_XPip.root"
file_Xpip_MC = f"{hist_dir}/X_MC/Kaon_excitations_with_X_XPip.root"
file_X_jpsipipi = f"{hist_dir}/Data/Kaon_excitations_with_X_jpsipipi.root"
file_X_jpsipipi_MC = f"{hist_dir}/X_MC/Kaon_excitations_with_X_jpsipipi.root"
file_XKpp = f"{hist_dir}/Data/Kaon_excitations_with_X_Kpp.root"
file_XKpp_MC = f"{hist_dir}/X_MC/Kaon_excitations_with_X_Kpp.root"
file_Xpim = f"{hist_dir}/Data/Kaon_excitations_with_X_XPim.root"
file_Xpim_MC = f"{hist_dir}/X_MC/Kaon_excitations_with_X_XPim.root"
file_Xpimp = f"{hist_dir}/Data/Kaon_excitations_with_X_XPimp.root"
file_Xpimp_MC = f"{hist_dir}/X_MC/Kaon_excitations_with_X_XPimp.root"

file_ccK = f"{hist_dir}/Data/Kaon_excitations_with_cc_XK.root"
file_ccK_MC = f"{hist_dir}/cc_MC/Kaon_excitations_with_cc_XK.root"
file_ccKpim = f"{hist_dir}/Data/Kaon_excitations_with_cc_XPimK.root"
file_ccKpim_MC = f"{hist_dir}/cc_MC/Kaon_excitations_with_cc_XPimK.root"
file_ccpip = f"{hist_dir}/Data/Kaon_excitations_with_cc_XPip.root"
file_ccpip_MC = f"{hist_dir}/cc_MC/Kaon_excitations_with_cc_XPip.root"
file_cc_jpsipipi = f"{hist_dir}/Data/Kaon_excitations_with_cc_jpsipipi.root"
file_cc_jpsipipi_MC = f"{hist_dir}/cc_MC/Kaon_excitations_with_cc_jpsipipi.root"
file_ccKpp = f"{hist_dir}/Data/Kaon_excitations_with_cc_Kpp.root"
file_ccKpp_MC = f"{hist_dir}/cc_MC/Kaon_excitations_with_cc_Kpp.root"
file_ccpim = f"{hist_dir}/Data/Kaon_excitations_with_cc_XPim.root"
file_ccpim_MC = f"{hist_dir}/cc_MC/Kaon_excitations_with_cc_XPim.root"
file_ccpimp = f"{hist_dir}/Data/Kaon_excitations_with_cc_XPimp.root"
file_ccpimp_MC = f"{hist_dir}/cc_MC/Kaon_excitations_with_cc_XPimp.root"

def hist_comp(file_name_1,file_name_2,particle,permutation):

    file = ROOT.TFile.Open(f"{file_name_1}","READ")
    hi_1 = file.Get(f"h{particle}1")
    file2 = ROOT.TFile.Open(f"{file_name_2}","READ")
    hi_2 = file2.Get(f"h{particle}1")
    c0 = ROOT.TCanvas()
    c0.cd()
    c0.SetFrameLineWidth(2)

    line = ROOT.TLine(700,0,6000,0)
    line.SetLineColor(36)
    legend = ROOT.TLegend(0.8, 0.75, 0.9, 0.85)
    legend.SetBorderSize(0)
    hi_1.Scale(1./hi_1.GetEntries())
    hi_2.Scale(1./hi_2.GetEntries())
    hi_1.SetLineColor(1)
    hi_2.SetLineColor(2)
    legend.AddEntry(hi_1,"Data")
    legend.AddEntry(hi_2,"MC")
    hi_1.Draw('E')
    hi_2.Draw("same")
    line.Draw("same")
    legend.Draw("same")
    # c0.SaveAs(f"{current_directory}/{particle}_{permutation}.root")

    c1 = ROOT.TCanvas()
    c1.cd()
    c1.SetFrameLineWidth(2)

    hi_W = ROOT.TH1D("weight","k", 100, 500, 2000)
    # hi_W = hi_1.Clone()
    # hi_W.Divide(hi_2)
    hi_W = hi_1/hi_2

    
    hi_W.Draw('E')
    line.Draw("same")
    
   
    return hi_W


# hist_comp(file_XK,file_XK_MC,"x","XK")
# hist_comp(file_ccK,file_ccK_MC,"cc","XK")
# hist_comp(file_XKpim,file_XKpim_MC,"x","KPim")
# hist_comp(file_ccKpim,file_ccKpim_MC,"cc","KPim")
# hist_comp(file_Xpip,file_Xpip_MC,"x","pip")
# hist_comp(file_ccpip,file_ccpip_MC,"cc","pip")  
# hist_comp(file_X_jpsipipi,file_X_jpsipipi_MC,"x","jpsipipi")
# hist_comp(file_cc_jpsipipi,file_cc_jpsipipi_MC,"cc","jpsipipi") 
h_X_W =hist_comp(file_XKpp,file_XKpp_MC,"x","Kpp")
h_cc_W = hist_comp(file_ccKpp,file_ccKpp_MC,"cc","Kpp")
# hist_comp(file_Xpim,file_Xpim_MC,"x","pim")
# hist_comp(file_ccpim,file_ccpim_MC,"cc","pim")
# hist_comp(file_Xpimp,file_Xpimp_MC,"x","pimp")
# hist_comp(file_ccpimp,file_ccpimp_MC,"cc","pimp")
    


#modifying weights using functions manually

# Fit_cc_l = poly.fit(h_cc_W,920,1200,0.0,2,0)

# output_file = ROOT.TFile(f"{mc_dir}/re-weightMC_cc.root", "RECREATE")
# tree_w = ROOT.TTree("histo", "Values from the histogram bins")
# val = array('d', [0.0])
# bin_center = array('d', [0.])
# bin_index = array('i', [0]) 
# tree_w.Branch("weight", val, "weight/D")
# tree_w.Branch("bin_center", bin_center, 'bin_center/D')
# tree_w.Branch("bin_index", bin_index, 'bin_index/I')
# hi_W = ROOT.TH1D("weight"," ", 100, 500, 2000)

# n_bins = h_cc_W.GetNbinsX()
# for i in range(1, 57):
#     bin_center[0] = h_cc_W.GetXaxis().GetBinCenter(i)       
#     val[0] = h_cc_W.GetBinContent(i)

#     if (bin_center[0] < 850):
#         val[0] = abs(h_cc_W.GetBinContent(28))
#         # print("less l",bin_center[0],val[0],i)
#         hi_W.Fill(val[0])
#     elif(850 < bin_center[0] < 1200):
#         val[0] = abs(Fit_cc_l.Eval(bin_center[0]))
#         hi_W.Fill(val[0])
#         # print("between",bin_center[0],h_cc_W.GetBinContent(i),i)
#     elif(1340 > bin_center[0] > 1200):        
#         val[0] = abs(h_cc_W.GetBinContent(i)) 
#         hi_W.Fill(val[0])
#         # print("after",bin_center[0],val[0],i) 

#     bin_index[0] = i
#     tree_w.Fill()      
    
    
# Fit_cc_u = poly.fit(h_cc_W,1340,1580,0.0,2,0)  
# for i in range(55, n_bins + 1):
#     bin_center[0] = h_cc_W.GetXaxis().GetBinCenter(i)       
#     val[0] = h_cc_W.GetBinContent(i)
#     if( 1605 > bin_center[0] > 1340):        
#         val[0] = Fit_cc_u.Eval(bin_center[0]) 
#         hi_W.Fill(val[0])
#         # print("between 2",bin_center[0],val[0],i)
#     elif( 1605 < bin_center[0]):        
#         val[0] = h_cc_W.GetBinContent(28) 
#         hi_W.Fill(val[0])
#         # print("end",bin_center[0],val[0],i)    

#     bin_index[0] = i
#     tree_w.Fill()

# output_file.cd()
# tree_w.Write()
# output_file.Close() 

# # modifying X weight
# output_file_X = ROOT.TFile(f"{mc_dir}/re-weightMC_X.root", "RECREATE")
# tree_w_X = ROOT.TTree("histo", "Values from the histogram bins")
# val_X = array('d', [0.0])
# bin_center_X = array('d', [0.])
# bin_index_X = array('i', [0]) 
# tree_w_X.Branch("weight", val_X, "weight/D")
# tree_w_X.Branch("bin_center", bin_center_X, 'bin_center/D')
# tree_w_X.Branch("bin_index", bin_index_X, 'bin_index/I')
# hi_W_X = ROOT.TH1D("weight"," ", 100, 500, 2000)

# Fit_X = DSCB.fit(h_X_W,900,1350,44,1280,100,-10,1.0,-10,1.5,-1)

# for i in range(1, n_bins + 1):
#     bin_center_X[0] = h_X_W.GetXaxis().GetBinCenter(i)       
#     val_X[0] = h_X_W.GetBinContent(i)

#     if (bin_center_X[0] < 957):
#         val_X[0] = abs(0.4)
#         print("less l",bin_center_X[0],val_X[0],i)
#         hi_W_X.Fill(val_X[0])
#     elif(957 < bin_center_X[0] < 1340):
#         val_X[0] = abs(Fit_X.Eval(bin_center_X[0]))
#         hi_W_X.Fill(val_X[0])
#         print("between",bin_center_X[0],h_X_W.GetBinContent(i),i)
#     elif(1340 < bin_center_X[0]< 1500):        
#         val_X[0] = abs(h_X_W.GetBinContent(58)) 
#         hi_W_X.Fill(val_X[0])
#         print("after",bin_center_X[0],val_X[0],i) 
#     elif(1500 < bin_center_X[0]):        
#         val_X[0] = abs(0.4) 
#         hi_W_X.Fill(val_X[0])
#         print("after",bin_center_X[0],val_X[0],i)     
#     bin_index_X[0] = i
#     tree_w_X.Fill()

# output_file_X.cd()
# tree_w_X.Write()
# output_file_X.Close()

