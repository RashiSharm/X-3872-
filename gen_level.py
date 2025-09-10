# This file was the first way to do sideband fitting, where I simply fit the humps in the Xmass, I thought I was doing the fit for upper and lower sidebands in X mass region. That is combined B Sideband.

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
ROOT.gROOT.LoadMacro('./plot_Scripts_T/sumH.C')
ROOT.gROOT.LoadMacro('./plot_Scripts_T/debug_R_NDoubleDSCBFit.C')
CB = ROOT.debug_R_NDoubleDSCBFit()


user_choice = input("1 to cc MC and 2 for X MC ")
# nL = nR = -100
# alphaL = -100
# alphaR = -100
# if user_choice == "0":
#     input = "subreso-Data"
#     mass = 3872
#     B_pos = 120
#     file_name = "./Data/subreso_Data.root"
#     sigma_B = 5.68
#     sigma_X = 4.70
#     output = "Data"
#     Lower = 3679
#     Upper = 3695
if user_choice == "1":
    input = "subreso-cc_MC"
    mass = 3686
    B_pos = 100
    # file_name = "/swdev/sharmar/X_analysis/MC_gen/DVntuple_002-50000ev-20250815.root"
    # weight_file = "/swdev/sharmar/X_analysis/Jul_25/Kaon_excitations/compared/rewight_Kpp_cc_Int_Nom.root"
    file_name = "/swdev/sharmar/X_analysis/Sept_25/cc_MC/DVntuple_002-50000ev-20250815.root"
    weight_file = "/swdev/sharmar/X_analysis/Sept_25/Kaon_excitations/compared/reweight_Kpp_cc.root"
    sigma_B = 5.03
    sigma_X = 2.6
    output = "cc_MC"
    Lower = 3682
    Upper = 3692
elif user_choice == "2":
    input = "subreso-X_MC"
    mass = 3872
    B_pos = 11000
    # file_name = "/swdev/sharmar/X_analysis/MC_gen/DVntuple_001-50000ev-20250815.root"
    # weight_file = "/swdev/sharmar/X_analysis/Jul_25/Kaon_excitations/compared/rewight_Kpp_x_Int_Nom.root"
    file_name = "/swdev/sharmar/X_analysis/Sept_25/X_MC/DVntuple_001-50000ev-20250815.root"
    weight_file = "/swdev/sharmar/X_analysis/Sept_25/Kaon_excitations/compared/reweight_Kpp_x.root"
    
    sigma_B = 5.5
    sigma_X = 2.5
    output = "X_MC"
    Lower = 3682
    Upper = 3692
else:
    print("Invalid")        


def PE_calculator(mass,px,py,pz):
    PE = np.sqrt(np.power(px,2)+np.power(py,2)+np.power(pz,2)+(np.power(mass,2)))
    return PE

