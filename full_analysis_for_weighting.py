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


current_directory = "./Jul_25/weighted"

user_choice = input("Enter 0 for Data , 1 to cc MC and 2 for X MC ")
nL = nR = -100
alphaL = -100
alphaR = -100
if user_choice == "0":
    input = "subreso-Data"
    mass = 3872
    B_pos = 120
    file_name = "./Data/subreso_Data.root"
    sigma_B = 5.68
    sigma_X = 4.70
    output = "Data"
    Lower = 3679
    Upper = 3695
elif user_choice == "1":
    input = "subreso-cc_MC"
    mass = 3686
    B_pos = 100
    file_name = "./cc_MC/subreso_cc.root"
    weight_file = "/swdev/sharmar/X_analysis/Jul_25/Kaon_excitations/compared/rewight_Kpp_cc_smooth.root"
    sigma_B = 5.03
    sigma_X = 2.6
    output = "cc_MC"
    Lower = 3682
    Upper = 3692
elif user_choice == "2":
    input = "subreso-X_MC"
    mass = 3872
    B_pos = 11000
    file_name = "./X_MC/subreso_X.root"
    weight_file = "/swdev/sharmar/X_analysis/Jul_25/Kaon_excitations/compared/rewight_Kpp_x_smooth.root"
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
def add_branch(file_name,file_h,tree_w,permutation):
    hist = file_h.Get(f"{tree_w}")

    #ROOT File
    file = ROOT.TFile.Open(f"{file_name}","UPDATE")
    my_tree = file.Get("nTuple;10")
    # my_tree.AddFriend("nTuple","/home/rsharm18/work/Rootfile/TMVA_Single_Entry_2_X.root")
    weight_arr = array('d',[0.]) 
    m_kpp_arr = array('d',[0.])

    weight = my_tree.Branch("weight",weight_arr,'weight/D')
    m_kpp = my_tree.Branch("m_kpp",m_kpp_arr,'m_kpp/D')

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

    # B +PV + Jpsi constraint variables 
    #K
    Bp_B_K_px = my_tree.GetBranch("Bp_B_K_px")
    Bp_B_K_py = my_tree.GetBranch("Bp_B_K_py")
    Bp_B_K_pz = my_tree.GetBranch("Bp_B_K_pz")
    # mu0
    Bp_B_mu0_px = my_tree.GetBranch("Bp_B_mu0_px")
    Bp_B_mu0_py = my_tree.GetBranch("Bp_B_mu0_py")
    Bp_B_mu0_pz = my_tree.GetBranch("Bp_B_mu0_pz")

    Bp_B_mu1_px = my_tree.GetBranch("Bp_B_mu1_px")
    Bp_B_mu1_py = my_tree.GetBranch("Bp_B_mu1_py")
    Bp_B_mu1_pz = my_tree.GetBranch("Bp_B_mu1_pz")
    # pi
    Bp_B_pi0_px = my_tree.GetBranch("Bp_B_pi0_px")
    Bp_B_pi0_py = my_tree.GetBranch("Bp_B_pi0_py")
    Bp_B_pi0_pz = my_tree.GetBranch("Bp_B_pi0_pz")

    Bp_B_pi1_px = my_tree.GetBranch("Bp_B_pi1_px")
    Bp_B_pi1_py = my_tree.GetBranch("Bp_B_pi1_py")
    Bp_B_pi1_pz = my_tree.GetBranch("Bp_B_pi1_pz")

    Bp_B_pi2_px = my_tree.GetBranch("Bp_B_pi2_px")
    Bp_B_pi2_py = my_tree.GetBranch("Bp_B_pi2_py")
    Bp_B_pi2_pz = my_tree.GetBranch("Bp_B_pi2_pz")

    Bp_B_pi3_px = my_tree.GetBranch("Bp_B_pi3_px")
    Bp_B_pi3_py = my_tree.GetBranch("Bp_B_pi3_py")
    Bp_B_pi3_pz = my_tree.GetBranch("Bp_B_pi3_pz")

    Pi2_PE = my_tree.GetBranch("Pi2_PE")
    Pi2_PX = my_tree.GetBranch("Pi2_PX")
    Pi2_PY = my_tree.GetBranch("Pi2_PY")
    Pi2_PZ = my_tree.GetBranch("Pi2_PZ")
    Pi3_PE = my_tree.GetBranch("Pi3_PE")
    Pi3_PX = my_tree.GetBranch("Pi3_PX")
    Pi3_PY = my_tree.GetBranch("Pi3_PY")
    Pi3_PZ = my_tree.GetBranch("Pi3_PZ")
    # print()
    for i in range(0,my_tree.GetEntries()):
    # for i in range(0,10000):
    # for entry in my_tree:
      my_tree.GetEntry(i)
      branch_value_B = Bp_Jpsi_B_M.GetLeaf("Bp_Jpsi_B_M").GetValue()
      branch_value_X = Bp_Jpsi_X_M.GetLeaf("Bp_Jpsi_X_M").GetValue()
      nCandidates_cut = nCandidate.GetLeaf("nCandidate").GetValue()
      Jpsi_reflection = Bp_B_jpsi_pi2pi3.GetLeaf("Bp_B_jpsi_pi2pi3").GetValue()
  #B + PV + Jpsi constrained variable
      B_K_px = Bp_B_K_px.GetLeaf("Bp_B_K_px").GetValue()
      B_K_py = Bp_B_K_py.GetLeaf("Bp_B_K_py").GetValue()
      B_K_pz = Bp_B_K_pz.GetLeaf("Bp_B_K_pz").GetValue()

      B_mu0_px = Bp_B_mu0_px.GetLeaf("Bp_B_mu0_px").GetValue()
      B_mu0_py = Bp_B_mu0_py.GetLeaf("Bp_B_mu0_py").GetValue()
      B_mu0_pz = Bp_B_mu0_pz.GetLeaf("Bp_B_mu0_pz").GetValue()

      B_mu1_px = Bp_B_mu1_px.GetLeaf("Bp_B_mu1_px").GetValue()
      B_mu1_py = Bp_B_mu1_py.GetLeaf("Bp_B_mu1_py").GetValue()
      B_mu1_pz = Bp_B_mu1_pz.GetLeaf("Bp_B_mu1_pz").GetValue()

      B_pi0_px = Bp_B_pi0_px.GetLeaf("Bp_B_pi0_px").GetValue()
      B_pi0_py = Bp_B_pi0_py.GetLeaf("Bp_B_pi0_py").GetValue()
      B_pi0_pz = Bp_B_pi0_pz.GetLeaf("Bp_B_pi0_pz").GetValue()

      B_pi1_px = Bp_B_pi1_px.GetLeaf("Bp_B_pi1_px").GetValue()
      B_pi1_py = Bp_B_pi1_py.GetLeaf("Bp_B_pi1_py").GetValue()
      B_pi1_pz = Bp_B_pi1_pz.GetLeaf("Bp_B_pi1_pz").GetValue()

      B_pi2_px = Bp_B_pi2_px.GetLeaf("Bp_B_pi2_px").GetValue()
      B_pi2_py = Bp_B_pi2_py.GetLeaf("Bp_B_pi2_py").GetValue()
      B_pi2_pz = Bp_B_pi2_pz.GetLeaf("Bp_B_pi2_pz").GetValue()

      B_pi3_px = Bp_B_pi3_px.GetLeaf("Bp_B_pi3_px").GetValue()
      B_pi3_py = Bp_B_pi3_py.GetLeaf("Bp_B_pi3_py").GetValue()
      B_pi3_pz = Bp_B_pi3_pz.GetLeaf("Bp_B_pi3_pz").GetValue()
      
      # PE calculation
      B_K_pe = PE_calculator(Kaon_mass,B_K_px,B_K_py,B_K_pz)
      B_mu0_pe = PE_calculator(mu_mass,B_mu0_px,B_mu0_py,B_mu0_pz)
      B_mu1_pe = PE_calculator(mu_mass,B_mu1_px,B_mu1_py,B_mu1_pz)
      B_pi0_pe = PE_calculator(pi_mass,B_pi0_px,B_pi0_py,B_pi0_pz)
      B_pi1_pe = PE_calculator(pi_mass,B_pi1_px,B_pi1_py,B_pi1_pz)
      B_pi2_pe = PE_calculator(pi_mass,B_pi2_px,B_pi2_py,B_pi2_pz)
      B_pi3_pe = PE_calculator(pi_mass,B_pi3_px,B_pi3_py,B_pi3_pz)
      

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
      # BDT_X = BDT.GetLeaf("BDT").GetValue()
      if (permutation == "Kpp"):
          PE = KPE+Pi2PE+Pi3PE
          PX = KPX+Pi2PX+Pi3PX
          PY = KPY+Pi2PY+Pi3PY
          PZ = KPZ+Pi2PZ+Pi3PZ
      elif (permutation == "Kpp_const"):
          PE = B_K_pe+B_pi2_pe+B_pi3_pe
          PX = B_K_px+B_pi2_px+B_pi3_px
          PY = B_K_py+B_pi2_py+B_pi3_py
          PZ = B_K_pz+B_pi2_pz+B_pi3_pz
      elif(permutation == "XK"):
          PE = B_mu0_pe+B_mu1_pe+B_pi0_pe+B_pi1_pe+B_K_pe
          PX = B_mu0_px+B_mu1_px+B_pi0_px+B_pi1_px+B_K_px
          PY = B_mu0_py+B_mu1_py+B_pi0_py+B_pi1_py+B_K_py
          PZ = B_mu0_pz+B_mu1_pz+B_pi0_pz+B_pi1_pz+B_K_pz
      elif(permutation == "jpsipipi"):
          PE = B_mu0_pe+B_mu1_pe+B_pi2_pe+B_pi3_pe
          PX = B_mu0_px+B_mu1_px+B_pi2_px+B_pi3_px
          PY = B_mu0_py+B_mu1_py+B_pi2_py+B_pi3_py
          PZ = B_mu0_pz+B_mu1_pz+B_pi2_pz+B_pi3_pz
      elif(permutation == "XPim"):
          PE = B_mu0_pe+B_mu1_pe+B_pi0_pe+B_pi1_pe+B_pi2_pe
          PX = B_mu0_px+B_mu1_px+B_pi0_px+B_pi1_px+B_pi2_px
          PY = B_mu0_py+B_mu1_py+B_pi0_py+B_pi1_py+B_pi2_py
          PZ = B_mu0_pz+B_mu1_pz+B_pi0_pz+B_pi1_pz+B_pi2_pz
      elif(permutation == "XPimK"):
          PE = B_mu0_pe+B_mu1_pe+B_pi0_pe+B_pi1_pe+B_pi2_pe+B_K_pe
          PX = B_mu0_px+B_mu1_px+B_pi0_px+B_pi1_px+B_pi2_px+B_K_px
          PY = B_mu0_py+B_mu1_py+B_pi0_py+B_pi1_py+B_pi2_py+B_K_py
          PZ = B_mu0_pz+B_mu1_pz+B_pi0_pz+B_pi1_pz+B_pi2_pz+B_K_pz
      elif(permutation == "XPip"):
          PE = B_mu0_pe+B_mu1_pe+B_pi0_pe+B_pi1_pe+B_pi3_pe
          PX = B_mu0_px+B_mu1_px+B_pi0_px+B_pi1_px+B_pi3_px
          PY = B_mu0_py+B_mu1_py+B_pi0_py+B_pi1_py+B_pi3_py
          PZ = B_mu0_pz+B_mu1_pz+B_pi0_pz+B_pi1_pz+B_pi3_pz 
      elif(permutation == "XPimp"):
          PE = B_mu0_pe+B_mu1_pe+B_pi0_pe+B_pi1_pe+B_pi2_pe+B_pi3_pe
          PX = B_mu0_px+B_mu1_px+B_pi0_px+B_pi1_px+B_pi2_px+B_pi3_px
          PY = B_mu0_py+B_mu1_py+B_pi0_py+B_pi1_py+B_pi2_py+B_pi3_py
          PZ = B_mu0_pz+B_mu1_pz+B_pi0_pz+B_pi1_pz+B_pi2_pz+B_pi3_pz   

      # K_exct = np.sqrt((PE-P)*(P+PE))
      K_exct = np.sqrt(np.power(PE,2)-np.power(PX,2)-np.power(PY,2)-np.power(PZ,2))
      m_kpp_arr[0] = K_exct
    #   print(K_exct, m_kpp_arr[0])
      

      
      nbins = hist.GetNbinsX()
      for j in range(1, nbins+1):
        L_E = hist.GetXaxis().GetBinLowEdge(j)
        U_E = L_E + 15.0
        if (L_E <= K_exct < U_E):
          if ( hist.GetBinContent(j) == 0.0):
            weight_arr[0] = 1.0
            # print("1.0",weight_arr,hist.GetBinContent(j))
          else:  
            k = hist.GetBinContent(j)
            weight_arr[0] = k
            # print("not 1.0",weight_arr,hist.GetBinContent(j))

    # #   weight.Fill()    
          # print(j, weight_arr,K_exct,i)
      my_tree.Fill()   # this one worked
    #   my_tree.Write("",ROOT.TObject.kOverwrite)  
      print(i)
    file.cd()
    file.Write("",ROOT.TObject.kOverwrite) 

if (user_choice == "1"):
  add_branch(file_name,file_h,"hcc1","Kpp")
elif (user_choice == "2"):
  add_branch(file_name,file_h,"hx1","Kpp")


