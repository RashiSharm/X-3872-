#define SubReso_cxx
#include "SubReso.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void SubReso::Loop(TString outfile)
{
//   In a ROOT session, you can do:
//      root> .L SubReso.C
//      root> SubReso t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
   if (fChain == 0) return;

   // copy tuple and add various invariant masses (J/psi and B mass constrained)
   
   TFile * newfile = new TFile(outfile,"recreate");
   newfile->cd();
   TTree * nt = fChain->CloneTree(0);
   nt -> AutoSave();

   Double_t Bp_B_pipi;
   nt->Branch("Bp_B_pipi",&Bp_B_pipi,"Bp_B_pipi/D");

   Double_t Bp_B_rec_pipi;
   nt->Branch("Bp_B_rec_pipi",&Bp_B_rec_pipi,"Bp_B_rec_pipi/D");

   Double_t Bp_B_rec_Kpipi;
   nt->Branch("Bp_B_rec_Kpipi",&Bp_B_rec_Kpipi,"Bp_B_rec_Kpipi/D");

   Double_t Bp_B_rec_Kpip;
   nt->Branch("Bp_B_rec_Kpip",&Bp_B_rec_Kpip,"Bp_B_rec_Kpip/D");

   Double_t Bp_B_rec_Kpim;
   nt->Branch("Bp_B_rec_Kpim",&Bp_B_rec_Kpim,"Bp_B_rec_Kpim/D");

   Double_t Bp_B_Xpip ;
   nt->Branch("Bp_B_Xpip",&Bp_B_Xpip ,"Bp_B_Xpip/D");

   Double_t Bp_B_Xpim ;
   nt->Branch("Bp_B_Xpim",&Bp_B_Xpim ,"Bp_B_Xpim/D");

   Double_t Bp_B_XK   ;
   nt->Branch("Bp_B_XK",&Bp_B_XK   ,"Bp_B_XK/D");

   Double_t Bp_B_Xpipi;
   nt->Branch("Bp_B_Xpipi",&Bp_B_Xpipi,"Bp_B_Xpipi/D");

   Double_t Bp_B_jpsi_pi0pi1;
   nt->Branch("Bp_B_jpsi_pi0pi1",&Bp_B_jpsi_pi0pi1,"Bp_B_jpsi_pi0pi1/D");

   Double_t Bp_B_jpsi_pi2pi3;
   nt->Branch("Bp_B_jpsi_pi2pi3",&Bp_B_jpsi_pi2pi3,"Bp_B_jpsi_pi2pi3/D");

   Double_t Bp_B_jpsi_4pi;
   nt->Branch("Bp_B_jpsi_4pi",&Bp_B_jpsi_4pi,"Bp_B_jpsi_4pi/D");

   Double_t Bp_B_jpsi_K4pi;
   nt->Branch("Bp_B_jpsi_K4pi",&Bp_B_jpsi_K4pi,"Bp_B_jpsi_K4pi/D");

   Double_t Bp_B_j_4pi ;
   nt->Branch("Bp_B_j_4pi",&Bp_B_j_4pi ,"Bp_B_j_4pi/D");

   Double_t Bp_B_jpsi_Kpip;
   nt->Branch("Bp_B_jpsi_Kpip",&Bp_B_jpsi_Kpip,"Bp_B_jpsi_Kpip/D");

   Double_t Bp_B_jpsi_Kpim;
   nt->Branch("Bp_B_jpsi_Kpim",&Bp_B_jpsi_Kpim,"Bp_B_jpsi_Kpim/D");

   Double_t Bp_B_jpsi_pi0pi3;
   nt->Branch("Bp_B_jpsi_pi0pi3",&Bp_B_jpsi_pi0pi3,"Bp_B_jpsi_pi0pi3/D");

   Double_t Bp_B_jpsi_pi1pi2;
   nt->Branch("Bp_B_jpsi_pi1pi2",&Bp_B_jpsi_pi1pi2,"Bp_B_jpsi_pi1pi2/D");

   const Double_t m_mu2=pow(105.6583755,2);
   const Double_t m_pi2=pow(139.57039,2);
   const Double_t m_K2=pow(493.677,2);
   
   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;

      
      Double_t Bp_B_mu0_E = sqrt( m_mu2 + pow(Bp_B_mu0_px,2) + pow(Bp_B_mu0_py,2) + pow(Bp_B_mu0_pz,2)); 
      Double_t Bp_B_mu1_E = sqrt( m_mu2 + pow(Bp_B_mu1_px,2) + pow(Bp_B_mu1_py,2) + pow(Bp_B_mu1_pz,2)); 
      Double_t Bp_B_pi0_E = sqrt( m_pi2 + pow(Bp_B_pi0_px,2) + pow(Bp_B_pi0_py,2) + pow(Bp_B_pi0_pz,2)); 
      Double_t Bp_B_pi1_E = sqrt( m_pi2 + pow(Bp_B_pi1_px,2) + pow(Bp_B_pi1_py,2) + pow(Bp_B_pi1_pz,2)); 
      Double_t Bp_B_pi2_E = sqrt( m_pi2 + pow(Bp_B_pi2_px,2) + pow(Bp_B_pi2_py,2) + pow(Bp_B_pi2_pz,2)); 
      Double_t Bp_B_pi3_E = sqrt( m_pi2 + pow(Bp_B_pi3_px,2) + pow(Bp_B_pi3_py,2) + pow(Bp_B_pi3_pz,2)); 
      Double_t Bp_B_K_E = sqrt( m_K2 + pow(Bp_B_K_px,2) + pow(Bp_B_K_py,2) + pow(Bp_B_K_pz,2) );

      Bp_B_pipi = sqrt( pow(Bp_B_pi0_E +Bp_B_pi1_E,2)-     
			pow(Bp_B_pi0_px+Bp_B_pi1_px,2)-     
			pow(Bp_B_pi0_py+Bp_B_pi1_py,2)-     
			pow(Bp_B_pi0_pz+Bp_B_pi1_pz,2));

      Bp_B_rec_pipi = sqrt( pow(Bp_B_pi2_E +Bp_B_pi3_E,2)-     
			     pow(Bp_B_pi2_px+Bp_B_pi3_px,2)-     
			     pow(Bp_B_pi2_py+Bp_B_pi3_py,2)-     
			     pow(Bp_B_pi2_pz+Bp_B_pi3_pz,2));

      Bp_B_rec_Kpipi = sqrt( pow(Bp_B_K_E +Bp_B_pi2_E +Bp_B_pi3_E,2)-     
			      pow(Bp_B_K_px+Bp_B_pi2_px+Bp_B_pi3_px,2)-     
			      pow(Bp_B_K_py+Bp_B_pi2_py+Bp_B_pi3_py,2)-     
			      pow(Bp_B_K_pz+Bp_B_pi2_pz+Bp_B_pi3_pz,2));
      Bp_B_rec_Kpip = sqrt( pow(Bp_B_K_E +Bp_B_pi2_E,2)-     
			     pow(Bp_B_K_px+Bp_B_pi2_px,2)-     
			     pow(Bp_B_K_py+Bp_B_pi2_py,2)-     
			     pow(Bp_B_K_pz+Bp_B_pi2_pz,2));
      Bp_B_rec_Kpim = sqrt( pow(Bp_B_K_E +Bp_B_pi3_E,2)-     
			     pow(Bp_B_K_px+Bp_B_pi3_px,2)-     
			     pow(Bp_B_K_py+Bp_B_pi3_py,2)-     
			     pow(Bp_B_K_pz+Bp_B_pi3_pz,2));

      Double_t Bp_B_X_E  = Bp_B_mu0_E +Bp_B_mu1_E +Bp_B_pi0_E +Bp_B_pi1_E; 
      Double_t Bp_B_X_px = Bp_B_mu0_px+Bp_B_mu1_px+Bp_B_pi0_px+Bp_B_pi1_px; 
      Double_t Bp_B_X_py = Bp_B_mu0_py+Bp_B_mu1_py+Bp_B_pi0_py+Bp_B_pi1_py; 
      Double_t Bp_B_X_pz = Bp_B_mu0_pz+Bp_B_mu1_pz+Bp_B_pi0_pz+Bp_B_pi1_pz;      
      Bp_B_Xpip  = sqrt( pow(Bp_B_X_E +Bp_B_pi2_E,2)-     
			 pow(Bp_B_X_px+Bp_B_pi2_px,2)-     
			 pow(Bp_B_X_py+Bp_B_pi2_py,2)-     
			 pow(Bp_B_X_pz+Bp_B_pi2_pz,2));
      Bp_B_Xpim  = sqrt( pow(Bp_B_X_E +Bp_B_pi3_E,2)-     
			 pow(Bp_B_X_px+Bp_B_pi3_px,2)-     
			 pow(Bp_B_X_py+Bp_B_pi3_py,2)-     
			 pow(Bp_B_X_pz+Bp_B_pi3_pz,2));
      Bp_B_XK    = sqrt( pow(Bp_B_X_E +Bp_B_K_E,2)-     
			 pow(Bp_B_X_px+Bp_B_K_px,2)-     
			 pow(Bp_B_X_py+Bp_B_K_py,2)-     
			 pow(Bp_B_X_pz+Bp_B_K_pz,2));
      Bp_B_Xpipi = sqrt( pow(Bp_B_X_E +Bp_B_pi2_E +Bp_B_pi3_E,2)-     
			 pow(Bp_B_X_px+Bp_B_pi2_px+Bp_B_pi3_px,2)-     
			 pow(Bp_B_X_py+Bp_B_pi2_py+Bp_B_pi3_py,2)-     
			 pow(Bp_B_X_pz+Bp_B_pi2_pz+Bp_B_pi3_pz,2));
      Bp_B_Xpip  = sqrt( pow(Bp_B_X_E +Bp_B_pi2_E,2)-     
			 pow(Bp_B_X_px+Bp_B_pi2_px,2)-     
			 pow(Bp_B_X_py+Bp_B_pi2_py,2)-     
			 pow(Bp_B_X_pz+Bp_B_pi2_pz,2));

      Double_t Bp_B_jpsi_E  = Bp_B_mu0_E +Bp_B_mu1_E;
      Double_t Bp_B_jpsi_px = Bp_B_mu0_px+Bp_B_mu1_px;
      Double_t Bp_B_jpsi_py = Bp_B_mu0_py+Bp_B_mu1_py;
      Double_t Bp_B_jpsi_pz = Bp_B_mu0_pz+Bp_B_mu1_pz;
      Bp_B_jpsi_pi0pi1 = sqrt( pow(Bp_B_jpsi_E +Bp_B_pi0_E +Bp_B_pi1_E,2)-     
			 pow(Bp_B_jpsi_px+Bp_B_pi0_px+Bp_B_pi1_px,2)-     
			 pow(Bp_B_jpsi_py+Bp_B_pi0_py+Bp_B_pi1_py,2)-     
			 pow(Bp_B_jpsi_pz+Bp_B_pi0_pz+Bp_B_pi1_pz,2));
      Bp_B_jpsi_pi2pi3 = sqrt( pow(Bp_B_jpsi_E +Bp_B_pi2_E +Bp_B_pi3_E,2)-     
			 pow(Bp_B_jpsi_px+Bp_B_pi2_px+Bp_B_pi3_px,2)-     
			 pow(Bp_B_jpsi_py+Bp_B_pi2_py+Bp_B_pi3_py,2)-     
			 pow(Bp_B_jpsi_pz+Bp_B_pi2_pz+Bp_B_pi3_pz,2));
      Bp_B_jpsi_4pi = sqrt( pow(Bp_B_jpsi_E +Bp_B_pi0_E +Bp_B_pi1_E+Bp_B_pi2_E +Bp_B_pi3_E,2)-     
			   pow(Bp_B_jpsi_px+Bp_B_pi0_px+Bp_B_pi1_px+Bp_B_pi2_px+Bp_B_pi3_px,2)-     
			   pow(Bp_B_jpsi_py+Bp_B_pi0_py+Bp_B_pi1_py+Bp_B_pi2_py+Bp_B_pi3_py,2)-     
			   pow(Bp_B_jpsi_pz+Bp_B_pi0_pz+Bp_B_pi1_pz+Bp_B_pi2_pz+Bp_B_pi3_pz,2));     


      Bp_B_jpsi_K4pi = sqrt( pow(Bp_B_K_E +Bp_B_pi0_E +Bp_B_pi1_E+Bp_B_pi2_E +Bp_B_pi3_E,2)-     
				pow(Bp_B_K_px+Bp_B_pi0_px+Bp_B_pi1_px+Bp_B_pi2_px+Bp_B_pi3_px,2)-     
				pow(Bp_B_K_py+Bp_B_pi0_py+Bp_B_pi1_py+Bp_B_pi2_py+Bp_B_pi3_py,2)-     
				pow(Bp_B_K_pz+Bp_B_pi0_pz+Bp_B_pi1_pz+Bp_B_pi2_pz+Bp_B_pi3_pz,2));     

      Bp_B_j_4pi  = sqrt( pow(Bp_B_pi0_E +Bp_B_pi1_E+Bp_B_pi2_E +Bp_B_pi3_E,2)-     
				pow(Bp_B_pi0_px+Bp_B_pi1_px+Bp_B_pi2_px+Bp_B_pi3_px,2)-     
				pow(Bp_B_pi0_py+Bp_B_pi1_py+Bp_B_pi2_py+Bp_B_pi3_py,2)-     
				pow(Bp_B_pi0_pz+Bp_B_pi1_pz+Bp_B_pi2_pz+Bp_B_pi3_pz,2));     

      Bp_B_jpsi_Kpip = sqrt( pow(Bp_B_K_E +Bp_B_pi0_E,2)-     
			     pow(Bp_B_K_px+Bp_B_pi0_px,2)-     
			     pow(Bp_B_K_py+Bp_B_pi0_py,2)-     
			     pow(Bp_B_K_pz+Bp_B_pi0_pz,2));
      Bp_B_jpsi_Kpim = sqrt( pow(Bp_B_K_E +Bp_B_pi1_E,2)-     
			     pow(Bp_B_K_px+Bp_B_pi1_px,2)-     
			     pow(Bp_B_K_py+Bp_B_pi1_py,2)-     
			     pow(Bp_B_K_pz+Bp_B_pi1_pz,2));

      Bp_B_jpsi_pi0pi3 = sqrt( pow(Bp_B_pi0_E +Bp_B_pi3_E,2)-     
				 pow(Bp_B_pi0_px+Bp_B_pi3_px,2)-     
				 pow(Bp_B_pi0_py+Bp_B_pi3_py,2)-     
				 pow(Bp_B_pi0_pz+Bp_B_pi3_pz,2));
      Bp_B_jpsi_pi1pi2 = sqrt( pow(Bp_B_pi1_E +Bp_B_pi2_E,2)-     
				 pow(Bp_B_pi1_px+Bp_B_pi2_px,2)-     
				 pow(Bp_B_pi1_py+Bp_B_pi2_py,2)-     
				 pow(Bp_B_pi1_pz+Bp_B_pi2_pz,2));
      
      nt->Fill();
   }
   nt -> AutoSave();

   newfile->Write();
   newfile->Close();
}
