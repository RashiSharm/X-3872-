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
# ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/debug_R_NDoubleDSCBFit.C')
ROOT.gROOT.LoadMacro('/home/rsharm18/work/plot_Scripts_T/debug_R_DSCB_BWFit.C')
# CB = ROOT.debug_R_NDoubleDSCBFit()
CB2 = ROOT.debug_R_DSCB_BWFit()

current_directory = "/home/rsharm18/work/Rootfile/June_25/Kaon_excitations"

user_choice = input("Enter 0 for Data , 1 to cc MC and 2 for X MC ")

nL = nR = -100
alphaL = -100
alphaR = -100

Kaon_mass = 493.68
mu_mass = 105.658
pi_mass = 139.5
if user_choice == "0":
    input = "subreso-Data"
    X_mass = 3872
    file_name = "/home/rsharm18/work/Rootfile/Data/subreso_Data.root"
    sigma_B = 5.68
    sigma_X = 3.70
    output = "Data"
    Lower = 3679
    Upper = 3695
elif user_choice == "1":
    input = "subreso-cc_MC"
    X_mass = 3686
    file_name = "/home/rsharm18/work/Rootfile/cc_MC/subreso_cc.root"
    sigma_B = 5.2
    sigma_X = 2.34
    output = "cc_MC"
    Lower = 3682
    Upper = 3692
elif user_choice == "2":
    input = "subreso-X_MC"
    X_mass = 3872
    file_name = "/home/rsharm18/work/Rootfile/X_MC/subreso_X.root"
    sigma_B = 4.79
    sigma_X = 3.13
    output = "X_MC"
    Lower = 3682
    Upper = 3692
else:
    print("Invalid")        

def PE_calculator(mass,px,py,pz):
    PE = np.sqrt(np.power(px,2)+np.power(py,2)+np.power(pz,2)+(np.power(mass,2)))
    return PE

file = ROOT.TFile.Open(f"{file_name}","READ")
def histo(file,particle,permutation,lower,upper):
    my_tree = file.Get("nTuple")
    # my_tree.AddFriend("nTuple","/home/rsharm18/work/Rootfile/TMVA_Single_Entry_2_X.root")

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

    # BDT = my_tree.GetBranch("BDT")
    Jpsi_reflection = Bp_B_jpsi_pi2pi3.GetLeaf("Bp_B_jpsi_pi2pi3").GetValue()
       

    histo_X  = ROOT.TH1F(f"X Constrained {particle} {permutation}"," ", 100, lower, upper)
    histo_cc = ROOT.TH1F(f"Psi(2S) Constrained {particle} {permutation}"," ", 100, lower, upper)

    histo_X_SB  = ROOT.TH1F(f"X gConstrained {particle} {permutation} SB"," ", 100, lower, upper)
    histo_cc_SB = ROOT.TH1F(f"Psi(2S) gConstrained {particle} {permutation} SB"," ", 100, lower, upper)


    for entry in my_tree:
        branch_value_B = Bp_Jpsi_B_M.GetLeaf("Bp_Jpsi_B_M").GetValue()
        branch_value_X = Bp_Jpsi_X_M.GetLeaf("Bp_Jpsi_X_M").GetValue()
        nCandidates_cut = nCandidate.GetLeaf("nCandidate").GetValue()
    #X   
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
        if (permutation == "Kpp_const"):
            PE = B_K_pe+B_pi2_pe+B_pi3_pe
            PX = B_K_px+B_pi2_px+B_pi3_px
            PY = B_K_py+B_pi2_py+B_pi3_py
            PZ = B_K_pz+B_pi2_pz+B_pi3_pz
            P = np.sqrt(np.power(PX,2)+np.power(PY,2)+np.power(PZ,2))

            
        elif(permutation == "XK"):
            PE = B_mu0_pe+B_mu1_pe+B_pi0_pe+B_pi1_pe+B_K_pe
            PX = B_mu0_px+B_mu1_px+B_pi0_px+B_pi1_px+B_K_px
            PY = B_mu0_py+B_mu1_py+B_pi0_py+B_pi1_py+B_K_py
            PZ = B_mu0_pz+B_mu1_pz+B_pi0_pz+B_pi1_pz+B_K_pz
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

        L01 = Bp_L0DiMuonDecision_TOS.GetLeaf("Bp_L0DiMuonDecision_TOS").GetValue()
        L02 = Bp_L0MuonDecision_TOS.GetLeaf("Bp_L0MuonDecision_TOS").GetValue()
        
        Hlt1_1 = Bp_Hlt1DiMuonHighMassDecision_TOS.GetLeaf("Bp_Hlt1DiMuonHighMassDecision_TOS").GetValue()

        Hlt1_3 = Bp_Hlt1TrackMuonDecision_TOS.GetLeaf("Bp_Hlt1TrackMuonDecision_TOS").GetValue()
        Hlt1_4 = Bp_Hlt1TrackMVADecision_TOS.GetLeaf("Bp_Hlt1TrackMVADecision_TOS").GetValue()

        Hlt2_1 = Bp_Hlt2DiMuonDetachedJPsiDecision_TOS.GetLeaf("Bp_Hlt2DiMuonDetachedJPsiDecision_TOS").GetValue()

        # histo_X.Fill(K_exct)