Kaon_mass = 493.68
mu_mass = 105.658
pi_mass = 139.5    
file_h = ROOT.TFile.Open(f"{weight_file}","READ")
# if (user_choice == "1" or user_choice == "2"):
def add_branch(file_name,file_h,tree_w,permutation,mean):
    hist = file_h.Get(f"{tree_w}")

    #ROOT File
    file = ROOT.TFile.Open(f"{file_name}","UPDATE")
    my_tree = file.Get("MCDecayTreeTuple/MCDecayTree")
    avg_weight_arr = array('d',[0.]) 
    weight_arr = array('d',[0.]) 
    m_kpp_arr = array('d',[0.])

    avg_weight = my_tree.Branch("avg_weight",avg_weight_arr,'avg_weight/D')
    weight = my_tree.Branch("weight",weight_arr,'weight/D')
    m_kpp = my_tree.Branch("m_kpp",m_kpp_arr,'m_kpp/D')
    
    Kplus_E = my_tree.GetBranch("Kplus_E")
    Kplus_PX = my_tree.GetBranch("Kplus_PX")
    Kplus_PY = my_tree.GetBranch("Kplus_PY")
    Kplus_PZ = my_tree.GetBranch("Kplus_PZ")

    muplus_E = my_tree.GetBranch("muplus_E")
    muplus_PX = my_tree.GetBranch("muplus_PX")
    muplus_PY = my_tree.GetBranch("muplus_PY")
    muplus_PZ = my_tree.GetBranch("muplus_PZ")

    muminus_E = my_tree.GetBranch("muminus_E")
    muminus_PX = my_tree.GetBranch("muminus_PX")
    muminus_PY = my_tree.GetBranch("muminus_PY")
    muminus_PZ = my_tree.GetBranch("muminus_PZ")

    piplus_E = my_tree.GetBranch("piplus_E")
    piplus_PX = my_tree.GetBranch("piplus_PX")
    piplus_PY = my_tree.GetBranch("piplus_PY")
    piplus_PZ = my_tree.GetBranch("piplus_PZ")

    piminus_E = my_tree.GetBranch("piminus_E")
    piminus_PX = my_tree.GetBranch("piminus_PX")
    piminus_PY = my_tree.GetBranch("piminus_PY")
    piminus_PZ = my_tree.GetBranch("piminus_PZ")

    piplus0_E = my_tree.GetBranch("piplus0_E")
    piplus0_PX = my_tree.GetBranch("piplus0_PX")
    piplus0_PY = my_tree.GetBranch("piplus0_PY")
    piplus0_PZ = my_tree.GetBranch("piplus0_PZ")

    piminus0_E = my_tree.GetBranch("piminus0_E")
    piminus0_PX = my_tree.GetBranch("piminus0_PX")
    piminus0_PY = my_tree.GetBranch("piminus0_PY")
    piminus0_PZ = my_tree.GetBranch("piminus0_PZ")
    # print(my_tree.GetEntries())
    for i in range(0,my_tree.GetEntries()):
    # for i in range(0,100):
    # for entry in my_tree:
      my_tree.GetEntry(i)

      Kplus_E_val = Kplus_E.GetLeaf("Kplus_E").GetValue()
      Kplus_PX_val = Kplus_PX.GetLeaf("Kplus_PX").GetValue()
      Kplus_PY_val = Kplus_PY.GetLeaf("Kplus_PY").GetValue()
      Kplus_PZ_val = Kplus_PZ.GetLeaf("Kplus_PZ").GetValue()

      muplus_E_val = muplus_E.GetLeaf("muplus_E").GetValue()
      muplus_PX_val = muplus_PX.GetLeaf("muplus_PX").GetValue()
      muplus_PY_val = muplus_PY.GetLeaf("muplus_PY").GetValue()
      muplus_PZ_val = muplus_PZ.GetLeaf("muplus_PZ").GetValue()

      muminus_E_val = muminus_E.GetLeaf("muminus_E").GetValue()
      muminus_PX_val = muminus_PX.GetLeaf("muminus_PX").GetValue()
      muminus_PY_val = muminus_PY.GetLeaf("muminus_PY").GetValue()
      muminus_PZ_val = muminus_PZ.GetLeaf("muminus_PZ").GetValue()

      piplus_E_val = piplus_E.GetLeaf("piplus_E").GetValue()
      piplus_PX_val = piplus_PX.GetLeaf("piplus_PX").GetValue()
      piplus_PY_val = piplus_PY.GetLeaf("piplus_PY").GetValue()
      piplus_PZ_val = piplus_PZ.GetLeaf("piplus_PZ").GetValue()

      piminus_E_val = piminus_E.GetLeaf("piminus_E").GetValue()
      piminus_PX_val = piminus_PX.GetLeaf("piminus_PX").GetValue()
      piminus_PY_val = piminus_PY.GetLeaf("piminus_PY").GetValue()
      piminus_PZ_val = piminus_PZ.GetLeaf("piminus_PZ").GetValue()

      piplus0_E_val = piplus0_E.GetLeaf("piplus0_E").GetValue()
      piplus0_PX_val = piplus0_PX.GetLeaf("piplus0_PX").GetValue()
      piplus0_PY_val = piplus0_PY.GetLeaf("piplus0_PY").GetValue()
      piplus0_PZ_val = piplus0_PZ.GetLeaf("piplus0_PZ").GetValue()

      piminus0_E_val = piminus0_E.GetLeaf("piminus0_E").GetValue()
      piminus0_PX_val = piminus0_PX.GetLeaf("piminus0_PX").GetValue()
      piminus0_PY_val = piminus0_PY.GetLeaf("piminus0_PY").GetValue()
      piminus0_PZ_val = piminus0_PZ.GetLeaf("piminus0_PZ").GetValue()
     
      PE = Kplus_E_val + piplus0_E_val + piminus0_E_val
      PX = Kplus_PX_val + piplus0_PX_val + piminus0_PX_val
      PY = Kplus_PY_val + piplus0_PY_val + piminus0_PY_val
      PZ = Kplus_PZ_val + piplus0_PZ_val + piminus0_PZ_val
  
      K_exct = np.sqrt(np.power(PE,2)-np.power(PX,2)-np.power(PY,2)-np.power(PZ,2))
      m_kpp_arr[0] = K_exct

      
      if (hist.Interpolate(K_exct) == 0.0):
        weight_arr[0]= 0.0
        avg_weight_arr[0] = 0.0
      else:  
        avg_weight_arr[0] = hist.Interpolate(K_exct)/mean
        weight_arr[0]= hist.Interpolate(K_exct)

      # nbins = hist.GetNbinsX()
      # for j in range(1, nbins+1):
      #   L_E = hist.GetXaxis().GetBinLowEdge(j)
      #   U_E = L_E + 15.0
      #   if (L_E <= K_exct < U_E):
      #     # if ( hist.GetBinContent(j) == 0.0):
      #     #   weight_arr[0] = 0.0
      #     # else:  
      #     k = hist.GetBinContent(j)
      #     weight_arr[0] = k
      
      weight.Fill()
      avg_weight.Fill()
      m_kpp.Fill()
    
      print(i)
    # my_tree.Write("",ROOT.TObject.kOverwrite)  
    file.cd()
    file.Write("",ROOT.TObject.kOverwrite) 
    # file.Close()

if (user_choice == "1"):
  add_branch(file_name,file_h,"hcc1","Kpp",0.97343723)
elif (user_choice == "2"):
  add_branch(file_name,file_h,"hx1","Kpp",0.96829675)


