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
# ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/sumH.C')
# # ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/debug_R_NDoubleDSCBFit.C')
# ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/debug_R_DSCB_BWFit.C')
# # CB = ROOT.debug_R_NDoubleDSCBFit()
# CB2 = ROOT.debug_R_DSCB_BWFit()

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
    c0.SaveAs(f"{current_directory}/{particle}_{permutation}.root")

hist_comp(file_XK,file_XK_MC,"x","XK")
hist_comp(file_ccK,file_ccK_MC,"cc","XK")
hist_comp(file_XKpim,file_XKpim_MC,"x","KPim")
hist_comp(file_ccKpim,file_ccKpim_MC,"cc","KPim")
hist_comp(file_Xpip,file_Xpip_MC,"x","pip")
hist_comp(file_ccpip,file_ccpip_MC,"cc","pip")  
hist_comp(file_X_jpsipipi,file_X_jpsipipi_MC,"x","jpsipipi")
hist_comp(file_cc_jpsipipi,file_cc_jpsipipi_MC,"cc","jpsipipi") 
hist_comp(file_XKpp,file_XKpp_MC,"x","Kpp")
hist_comp(file_ccKpp,file_ccKpp_MC,"cc","Kpp")
hist_comp(file_Xpim,file_Xpim_MC,"x","pim")
hist_comp(file_ccpim,file_ccpim_MC,"cc","pim")
hist_comp(file_Xpimp,file_Xpimp_MC,"x","pimp")
hist_comp(file_ccpimp,file_ccpimp_MC,"cc","pimp")
    

   
