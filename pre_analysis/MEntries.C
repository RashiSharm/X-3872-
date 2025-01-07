#define MEntries_cxx
#include "MEntries.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <bits/stdc++.h>
#include <algorithm>
#include <iostream>

using namespace std;
struct EventS{
       Double_t ptsum;
       Double_t ptmin;
       Double_t Q;
       int save;
       Long64_t ie;
     };

struct less_k
{
  inline bool operator() (const EventS& e1, const EventS& e2)
  {
    if(fabs(e1.ptsum-e2.ptsum)<0.01){
        return (e1.Q < e2.Q);
    }
    if(e1.ptsum > e2.ptsum) return true;
    if(e1.ptsum < e2.ptsum) return false;
    return (e1.Q < e2.Q);
  }
};


void MEntries::Loop()
{
//   In a ROOT session, you can do:
//      root> .L MEntries.C
//      root> MEntries t
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

   TFile * newfile = new TFile("SEntries_cc.root","recreate");
   newfile->cd();
   TTree * nt = fChain->CloneTree(0);

   UInt_t isMaxptmin;
   nt->Branch("isMaxptmin",&isMaxptmin,"isMaxptmin/i");

   ULong64_t rn(0);
   ULong64_t en(0);
   //   ULong64_t ie(0);
   Double_t best(0.0);


   int all(0);
   int allp(0);
   int un(0);                                     

   Long64_t nentries = fChain->GetEntriesFast();

   //   std::vector <Long64_t> ie;

   std::vector <EventS> v;

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
   
      ++all;
      if( all%10000==0 )std::cout << " read " << all << " passed PID " << allp << " frac.rej. " << double(all-allp)/((all>0)?all:1) <<  " wrote " << un << " fraq.rej. " << double(allp-un)/((allp>0)?allp:1) << std::endl;

      if( X_MM-Jpsi_MM-sqrt(pow(Pi0_PE+Pi1_PE,2)-pow(Pi0_PX+Pi1_PX,2)-pow(Pi0_PY+Pi1_PY,2)-pow(Pi0_PZ+Pi1_PZ,2)) > 300 )continue;// remove events with Q greater than 300
      if( K_PIDK < Pi0_PIDK )continue;
      if( K_PIDK < Pi1_PIDK )continue;
      if( K_PIDK < Pi2_PIDK )continue;
      if( K_PIDK < Pi3_PIDK )continue;// reject if its more likely to be a pion than a kaon
      if( min(min(Pi0_IPCHI2_OWNPV,Pi1_IPCHI2_OWNPV),min(Pi2_IPCHI2_OWNPV,Pi3_IPCHI2_OWNPV)) < 16.0 )continue;// reject if less than 16
      if( K_PIDK < 0 )continue; //K_PIDK must be greater > than 0, so remove every less < than 0
      if( Bp_Jpsi_B_M-5279 > 221 )continue;// reject if B mass is greater than 200
      if( 5279-Bp_Jpsi_B_M > 176 )continue;//
      if(min(min(Pi0_PT,Pi1_PT),min(Pi2_PT,Pi3_PT))<100)continue;      

      ++allp;
      


      EventS a;
      a.ptsum = Pi0_PT+Pi1_PT+Pi2_PT+Pi3_PT+K_PT+Jpsi_PT;
      a.Q = X_MM-Jpsi_MM-sqrt(pow(Pi0_PE+Pi1_PE,2)-pow(Pi0_PX+Pi1_PX,2)-pow(Pi0_PY+Pi1_PY,2)-pow(Pi0_PZ+Pi1_PZ,2));
      a.ie = jentry;
      a.ptmin=min(min(Pi0_PT,Pi1_PT),min(Pi2_PT,Pi3_PT));      
                                   
      if( rn==0 ){
        rn = runNumber;
        en = eventNumber;
      }

//      Double_t ptsum = Pi0_PT+Pi1_PT+Pi2_PT+Pi3_PT+K_PT+Jpsi_PT;
      if( (runNumber==rn) && (eventNumber==en) ){
	v.push_back(a);
//	ie.push_back(jentry);
//        if( ptsum > best ){
//          best = ptsum;
//	  //          ie = jentry;
//        }
        continue;
      }

      // new event                                                                                          
      rn = runNumber;
      en = eventNumber;
      // best = ptsum;

      //      GetEntry(ie);  // load previous best entry here and do something with it if needed                    
      //ie = jentry;

//      for (auto j = ie.begin(); j != ie.end(); ++j){
//	GetEntry(*j);
//        totCandidates = ie.size();
//	nt->Fill();
//	++un;
//      }
//      ie.clear();
//      ie.push_back(jentry);
//
//   }
//
//   if( ie.size() ){
//      totCandidates = ie.size();
//      for (auto j = ie.begin(); j != ie.end(); ++j){
//	GetEntry(*j);
//	nt->Fill();
//	++un;
//      }
      std::sort(v.begin(), v.end(), less_k());   
      // removing repeated PTSUM's
      int ltotCandidates = 0;
      Double_t maxptmin=0;
      for (unsigned int i=0; i < v.size(); ++i){
	if(i>0){
	  if(fabs(v[i].ptsum - v[i-1].ptsum)<0.01){
	    v[i].save = 0;
	    continue;
	  }
          maxptmin = (v[i].ptmin>maxptmin)?v[i].ptmin:maxptmin;
	}
	++ltotCandidates;
	v[i].save = 1;	
      }
      
      int lnCandidate=0;
      for (unsigned int j=0; j< v.size();++j){
	if(v[j].save==1){
	  GetEntry(v[j].ie);
          totCandidates=ltotCandidates;
          nCandidate=lnCandidate;
          isMaxptmin = (maxptmin==v[j].ptmin)?1:0;
	  nt->Fill();
          ++lnCandidate;
	  ++un;
	}
      }

      v.clear();
      v.push_back(a);
   }

      std::sort(v.begin(), v.end(), less_k());   
      // removing repeated PTSUM's
      int ltotCandidates = 0;
      Double_t maxptmin=0;
      for (unsigned int i=0; i < v.size(); ++i){
	if(i>0){
	  if(fabs(v[i].ptsum - v[i-1].ptsum)<0.01){
	    v[i].save = 0;
	    continue;
	  }
          maxptmin = (v[i].ptmin>maxptmin)?v[i].ptmin:maxptmin;
	}
	++ltotCandidates;
	v[i].save = 1;	
      }
      
      int lnCandidate=0;
      for (unsigned int j=0; j< v.size();++j){
	if(v[j].save==1){
	  GetEntry(v[j].ie);
          totCandidates=ltotCandidates;
          nCandidate=lnCandidate;
          isMaxptmin = (maxptmin==v[j].ptmin)?1:0;
	  nt->Fill();
          ++lnCandidate;
	  ++un;
	}
      }


   std::cout << " ========== FINAL =========== " << std::endl;
   std::cout << " read " << all << " passed PID " << allp << " frac.rej. " << double(all-allp)/((all>0)?all:1) <<  " wrote " << un << " fraq.rej. " << double(allp-un)/((allp>0)?allp:1) << std::endl;

   nt -> AutoSave();

   newfile->Write();
   newfile->Close();

}