# defining the Kaon excitation variable  
        if (L01 or L02) and (Hlt1_1 or Hlt1_3 or Hlt1_4 ) and (Hlt2_1) and (nCandidates_cut==0) and ((Lower>Jpsi_reflection or Jpsi_reflection>Upper)):            
         if (abs(branch_value_B-5279.92) < 2.0*sigma_B) :        
            if(particle=='X'and abs(branch_value_X-3872.)<2.0*sigma_X ):
             histo_X.Fill(K_exct) 
            elif (particle=='cc' and abs(branch_value_X-3686.)<2.0*sigma_X):  
             histo_cc.Fill(K_exct)
        # sideband   
         if (abs(branch_value_B-5279.90) > 4.0*sigma_B) and (abs(branch_value_B-5279.90) < 10.0*sigma_B) :     
          if (particle =="X" and abs(branch_value_X-3872.) > 4.0*sigma_X) and (abs(branch_value_X-3872.) < 10.0*sigma_X) :    
            histo_X_SB.Fill(K_exct)    
          elif(particle == "cc" and abs(branch_value_X-3872.) > 4.0*sigma_X) and (abs(branch_value_X-3872.) < 10.0*sigma_X) : 
            histo_cc_SB.Fill(K_exct)   
 
    del my_tree  
    return  histo_X,histo_cc,histo_X_SB,histo_cc_SB


#debug ################
# histogram_X_XK,h_cc_XK,h_X_SB_XK,h_ccsb_XK = histo(file,"X","XK") 
###########################
def hist_save(histog,hist_SB,particle,permutation,lower,upper):

    c0 = ROOT.TCanvas()
    c0.cd()
    c0.SetFrameLineWidth(2)

    
    legend = ROOT.TLegend(0.8, 0.75, 0.9, 0.85)
    # legend.AddEntry(histo_B_mass_signal, "Data")
    # legend.AddEntry(Fit_B_sig, "Fit")
    legend.SetBorderSize(0)

    if (permutation == "Kpp"):
        histog.GetXaxis().SetTitle("m(K^{+}#pi^{+}#pi^{-}) [MeV]")
    elif(permutation == "Xpp_const"):   
        histog.GetXaxis().SetTitle("m_(const)(K^{+}#pi^{+}#pi^{-}) [MeV]")
    elif(permutation == "XK"):   
        histog.GetXaxis().SetTitle(f"m({particle}""K^{+}) [MeV]")
    elif(permutation == "XPim"):
        histog.GetXaxis().SetTitle(f"m({particle}""#pi^{-}) [MeV]") 
    elif(permutation == "XPimK"):
        histog.GetXaxis().SetTitle(f"m({particle}""K^{+}#pi^{-}) [MeV]")     
    elif(permutation == "XPip"):
        histog.GetXaxis().SetTitle(f"m({particle}""#pi^{+}) [MeV]") 
    elif(permutation == "XPimp"): 
        if (particle == "cc"):
            histog.GetXaxis().SetTitle("m(#psi(2S)#pi^{-}#pi^{+}) [MeV]")
        else:    
            histog.GetXaxis().SetTitle("m(X#pi^{-}#pi^{+}) [MeV]")
    

    histog.GetYaxis().SetTitle(f"Number Of Candidates/{histog.GetBinWidth(1)} MeV")
    histog.SetMarkerStyle(20) 
    histog.SetLineWidth(2)
    histog.SetMarkerSize(0.1)
    histog.SetMarkerColor(1)
    histog.SetLineColor(1) 
    histog.Draw("E")
    legend.AddEntry(histog,"Without SB reduction")

    hi_S = ROOT.TH1F(" "," ", 100, lower, upper)
    hist_SB.Scale(1/3.0)
    hi_S = histog - hist_SB
    hi_S.SetLineColor(2)
    hi_S.Draw('same')
    legend.AddEntry(hi_S,"With SB reduction")
    hist_SB.SetLineColor(4)
    legend.AddEntry(hist_SB,"Scaled SB")
    hist_SB.Draw('same')
    legend.Draw('same')
    if (particle == "#psi(2S)"):
        c0.SaveAs(f"{current_directory}/{output}/Kaon_excitations_with_cc_{permutation}.root")
    else:
         c0.SaveAs(f"{current_directory}/{output}/Kaon_excitations_with_{particle}_{permutation}.root")
       
    c0.SaveAs(f"{current_directory}/{output}/Kaon_excitations_with_"f"{particle}_{permutation}.pdf")

    return hi_S

# # Kpp
# histogram_X,h_cc,h_X_SB,h_ccsb = histo(file,"X","Kpp",500,2000)  
# h_X,histogram_cc,h_xsb,h_cc_SB = histo(file,"cc","Kpp",500,2000)

# hist_x = hist_save(histogram_X,h_X_SB,"X","Kpp",500,2000)
# hist_cc = hist_save(histogram_cc,h_cc_SB,"#psi(2S)","Kpp",500,2000)
# #Kpp_Jpsi_const
histogram_X_C,h_cc_C,h_X_SB_C,h_ccsb_C = histo(file,"X","Kpp_const",500,2000)  
h_X_C,histogram_cc_C,h_xsb_C,h_cc_SB_C = histo(file,"cc","Kpp_const",500,2000)

hist_x_C = hist_save(histogram_X_C,h_X_SB_C,"X","Kpp_const",500,2000)
hist_cc_C = hist_save(histogram_cc_C,h_cc_SB_C,"#psi(2S)","Kpp_const",500,2000)
# # #XK
# histogram_X_XK,h_cc_XK,h_X_SB_XK,h_ccsb_XK = histo(file,"X","XK",3000,5000)  
# h_X_XK,histogram_cc_XK,h_xsb_XK,h_cc_SB_XK = histo(file,"cc","XK",3000,5000)

# hist_x_XK = hist_save(histogram_X_XK,h_X_SB_XK,"X","XK",3000,5000)
# hist_cc_XK = hist_save(histogram_cc_XK,h_cc_SB_XK,"#psi(2S)","XK",3000,5000)
# # #XPim
# histogram_X_XPim,h_cc_XPim,h_X_SB_XPim,h_ccsb_XPim = histo(file,"X","XPim",3000,5000)  
# h_X_XPim,histogram_cc_XPim,h_xsb_XPim,h_cc_SB_XPim = histo(file,"cc","XPim",3000,5000)

# hist_x_XPim = hist_save(histogram_X_XPim,h_X_SB_XPim,"X","XPim",3000,5000)
# hist_cc_XPim = hist_save(histogram_cc_XPim,h_cc_SB_XPim,"#psi(2S)","XPim",3000,5000)
# #XPimk
# histogram_X_XPimK,h_cc_XPimK,h_X_SB_XPimK,h_ccsb_XPimK = histo(file,"X","XPimK",3000,6000)  
# h_X_XPimK,histogram_cc_XPimK,h_xsb_XPimK,h_cc_SB_XPimK = histo(file,"cc","XPimK",3000,6000)

# hist_x_XPimK = hist_save(histogram_X_XPimK,h_X_SB_XPimK,"X","XPimK",3000,6000)
# hist_cc_XPimK = hist_save(histogram_cc_XPimK,h_cc_SB_XPimK,"#psi(2S)","XPimK",3000,6000)
# #XPip
# histogram_X_XPip,h_cc_XPip,h_X_SB_XPip,h_ccsb_XPip = histo(file,"X","XPip",3000,5000)  
# h_X_XPip,histogram_cc_XPip,h_xsb_XPip,h_cc_SB_XPip = histo(file,"cc","XPip",3000,5000)

# hist_x_XPip = hist_save(histogram_X_XPip,h_X_SB_XPip,"X","XPip",3000,5000)
# hist_cc_XPip = hist_save(histogram_cc_XPip,h_cc_SB_XPip,"#psi(2S)","XPip",3000,5000)
# # #XPimp
histogram_X_XPimp,h_cc_XPimp,h_X_SB_XPimp,h_ccsb_XPimp = histo(file,"X","XPimp",3000,5000)  
h_X_XPimp,histogram_cc_XPimp,h_xsb_XPimp,h_cc_SB_XPimp = histo(file,"cc","XPimp",3000,5000)

hist_x_Pimp = hist_save(histogram_X_XPimp,h_X_SB_XPimp,"X","XPimp",3000,5000)
hist_cc_Pimp = hist_save(histogram_cc_XPimp,h_cc_SB_XPimp,"#psi(2S)","XPimp",3000,5000)

