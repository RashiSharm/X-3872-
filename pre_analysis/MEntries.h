//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Mon Oct 30 20:28:05 2023 by ROOT version 6.24/08
// from TChain /Bp2XK4Pi/nTuple/
//////////////////////////////////////////////////////////

#ifndef MEntries_h
#define MEntries_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

class MEntries {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.
   static constexpr Int_t kMaxBp_ENDVERTEX_COV = 1;
   static constexpr Int_t kMaxBp_OWNPV_COV = 1;
   static constexpr Int_t kMaxMu0_OWNPV_COV = 1;
   static constexpr Int_t kMaxMu0_ORIVX_COV = 1;
   static constexpr Int_t kMaxMu1_OWNPV_COV = 1;
   static constexpr Int_t kMaxMu1_ORIVX_COV = 1;
   static constexpr Int_t kMaxPi0_OWNPV_COV = 1;
   static constexpr Int_t kMaxPi0_ORIVX_COV = 1;
   static constexpr Int_t kMaxPi1_OWNPV_COV = 1;
   static constexpr Int_t kMaxPi1_ORIVX_COV = 1;
   static constexpr Int_t kMaxK_OWNPV_COV = 1;
   static constexpr Int_t kMaxK_ORIVX_COV = 1;
   static constexpr Int_t kMaxPi2_OWNPV_COV = 1;
   static constexpr Int_t kMaxPi2_ORIVX_COV = 1;
   static constexpr Int_t kMaxPi3_OWNPV_COV = 1;
   static constexpr Int_t kMaxPi3_ORIVX_COV = 1;

   // Declaration of leaf types
   Double_t        Bp_B_Chi2NDoF;
   Double_t        Bp_B_K_px;
   Double_t        Bp_B_K_py;
   Double_t        Bp_B_K_pz;
   Double_t        Bp_B_X_M;
   Double_t        Bp_B_mu0_px;
   Double_t        Bp_B_mu0_py;
   Double_t        Bp_B_mu0_pz;
   Double_t        Bp_B_mu1_px;
   Double_t        Bp_B_mu1_py;
   Double_t        Bp_B_mu1_pz;
   Double_t        Bp_B_pi0_px;
   Double_t        Bp_B_pi0_py;
   Double_t        Bp_B_pi0_pz;
   Double_t        Bp_B_pi1_px;
   Double_t        Bp_B_pi1_py;
   Double_t        Bp_B_pi1_pz;
   Double_t        Bp_B_pi2_px;
   Double_t        Bp_B_pi2_py;
   Double_t        Bp_B_pi2_pz;
   Double_t        Bp_B_pi3_px;
   Double_t        Bp_B_pi3_py;
   Double_t        Bp_B_pi3_pz;
   Double_t        Bp_Jpsi_B_M;
   Double_t        Bp_Jpsi_B_ctau;
   Double_t        Bp_Jpsi_Chi2NDoF;
   Double_t        Bp_Jpsi_X_M;
   Double_t        Bp_ENDVERTEX_X;
   Double_t        Bp_ENDVERTEX_Y;
   Double_t        Bp_ENDVERTEX_Z;
   Double_t        Bp_ENDVERTEX_XERR;
   Double_t        Bp_ENDVERTEX_YERR;
   Double_t        Bp_ENDVERTEX_ZERR;
   Double_t        Bp_ENDVERTEX_CHI2;
   Int_t           Bp_ENDVERTEX_NDOF;
   Float_t         Bp_ENDVERTEX_COV_[3][3];
   Double_t        Bp_OWNPV_X;
   Double_t        Bp_OWNPV_Y;
   Double_t        Bp_OWNPV_Z;
   Double_t        Bp_OWNPV_XERR;
   Double_t        Bp_OWNPV_YERR;
   Double_t        Bp_OWNPV_ZERR;
   Double_t        Bp_OWNPV_CHI2;
   Int_t           Bp_OWNPV_NDOF;
   Float_t         Bp_OWNPV_COV_[3][3];
   Double_t        Bp_IP_OWNPV;
   Double_t        Bp_IPCHI2_OWNPV;
   Double_t        Bp_FD_OWNPV;
   Double_t        Bp_FDCHI2_OWNPV;
   Double_t        Bp_DIRA_OWNPV;
   Double_t        Bp_P;
   Double_t        Bp_PT;
   Double_t        Bp_PE;
   Double_t        Bp_PX;
   Double_t        Bp_PY;
   Double_t        Bp_PZ;
   Double_t        Bp_MM;
   Double_t        Bp_MMERR;
   Double_t        Bp_M;
   Double_t        Bp_TAU;
   Double_t        Bp_TAUERR;
   Double_t        Bp_TAUCHI2;
   Bool_t          Bp_L0Global_Dec;
   Bool_t          Bp_L0Global_TIS;
   Bool_t          Bp_L0Global_TOS;
   Bool_t          Bp_Hlt1Global_Dec;
   Bool_t          Bp_Hlt1Global_TIS;
   Bool_t          Bp_Hlt1Global_TOS;
   Bool_t          Bp_Hlt1Phys_Dec;
   Bool_t          Bp_Hlt1Phys_TIS;
   Bool_t          Bp_Hlt1Phys_TOS;
   Bool_t          Bp_Hlt2Global_Dec;
   Bool_t          Bp_Hlt2Global_TIS;
   Bool_t          Bp_Hlt2Global_TOS;
   Bool_t          Bp_Hlt2Phys_Dec;
   Bool_t          Bp_Hlt2Phys_TIS;
   Bool_t          Bp_Hlt2Phys_TOS;
   Bool_t          Bp_L0DiMuonDecision_Dec;
   Bool_t          Bp_L0DiMuonDecision_TIS;
   Bool_t          Bp_L0DiMuonDecision_TOS;
   Bool_t          Bp_L0MuonDecision_Dec;
   Bool_t          Bp_L0MuonDecision_TIS;
   Bool_t          Bp_L0MuonDecision_TOS;
   Bool_t          Bp_Hlt1DiMuonHighMassDecision_Dec;
   Bool_t          Bp_Hlt1DiMuonHighMassDecision_TIS;
   Bool_t          Bp_Hlt1DiMuonHighMassDecision_TOS;
   Bool_t          Bp_Hlt1TrackMuonDecision_Dec;
   Bool_t          Bp_Hlt1TrackMuonDecision_TIS;
   Bool_t          Bp_Hlt1TrackMuonDecision_TOS;
   Bool_t          Bp_Hlt1TrackMVADecision_Dec;
   Bool_t          Bp_Hlt1TrackMVADecision_TIS;
   Bool_t          Bp_Hlt1TrackMVADecision_TOS;
   Bool_t          Bp_Hlt2DiMuonDetachedJPsiDecision_Dec;
   Bool_t          Bp_Hlt2DiMuonDetachedJPsiDecision_TIS;
   Bool_t          Bp_Hlt2DiMuonDetachedJPsiDecision_TOS;
   Double_t        X_P;
   Double_t        X_PT;
   Double_t        X_PE;
   Double_t        X_PX;
   Double_t        X_PY;
   Double_t        X_PZ;
   Double_t        X_MM;
   Double_t        X_MMERR;
   Double_t        X_M;
   Double_t        Jpsi_P;
   Double_t        Jpsi_PT;
   Double_t        Jpsi_PE;
   Double_t        Jpsi_PX;
   Double_t        Jpsi_PY;
   Double_t        Jpsi_PZ;
   Double_t        Jpsi_MM;
   Double_t        Jpsi_MMERR;
   Double_t        Jpsi_M;
   Double_t        Mu0_OWNPV_X;
   Double_t        Mu0_OWNPV_Y;
   Double_t        Mu0_OWNPV_Z;
   Double_t        Mu0_OWNPV_XERR;
   Double_t        Mu0_OWNPV_YERR;
   Double_t        Mu0_OWNPV_ZERR;
   Double_t        Mu0_OWNPV_CHI2;
   Int_t           Mu0_OWNPV_NDOF;
   Float_t         Mu0_OWNPV_COV_[3][3];
   Double_t        Mu0_IP_OWNPV;
   Double_t        Mu0_IPCHI2_OWNPV;
   Double_t        Mu0_ORIVX_X;
   Double_t        Mu0_ORIVX_Y;
   Double_t        Mu0_ORIVX_Z;
   Double_t        Mu0_ORIVX_XERR;
   Double_t        Mu0_ORIVX_YERR;
   Double_t        Mu0_ORIVX_ZERR;
   Double_t        Mu0_ORIVX_CHI2;
   Int_t           Mu0_ORIVX_NDOF;
   Float_t         Mu0_ORIVX_COV_[3][3];
   Double_t        Mu0_P;
   Double_t        Mu0_PT;
   Double_t        Mu0_PE;
   Double_t        Mu0_PX;
   Double_t        Mu0_PY;
   Double_t        Mu0_PZ;
   Double_t        Mu0_M;
   Int_t           Mu0_ID;
   Double_t        Mu0_PIDe;
   Double_t        Mu0_PIDmu;
   Double_t        Mu0_PIDK;
   Double_t        Mu0_PIDp;
   Double_t        Mu0_PIDd;
   Double_t        Mu0_ProbNNe;
   Double_t        Mu0_ProbNNk;
   Double_t        Mu0_ProbNNp;
   Double_t        Mu0_ProbNNpi;
   Double_t        Mu0_ProbNNmu;
   Double_t        Mu0_ProbNNd;
   Double_t        Mu0_ProbNNghost;
   Bool_t          Mu0_hasMuon;
   Bool_t          Mu0_isMuon;
   Bool_t          Mu0_hasRich;
   Bool_t          Mu0_UsedRichAerogel;
   Bool_t          Mu0_UsedRich1Gas;
   Bool_t          Mu0_UsedRich2Gas;
   Bool_t          Mu0_RichAboveElThres;
   Bool_t          Mu0_RichAboveMuThres;
   Bool_t          Mu0_RichAbovePiThres;
   Bool_t          Mu0_RichAboveKaThres;
   Bool_t          Mu0_RichAbovePrThres;
   Bool_t          Mu0_hasCalo;
   Double_t        Mu1_OWNPV_X;
   Double_t        Mu1_OWNPV_Y;
   Double_t        Mu1_OWNPV_Z;
   Double_t        Mu1_OWNPV_XERR;
   Double_t        Mu1_OWNPV_YERR;
   Double_t        Mu1_OWNPV_ZERR;
   Double_t        Mu1_OWNPV_CHI2;
   Int_t           Mu1_OWNPV_NDOF;
   Float_t         Mu1_OWNPV_COV_[3][3];
   Double_t        Mu1_IP_OWNPV;
   Double_t        Mu1_IPCHI2_OWNPV;
   Double_t        Mu1_ORIVX_X;
   Double_t        Mu1_ORIVX_Y;
   Double_t        Mu1_ORIVX_Z;
   Double_t        Mu1_ORIVX_XERR;
   Double_t        Mu1_ORIVX_YERR;
   Double_t        Mu1_ORIVX_ZERR;
   Double_t        Mu1_ORIVX_CHI2;
   Int_t           Mu1_ORIVX_NDOF;
   Float_t         Mu1_ORIVX_COV_[3][3];
   Double_t        Mu1_P;
   Double_t        Mu1_PT;
   Double_t        Mu1_PE;
   Double_t        Mu1_PX;
   Double_t        Mu1_PY;
   Double_t        Mu1_PZ;
   Double_t        Mu1_M;
   Int_t           Mu1_ID;
   Double_t        Mu1_PIDe;
   Double_t        Mu1_PIDmu;
   Double_t        Mu1_PIDK;
   Double_t        Mu1_PIDp;
   Double_t        Mu1_PIDd;
   Double_t        Mu1_ProbNNe;
   Double_t        Mu1_ProbNNk;
   Double_t        Mu1_ProbNNp;
   Double_t        Mu1_ProbNNpi;
   Double_t        Mu1_ProbNNmu;
   Double_t        Mu1_ProbNNd;
   Double_t        Mu1_ProbNNghost;
   Bool_t          Mu1_hasMuon;
   Bool_t          Mu1_isMuon;
   Bool_t          Mu1_hasRich;
   Bool_t          Mu1_UsedRichAerogel;
   Bool_t          Mu1_UsedRich1Gas;
   Bool_t          Mu1_UsedRich2Gas;
   Bool_t          Mu1_RichAboveElThres;
   Bool_t          Mu1_RichAboveMuThres;
   Bool_t          Mu1_RichAbovePiThres;
   Bool_t          Mu1_RichAboveKaThres;
   Bool_t          Mu1_RichAbovePrThres;
   Bool_t          Mu1_hasCalo;
   Double_t        Pi0_OWNPV_X;
   Double_t        Pi0_OWNPV_Y;
   Double_t        Pi0_OWNPV_Z;
   Double_t        Pi0_OWNPV_XERR;
   Double_t        Pi0_OWNPV_YERR;
   Double_t        Pi0_OWNPV_ZERR;
   Double_t        Pi0_OWNPV_CHI2;
   Int_t           Pi0_OWNPV_NDOF;
   Float_t         Pi0_OWNPV_COV_[3][3];
   Double_t        Pi0_IP_OWNPV;
   Double_t        Pi0_IPCHI2_OWNPV;
   Double_t        Pi0_ORIVX_X;
   Double_t        Pi0_ORIVX_Y;
   Double_t        Pi0_ORIVX_Z;
   Double_t        Pi0_ORIVX_XERR;
   Double_t        Pi0_ORIVX_YERR;
   Double_t        Pi0_ORIVX_ZERR;
   Double_t        Pi0_ORIVX_CHI2;
   Int_t           Pi0_ORIVX_NDOF;
   Float_t         Pi0_ORIVX_COV_[3][3];
   Double_t        Pi0_P;
   Double_t        Pi0_PT;
   Double_t        Pi0_PE;
   Double_t        Pi0_PX;
   Double_t        Pi0_PY;
   Double_t        Pi0_PZ;
   Double_t        Pi0_M;
   Int_t           Pi0_ID;
   Double_t        Pi0_PIDe;
   Double_t        Pi0_PIDmu;
   Double_t        Pi0_PIDK;
   Double_t        Pi0_PIDp;
   Double_t        Pi0_PIDd;
   Double_t        Pi0_ProbNNe;
   Double_t        Pi0_ProbNNk;
   Double_t        Pi0_ProbNNp;
   Double_t        Pi0_ProbNNpi;
   Double_t        Pi0_ProbNNmu;
   Double_t        Pi0_ProbNNd;
   Double_t        Pi0_ProbNNghost;
   Bool_t          Pi0_hasMuon;
   Bool_t          Pi0_isMuon;
   Bool_t          Pi0_hasRich;
   Bool_t          Pi0_UsedRichAerogel;
   Bool_t          Pi0_UsedRich1Gas;
   Bool_t          Pi0_UsedRich2Gas;
   Bool_t          Pi0_RichAboveElThres;
   Bool_t          Pi0_RichAboveMuThres;
   Bool_t          Pi0_RichAbovePiThres;
   Bool_t          Pi0_RichAboveKaThres;
   Bool_t          Pi0_RichAbovePrThres;
   Bool_t          Pi0_hasCalo;
   Double_t        Pi1_OWNPV_X;
   Double_t        Pi1_OWNPV_Y;
   Double_t        Pi1_OWNPV_Z;
   Double_t        Pi1_OWNPV_XERR;
   Double_t        Pi1_OWNPV_YERR;
   Double_t        Pi1_OWNPV_ZERR;
   Double_t        Pi1_OWNPV_CHI2;
   Int_t           Pi1_OWNPV_NDOF;
   Float_t         Pi1_OWNPV_COV_[3][3];
   Double_t        Pi1_IP_OWNPV;
   Double_t        Pi1_IPCHI2_OWNPV;
   Double_t        Pi1_ORIVX_X;
   Double_t        Pi1_ORIVX_Y;
   Double_t        Pi1_ORIVX_Z;
   Double_t        Pi1_ORIVX_XERR;
   Double_t        Pi1_ORIVX_YERR;
   Double_t        Pi1_ORIVX_ZERR;
   Double_t        Pi1_ORIVX_CHI2;
   Int_t           Pi1_ORIVX_NDOF;
   Float_t         Pi1_ORIVX_COV_[3][3];
   Double_t        Pi1_P;
   Double_t        Pi1_PT;
   Double_t        Pi1_PE;
   Double_t        Pi1_PX;
   Double_t        Pi1_PY;
   Double_t        Pi1_PZ;
   Double_t        Pi1_M;
   Int_t           Pi1_ID;
   Double_t        Pi1_PIDe;
   Double_t        Pi1_PIDmu;
   Double_t        Pi1_PIDK;
   Double_t        Pi1_PIDp;
   Double_t        Pi1_PIDd;
   Double_t        Pi1_ProbNNe;
   Double_t        Pi1_ProbNNk;
   Double_t        Pi1_ProbNNp;
   Double_t        Pi1_ProbNNpi;
   Double_t        Pi1_ProbNNmu;
   Double_t        Pi1_ProbNNd;
   Double_t        Pi1_ProbNNghost;
   Bool_t          Pi1_hasMuon;
   Bool_t          Pi1_isMuon;
   Bool_t          Pi1_hasRich;
   Bool_t          Pi1_UsedRichAerogel;
   Bool_t          Pi1_UsedRich1Gas;
   Bool_t          Pi1_UsedRich2Gas;
   Bool_t          Pi1_RichAboveElThres;
   Bool_t          Pi1_RichAboveMuThres;
   Bool_t          Pi1_RichAbovePiThres;
   Bool_t          Pi1_RichAboveKaThres;
   Bool_t          Pi1_RichAbovePrThres;
   Bool_t          Pi1_hasCalo;
   Double_t        K_OWNPV_X;
   Double_t        K_OWNPV_Y;
   Double_t        K_OWNPV_Z;
   Double_t        K_OWNPV_XERR;
   Double_t        K_OWNPV_YERR;
   Double_t        K_OWNPV_ZERR;
   Double_t        K_OWNPV_CHI2;
   Int_t           K_OWNPV_NDOF;
   Float_t         K_OWNPV_COV_[3][3];
   Double_t        K_IP_OWNPV;
   Double_t        K_IPCHI2_OWNPV;
   Double_t        K_ORIVX_X;
   Double_t        K_ORIVX_Y;
   Double_t        K_ORIVX_Z;
   Double_t        K_ORIVX_XERR;
   Double_t        K_ORIVX_YERR;
   Double_t        K_ORIVX_ZERR;
   Double_t        K_ORIVX_CHI2;
   Int_t           K_ORIVX_NDOF;
   Float_t         K_ORIVX_COV_[3][3];
   Double_t        K_P;
   Double_t        K_PT;
   Double_t        K_PE;
   Double_t        K_PX;
   Double_t        K_PY;
   Double_t        K_PZ;
   Double_t        K_M;
   Int_t           K_ID;
   Double_t        K_PIDe;
   Double_t        K_PIDmu;
   Double_t        K_PIDK;
   Double_t        K_PIDp;
   Double_t        K_PIDd;
   Double_t        K_ProbNNe;
   Double_t        K_ProbNNk;
   Double_t        K_ProbNNp;
   Double_t        K_ProbNNpi;
   Double_t        K_ProbNNmu;
   Double_t        K_ProbNNd;
   Double_t        K_ProbNNghost;
   Bool_t          K_hasMuon;
   Bool_t          K_isMuon;
   Bool_t          K_hasRich;
   Bool_t          K_UsedRichAerogel;
   Bool_t          K_UsedRich1Gas;
   Bool_t          K_UsedRich2Gas;
   Bool_t          K_RichAboveElThres;
   Bool_t          K_RichAboveMuThres;
   Bool_t          K_RichAbovePiThres;
   Bool_t          K_RichAboveKaThres;
   Bool_t          K_RichAbovePrThres;
   Bool_t          K_hasCalo;
   Double_t        Pi2_OWNPV_X;
   Double_t        Pi2_OWNPV_Y;
   Double_t        Pi2_OWNPV_Z;
   Double_t        Pi2_OWNPV_XERR;
   Double_t        Pi2_OWNPV_YERR;
   Double_t        Pi2_OWNPV_ZERR;
   Double_t        Pi2_OWNPV_CHI2;
   Int_t           Pi2_OWNPV_NDOF;
   Float_t         Pi2_OWNPV_COV_[3][3];
   Double_t        Pi2_IP_OWNPV;
   Double_t        Pi2_IPCHI2_OWNPV;
   Double_t        Pi2_ORIVX_X;
   Double_t        Pi2_ORIVX_Y;
   Double_t        Pi2_ORIVX_Z;
   Double_t        Pi2_ORIVX_XERR;
   Double_t        Pi2_ORIVX_YERR;
   Double_t        Pi2_ORIVX_ZERR;
   Double_t        Pi2_ORIVX_CHI2;
   Int_t           Pi2_ORIVX_NDOF;
   Float_t         Pi2_ORIVX_COV_[3][3];
   Double_t        Pi2_P;
   Double_t        Pi2_PT;
   Double_t        Pi2_PE;
   Double_t        Pi2_PX;
   Double_t        Pi2_PY;
   Double_t        Pi2_PZ;
   Double_t        Pi2_M;
   Int_t           Pi2_ID;
   Double_t        Pi2_PIDe;
   Double_t        Pi2_PIDmu;
   Double_t        Pi2_PIDK;
   Double_t        Pi2_PIDp;
   Double_t        Pi2_PIDd;
   Double_t        Pi2_ProbNNe;
   Double_t        Pi2_ProbNNk;
   Double_t        Pi2_ProbNNp;
   Double_t        Pi2_ProbNNpi;
   Double_t        Pi2_ProbNNmu;
   Double_t        Pi2_ProbNNd;
   Double_t        Pi2_ProbNNghost;
   Bool_t          Pi2_hasMuon;
   Bool_t          Pi2_isMuon;
   Bool_t          Pi2_hasRich;
   Bool_t          Pi2_UsedRichAerogel;
   Bool_t          Pi2_UsedRich1Gas;
   Bool_t          Pi2_UsedRich2Gas;
   Bool_t          Pi2_RichAboveElThres;
   Bool_t          Pi2_RichAboveMuThres;
   Bool_t          Pi2_RichAbovePiThres;
   Bool_t          Pi2_RichAboveKaThres;
   Bool_t          Pi2_RichAbovePrThres;
   Bool_t          Pi2_hasCalo;
   Double_t        Pi3_OWNPV_X;
   Double_t        Pi3_OWNPV_Y;
   Double_t        Pi3_OWNPV_Z;
   Double_t        Pi3_OWNPV_XERR;
   Double_t        Pi3_OWNPV_YERR;
   Double_t        Pi3_OWNPV_ZERR;
   Double_t        Pi3_OWNPV_CHI2;
   Int_t           Pi3_OWNPV_NDOF;
   Float_t         Pi3_OWNPV_COV_[3][3];
   Double_t        Pi3_IP_OWNPV;
   Double_t        Pi3_IPCHI2_OWNPV;
   Double_t        Pi3_ORIVX_X;
   Double_t        Pi3_ORIVX_Y;
   Double_t        Pi3_ORIVX_Z;
   Double_t        Pi3_ORIVX_XERR;
   Double_t        Pi3_ORIVX_YERR;
   Double_t        Pi3_ORIVX_ZERR;
   Double_t        Pi3_ORIVX_CHI2;
   Int_t           Pi3_ORIVX_NDOF;
   Float_t         Pi3_ORIVX_COV_[3][3];
   Double_t        Pi3_P;
   Double_t        Pi3_PT;
   Double_t        Pi3_PE;
   Double_t        Pi3_PX;
   Double_t        Pi3_PY;
   Double_t        Pi3_PZ;
   Double_t        Pi3_M;
   Int_t           Pi3_ID;
   Double_t        Pi3_PIDe;
   Double_t        Pi3_PIDmu;
   Double_t        Pi3_PIDK;
   Double_t        Pi3_PIDp;
   Double_t        Pi3_PIDd;
   Double_t        Pi3_ProbNNe;
   Double_t        Pi3_ProbNNk;
   Double_t        Pi3_ProbNNp;
   Double_t        Pi3_ProbNNpi;
   Double_t        Pi3_ProbNNmu;
   Double_t        Pi3_ProbNNd;
   Double_t        Pi3_ProbNNghost;
   Bool_t          Pi3_hasMuon;
   Bool_t          Pi3_isMuon;
   Bool_t          Pi3_hasRich;
   Bool_t          Pi3_UsedRichAerogel;
   Bool_t          Pi3_UsedRich1Gas;
   Bool_t          Pi3_UsedRich2Gas;
   Bool_t          Pi3_RichAboveElThres;
   Bool_t          Pi3_RichAboveMuThres;
   Bool_t          Pi3_RichAbovePiThres;
   Bool_t          Pi3_RichAboveKaThres;
   Bool_t          Pi3_RichAbovePrThres;
   Bool_t          Pi3_hasCalo;
   UInt_t          nCandidate;
   ULong64_t       totCandidates;
   ULong64_t       EventInSequence;
   UInt_t          runNumber;
   ULong64_t       eventNumber;
   UInt_t          BCID;
   Int_t           BCType;
   UInt_t          OdinTCK;
   UInt_t          L0DUTCK;
   UInt_t          HLT1TCK;
   UInt_t          HLT2TCK;
   ULong64_t       GpsTime;
   Short_t         Polarity;
   Int_t           nPV;
   Float_t         PVX[100];   //[nPV]
   Float_t         PVY[100];   //[nPV]
   Float_t         PVZ[100];   //[nPV]
   Float_t         PVXERR[100];   //[nPV]
   Float_t         PVYERR[100];   //[nPV]
   Float_t         PVZERR[100];   //[nPV]
   Float_t         PVCHI2[100];   //[nPV]
   Float_t         PVNDOF[100];   //[nPV]
   Float_t         PVNTRACKS[100];   //[nPV]
   Int_t           nPVs;
   Int_t           nTracks;
   Int_t           nLongTracks;
   Int_t           nDownstreamTracks;
   Int_t           nUpstreamTracks;
   Int_t           nVeloTracks;
   Int_t           nTTracks;
   Int_t           nBackTracks;
   Int_t           nRich1Hits;
   Int_t           nRich2Hits;
   Int_t           nVeloClusters;
   Int_t           nITClusters;
   Int_t           nTTClusters;
   Int_t           nOTClusters;
   Int_t           nSPDHits;
   Int_t           nMuonCoordsS0;
   Int_t           nMuonCoordsS1;
   Int_t           nMuonCoordsS2;
   Int_t           nMuonCoordsS3;
   Int_t           nMuonCoordsS4;
   Int_t           nMuonTracks;

   // List of branches
   TBranch        *b_Bp_B_Chi2NDoF;   //!
   TBranch        *b_Bp_B_K_px;   //!
   TBranch        *b_Bp_B_K_py;   //!
   TBranch        *b_Bp_B_K_pz;   //!
   TBranch        *b_Bp_B_X_M;   //!
   TBranch        *b_Bp_B_mu0_px;   //!
   TBranch        *b_Bp_B_mu0_py;   //!
   TBranch        *b_Bp_B_mu0_pz;   //!
   TBranch        *b_Bp_B_mu1_px;   //!
   TBranch        *b_Bp_B_mu1_py;   //!
   TBranch        *b_Bp_B_mu1_pz;   //!
   TBranch        *b_Bp_B_pi0_px;   //!
   TBranch        *b_Bp_B_pi0_py;   //!
   TBranch        *b_Bp_B_pi0_pz;   //!
   TBranch        *b_Bp_B_pi1_px;   //!
   TBranch        *b_Bp_B_pi1_py;   //!
   TBranch        *b_Bp_B_pi1_pz;   //!
   TBranch        *b_Bp_B_pi2_px;   //!
   TBranch        *b_Bp_B_pi2_py;   //!
   TBranch        *b_Bp_B_pi2_pz;   //!
   TBranch        *b_Bp_B_pi3_px;   //!
   TBranch        *b_Bp_B_pi3_py;   //!
   TBranch        *b_Bp_B_pi3_pz;   //!
   TBranch        *b_Bp_Jpsi_B_M;   //!
   TBranch        *b_Bp_Jpsi_B_ctau;   //!
   TBranch        *b_Bp_Jpsi_Chi2NDoF;   //!
   TBranch        *b_Bp_Jpsi_X_M;   //!
   TBranch        *b_Bp_ENDVERTEX_X;   //!
   TBranch        *b_Bp_ENDVERTEX_Y;   //!
   TBranch        *b_Bp_ENDVERTEX_Z;   //!
   TBranch        *b_Bp_ENDVERTEX_XERR;   //!
   TBranch        *b_Bp_ENDVERTEX_YERR;   //!
   TBranch        *b_Bp_ENDVERTEX_ZERR;   //!
   TBranch        *b_Bp_ENDVERTEX_CHI2;   //!
   TBranch        *b_Bp_ENDVERTEX_NDOF;   //!
   TBranch        *b_Bp_ENDVERTEX_COV_;   //!
   TBranch        *b_Bp_OWNPV_X;   //!
   TBranch        *b_Bp_OWNPV_Y;   //!
   TBranch        *b_Bp_OWNPV_Z;   //!
   TBranch        *b_Bp_OWNPV_XERR;   //!
   TBranch        *b_Bp_OWNPV_YERR;   //!
   TBranch        *b_Bp_OWNPV_ZERR;   //!
   TBranch        *b_Bp_OWNPV_CHI2;   //!
   TBranch        *b_Bp_OWNPV_NDOF;   //!
   TBranch        *b_Bp_OWNPV_COV_;   //!
   TBranch        *b_Bp_IP_OWNPV;   //!
   TBranch        *b_Bp_IPCHI2_OWNPV;   //!
   TBranch        *b_Bp_FD_OWNPV;   //!
   TBranch        *b_Bp_FDCHI2_OWNPV;   //!
   TBranch        *b_Bp_DIRA_OWNPV;   //!
   TBranch        *b_Bp_P;   //!
   TBranch        *b_Bp_PT;   //!
   TBranch        *b_Bp_PE;   //!
   TBranch        *b_Bp_PX;   //!
   TBranch        *b_Bp_PY;   //!
   TBranch        *b_Bp_PZ;   //!
   TBranch        *b_Bp_MM;   //!
   TBranch        *b_Bp_MMERR;   //!
   TBranch        *b_Bp_M;   //!
   TBranch        *b_Bp_TAU;   //!
   TBranch        *b_Bp_TAUERR;   //!
   TBranch        *b_Bp_TAUCHI2;   //!
   TBranch        *b_Bp_L0Global_Dec;   //!
   TBranch        *b_Bp_L0Global_TIS;   //!
   TBranch        *b_Bp_L0Global_TOS;   //!
   TBranch        *b_Bp_Hlt1Global_Dec;   //!
   TBranch        *b_Bp_Hlt1Global_TIS;   //!
   TBranch        *b_Bp_Hlt1Global_TOS;   //!
   TBranch        *b_Bp_Hlt1Phys_Dec;   //!
   TBranch        *b_Bp_Hlt1Phys_TIS;   //!
   TBranch        *b_Bp_Hlt1Phys_TOS;   //!
   TBranch        *b_Bp_Hlt2Global_Dec;   //!
   TBranch        *b_Bp_Hlt2Global_TIS;   //!
   TBranch        *b_Bp_Hlt2Global_TOS;   //!
   TBranch        *b_Bp_Hlt2Phys_Dec;   //!
   TBranch        *b_Bp_Hlt2Phys_TIS;   //!
   TBranch        *b_Bp_Hlt2Phys_TOS;   //!
   TBranch        *b_Bp_L0DiMuonDecision_Dec;   //!
   TBranch        *b_Bp_L0DiMuonDecision_TIS;   //!
   TBranch        *b_Bp_L0DiMuonDecision_TOS;   //!
   TBranch        *b_Bp_L0MuonDecision_Dec;   //!
   TBranch        *b_Bp_L0MuonDecision_TIS;   //!
   TBranch        *b_Bp_L0MuonDecision_TOS;   //!
   TBranch        *b_Bp_Hlt1DiMuonHighMassDecision_Dec;   //!
   TBranch        *b_Bp_Hlt1DiMuonHighMassDecision_TIS;   //!
   TBranch        *b_Bp_Hlt1DiMuonHighMassDecision_TOS;   //!
   TBranch        *b_Bp_Hlt1TrackMuonDecision_Dec;   //!
   TBranch        *b_Bp_Hlt1TrackMuonDecision_TIS;   //!
   TBranch        *b_Bp_Hlt1TrackMuonDecision_TOS;   //!
   TBranch        *b_Bp_Hlt1TrackMVADecision_Dec;   //!
   TBranch        *b_Bp_Hlt1TrackMVADecision_TIS;   //!
   TBranch        *b_Bp_Hlt1TrackMVADecision_TOS;   //!
   TBranch        *b_Bp_Hlt2DiMuonDetachedJPsiDecision_Dec;   //!
   TBranch        *b_Bp_Hlt2DiMuonDetachedJPsiDecision_TIS;   //!
   TBranch        *b_Bp_Hlt2DiMuonDetachedJPsiDecision_TOS;   //!
   TBranch        *b_X_P;   //!
   TBranch        *b_X_PT;   //!
   TBranch        *b_X_PE;   //!
   TBranch        *b_X_PX;   //!
   TBranch        *b_X_PY;   //!
   TBranch        *b_X_PZ;   //!
   TBranch        *b_X_MM;   //!
   TBranch        *b_X_MMERR;   //!
   TBranch        *b_X_M;   //!
   TBranch        *b_Jpsi_P;   //!
   TBranch        *b_Jpsi_PT;   //!
   TBranch        *b_Jpsi_PE;   //!
   TBranch        *b_Jpsi_PX;   //!
   TBranch        *b_Jpsi_PY;   //!
   TBranch        *b_Jpsi_PZ;   //!
   TBranch        *b_Jpsi_MM;   //!
   TBranch        *b_Jpsi_MMERR;   //!
   TBranch        *b_Jpsi_M;   //!
   TBranch        *b_Mu0_OWNPV_X;   //!
   TBranch        *b_Mu0_OWNPV_Y;   //!
   TBranch        *b_Mu0_OWNPV_Z;   //!
   TBranch        *b_Mu0_OWNPV_XERR;   //!
   TBranch        *b_Mu0_OWNPV_YERR;   //!
   TBranch        *b_Mu0_OWNPV_ZERR;   //!
   TBranch        *b_Mu0_OWNPV_CHI2;   //!
   TBranch        *b_Mu0_OWNPV_NDOF;   //!
   TBranch        *b_Mu0_OWNPV_COV_;   //!
   TBranch        *b_Mu0_IP_OWNPV;   //!
   TBranch        *b_Mu0_IPCHI2_OWNPV;   //!
   TBranch        *b_Mu0_ORIVX_X;   //!
   TBranch        *b_Mu0_ORIVX_Y;   //!
   TBranch        *b_Mu0_ORIVX_Z;   //!
   TBranch        *b_Mu0_ORIVX_XERR;   //!
   TBranch        *b_Mu0_ORIVX_YERR;   //!
   TBranch        *b_Mu0_ORIVX_ZERR;   //!
   TBranch        *b_Mu0_ORIVX_CHI2;   //!
   TBranch        *b_Mu0_ORIVX_NDOF;   //!
   TBranch        *b_Mu0_ORIVX_COV_;   //!
   TBranch        *b_Mu0_P;   //!
   TBranch        *b_Mu0_PT;   //!
   TBranch        *b_Mu0_PE;   //!
   TBranch        *b_Mu0_PX;   //!
   TBranch        *b_Mu0_PY;   //!
   TBranch        *b_Mu0_PZ;   //!
   TBranch        *b_Mu0_M;   //!
   TBranch        *b_Mu0_ID;   //!
   TBranch        *b_Mu0_PIDe;   //!
   TBranch        *b_Mu0_PIDmu;   //!
   TBranch        *b_Mu0_PIDK;   //!
   TBranch        *b_Mu0_PIDp;   //!
   TBranch        *b_Mu0_PIDd;   //!
   TBranch        *b_Mu0_ProbNNe;   //!
   TBranch        *b_Mu0_ProbNNk;   //!
   TBranch        *b_Mu0_ProbNNp;   //!
   TBranch        *b_Mu0_ProbNNpi;   //!
   TBranch        *b_Mu0_ProbNNmu;   //!
   TBranch        *b_Mu0_ProbNNd;   //!
   TBranch        *b_Mu0_ProbNNghost;   //!
   TBranch        *b_Mu0_hasMuon;   //!
   TBranch        *b_Mu0_isMuon;   //!
   TBranch        *b_Mu0_hasRich;   //!
   TBranch        *b_Mu0_UsedRichAerogel;   //!
   TBranch        *b_Mu0_UsedRich1Gas;   //!
   TBranch        *b_Mu0_UsedRich2Gas;   //!
   TBranch        *b_Mu0_RichAboveElThres;   //!
   TBranch        *b_Mu0_RichAboveMuThres;   //!
   TBranch        *b_Mu0_RichAbovePiThres;   //!
   TBranch        *b_Mu0_RichAboveKaThres;   //!
   TBranch        *b_Mu0_RichAbovePrThres;   //!
   TBranch        *b_Mu0_hasCalo;   //!
   TBranch        *b_Mu1_OWNPV_X;   //!
   TBranch        *b_Mu1_OWNPV_Y;   //!
   TBranch        *b_Mu1_OWNPV_Z;   //!
   TBranch        *b_Mu1_OWNPV_XERR;   //!
   TBranch        *b_Mu1_OWNPV_YERR;   //!
   TBranch        *b_Mu1_OWNPV_ZERR;   //!
   TBranch        *b_Mu1_OWNPV_CHI2;   //!
   TBranch        *b_Mu1_OWNPV_NDOF;   //!
   TBranch        *b_Mu1_OWNPV_COV_;   //!
   TBranch        *b_Mu1_IP_OWNPV;   //!
   TBranch        *b_Mu1_IPCHI2_OWNPV;   //!
   TBranch        *b_Mu1_ORIVX_X;   //!
   TBranch        *b_Mu1_ORIVX_Y;   //!
   TBranch        *b_Mu1_ORIVX_Z;   //!
   TBranch        *b_Mu1_ORIVX_XERR;   //!
   TBranch        *b_Mu1_ORIVX_YERR;   //!
   TBranch        *b_Mu1_ORIVX_ZERR;   //!
   TBranch        *b_Mu1_ORIVX_CHI2;   //!
   TBranch        *b_Mu1_ORIVX_NDOF;   //!
   TBranch        *b_Mu1_ORIVX_COV_;   //!
   TBranch        *b_Mu1_P;   //!
   TBranch        *b_Mu1_PT;   //!
   TBranch        *b_Mu1_PE;   //!
   TBranch        *b_Mu1_PX;   //!
   TBranch        *b_Mu1_PY;   //!
   TBranch        *b_Mu1_PZ;   //!
   TBranch        *b_Mu1_M;   //!
   TBranch        *b_Mu1_ID;   //!
   TBranch        *b_Mu1_PIDe;   //!
   TBranch        *b_Mu1_PIDmu;   //!
   TBranch        *b_Mu1_PIDK;   //!
   TBranch        *b_Mu1_PIDp;   //!
   TBranch        *b_Mu1_PIDd;   //!
   TBranch        *b_Mu1_ProbNNe;   //!
   TBranch        *b_Mu1_ProbNNk;   //!
   TBranch        *b_Mu1_ProbNNp;   //!
   TBranch        *b_Mu1_ProbNNpi;   //!
   TBranch        *b_Mu1_ProbNNmu;   //!
   TBranch        *b_Mu1_ProbNNd;   //!
   TBranch        *b_Mu1_ProbNNghost;   //!
   TBranch        *b_Mu1_hasMuon;   //!
   TBranch        *b_Mu1_isMuon;   //!
   TBranch        *b_Mu1_hasRich;   //!
   TBranch        *b_Mu1_UsedRichAerogel;   //!
   TBranch        *b_Mu1_UsedRich1Gas;   //!
   TBranch        *b_Mu1_UsedRich2Gas;   //!
   TBranch        *b_Mu1_RichAboveElThres;   //!
   TBranch        *b_Mu1_RichAboveMuThres;   //!
   TBranch        *b_Mu1_RichAbovePiThres;   //!
   TBranch        *b_Mu1_RichAboveKaThres;   //!
   TBranch        *b_Mu1_RichAbovePrThres;   //!
   TBranch        *b_Mu1_hasCalo;   //!
   TBranch        *b_Pi0_OWNPV_X;   //!
   TBranch        *b_Pi0_OWNPV_Y;   //!
   TBranch        *b_Pi0_OWNPV_Z;   //!
   TBranch        *b_Pi0_OWNPV_XERR;   //!
   TBranch        *b_Pi0_OWNPV_YERR;   //!
   TBranch        *b_Pi0_OWNPV_ZERR;   //!
   TBranch        *b_Pi0_OWNPV_CHI2;   //!
   TBranch        *b_Pi0_OWNPV_NDOF;   //!
   TBranch        *b_Pi0_OWNPV_COV_;   //!
   TBranch        *b_Pi0_IP_OWNPV;   //!
   TBranch        *b_Pi0_IPCHI2_OWNPV;   //!
   TBranch        *b_Pi0_ORIVX_X;   //!
   TBranch        *b_Pi0_ORIVX_Y;   //!
   TBranch        *b_Pi0_ORIVX_Z;   //!
   TBranch        *b_Pi0_ORIVX_XERR;   //!
   TBranch        *b_Pi0_ORIVX_YERR;   //!
   TBranch        *b_Pi0_ORIVX_ZERR;   //!
   TBranch        *b_Pi0_ORIVX_CHI2;   //!
   TBranch        *b_Pi0_ORIVX_NDOF;   //!
   TBranch        *b_Pi0_ORIVX_COV_;   //!
   TBranch        *b_Pi0_P;   //!
   TBranch        *b_Pi0_PT;   //!
   TBranch        *b_Pi0_PE;   //!
   TBranch        *b_Pi0_PX;   //!
   TBranch        *b_Pi0_PY;   //!
   TBranch        *b_Pi0_PZ;   //!
   TBranch        *b_Pi0_M;   //!
   TBranch        *b_Pi0_ID;   //!
   TBranch        *b_Pi0_PIDe;   //!
   TBranch        *b_Pi0_PIDmu;   //!
   TBranch        *b_Pi0_PIDK;   //!
   TBranch        *b_Pi0_PIDp;   //!
   TBranch        *b_Pi0_PIDd;   //!
   TBranch        *b_Pi0_ProbNNe;   //!
   TBranch        *b_Pi0_ProbNNk;   //!
   TBranch        *b_Pi0_ProbNNp;   //!
   TBranch        *b_Pi0_ProbNNpi;   //!
   TBranch        *b_Pi0_ProbNNmu;   //!
   TBranch        *b_Pi0_ProbNNd;   //!
   TBranch        *b_Pi0_ProbNNghost;   //!
   TBranch        *b_Pi0_hasMuon;   //!
   TBranch        *b_Pi0_isMuon;   //!
   TBranch        *b_Pi0_hasRich;   //!
   TBranch        *b_Pi0_UsedRichAerogel;   //!
   TBranch        *b_Pi0_UsedRich1Gas;   //!
   TBranch        *b_Pi0_UsedRich2Gas;   //!
   TBranch        *b_Pi0_RichAboveElThres;   //!
   TBranch        *b_Pi0_RichAboveMuThres;   //!
   TBranch        *b_Pi0_RichAbovePiThres;   //!
   TBranch        *b_Pi0_RichAboveKaThres;   //!
   TBranch        *b_Pi0_RichAbovePrThres;   //!
   TBranch        *b_Pi0_hasCalo;   //!
   TBranch        *b_Pi1_OWNPV_X;   //!
   TBranch        *b_Pi1_OWNPV_Y;   //!
   TBranch        *b_Pi1_OWNPV_Z;   //!
   TBranch        *b_Pi1_OWNPV_XERR;   //!
   TBranch        *b_Pi1_OWNPV_YERR;   //!
   TBranch        *b_Pi1_OWNPV_ZERR;   //!
   TBranch        *b_Pi1_OWNPV_CHI2;   //!
   TBranch        *b_Pi1_OWNPV_NDOF;   //!
   TBranch        *b_Pi1_OWNPV_COV_;   //!
   TBranch        *b_Pi1_IP_OWNPV;   //!
   TBranch        *b_Pi1_IPCHI2_OWNPV;   //!
   TBranch        *b_Pi1_ORIVX_X;   //!
   TBranch        *b_Pi1_ORIVX_Y;   //!
   TBranch        *b_Pi1_ORIVX_Z;   //!
   TBranch        *b_Pi1_ORIVX_XERR;   //!
   TBranch        *b_Pi1_ORIVX_YERR;   //!
   TBranch        *b_Pi1_ORIVX_ZERR;   //!
   TBranch        *b_Pi1_ORIVX_CHI2;   //!
   TBranch        *b_Pi1_ORIVX_NDOF;   //!
   TBranch        *b_Pi1_ORIVX_COV_;   //!
   TBranch        *b_Pi1_P;   //!
   TBranch        *b_Pi1_PT;   //!
   TBranch        *b_Pi1_PE;   //!
   TBranch        *b_Pi1_PX;   //!
   TBranch        *b_Pi1_PY;   //!
   TBranch        *b_Pi1_PZ;   //!
   TBranch        *b_Pi1_M;   //!
   TBranch        *b_Pi1_ID;   //!
   TBranch        *b_Pi1_PIDe;   //!
   TBranch        *b_Pi1_PIDmu;   //!
   TBranch        *b_Pi1_PIDK;   //!
   TBranch        *b_Pi1_PIDp;   //!
   TBranch        *b_Pi1_PIDd;   //!
   TBranch        *b_Pi1_ProbNNe;   //!
   TBranch        *b_Pi1_ProbNNk;   //!
   TBranch        *b_Pi1_ProbNNp;   //!
   TBranch        *b_Pi1_ProbNNpi;   //!
   TBranch        *b_Pi1_ProbNNmu;   //!
   TBranch        *b_Pi1_ProbNNd;   //!
   TBranch        *b_Pi1_ProbNNghost;   //!
   TBranch        *b_Pi1_hasMuon;   //!
   TBranch        *b_Pi1_isMuon;   //!
   TBranch        *b_Pi1_hasRich;   //!
   TBranch        *b_Pi1_UsedRichAerogel;   //!
   TBranch        *b_Pi1_UsedRich1Gas;   //!
   TBranch        *b_Pi1_UsedRich2Gas;   //!
   TBranch        *b_Pi1_RichAboveElThres;   //!
   TBranch        *b_Pi1_RichAboveMuThres;   //!
   TBranch        *b_Pi1_RichAbovePiThres;   //!
   TBranch        *b_Pi1_RichAboveKaThres;   //!
   TBranch        *b_Pi1_RichAbovePrThres;   //!
   TBranch        *b_Pi1_hasCalo;   //!
   TBranch        *b_K_OWNPV_X;   //!
   TBranch        *b_K_OWNPV_Y;   //!
   TBranch        *b_K_OWNPV_Z;   //!
   TBranch        *b_K_OWNPV_XERR;   //!
   TBranch        *b_K_OWNPV_YERR;   //!
   TBranch        *b_K_OWNPV_ZERR;   //!
   TBranch        *b_K_OWNPV_CHI2;   //!
   TBranch        *b_K_OWNPV_NDOF;   //!
   TBranch        *b_K_OWNPV_COV_;   //!
   TBranch        *b_K_IP_OWNPV;   //!
   TBranch        *b_K_IPCHI2_OWNPV;   //!
   TBranch        *b_K_ORIVX_X;   //!
   TBranch        *b_K_ORIVX_Y;   //!
   TBranch        *b_K_ORIVX_Z;   //!
   TBranch        *b_K_ORIVX_XERR;   //!
   TBranch        *b_K_ORIVX_YERR;   //!
   TBranch        *b_K_ORIVX_ZERR;   //!
   TBranch        *b_K_ORIVX_CHI2;   //!
   TBranch        *b_K_ORIVX_NDOF;   //!
   TBranch        *b_K_ORIVX_COV_;   //!
   TBranch        *b_K_P;   //!
   TBranch        *b_K_PT;   //!
   TBranch        *b_K_PE;   //!
   TBranch        *b_K_PX;   //!
   TBranch        *b_K_PY;   //!
   TBranch        *b_K_PZ;   //!
   TBranch        *b_K_M;   //!
   TBranch        *b_K_ID;   //!
   TBranch        *b_K_PIDe;   //!
   TBranch        *b_K_PIDmu;   //!
   TBranch        *b_K_PIDK;   //!
   TBranch        *b_K_PIDp;   //!
   TBranch        *b_K_PIDd;   //!
   TBranch        *b_K_ProbNNe;   //!
   TBranch        *b_K_ProbNNk;   //!
   TBranch        *b_K_ProbNNp;   //!
   TBranch        *b_K_ProbNNpi;   //!
   TBranch        *b_K_ProbNNmu;   //!
   TBranch        *b_K_ProbNNd;   //!
   TBranch        *b_K_ProbNNghost;   //!
   TBranch        *b_K_hasMuon;   //!
   TBranch        *b_K_isMuon;   //!
   TBranch        *b_K_hasRich;   //!
   TBranch        *b_K_UsedRichAerogel;   //!
   TBranch        *b_K_UsedRich1Gas;   //!
   TBranch        *b_K_UsedRich2Gas;   //!
   TBranch        *b_K_RichAboveElThres;   //!
   TBranch        *b_K_RichAboveMuThres;   //!
   TBranch        *b_K_RichAbovePiThres;   //!
   TBranch        *b_K_RichAboveKaThres;   //!
   TBranch        *b_K_RichAbovePrThres;   //!
   TBranch        *b_K_hasCalo;   //!
   TBranch        *b_Pi2_OWNPV_X;   //!
   TBranch        *b_Pi2_OWNPV_Y;   //!
   TBranch        *b_Pi2_OWNPV_Z;   //!
   TBranch        *b_Pi2_OWNPV_XERR;   //!
   TBranch        *b_Pi2_OWNPV_YERR;   //!
   TBranch        *b_Pi2_OWNPV_ZERR;   //!
   TBranch        *b_Pi2_OWNPV_CHI2;   //!
   TBranch        *b_Pi2_OWNPV_NDOF;   //!
   TBranch        *b_Pi2_OWNPV_COV_;   //!
   TBranch        *b_Pi2_IP_OWNPV;   //!
   TBranch        *b_Pi2_IPCHI2_OWNPV;   //!
   TBranch        *b_Pi2_ORIVX_X;   //!
   TBranch        *b_Pi2_ORIVX_Y;   //!
   TBranch        *b_Pi2_ORIVX_Z;   //!
   TBranch        *b_Pi2_ORIVX_XERR;   //!
   TBranch        *b_Pi2_ORIVX_YERR;   //!
   TBranch        *b_Pi2_ORIVX_ZERR;   //!
   TBranch        *b_Pi2_ORIVX_CHI2;   //!
   TBranch        *b_Pi2_ORIVX_NDOF;   //!
   TBranch        *b_Pi2_ORIVX_COV_;   //!
   TBranch        *b_Pi2_P;   //!
   TBranch        *b_Pi2_PT;   //!
   TBranch        *b_Pi2_PE;   //!
   TBranch        *b_Pi2_PX;   //!
   TBranch        *b_Pi2_PY;   //!
   TBranch        *b_Pi2_PZ;   //!
   TBranch        *b_Pi2_M;   //!
   TBranch        *b_Pi2_ID;   //!
   TBranch        *b_Pi2_PIDe;   //!
   TBranch        *b_Pi2_PIDmu;   //!
   TBranch        *b_Pi2_PIDK;   //!
   TBranch        *b_Pi2_PIDp;   //!
   TBranch        *b_Pi2_PIDd;   //!
   TBranch        *b_Pi2_ProbNNe;   //!
   TBranch        *b_Pi2_ProbNNk;   //!
   TBranch        *b_Pi2_ProbNNp;   //!
   TBranch        *b_Pi2_ProbNNpi;   //!
   TBranch        *b_Pi2_ProbNNmu;   //!
   TBranch        *b_Pi2_ProbNNd;   //!
   TBranch        *b_Pi2_ProbNNghost;   //!
   TBranch        *b_Pi2_hasMuon;   //!
   TBranch        *b_Pi2_isMuon;   //!
   TBranch        *b_Pi2_hasRich;   //!
   TBranch        *b_Pi2_UsedRichAerogel;   //!
   TBranch        *b_Pi2_UsedRich1Gas;   //!
   TBranch        *b_Pi2_UsedRich2Gas;   //!
   TBranch        *b_Pi2_RichAboveElThres;   //!
   TBranch        *b_Pi2_RichAboveMuThres;   //!
   TBranch        *b_Pi2_RichAbovePiThres;   //!
   TBranch        *b_Pi2_RichAboveKaThres;   //!
   TBranch        *b_Pi2_RichAbovePrThres;   //!
   TBranch        *b_Pi2_hasCalo;   //!
   TBranch        *b_Pi3_OWNPV_X;   //!
   TBranch        *b_Pi3_OWNPV_Y;   //!
   TBranch        *b_Pi3_OWNPV_Z;   //!
   TBranch        *b_Pi3_OWNPV_XERR;   //!
   TBranch        *b_Pi3_OWNPV_YERR;   //!
   TBranch        *b_Pi3_OWNPV_ZERR;   //!
   TBranch        *b_Pi3_OWNPV_CHI2;   //!
   TBranch        *b_Pi3_OWNPV_NDOF;   //!
   TBranch        *b_Pi3_OWNPV_COV_;   //!
   TBranch        *b_Pi3_IP_OWNPV;   //!
   TBranch        *b_Pi3_IPCHI2_OWNPV;   //!
   TBranch        *b_Pi3_ORIVX_X;   //!
   TBranch        *b_Pi3_ORIVX_Y;   //!
   TBranch        *b_Pi3_ORIVX_Z;   //!
   TBranch        *b_Pi3_ORIVX_XERR;   //!
   TBranch        *b_Pi3_ORIVX_YERR;   //!
   TBranch        *b_Pi3_ORIVX_ZERR;   //!
   TBranch        *b_Pi3_ORIVX_CHI2;   //!
   TBranch        *b_Pi3_ORIVX_NDOF;   //!
   TBranch        *b_Pi3_ORIVX_COV_;   //!
   TBranch        *b_Pi3_P;   //!
   TBranch        *b_Pi3_PT;   //!
   TBranch        *b_Pi3_PE;   //!
   TBranch        *b_Pi3_PX;   //!
   TBranch        *b_Pi3_PY;   //!
   TBranch        *b_Pi3_PZ;   //!
   TBranch        *b_Pi3_M;   //!
   TBranch        *b_Pi3_ID;   //!
   TBranch        *b_Pi3_PIDe;   //!
   TBranch        *b_Pi3_PIDmu;   //!
   TBranch        *b_Pi3_PIDK;   //!
   TBranch        *b_Pi3_PIDp;   //!
   TBranch        *b_Pi3_PIDd;   //!
   TBranch        *b_Pi3_ProbNNe;   //!
   TBranch        *b_Pi3_ProbNNk;   //!
   TBranch        *b_Pi3_ProbNNp;   //!
   TBranch        *b_Pi3_ProbNNpi;   //!
   TBranch        *b_Pi3_ProbNNmu;   //!
   TBranch        *b_Pi3_ProbNNd;   //!
   TBranch        *b_Pi3_ProbNNghost;   //!
   TBranch        *b_Pi3_hasMuon;   //!
   TBranch        *b_Pi3_isMuon;   //!
   TBranch        *b_Pi3_hasRich;   //!
   TBranch        *b_Pi3_UsedRichAerogel;   //!
   TBranch        *b_Pi3_UsedRich1Gas;   //!
   TBranch        *b_Pi3_UsedRich2Gas;   //!
   TBranch        *b_Pi3_RichAboveElThres;   //!
   TBranch        *b_Pi3_RichAboveMuThres;   //!
   TBranch        *b_Pi3_RichAbovePiThres;   //!
   TBranch        *b_Pi3_RichAboveKaThres;   //!
   TBranch        *b_Pi3_RichAbovePrThres;   //!
   TBranch        *b_Pi3_hasCalo;   //!
   TBranch        *b_nCandidate;   //!
   TBranch        *b_totCandidates;   //!
   TBranch        *b_EventInSequence;   //!
   TBranch        *b_runNumber;   //!
   TBranch        *b_eventNumber;   //!
   TBranch        *b_BCID;   //!
   TBranch        *b_BCType;   //!
   TBranch        *b_OdinTCK;   //!
   TBranch        *b_L0DUTCK;   //!
   TBranch        *b_HLT1TCK;   //!
   TBranch        *b_HLT2TCK;   //!
   TBranch        *b_GpsTime;   //!
   TBranch        *b_Polarity;   //!
   TBranch        *b_nPV;   //!
   TBranch        *b_PVX;   //!
   TBranch        *b_PVY;   //!
   TBranch        *b_PVZ;   //!
   TBranch        *b_PVXERR;   //!
   TBranch        *b_PVYERR;   //!
   TBranch        *b_PVZERR;   //!
   TBranch        *b_PVCHI2;   //!
   TBranch        *b_PVNDOF;   //!
   TBranch        *b_PVNTRACKS;   //!
   TBranch        *b_nPVs;   //!
   TBranch        *b_nTracks;   //!
   TBranch        *b_nLongTracks;   //!
   TBranch        *b_nDownstreamTracks;   //!
   TBranch        *b_nUpstreamTracks;   //!
   TBranch        *b_nVeloTracks;   //!
   TBranch        *b_nTTracks;   //!
   TBranch        *b_nBackTracks;   //!
   TBranch        *b_nRich1Hits;   //!
   TBranch        *b_nRich2Hits;   //!
   TBranch        *b_nVeloClusters;   //!
   TBranch        *b_nITClusters;   //!
   TBranch        *b_nTTClusters;   //!
   TBranch        *b_nOTClusters;   //!
   TBranch        *b_nSPDHits;   //!
   TBranch        *b_nMuonCoordsS0;   //!
   TBranch        *b_nMuonCoordsS1;   //!
   TBranch        *b_nMuonCoordsS2;   //!
   TBranch        *b_nMuonCoordsS3;   //!
   TBranch        *b_nMuonCoordsS4;   //!
   TBranch        *b_nMuonTracks;   //!

   MEntries(TTree *tree=0);
   virtual ~MEntries();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef MEntries_cxx
MEntries::MEntries(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {

     //#ifdef SINGLE_TREE
      // The following code should be used if you want this class to access
      // a single tree instead of a chain
      //TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("Memory Directory");
      //if (!f || !f->IsOpen()) {
     //    f = new TFile("Memory Directory");
     // }
     // f->GetObject("/Bp2XK4Pi/nTuple",tree);

     //#else // SINGLE_TREE

      // The following code should be used if you want this class to access a chain
      // of trees.
      TChain * chain = new TChain("/Bp2XK4Pi/nTuple","");
      chain->Add("self_4pi_MC_18U_cc.root//Bp2XK4Pi/nTuple");
      chain->Add("self_4pi_MC_18D_cc.root//Bp2XK4Pi/nTuple");
      chain->Add("self_4pi_MC_17D_cc.root//Bp2XK4Pi/nTuple");
      chain->Add("self_4pi_MC_17U_cc.root//Bp2XK4Pi/nTuple");
      chain->Add("self_4pi_MC_16U_cc.root//Bp2XK4Pi/nTuple");
      chain->Add("self_4pi_MC_16D_cc.root//Bp2XK4Pi/nTuple");
      chain->Add("self_4pi_MC_15U_cc.root//Bp2XK4Pi/nTuple");
      chain->Add("self_4pi_MC_15U_cc.root//Bp2XK4Pi/nTuple");
      chain->Add("self_4pi_MC_12U_cc.root//Bp2XK4Pi/nTuple");
      chain->Add("self_4pi_MC_12D_cc.root//Bp2XK4Pi/nTuple");
      chain->Add("self_4pi_MC_11U_cc.root//Bp2XK4Pi/nTuple");
      chain->Add("self_4pi_MC_11D_cc.root//Bp2XK4Pi/nTuple");
      tree = chain;
      //#endif // SINGLE_TREE

   }
   Init(tree);
}

MEntries::~MEntries()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t MEntries::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t MEntries::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void MEntries::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("Bp_B_Chi2NDoF", &Bp_B_Chi2NDoF, &b_Bp_B_Chi2NDoF);
   fChain->SetBranchAddress("Bp_B_K_px", &Bp_B_K_px, &b_Bp_B_K_px);
   fChain->SetBranchAddress("Bp_B_K_py", &Bp_B_K_py, &b_Bp_B_K_py);
   fChain->SetBranchAddress("Bp_B_K_pz", &Bp_B_K_pz, &b_Bp_B_K_pz);
   fChain->SetBranchAddress("Bp_B_X_M", &Bp_B_X_M, &b_Bp_B_X_M);
   fChain->SetBranchAddress("Bp_B_mu0_px", &Bp_B_mu0_px, &b_Bp_B_mu0_px);
   fChain->SetBranchAddress("Bp_B_mu0_py", &Bp_B_mu0_py, &b_Bp_B_mu0_py);
   fChain->SetBranchAddress("Bp_B_mu0_pz", &Bp_B_mu0_pz, &b_Bp_B_mu0_pz);
   fChain->SetBranchAddress("Bp_B_mu1_px", &Bp_B_mu1_px, &b_Bp_B_mu1_px);
   fChain->SetBranchAddress("Bp_B_mu1_py", &Bp_B_mu1_py, &b_Bp_B_mu1_py);
   fChain->SetBranchAddress("Bp_B_mu1_pz", &Bp_B_mu1_pz, &b_Bp_B_mu1_pz);
   fChain->SetBranchAddress("Bp_B_pi0_px", &Bp_B_pi0_px, &b_Bp_B_pi0_px);
   fChain->SetBranchAddress("Bp_B_pi0_py", &Bp_B_pi0_py, &b_Bp_B_pi0_py);
   fChain->SetBranchAddress("Bp_B_pi0_pz", &Bp_B_pi0_pz, &b_Bp_B_pi0_pz);
   fChain->SetBranchAddress("Bp_B_pi1_px", &Bp_B_pi1_px, &b_Bp_B_pi1_px);
   fChain->SetBranchAddress("Bp_B_pi1_py", &Bp_B_pi1_py, &b_Bp_B_pi1_py);
   fChain->SetBranchAddress("Bp_B_pi1_pz", &Bp_B_pi1_pz, &b_Bp_B_pi1_pz);
   fChain->SetBranchAddress("Bp_B_pi2_px", &Bp_B_pi2_px, &b_Bp_B_pi2_px);
   fChain->SetBranchAddress("Bp_B_pi2_py", &Bp_B_pi2_py, &b_Bp_B_pi2_py);
   fChain->SetBranchAddress("Bp_B_pi2_pz", &Bp_B_pi2_pz, &b_Bp_B_pi2_pz);
   fChain->SetBranchAddress("Bp_B_pi3_px", &Bp_B_pi3_px, &b_Bp_B_pi3_px);
   fChain->SetBranchAddress("Bp_B_pi3_py", &Bp_B_pi3_py, &b_Bp_B_pi3_py);
   fChain->SetBranchAddress("Bp_B_pi3_pz", &Bp_B_pi3_pz, &b_Bp_B_pi3_pz);
   fChain->SetBranchAddress("Bp_Jpsi_B_M", &Bp_Jpsi_B_M, &b_Bp_Jpsi_B_M);
   fChain->SetBranchAddress("Bp_Jpsi_B_ctau", &Bp_Jpsi_B_ctau, &b_Bp_Jpsi_B_ctau);
   fChain->SetBranchAddress("Bp_Jpsi_Chi2NDoF", &Bp_Jpsi_Chi2NDoF, &b_Bp_Jpsi_Chi2NDoF);
   fChain->SetBranchAddress("Bp_Jpsi_X_M", &Bp_Jpsi_X_M, &b_Bp_Jpsi_X_M);
   fChain->SetBranchAddress("Bp_ENDVERTEX_X", &Bp_ENDVERTEX_X, &b_Bp_ENDVERTEX_X);
   fChain->SetBranchAddress("Bp_ENDVERTEX_Y", &Bp_ENDVERTEX_Y, &b_Bp_ENDVERTEX_Y);
   fChain->SetBranchAddress("Bp_ENDVERTEX_Z", &Bp_ENDVERTEX_Z, &b_Bp_ENDVERTEX_Z);
   fChain->SetBranchAddress("Bp_ENDVERTEX_XERR", &Bp_ENDVERTEX_XERR, &b_Bp_ENDVERTEX_XERR);
   fChain->SetBranchAddress("Bp_ENDVERTEX_YERR", &Bp_ENDVERTEX_YERR, &b_Bp_ENDVERTEX_YERR);
   fChain->SetBranchAddress("Bp_ENDVERTEX_ZERR", &Bp_ENDVERTEX_ZERR, &b_Bp_ENDVERTEX_ZERR);
   fChain->SetBranchAddress("Bp_ENDVERTEX_CHI2", &Bp_ENDVERTEX_CHI2, &b_Bp_ENDVERTEX_CHI2);
   fChain->SetBranchAddress("Bp_ENDVERTEX_NDOF", &Bp_ENDVERTEX_NDOF, &b_Bp_ENDVERTEX_NDOF);
   fChain->SetBranchAddress("Bp_ENDVERTEX_COV_", Bp_ENDVERTEX_COV_, &b_Bp_ENDVERTEX_COV_);
   fChain->SetBranchAddress("Bp_OWNPV_X", &Bp_OWNPV_X, &b_Bp_OWNPV_X);
   fChain->SetBranchAddress("Bp_OWNPV_Y", &Bp_OWNPV_Y, &b_Bp_OWNPV_Y);
   fChain->SetBranchAddress("Bp_OWNPV_Z", &Bp_OWNPV_Z, &b_Bp_OWNPV_Z);
   fChain->SetBranchAddress("Bp_OWNPV_XERR", &Bp_OWNPV_XERR, &b_Bp_OWNPV_XERR);
   fChain->SetBranchAddress("Bp_OWNPV_YERR", &Bp_OWNPV_YERR, &b_Bp_OWNPV_YERR);
   fChain->SetBranchAddress("Bp_OWNPV_ZERR", &Bp_OWNPV_ZERR, &b_Bp_OWNPV_ZERR);
   fChain->SetBranchAddress("Bp_OWNPV_CHI2", &Bp_OWNPV_CHI2, &b_Bp_OWNPV_CHI2);
   fChain->SetBranchAddress("Bp_OWNPV_NDOF", &Bp_OWNPV_NDOF, &b_Bp_OWNPV_NDOF);
   fChain->SetBranchAddress("Bp_OWNPV_COV_", Bp_OWNPV_COV_, &b_Bp_OWNPV_COV_);
   fChain->SetBranchAddress("Bp_IP_OWNPV", &Bp_IP_OWNPV, &b_Bp_IP_OWNPV);
   fChain->SetBranchAddress("Bp_IPCHI2_OWNPV", &Bp_IPCHI2_OWNPV, &b_Bp_IPCHI2_OWNPV);
   fChain->SetBranchAddress("Bp_FD_OWNPV", &Bp_FD_OWNPV, &b_Bp_FD_OWNPV);
   fChain->SetBranchAddress("Bp_FDCHI2_OWNPV", &Bp_FDCHI2_OWNPV, &b_Bp_FDCHI2_OWNPV);
   fChain->SetBranchAddress("Bp_DIRA_OWNPV", &Bp_DIRA_OWNPV, &b_Bp_DIRA_OWNPV);
   fChain->SetBranchAddress("Bp_P", &Bp_P, &b_Bp_P);
   fChain->SetBranchAddress("Bp_PT", &Bp_PT, &b_Bp_PT);
   fChain->SetBranchAddress("Bp_PE", &Bp_PE, &b_Bp_PE);
   fChain->SetBranchAddress("Bp_PX", &Bp_PX, &b_Bp_PX);
   fChain->SetBranchAddress("Bp_PY", &Bp_PY, &b_Bp_PY);
   fChain->SetBranchAddress("Bp_PZ", &Bp_PZ, &b_Bp_PZ);
   fChain->SetBranchAddress("Bp_MM", &Bp_MM, &b_Bp_MM);
   fChain->SetBranchAddress("Bp_MMERR", &Bp_MMERR, &b_Bp_MMERR);
   fChain->SetBranchAddress("Bp_M", &Bp_M, &b_Bp_M);
   fChain->SetBranchAddress("Bp_TAU", &Bp_TAU, &b_Bp_TAU);
   fChain->SetBranchAddress("Bp_TAUERR", &Bp_TAUERR, &b_Bp_TAUERR);
   fChain->SetBranchAddress("Bp_TAUCHI2", &Bp_TAUCHI2, &b_Bp_TAUCHI2);
   fChain->SetBranchAddress("Bp_L0Global_Dec", &Bp_L0Global_Dec, &b_Bp_L0Global_Dec);
   fChain->SetBranchAddress("Bp_L0Global_TIS", &Bp_L0Global_TIS, &b_Bp_L0Global_TIS);
   fChain->SetBranchAddress("Bp_L0Global_TOS", &Bp_L0Global_TOS, &b_Bp_L0Global_TOS);
   fChain->SetBranchAddress("Bp_Hlt1Global_Dec", &Bp_Hlt1Global_Dec, &b_Bp_Hlt1Global_Dec);
   fChain->SetBranchAddress("Bp_Hlt1Global_TIS", &Bp_Hlt1Global_TIS, &b_Bp_Hlt1Global_TIS);
   fChain->SetBranchAddress("Bp_Hlt1Global_TOS", &Bp_Hlt1Global_TOS, &b_Bp_Hlt1Global_TOS);
   fChain->SetBranchAddress("Bp_Hlt1Phys_Dec", &Bp_Hlt1Phys_Dec, &b_Bp_Hlt1Phys_Dec);
   fChain->SetBranchAddress("Bp_Hlt1Phys_TIS", &Bp_Hlt1Phys_TIS, &b_Bp_Hlt1Phys_TIS);
   fChain->SetBranchAddress("Bp_Hlt1Phys_TOS", &Bp_Hlt1Phys_TOS, &b_Bp_Hlt1Phys_TOS);
   fChain->SetBranchAddress("Bp_Hlt2Global_Dec", &Bp_Hlt2Global_Dec, &b_Bp_Hlt2Global_Dec);
   fChain->SetBranchAddress("Bp_Hlt2Global_TIS", &Bp_Hlt2Global_TIS, &b_Bp_Hlt2Global_TIS);
   fChain->SetBranchAddress("Bp_Hlt2Global_TOS", &Bp_Hlt2Global_TOS, &b_Bp_Hlt2Global_TOS);
   fChain->SetBranchAddress("Bp_Hlt2Phys_Dec", &Bp_Hlt2Phys_Dec, &b_Bp_Hlt2Phys_Dec);
   fChain->SetBranchAddress("Bp_Hlt2Phys_TIS", &Bp_Hlt2Phys_TIS, &b_Bp_Hlt2Phys_TIS);
   fChain->SetBranchAddress("Bp_Hlt2Phys_TOS", &Bp_Hlt2Phys_TOS, &b_Bp_Hlt2Phys_TOS);
   fChain->SetBranchAddress("Bp_L0DiMuonDecision_Dec", &Bp_L0DiMuonDecision_Dec, &b_Bp_L0DiMuonDecision_Dec);
   fChain->SetBranchAddress("Bp_L0DiMuonDecision_TIS", &Bp_L0DiMuonDecision_TIS, &b_Bp_L0DiMuonDecision_TIS);
   fChain->SetBranchAddress("Bp_L0DiMuonDecision_TOS", &Bp_L0DiMuonDecision_TOS, &b_Bp_L0DiMuonDecision_TOS);
   fChain->SetBranchAddress("Bp_L0MuonDecision_Dec", &Bp_L0MuonDecision_Dec, &b_Bp_L0MuonDecision_Dec);
   fChain->SetBranchAddress("Bp_L0MuonDecision_TIS", &Bp_L0MuonDecision_TIS, &b_Bp_L0MuonDecision_TIS);
   fChain->SetBranchAddress("Bp_L0MuonDecision_TOS", &Bp_L0MuonDecision_TOS, &b_Bp_L0MuonDecision_TOS);
   fChain->SetBranchAddress("Bp_Hlt1DiMuonHighMassDecision_Dec", &Bp_Hlt1DiMuonHighMassDecision_Dec, &b_Bp_Hlt1DiMuonHighMassDecision_Dec);
   fChain->SetBranchAddress("Bp_Hlt1DiMuonHighMassDecision_TIS", &Bp_Hlt1DiMuonHighMassDecision_TIS, &b_Bp_Hlt1DiMuonHighMassDecision_TIS);
   fChain->SetBranchAddress("Bp_Hlt1DiMuonHighMassDecision_TOS", &Bp_Hlt1DiMuonHighMassDecision_TOS, &b_Bp_Hlt1DiMuonHighMassDecision_TOS);
   fChain->SetBranchAddress("Bp_Hlt1TrackMuonDecision_Dec", &Bp_Hlt1TrackMuonDecision_Dec, &b_Bp_Hlt1TrackMuonDecision_Dec);
   fChain->SetBranchAddress("Bp_Hlt1TrackMuonDecision_TIS", &Bp_Hlt1TrackMuonDecision_TIS, &b_Bp_Hlt1TrackMuonDecision_TIS);
   fChain->SetBranchAddress("Bp_Hlt1TrackMuonDecision_TOS", &Bp_Hlt1TrackMuonDecision_TOS, &b_Bp_Hlt1TrackMuonDecision_TOS);
   fChain->SetBranchAddress("Bp_Hlt1TrackMVADecision_Dec", &Bp_Hlt1TrackMVADecision_Dec, &b_Bp_Hlt1TrackMVADecision_Dec);
   fChain->SetBranchAddress("Bp_Hlt1TrackMVADecision_TIS", &Bp_Hlt1TrackMVADecision_TIS, &b_Bp_Hlt1TrackMVADecision_TIS);
   fChain->SetBranchAddress("Bp_Hlt1TrackMVADecision_TOS", &Bp_Hlt1TrackMVADecision_TOS, &b_Bp_Hlt1TrackMVADecision_TOS);
   fChain->SetBranchAddress("Bp_Hlt2DiMuonDetachedJPsiDecision_Dec", &Bp_Hlt2DiMuonDetachedJPsiDecision_Dec, &b_Bp_Hlt2DiMuonDetachedJPsiDecision_Dec);
   fChain->SetBranchAddress("Bp_Hlt2DiMuonDetachedJPsiDecision_TIS", &Bp_Hlt2DiMuonDetachedJPsiDecision_TIS, &b_Bp_Hlt2DiMuonDetachedJPsiDecision_TIS);
   fChain->SetBranchAddress("Bp_Hlt2DiMuonDetachedJPsiDecision_TOS", &Bp_Hlt2DiMuonDetachedJPsiDecision_TOS, &b_Bp_Hlt2DiMuonDetachedJPsiDecision_TOS);
   fChain->SetBranchAddress("X_P", &X_P, &b_X_P);
   fChain->SetBranchAddress("X_PT", &X_PT, &b_X_PT);
   fChain->SetBranchAddress("X_PE", &X_PE, &b_X_PE);
   fChain->SetBranchAddress("X_PX", &X_PX, &b_X_PX);
   fChain->SetBranchAddress("X_PY", &X_PY, &b_X_PY);
   fChain->SetBranchAddress("X_PZ", &X_PZ, &b_X_PZ);
   fChain->SetBranchAddress("X_MM", &X_MM, &b_X_MM);
   fChain->SetBranchAddress("X_MMERR", &X_MMERR, &b_X_MMERR);
   fChain->SetBranchAddress("X_M", &X_M, &b_X_M);
   fChain->SetBranchAddress("Jpsi_P", &Jpsi_P, &b_Jpsi_P);
   fChain->SetBranchAddress("Jpsi_PT", &Jpsi_PT, &b_Jpsi_PT);
   fChain->SetBranchAddress("Jpsi_PE", &Jpsi_PE, &b_Jpsi_PE);
   fChain->SetBranchAddress("Jpsi_PX", &Jpsi_PX, &b_Jpsi_PX);
   fChain->SetBranchAddress("Jpsi_PY", &Jpsi_PY, &b_Jpsi_PY);
   fChain->SetBranchAddress("Jpsi_PZ", &Jpsi_PZ, &b_Jpsi_PZ);
   fChain->SetBranchAddress("Jpsi_MM", &Jpsi_MM, &b_Jpsi_MM);
   fChain->SetBranchAddress("Jpsi_MMERR", &Jpsi_MMERR, &b_Jpsi_MMERR);
   fChain->SetBranchAddress("Jpsi_M", &Jpsi_M, &b_Jpsi_M);
   fChain->SetBranchAddress("Mu0_OWNPV_X", &Mu0_OWNPV_X, &b_Mu0_OWNPV_X);
   fChain->SetBranchAddress("Mu0_OWNPV_Y", &Mu0_OWNPV_Y, &b_Mu0_OWNPV_Y);
   fChain->SetBranchAddress("Mu0_OWNPV_Z", &Mu0_OWNPV_Z, &b_Mu0_OWNPV_Z);
   fChain->SetBranchAddress("Mu0_OWNPV_XERR", &Mu0_OWNPV_XERR, &b_Mu0_OWNPV_XERR);
   fChain->SetBranchAddress("Mu0_OWNPV_YERR", &Mu0_OWNPV_YERR, &b_Mu0_OWNPV_YERR);
   fChain->SetBranchAddress("Mu0_OWNPV_ZERR", &Mu0_OWNPV_ZERR, &b_Mu0_OWNPV_ZERR);
   fChain->SetBranchAddress("Mu0_OWNPV_CHI2", &Mu0_OWNPV_CHI2, &b_Mu0_OWNPV_CHI2);
   fChain->SetBranchAddress("Mu0_OWNPV_NDOF", &Mu0_OWNPV_NDOF, &b_Mu0_OWNPV_NDOF);
   fChain->SetBranchAddress("Mu0_OWNPV_COV_", Mu0_OWNPV_COV_, &b_Mu0_OWNPV_COV_);
   fChain->SetBranchAddress("Mu0_IP_OWNPV", &Mu0_IP_OWNPV, &b_Mu0_IP_OWNPV);
   fChain->SetBranchAddress("Mu0_IPCHI2_OWNPV", &Mu0_IPCHI2_OWNPV, &b_Mu0_IPCHI2_OWNPV);
   fChain->SetBranchAddress("Mu0_ORIVX_X", &Mu0_ORIVX_X, &b_Mu0_ORIVX_X);
   fChain->SetBranchAddress("Mu0_ORIVX_Y", &Mu0_ORIVX_Y, &b_Mu0_ORIVX_Y);
   fChain->SetBranchAddress("Mu0_ORIVX_Z", &Mu0_ORIVX_Z, &b_Mu0_ORIVX_Z);
   fChain->SetBranchAddress("Mu0_ORIVX_XERR", &Mu0_ORIVX_XERR, &b_Mu0_ORIVX_XERR);
   fChain->SetBranchAddress("Mu0_ORIVX_YERR", &Mu0_ORIVX_YERR, &b_Mu0_ORIVX_YERR);
   fChain->SetBranchAddress("Mu0_ORIVX_ZERR", &Mu0_ORIVX_ZERR, &b_Mu0_ORIVX_ZERR);
   fChain->SetBranchAddress("Mu0_ORIVX_CHI2", &Mu0_ORIVX_CHI2, &b_Mu0_ORIVX_CHI2);
   fChain->SetBranchAddress("Mu0_ORIVX_NDOF", &Mu0_ORIVX_NDOF, &b_Mu0_ORIVX_NDOF);
   fChain->SetBranchAddress("Mu0_ORIVX_COV_", Mu0_ORIVX_COV_, &b_Mu0_ORIVX_COV_);
   fChain->SetBranchAddress("Mu0_P", &Mu0_P, &b_Mu0_P);
   fChain->SetBranchAddress("Mu0_PT", &Mu0_PT, &b_Mu0_PT);
   fChain->SetBranchAddress("Mu0_PE", &Mu0_PE, &b_Mu0_PE);
   fChain->SetBranchAddress("Mu0_PX", &Mu0_PX, &b_Mu0_PX);
   fChain->SetBranchAddress("Mu0_PY", &Mu0_PY, &b_Mu0_PY);
   fChain->SetBranchAddress("Mu0_PZ", &Mu0_PZ, &b_Mu0_PZ);
   fChain->SetBranchAddress("Mu0_M", &Mu0_M, &b_Mu0_M);
   fChain->SetBranchAddress("Mu0_ID", &Mu0_ID, &b_Mu0_ID);
   fChain->SetBranchAddress("Mu0_PIDe", &Mu0_PIDe, &b_Mu0_PIDe);
   fChain->SetBranchAddress("Mu0_PIDmu", &Mu0_PIDmu, &b_Mu0_PIDmu);
   fChain->SetBranchAddress("Mu0_PIDK", &Mu0_PIDK, &b_Mu0_PIDK);
   fChain->SetBranchAddress("Mu0_PIDp", &Mu0_PIDp, &b_Mu0_PIDp);
   fChain->SetBranchAddress("Mu0_PIDd", &Mu0_PIDd, &b_Mu0_PIDd);
   fChain->SetBranchAddress("Mu0_ProbNNe", &Mu0_ProbNNe, &b_Mu0_ProbNNe);
   fChain->SetBranchAddress("Mu0_ProbNNk", &Mu0_ProbNNk, &b_Mu0_ProbNNk);
   fChain->SetBranchAddress("Mu0_ProbNNp", &Mu0_ProbNNp, &b_Mu0_ProbNNp);
   fChain->SetBranchAddress("Mu0_ProbNNpi", &Mu0_ProbNNpi, &b_Mu0_ProbNNpi);
   fChain->SetBranchAddress("Mu0_ProbNNmu", &Mu0_ProbNNmu, &b_Mu0_ProbNNmu);
   fChain->SetBranchAddress("Mu0_ProbNNd", &Mu0_ProbNNd, &b_Mu0_ProbNNd);
   fChain->SetBranchAddress("Mu0_ProbNNghost", &Mu0_ProbNNghost, &b_Mu0_ProbNNghost);
   fChain->SetBranchAddress("Mu0_hasMuon", &Mu0_hasMuon, &b_Mu0_hasMuon);
   fChain->SetBranchAddress("Mu0_isMuon", &Mu0_isMuon, &b_Mu0_isMuon);
   fChain->SetBranchAddress("Mu0_hasRich", &Mu0_hasRich, &b_Mu0_hasRich);
   fChain->SetBranchAddress("Mu0_UsedRichAerogel", &Mu0_UsedRichAerogel, &b_Mu0_UsedRichAerogel);
   fChain->SetBranchAddress("Mu0_UsedRich1Gas", &Mu0_UsedRich1Gas, &b_Mu0_UsedRich1Gas);
   fChain->SetBranchAddress("Mu0_UsedRich2Gas", &Mu0_UsedRich2Gas, &b_Mu0_UsedRich2Gas);
   fChain->SetBranchAddress("Mu0_RichAboveElThres", &Mu0_RichAboveElThres, &b_Mu0_RichAboveElThres);
   fChain->SetBranchAddress("Mu0_RichAboveMuThres", &Mu0_RichAboveMuThres, &b_Mu0_RichAboveMuThres);
   fChain->SetBranchAddress("Mu0_RichAbovePiThres", &Mu0_RichAbovePiThres, &b_Mu0_RichAbovePiThres);
   fChain->SetBranchAddress("Mu0_RichAboveKaThres", &Mu0_RichAboveKaThres, &b_Mu0_RichAboveKaThres);
   fChain->SetBranchAddress("Mu0_RichAbovePrThres", &Mu0_RichAbovePrThres, &b_Mu0_RichAbovePrThres);
   fChain->SetBranchAddress("Mu0_hasCalo", &Mu0_hasCalo, &b_Mu0_hasCalo);
   fChain->SetBranchAddress("Mu1_OWNPV_X", &Mu1_OWNPV_X, &b_Mu1_OWNPV_X);
   fChain->SetBranchAddress("Mu1_OWNPV_Y", &Mu1_OWNPV_Y, &b_Mu1_OWNPV_Y);
   fChain->SetBranchAddress("Mu1_OWNPV_Z", &Mu1_OWNPV_Z, &b_Mu1_OWNPV_Z);
   fChain->SetBranchAddress("Mu1_OWNPV_XERR", &Mu1_OWNPV_XERR, &b_Mu1_OWNPV_XERR);
   fChain->SetBranchAddress("Mu1_OWNPV_YERR", &Mu1_OWNPV_YERR, &b_Mu1_OWNPV_YERR);
   fChain->SetBranchAddress("Mu1_OWNPV_ZERR", &Mu1_OWNPV_ZERR, &b_Mu1_OWNPV_ZERR);
   fChain->SetBranchAddress("Mu1_OWNPV_CHI2", &Mu1_OWNPV_CHI2, &b_Mu1_OWNPV_CHI2);
   fChain->SetBranchAddress("Mu1_OWNPV_NDOF", &Mu1_OWNPV_NDOF, &b_Mu1_OWNPV_NDOF);
   fChain->SetBranchAddress("Mu1_OWNPV_COV_", Mu1_OWNPV_COV_, &b_Mu1_OWNPV_COV_);
   fChain->SetBranchAddress("Mu1_IP_OWNPV", &Mu1_IP_OWNPV, &b_Mu1_IP_OWNPV);
   fChain->SetBranchAddress("Mu1_IPCHI2_OWNPV", &Mu1_IPCHI2_OWNPV, &b_Mu1_IPCHI2_OWNPV);
   fChain->SetBranchAddress("Mu1_ORIVX_X", &Mu1_ORIVX_X, &b_Mu1_ORIVX_X);
   fChain->SetBranchAddress("Mu1_ORIVX_Y", &Mu1_ORIVX_Y, &b_Mu1_ORIVX_Y);
   fChain->SetBranchAddress("Mu1_ORIVX_Z", &Mu1_ORIVX_Z, &b_Mu1_ORIVX_Z);
   fChain->SetBranchAddress("Mu1_ORIVX_XERR", &Mu1_ORIVX_XERR, &b_Mu1_ORIVX_XERR);
   fChain->SetBranchAddress("Mu1_ORIVX_YERR", &Mu1_ORIVX_YERR, &b_Mu1_ORIVX_YERR);
   fChain->SetBranchAddress("Mu1_ORIVX_ZERR", &Mu1_ORIVX_ZERR, &b_Mu1_ORIVX_ZERR);
   fChain->SetBranchAddress("Mu1_ORIVX_CHI2", &Mu1_ORIVX_CHI2, &b_Mu1_ORIVX_CHI2);
   fChain->SetBranchAddress("Mu1_ORIVX_NDOF", &Mu1_ORIVX_NDOF, &b_Mu1_ORIVX_NDOF);
   fChain->SetBranchAddress("Mu1_ORIVX_COV_", Mu1_ORIVX_COV_, &b_Mu1_ORIVX_COV_);
   fChain->SetBranchAddress("Mu1_P", &Mu1_P, &b_Mu1_P);
   fChain->SetBranchAddress("Mu1_PT", &Mu1_PT, &b_Mu1_PT);
   fChain->SetBranchAddress("Mu1_PE", &Mu1_PE, &b_Mu1_PE);
   fChain->SetBranchAddress("Mu1_PX", &Mu1_PX, &b_Mu1_PX);
   fChain->SetBranchAddress("Mu1_PY", &Mu1_PY, &b_Mu1_PY);
   fChain->SetBranchAddress("Mu1_PZ", &Mu1_PZ, &b_Mu1_PZ);
   fChain->SetBranchAddress("Mu1_M", &Mu1_M, &b_Mu1_M);
   fChain->SetBranchAddress("Mu1_ID", &Mu1_ID, &b_Mu1_ID);
   fChain->SetBranchAddress("Mu1_PIDe", &Mu1_PIDe, &b_Mu1_PIDe);
   fChain->SetBranchAddress("Mu1_PIDmu", &Mu1_PIDmu, &b_Mu1_PIDmu);
   fChain->SetBranchAddress("Mu1_PIDK", &Mu1_PIDK, &b_Mu1_PIDK);
   fChain->SetBranchAddress("Mu1_PIDp", &Mu1_PIDp, &b_Mu1_PIDp);
   fChain->SetBranchAddress("Mu1_PIDd", &Mu1_PIDd, &b_Mu1_PIDd);
   fChain->SetBranchAddress("Mu1_ProbNNe", &Mu1_ProbNNe, &b_Mu1_ProbNNe);
   fChain->SetBranchAddress("Mu1_ProbNNk", &Mu1_ProbNNk, &b_Mu1_ProbNNk);
   fChain->SetBranchAddress("Mu1_ProbNNp", &Mu1_ProbNNp, &b_Mu1_ProbNNp);
   fChain->SetBranchAddress("Mu1_ProbNNpi", &Mu1_ProbNNpi, &b_Mu1_ProbNNpi);
   fChain->SetBranchAddress("Mu1_ProbNNmu", &Mu1_ProbNNmu, &b_Mu1_ProbNNmu);
   fChain->SetBranchAddress("Mu1_ProbNNd", &Mu1_ProbNNd, &b_Mu1_ProbNNd);
   fChain->SetBranchAddress("Mu1_ProbNNghost", &Mu1_ProbNNghost, &b_Mu1_ProbNNghost);
   fChain->SetBranchAddress("Mu1_hasMuon", &Mu1_hasMuon, &b_Mu1_hasMuon);
   fChain->SetBranchAddress("Mu1_isMuon", &Mu1_isMuon, &b_Mu1_isMuon);
   fChain->SetBranchAddress("Mu1_hasRich", &Mu1_hasRich, &b_Mu1_hasRich);
   fChain->SetBranchAddress("Mu1_UsedRichAerogel", &Mu1_UsedRichAerogel, &b_Mu1_UsedRichAerogel);
   fChain->SetBranchAddress("Mu1_UsedRich1Gas", &Mu1_UsedRich1Gas, &b_Mu1_UsedRich1Gas);
   fChain->SetBranchAddress("Mu1_UsedRich2Gas", &Mu1_UsedRich2Gas, &b_Mu1_UsedRich2Gas);
   fChain->SetBranchAddress("Mu1_RichAboveElThres", &Mu1_RichAboveElThres, &b_Mu1_RichAboveElThres);
   fChain->SetBranchAddress("Mu1_RichAboveMuThres", &Mu1_RichAboveMuThres, &b_Mu1_RichAboveMuThres);
   fChain->SetBranchAddress("Mu1_RichAbovePiThres", &Mu1_RichAbovePiThres, &b_Mu1_RichAbovePiThres);
   fChain->SetBranchAddress("Mu1_RichAboveKaThres", &Mu1_RichAboveKaThres, &b_Mu1_RichAboveKaThres);
   fChain->SetBranchAddress("Mu1_RichAbovePrThres", &Mu1_RichAbovePrThres, &b_Mu1_RichAbovePrThres);
   fChain->SetBranchAddress("Mu1_hasCalo", &Mu1_hasCalo, &b_Mu1_hasCalo);
   fChain->SetBranchAddress("Pi0_OWNPV_X", &Pi0_OWNPV_X, &b_Pi0_OWNPV_X);
   fChain->SetBranchAddress("Pi0_OWNPV_Y", &Pi0_OWNPV_Y, &b_Pi0_OWNPV_Y);
   fChain->SetBranchAddress("Pi0_OWNPV_Z", &Pi0_OWNPV_Z, &b_Pi0_OWNPV_Z);
   fChain->SetBranchAddress("Pi0_OWNPV_XERR", &Pi0_OWNPV_XERR, &b_Pi0_OWNPV_XERR);
   fChain->SetBranchAddress("Pi0_OWNPV_YERR", &Pi0_OWNPV_YERR, &b_Pi0_OWNPV_YERR);
   fChain->SetBranchAddress("Pi0_OWNPV_ZERR", &Pi0_OWNPV_ZERR, &b_Pi0_OWNPV_ZERR);
   fChain->SetBranchAddress("Pi0_OWNPV_CHI2", &Pi0_OWNPV_CHI2, &b_Pi0_OWNPV_CHI2);
   fChain->SetBranchAddress("Pi0_OWNPV_NDOF", &Pi0_OWNPV_NDOF, &b_Pi0_OWNPV_NDOF);
   fChain->SetBranchAddress("Pi0_OWNPV_COV_", Pi0_OWNPV_COV_, &b_Pi0_OWNPV_COV_);
   fChain->SetBranchAddress("Pi0_IP_OWNPV", &Pi0_IP_OWNPV, &b_Pi0_IP_OWNPV);
   fChain->SetBranchAddress("Pi0_IPCHI2_OWNPV", &Pi0_IPCHI2_OWNPV, &b_Pi0_IPCHI2_OWNPV);
   fChain->SetBranchAddress("Pi0_ORIVX_X", &Pi0_ORIVX_X, &b_Pi0_ORIVX_X);
   fChain->SetBranchAddress("Pi0_ORIVX_Y", &Pi0_ORIVX_Y, &b_Pi0_ORIVX_Y);
   fChain->SetBranchAddress("Pi0_ORIVX_Z", &Pi0_ORIVX_Z, &b_Pi0_ORIVX_Z);
   fChain->SetBranchAddress("Pi0_ORIVX_XERR", &Pi0_ORIVX_XERR, &b_Pi0_ORIVX_XERR);
   fChain->SetBranchAddress("Pi0_ORIVX_YERR", &Pi0_ORIVX_YERR, &b_Pi0_ORIVX_YERR);
   fChain->SetBranchAddress("Pi0_ORIVX_ZERR", &Pi0_ORIVX_ZERR, &b_Pi0_ORIVX_ZERR);
   fChain->SetBranchAddress("Pi0_ORIVX_CHI2", &Pi0_ORIVX_CHI2, &b_Pi0_ORIVX_CHI2);
   fChain->SetBranchAddress("Pi0_ORIVX_NDOF", &Pi0_ORIVX_NDOF, &b_Pi0_ORIVX_NDOF);
   fChain->SetBranchAddress("Pi0_ORIVX_COV_", Pi0_ORIVX_COV_, &b_Pi0_ORIVX_COV_);
   fChain->SetBranchAddress("Pi0_P", &Pi0_P, &b_Pi0_P);
   fChain->SetBranchAddress("Pi0_PT", &Pi0_PT, &b_Pi0_PT);
   fChain->SetBranchAddress("Pi0_PE", &Pi0_PE, &b_Pi0_PE);
   fChain->SetBranchAddress("Pi0_PX", &Pi0_PX, &b_Pi0_PX);
   fChain->SetBranchAddress("Pi0_PY", &Pi0_PY, &b_Pi0_PY);
   fChain->SetBranchAddress("Pi0_PZ", &Pi0_PZ, &b_Pi0_PZ);
   fChain->SetBranchAddress("Pi0_M", &Pi0_M, &b_Pi0_M);
   fChain->SetBranchAddress("Pi0_ID", &Pi0_ID, &b_Pi0_ID);
   fChain->SetBranchAddress("Pi0_PIDe", &Pi0_PIDe, &b_Pi0_PIDe);
   fChain->SetBranchAddress("Pi0_PIDmu", &Pi0_PIDmu, &b_Pi0_PIDmu);
   fChain->SetBranchAddress("Pi0_PIDK", &Pi0_PIDK, &b_Pi0_PIDK);
   fChain->SetBranchAddress("Pi0_PIDp", &Pi0_PIDp, &b_Pi0_PIDp);
   fChain->SetBranchAddress("Pi0_PIDd", &Pi0_PIDd, &b_Pi0_PIDd);
   fChain->SetBranchAddress("Pi0_ProbNNe", &Pi0_ProbNNe, &b_Pi0_ProbNNe);
   fChain->SetBranchAddress("Pi0_ProbNNk", &Pi0_ProbNNk, &b_Pi0_ProbNNk);
   fChain->SetBranchAddress("Pi0_ProbNNp", &Pi0_ProbNNp, &b_Pi0_ProbNNp);
   fChain->SetBranchAddress("Pi0_ProbNNpi", &Pi0_ProbNNpi, &b_Pi0_ProbNNpi);
   fChain->SetBranchAddress("Pi0_ProbNNmu", &Pi0_ProbNNmu, &b_Pi0_ProbNNmu);
   fChain->SetBranchAddress("Pi0_ProbNNd", &Pi0_ProbNNd, &b_Pi0_ProbNNd);
   fChain->SetBranchAddress("Pi0_ProbNNghost", &Pi0_ProbNNghost, &b_Pi0_ProbNNghost);
   fChain->SetBranchAddress("Pi0_hasMuon", &Pi0_hasMuon, &b_Pi0_hasMuon);
   fChain->SetBranchAddress("Pi0_isMuon", &Pi0_isMuon, &b_Pi0_isMuon);
   fChain->SetBranchAddress("Pi0_hasRich", &Pi0_hasRich, &b_Pi0_hasRich);
   fChain->SetBranchAddress("Pi0_UsedRichAerogel", &Pi0_UsedRichAerogel, &b_Pi0_UsedRichAerogel);
   fChain->SetBranchAddress("Pi0_UsedRich1Gas", &Pi0_UsedRich1Gas, &b_Pi0_UsedRich1Gas);
   fChain->SetBranchAddress("Pi0_UsedRich2Gas", &Pi0_UsedRich2Gas, &b_Pi0_UsedRich2Gas);
   fChain->SetBranchAddress("Pi0_RichAboveElThres", &Pi0_RichAboveElThres, &b_Pi0_RichAboveElThres);
   fChain->SetBranchAddress("Pi0_RichAboveMuThres", &Pi0_RichAboveMuThres, &b_Pi0_RichAboveMuThres);
   fChain->SetBranchAddress("Pi0_RichAbovePiThres", &Pi0_RichAbovePiThres, &b_Pi0_RichAbovePiThres);
   fChain->SetBranchAddress("Pi0_RichAboveKaThres", &Pi0_RichAboveKaThres, &b_Pi0_RichAboveKaThres);
   fChain->SetBranchAddress("Pi0_RichAbovePrThres", &Pi0_RichAbovePrThres, &b_Pi0_RichAbovePrThres);
   fChain->SetBranchAddress("Pi0_hasCalo", &Pi0_hasCalo, &b_Pi0_hasCalo);
   fChain->SetBranchAddress("Pi1_OWNPV_X", &Pi1_OWNPV_X, &b_Pi1_OWNPV_X);
   fChain->SetBranchAddress("Pi1_OWNPV_Y", &Pi1_OWNPV_Y, &b_Pi1_OWNPV_Y);
   fChain->SetBranchAddress("Pi1_OWNPV_Z", &Pi1_OWNPV_Z, &b_Pi1_OWNPV_Z);
   fChain->SetBranchAddress("Pi1_OWNPV_XERR", &Pi1_OWNPV_XERR, &b_Pi1_OWNPV_XERR);
   fChain->SetBranchAddress("Pi1_OWNPV_YERR", &Pi1_OWNPV_YERR, &b_Pi1_OWNPV_YERR);
   fChain->SetBranchAddress("Pi1_OWNPV_ZERR", &Pi1_OWNPV_ZERR, &b_Pi1_OWNPV_ZERR);
   fChain->SetBranchAddress("Pi1_OWNPV_CHI2", &Pi1_OWNPV_CHI2, &b_Pi1_OWNPV_CHI2);
   fChain->SetBranchAddress("Pi1_OWNPV_NDOF", &Pi1_OWNPV_NDOF, &b_Pi1_OWNPV_NDOF);
   fChain->SetBranchAddress("Pi1_OWNPV_COV_", Pi1_OWNPV_COV_, &b_Pi1_OWNPV_COV_);
   fChain->SetBranchAddress("Pi1_IP_OWNPV", &Pi1_IP_OWNPV, &b_Pi1_IP_OWNPV);
   fChain->SetBranchAddress("Pi1_IPCHI2_OWNPV", &Pi1_IPCHI2_OWNPV, &b_Pi1_IPCHI2_OWNPV);
   fChain->SetBranchAddress("Pi1_ORIVX_X", &Pi1_ORIVX_X, &b_Pi1_ORIVX_X);
   fChain->SetBranchAddress("Pi1_ORIVX_Y", &Pi1_ORIVX_Y, &b_Pi1_ORIVX_Y);
   fChain->SetBranchAddress("Pi1_ORIVX_Z", &Pi1_ORIVX_Z, &b_Pi1_ORIVX_Z);
   fChain->SetBranchAddress("Pi1_ORIVX_XERR", &Pi1_ORIVX_XERR, &b_Pi1_ORIVX_XERR);
   fChain->SetBranchAddress("Pi1_ORIVX_YERR", &Pi1_ORIVX_YERR, &b_Pi1_ORIVX_YERR);
   fChain->SetBranchAddress("Pi1_ORIVX_ZERR", &Pi1_ORIVX_ZERR, &b_Pi1_ORIVX_ZERR);
   fChain->SetBranchAddress("Pi1_ORIVX_CHI2", &Pi1_ORIVX_CHI2, &b_Pi1_ORIVX_CHI2);
   fChain->SetBranchAddress("Pi1_ORIVX_NDOF", &Pi1_ORIVX_NDOF, &b_Pi1_ORIVX_NDOF);
   fChain->SetBranchAddress("Pi1_ORIVX_COV_", Pi1_ORIVX_COV_, &b_Pi1_ORIVX_COV_);
   fChain->SetBranchAddress("Pi1_P", &Pi1_P, &b_Pi1_P);
   fChain->SetBranchAddress("Pi1_PT", &Pi1_PT, &b_Pi1_PT);
   fChain->SetBranchAddress("Pi1_PE", &Pi1_PE, &b_Pi1_PE);
   fChain->SetBranchAddress("Pi1_PX", &Pi1_PX, &b_Pi1_PX);
   fChain->SetBranchAddress("Pi1_PY", &Pi1_PY, &b_Pi1_PY);
   fChain->SetBranchAddress("Pi1_PZ", &Pi1_PZ, &b_Pi1_PZ);
   fChain->SetBranchAddress("Pi1_M", &Pi1_M, &b_Pi1_M);
   fChain->SetBranchAddress("Pi1_ID", &Pi1_ID, &b_Pi1_ID);
   fChain->SetBranchAddress("Pi1_PIDe", &Pi1_PIDe, &b_Pi1_PIDe);
   fChain->SetBranchAddress("Pi1_PIDmu", &Pi1_PIDmu, &b_Pi1_PIDmu);
   fChain->SetBranchAddress("Pi1_PIDK", &Pi1_PIDK, &b_Pi1_PIDK);
   fChain->SetBranchAddress("Pi1_PIDp", &Pi1_PIDp, &b_Pi1_PIDp);
   fChain->SetBranchAddress("Pi1_PIDd", &Pi1_PIDd, &b_Pi1_PIDd);
   fChain->SetBranchAddress("Pi1_ProbNNe", &Pi1_ProbNNe, &b_Pi1_ProbNNe);
   fChain->SetBranchAddress("Pi1_ProbNNk", &Pi1_ProbNNk, &b_Pi1_ProbNNk);
   fChain->SetBranchAddress("Pi1_ProbNNp", &Pi1_ProbNNp, &b_Pi1_ProbNNp);
   fChain->SetBranchAddress("Pi1_ProbNNpi", &Pi1_ProbNNpi, &b_Pi1_ProbNNpi);
   fChain->SetBranchAddress("Pi1_ProbNNmu", &Pi1_ProbNNmu, &b_Pi1_ProbNNmu);
   fChain->SetBranchAddress("Pi1_ProbNNd", &Pi1_ProbNNd, &b_Pi1_ProbNNd);
   fChain->SetBranchAddress("Pi1_ProbNNghost", &Pi1_ProbNNghost, &b_Pi1_ProbNNghost);
   fChain->SetBranchAddress("Pi1_hasMuon", &Pi1_hasMuon, &b_Pi1_hasMuon);
   fChain->SetBranchAddress("Pi1_isMuon", &Pi1_isMuon, &b_Pi1_isMuon);
   fChain->SetBranchAddress("Pi1_hasRich", &Pi1_hasRich, &b_Pi1_hasRich);
   fChain->SetBranchAddress("Pi1_UsedRichAerogel", &Pi1_UsedRichAerogel, &b_Pi1_UsedRichAerogel);
   fChain->SetBranchAddress("Pi1_UsedRich1Gas", &Pi1_UsedRich1Gas, &b_Pi1_UsedRich1Gas);
   fChain->SetBranchAddress("Pi1_UsedRich2Gas", &Pi1_UsedRich2Gas, &b_Pi1_UsedRich2Gas);
   fChain->SetBranchAddress("Pi1_RichAboveElThres", &Pi1_RichAboveElThres, &b_Pi1_RichAboveElThres);
   fChain->SetBranchAddress("Pi1_RichAboveMuThres", &Pi1_RichAboveMuThres, &b_Pi1_RichAboveMuThres);
   fChain->SetBranchAddress("Pi1_RichAbovePiThres", &Pi1_RichAbovePiThres, &b_Pi1_RichAbovePiThres);
   fChain->SetBranchAddress("Pi1_RichAboveKaThres", &Pi1_RichAboveKaThres, &b_Pi1_RichAboveKaThres);
   fChain->SetBranchAddress("Pi1_RichAbovePrThres", &Pi1_RichAbovePrThres, &b_Pi1_RichAbovePrThres);
   fChain->SetBranchAddress("Pi1_hasCalo", &Pi1_hasCalo, &b_Pi1_hasCalo);
   fChain->SetBranchAddress("K_OWNPV_X", &K_OWNPV_X, &b_K_OWNPV_X);
   fChain->SetBranchAddress("K_OWNPV_Y", &K_OWNPV_Y, &b_K_OWNPV_Y);
   fChain->SetBranchAddress("K_OWNPV_Z", &K_OWNPV_Z, &b_K_OWNPV_Z);
   fChain->SetBranchAddress("K_OWNPV_XERR", &K_OWNPV_XERR, &b_K_OWNPV_XERR);
   fChain->SetBranchAddress("K_OWNPV_YERR", &K_OWNPV_YERR, &b_K_OWNPV_YERR);
   fChain->SetBranchAddress("K_OWNPV_ZERR", &K_OWNPV_ZERR, &b_K_OWNPV_ZERR);
   fChain->SetBranchAddress("K_OWNPV_CHI2", &K_OWNPV_CHI2, &b_K_OWNPV_CHI2);
   fChain->SetBranchAddress("K_OWNPV_NDOF", &K_OWNPV_NDOF, &b_K_OWNPV_NDOF);
   fChain->SetBranchAddress("K_OWNPV_COV_", K_OWNPV_COV_, &b_K_OWNPV_COV_);
   fChain->SetBranchAddress("K_IP_OWNPV", &K_IP_OWNPV, &b_K_IP_OWNPV);
   fChain->SetBranchAddress("K_IPCHI2_OWNPV", &K_IPCHI2_OWNPV, &b_K_IPCHI2_OWNPV);
   fChain->SetBranchAddress("K_ORIVX_X", &K_ORIVX_X, &b_K_ORIVX_X);
   fChain->SetBranchAddress("K_ORIVX_Y", &K_ORIVX_Y, &b_K_ORIVX_Y);
   fChain->SetBranchAddress("K_ORIVX_Z", &K_ORIVX_Z, &b_K_ORIVX_Z);
   fChain->SetBranchAddress("K_ORIVX_XERR", &K_ORIVX_XERR, &b_K_ORIVX_XERR);
   fChain->SetBranchAddress("K_ORIVX_YERR", &K_ORIVX_YERR, &b_K_ORIVX_YERR);
   fChain->SetBranchAddress("K_ORIVX_ZERR", &K_ORIVX_ZERR, &b_K_ORIVX_ZERR);
   fChain->SetBranchAddress("K_ORIVX_CHI2", &K_ORIVX_CHI2, &b_K_ORIVX_CHI2);
   fChain->SetBranchAddress("K_ORIVX_NDOF", &K_ORIVX_NDOF, &b_K_ORIVX_NDOF);
   fChain->SetBranchAddress("K_ORIVX_COV_", K_ORIVX_COV_, &b_K_ORIVX_COV_);
   fChain->SetBranchAddress("K_P", &K_P, &b_K_P);
   fChain->SetBranchAddress("K_PT", &K_PT, &b_K_PT);
   fChain->SetBranchAddress("K_PE", &K_PE, &b_K_PE);
   fChain->SetBranchAddress("K_PX", &K_PX, &b_K_PX);
   fChain->SetBranchAddress("K_PY", &K_PY, &b_K_PY);
   fChain->SetBranchAddress("K_PZ", &K_PZ, &b_K_PZ);
   fChain->SetBranchAddress("K_M", &K_M, &b_K_M);
   fChain->SetBranchAddress("K_ID", &K_ID, &b_K_ID);
   fChain->SetBranchAddress("K_PIDe", &K_PIDe, &b_K_PIDe);
   fChain->SetBranchAddress("K_PIDmu", &K_PIDmu, &b_K_PIDmu);
   fChain->SetBranchAddress("K_PIDK", &K_PIDK, &b_K_PIDK);
   fChain->SetBranchAddress("K_PIDp", &K_PIDp, &b_K_PIDp);
   fChain->SetBranchAddress("K_PIDd", &K_PIDd, &b_K_PIDd);
   fChain->SetBranchAddress("K_ProbNNe", &K_ProbNNe, &b_K_ProbNNe);
   fChain->SetBranchAddress("K_ProbNNk", &K_ProbNNk, &b_K_ProbNNk);
   fChain->SetBranchAddress("K_ProbNNp", &K_ProbNNp, &b_K_ProbNNp);
   fChain->SetBranchAddress("K_ProbNNpi", &K_ProbNNpi, &b_K_ProbNNpi);
   fChain->SetBranchAddress("K_ProbNNmu", &K_ProbNNmu, &b_K_ProbNNmu);
   fChain->SetBranchAddress("K_ProbNNd", &K_ProbNNd, &b_K_ProbNNd);
   fChain->SetBranchAddress("K_ProbNNghost", &K_ProbNNghost, &b_K_ProbNNghost);
   fChain->SetBranchAddress("K_hasMuon", &K_hasMuon, &b_K_hasMuon);
   fChain->SetBranchAddress("K_isMuon", &K_isMuon, &b_K_isMuon);
   fChain->SetBranchAddress("K_hasRich", &K_hasRich, &b_K_hasRich);
   fChain->SetBranchAddress("K_UsedRichAerogel", &K_UsedRichAerogel, &b_K_UsedRichAerogel);
   fChain->SetBranchAddress("K_UsedRich1Gas", &K_UsedRich1Gas, &b_K_UsedRich1Gas);
   fChain->SetBranchAddress("K_UsedRich2Gas", &K_UsedRich2Gas, &b_K_UsedRich2Gas);
   fChain->SetBranchAddress("K_RichAboveElThres", &K_RichAboveElThres, &b_K_RichAboveElThres);
   fChain->SetBranchAddress("K_RichAboveMuThres", &K_RichAboveMuThres, &b_K_RichAboveMuThres);
   fChain->SetBranchAddress("K_RichAbovePiThres", &K_RichAbovePiThres, &b_K_RichAbovePiThres);
   fChain->SetBranchAddress("K_RichAboveKaThres", &K_RichAboveKaThres, &b_K_RichAboveKaThres);
   fChain->SetBranchAddress("K_RichAbovePrThres", &K_RichAbovePrThres, &b_K_RichAbovePrThres);
   fChain->SetBranchAddress("K_hasCalo", &K_hasCalo, &b_K_hasCalo);
   fChain->SetBranchAddress("Pi2_OWNPV_X", &Pi2_OWNPV_X, &b_Pi2_OWNPV_X);
   fChain->SetBranchAddress("Pi2_OWNPV_Y", &Pi2_OWNPV_Y, &b_Pi2_OWNPV_Y);
   fChain->SetBranchAddress("Pi2_OWNPV_Z", &Pi2_OWNPV_Z, &b_Pi2_OWNPV_Z);
   fChain->SetBranchAddress("Pi2_OWNPV_XERR", &Pi2_OWNPV_XERR, &b_Pi2_OWNPV_XERR);
   fChain->SetBranchAddress("Pi2_OWNPV_YERR", &Pi2_OWNPV_YERR, &b_Pi2_OWNPV_YERR);
   fChain->SetBranchAddress("Pi2_OWNPV_ZERR", &Pi2_OWNPV_ZERR, &b_Pi2_OWNPV_ZERR);
   fChain->SetBranchAddress("Pi2_OWNPV_CHI2", &Pi2_OWNPV_CHI2, &b_Pi2_OWNPV_CHI2);
   fChain->SetBranchAddress("Pi2_OWNPV_NDOF", &Pi2_OWNPV_NDOF, &b_Pi2_OWNPV_NDOF);
   fChain->SetBranchAddress("Pi2_OWNPV_COV_", Pi2_OWNPV_COV_, &b_Pi2_OWNPV_COV_);
   fChain->SetBranchAddress("Pi2_IP_OWNPV", &Pi2_IP_OWNPV, &b_Pi2_IP_OWNPV);
   fChain->SetBranchAddress("Pi2_IPCHI2_OWNPV", &Pi2_IPCHI2_OWNPV, &b_Pi2_IPCHI2_OWNPV);
   fChain->SetBranchAddress("Pi2_ORIVX_X", &Pi2_ORIVX_X, &b_Pi2_ORIVX_X);
   fChain->SetBranchAddress("Pi2_ORIVX_Y", &Pi2_ORIVX_Y, &b_Pi2_ORIVX_Y);
   fChain->SetBranchAddress("Pi2_ORIVX_Z", &Pi2_ORIVX_Z, &b_Pi2_ORIVX_Z);
   fChain->SetBranchAddress("Pi2_ORIVX_XERR", &Pi2_ORIVX_XERR, &b_Pi2_ORIVX_XERR);
   fChain->SetBranchAddress("Pi2_ORIVX_YERR", &Pi2_ORIVX_YERR, &b_Pi2_ORIVX_YERR);
   fChain->SetBranchAddress("Pi2_ORIVX_ZERR", &Pi2_ORIVX_ZERR, &b_Pi2_ORIVX_ZERR);
   fChain->SetBranchAddress("Pi2_ORIVX_CHI2", &Pi2_ORIVX_CHI2, &b_Pi2_ORIVX_CHI2);
   fChain->SetBranchAddress("Pi2_ORIVX_NDOF", &Pi2_ORIVX_NDOF, &b_Pi2_ORIVX_NDOF);
   fChain->SetBranchAddress("Pi2_ORIVX_COV_", Pi2_ORIVX_COV_, &b_Pi2_ORIVX_COV_);
   fChain->SetBranchAddress("Pi2_P", &Pi2_P, &b_Pi2_P);
   fChain->SetBranchAddress("Pi2_PT", &Pi2_PT, &b_Pi2_PT);
   fChain->SetBranchAddress("Pi2_PE", &Pi2_PE, &b_Pi2_PE);
   fChain->SetBranchAddress("Pi2_PX", &Pi2_PX, &b_Pi2_PX);
   fChain->SetBranchAddress("Pi2_PY", &Pi2_PY, &b_Pi2_PY);
   fChain->SetBranchAddress("Pi2_PZ", &Pi2_PZ, &b_Pi2_PZ);
   fChain->SetBranchAddress("Pi2_M", &Pi2_M, &b_Pi2_M);
   fChain->SetBranchAddress("Pi2_ID", &Pi2_ID, &b_Pi2_ID);
   fChain->SetBranchAddress("Pi2_PIDe", &Pi2_PIDe, &b_Pi2_PIDe);
   fChain->SetBranchAddress("Pi2_PIDmu", &Pi2_PIDmu, &b_Pi2_PIDmu);
   fChain->SetBranchAddress("Pi2_PIDK", &Pi2_PIDK, &b_Pi2_PIDK);
   fChain->SetBranchAddress("Pi2_PIDp", &Pi2_PIDp, &b_Pi2_PIDp);
   fChain->SetBranchAddress("Pi2_PIDd", &Pi2_PIDd, &b_Pi2_PIDd);
   fChain->SetBranchAddress("Pi2_ProbNNe", &Pi2_ProbNNe, &b_Pi2_ProbNNe);
   fChain->SetBranchAddress("Pi2_ProbNNk", &Pi2_ProbNNk, &b_Pi2_ProbNNk);
   fChain->SetBranchAddress("Pi2_ProbNNp", &Pi2_ProbNNp, &b_Pi2_ProbNNp);
   fChain->SetBranchAddress("Pi2_ProbNNpi", &Pi2_ProbNNpi, &b_Pi2_ProbNNpi);
   fChain->SetBranchAddress("Pi2_ProbNNmu", &Pi2_ProbNNmu, &b_Pi2_ProbNNmu);
   fChain->SetBranchAddress("Pi2_ProbNNd", &Pi2_ProbNNd, &b_Pi2_ProbNNd);
   fChain->SetBranchAddress("Pi2_ProbNNghost", &Pi2_ProbNNghost, &b_Pi2_ProbNNghost);
   fChain->SetBranchAddress("Pi2_hasMuon", &Pi2_hasMuon, &b_Pi2_hasMuon);
   fChain->SetBranchAddress("Pi2_isMuon", &Pi2_isMuon, &b_Pi2_isMuon);
   fChain->SetBranchAddress("Pi2_hasRich", &Pi2_hasRich, &b_Pi2_hasRich);
   fChain->SetBranchAddress("Pi2_UsedRichAerogel", &Pi2_UsedRichAerogel, &b_Pi2_UsedRichAerogel);
   fChain->SetBranchAddress("Pi2_UsedRich1Gas", &Pi2_UsedRich1Gas, &b_Pi2_UsedRich1Gas);
   fChain->SetBranchAddress("Pi2_UsedRich2Gas", &Pi2_UsedRich2Gas, &b_Pi2_UsedRich2Gas);
   fChain->SetBranchAddress("Pi2_RichAboveElThres", &Pi2_RichAboveElThres, &b_Pi2_RichAboveElThres);
   fChain->SetBranchAddress("Pi2_RichAboveMuThres", &Pi2_RichAboveMuThres, &b_Pi2_RichAboveMuThres);
   fChain->SetBranchAddress("Pi2_RichAbovePiThres", &Pi2_RichAbovePiThres, &b_Pi2_RichAbovePiThres);
   fChain->SetBranchAddress("Pi2_RichAboveKaThres", &Pi2_RichAboveKaThres, &b_Pi2_RichAboveKaThres);
   fChain->SetBranchAddress("Pi2_RichAbovePrThres", &Pi2_RichAbovePrThres, &b_Pi2_RichAbovePrThres);
   fChain->SetBranchAddress("Pi2_hasCalo", &Pi2_hasCalo, &b_Pi2_hasCalo);
   fChain->SetBranchAddress("Pi3_OWNPV_X", &Pi3_OWNPV_X, &b_Pi3_OWNPV_X);
   fChain->SetBranchAddress("Pi3_OWNPV_Y", &Pi3_OWNPV_Y, &b_Pi3_OWNPV_Y);
   fChain->SetBranchAddress("Pi3_OWNPV_Z", &Pi3_OWNPV_Z, &b_Pi3_OWNPV_Z);
   fChain->SetBranchAddress("Pi3_OWNPV_XERR", &Pi3_OWNPV_XERR, &b_Pi3_OWNPV_XERR);
   fChain->SetBranchAddress("Pi3_OWNPV_YERR", &Pi3_OWNPV_YERR, &b_Pi3_OWNPV_YERR);
   fChain->SetBranchAddress("Pi3_OWNPV_ZERR", &Pi3_OWNPV_ZERR, &b_Pi3_OWNPV_ZERR);
   fChain->SetBranchAddress("Pi3_OWNPV_CHI2", &Pi3_OWNPV_CHI2, &b_Pi3_OWNPV_CHI2);
   fChain->SetBranchAddress("Pi3_OWNPV_NDOF", &Pi3_OWNPV_NDOF, &b_Pi3_OWNPV_NDOF);
   fChain->SetBranchAddress("Pi3_OWNPV_COV_", Pi3_OWNPV_COV_, &b_Pi3_OWNPV_COV_);
   fChain->SetBranchAddress("Pi3_IP_OWNPV", &Pi3_IP_OWNPV, &b_Pi3_IP_OWNPV);
   fChain->SetBranchAddress("Pi3_IPCHI2_OWNPV", &Pi3_IPCHI2_OWNPV, &b_Pi3_IPCHI2_OWNPV);
   fChain->SetBranchAddress("Pi3_ORIVX_X", &Pi3_ORIVX_X, &b_Pi3_ORIVX_X);
   fChain->SetBranchAddress("Pi3_ORIVX_Y", &Pi3_ORIVX_Y, &b_Pi3_ORIVX_Y);
   fChain->SetBranchAddress("Pi3_ORIVX_Z", &Pi3_ORIVX_Z, &b_Pi3_ORIVX_Z);
   fChain->SetBranchAddress("Pi3_ORIVX_XERR", &Pi3_ORIVX_XERR, &b_Pi3_ORIVX_XERR);
   fChain->SetBranchAddress("Pi3_ORIVX_YERR", &Pi3_ORIVX_YERR, &b_Pi3_ORIVX_YERR);
   fChain->SetBranchAddress("Pi3_ORIVX_ZERR", &Pi3_ORIVX_ZERR, &b_Pi3_ORIVX_ZERR);
   fChain->SetBranchAddress("Pi3_ORIVX_CHI2", &Pi3_ORIVX_CHI2, &b_Pi3_ORIVX_CHI2);
   fChain->SetBranchAddress("Pi3_ORIVX_NDOF", &Pi3_ORIVX_NDOF, &b_Pi3_ORIVX_NDOF);
   fChain->SetBranchAddress("Pi3_ORIVX_COV_", Pi3_ORIVX_COV_, &b_Pi3_ORIVX_COV_);
   fChain->SetBranchAddress("Pi3_P", &Pi3_P, &b_Pi3_P);
   fChain->SetBranchAddress("Pi3_PT", &Pi3_PT, &b_Pi3_PT);
   fChain->SetBranchAddress("Pi3_PE", &Pi3_PE, &b_Pi3_PE);
   fChain->SetBranchAddress("Pi3_PX", &Pi3_PX, &b_Pi3_PX);
   fChain->SetBranchAddress("Pi3_PY", &Pi3_PY, &b_Pi3_PY);
   fChain->SetBranchAddress("Pi3_PZ", &Pi3_PZ, &b_Pi3_PZ);
   fChain->SetBranchAddress("Pi3_M", &Pi3_M, &b_Pi3_M);
   fChain->SetBranchAddress("Pi3_ID", &Pi3_ID, &b_Pi3_ID);
   fChain->SetBranchAddress("Pi3_PIDe", &Pi3_PIDe, &b_Pi3_PIDe);
   fChain->SetBranchAddress("Pi3_PIDmu", &Pi3_PIDmu, &b_Pi3_PIDmu);
   fChain->SetBranchAddress("Pi3_PIDK", &Pi3_PIDK, &b_Pi3_PIDK);
   fChain->SetBranchAddress("Pi3_PIDp", &Pi3_PIDp, &b_Pi3_PIDp);
   fChain->SetBranchAddress("Pi3_PIDd", &Pi3_PIDd, &b_Pi3_PIDd);
   fChain->SetBranchAddress("Pi3_ProbNNe", &Pi3_ProbNNe, &b_Pi3_ProbNNe);
   fChain->SetBranchAddress("Pi3_ProbNNk", &Pi3_ProbNNk, &b_Pi3_ProbNNk);
   fChain->SetBranchAddress("Pi3_ProbNNp", &Pi3_ProbNNp, &b_Pi3_ProbNNp);
   fChain->SetBranchAddress("Pi3_ProbNNpi", &Pi3_ProbNNpi, &b_Pi3_ProbNNpi);
   fChain->SetBranchAddress("Pi3_ProbNNmu", &Pi3_ProbNNmu, &b_Pi3_ProbNNmu);
   fChain->SetBranchAddress("Pi3_ProbNNd", &Pi3_ProbNNd, &b_Pi3_ProbNNd);
   fChain->SetBranchAddress("Pi3_ProbNNghost", &Pi3_ProbNNghost, &b_Pi3_ProbNNghost);
   fChain->SetBranchAddress("Pi3_hasMuon", &Pi3_hasMuon, &b_Pi3_hasMuon);
   fChain->SetBranchAddress("Pi3_isMuon", &Pi3_isMuon, &b_Pi3_isMuon);
   fChain->SetBranchAddress("Pi3_hasRich", &Pi3_hasRich, &b_Pi3_hasRich);
   fChain->SetBranchAddress("Pi3_UsedRichAerogel", &Pi3_UsedRichAerogel, &b_Pi3_UsedRichAerogel);
   fChain->SetBranchAddress("Pi3_UsedRich1Gas", &Pi3_UsedRich1Gas, &b_Pi3_UsedRich1Gas);
   fChain->SetBranchAddress("Pi3_UsedRich2Gas", &Pi3_UsedRich2Gas, &b_Pi3_UsedRich2Gas);
   fChain->SetBranchAddress("Pi3_RichAboveElThres", &Pi3_RichAboveElThres, &b_Pi3_RichAboveElThres);
   fChain->SetBranchAddress("Pi3_RichAboveMuThres", &Pi3_RichAboveMuThres, &b_Pi3_RichAboveMuThres);
   fChain->SetBranchAddress("Pi3_RichAbovePiThres", &Pi3_RichAbovePiThres, &b_Pi3_RichAbovePiThres);
   fChain->SetBranchAddress("Pi3_RichAboveKaThres", &Pi3_RichAboveKaThres, &b_Pi3_RichAboveKaThres);
   fChain->SetBranchAddress("Pi3_RichAbovePrThres", &Pi3_RichAbovePrThres, &b_Pi3_RichAbovePrThres);
   fChain->SetBranchAddress("Pi3_hasCalo", &Pi3_hasCalo, &b_Pi3_hasCalo);
   fChain->SetBranchAddress("nCandidate", &nCandidate, &b_nCandidate);
   fChain->SetBranchAddress("totCandidates", &totCandidates, &b_totCandidates);
   fChain->SetBranchAddress("EventInSequence", &EventInSequence, &b_EventInSequence);
   fChain->SetBranchAddress("runNumber", &runNumber, &b_runNumber);
   fChain->SetBranchAddress("eventNumber", &eventNumber, &b_eventNumber);
   fChain->SetBranchAddress("BCID", &BCID, &b_BCID);
   fChain->SetBranchAddress("BCType", &BCType, &b_BCType);
   fChain->SetBranchAddress("OdinTCK", &OdinTCK, &b_OdinTCK);
   fChain->SetBranchAddress("L0DUTCK", &L0DUTCK, &b_L0DUTCK);
   fChain->SetBranchAddress("HLT1TCK", &HLT1TCK, &b_HLT1TCK);
   fChain->SetBranchAddress("HLT2TCK", &HLT2TCK, &b_HLT2TCK);
   fChain->SetBranchAddress("GpsTime", &GpsTime, &b_GpsTime);
   fChain->SetBranchAddress("Polarity", &Polarity, &b_Polarity);
   fChain->SetBranchAddress("nPV", &nPV, &b_nPV);
   fChain->SetBranchAddress("PVX", PVX, &b_PVX);
   fChain->SetBranchAddress("PVY", PVY, &b_PVY);
   fChain->SetBranchAddress("PVZ", PVZ, &b_PVZ);
   fChain->SetBranchAddress("PVXERR", PVXERR, &b_PVXERR);
   fChain->SetBranchAddress("PVYERR", PVYERR, &b_PVYERR);
   fChain->SetBranchAddress("PVZERR", PVZERR, &b_PVZERR);
   fChain->SetBranchAddress("PVCHI2", PVCHI2, &b_PVCHI2);
   fChain->SetBranchAddress("PVNDOF", PVNDOF, &b_PVNDOF);
   fChain->SetBranchAddress("PVNTRACKS", PVNTRACKS, &b_PVNTRACKS);
   fChain->SetBranchAddress("nPVs", &nPVs, &b_nPVs);
   fChain->SetBranchAddress("nTracks", &nTracks, &b_nTracks);
   fChain->SetBranchAddress("nLongTracks", &nLongTracks, &b_nLongTracks);
   fChain->SetBranchAddress("nDownstreamTracks", &nDownstreamTracks, &b_nDownstreamTracks);
   fChain->SetBranchAddress("nUpstreamTracks", &nUpstreamTracks, &b_nUpstreamTracks);
   fChain->SetBranchAddress("nVeloTracks", &nVeloTracks, &b_nVeloTracks);
   fChain->SetBranchAddress("nTTracks", &nTTracks, &b_nTTracks);
   fChain->SetBranchAddress("nBackTracks", &nBackTracks, &b_nBackTracks);
   fChain->SetBranchAddress("nRich1Hits", &nRich1Hits, &b_nRich1Hits);
   fChain->SetBranchAddress("nRich2Hits", &nRich2Hits, &b_nRich2Hits);
   fChain->SetBranchAddress("nVeloClusters", &nVeloClusters, &b_nVeloClusters);
   fChain->SetBranchAddress("nITClusters", &nITClusters, &b_nITClusters);
   fChain->SetBranchAddress("nTTClusters", &nTTClusters, &b_nTTClusters);
   fChain->SetBranchAddress("nOTClusters", &nOTClusters, &b_nOTClusters);
   fChain->SetBranchAddress("nSPDHits", &nSPDHits, &b_nSPDHits);
   fChain->SetBranchAddress("nMuonCoordsS0", &nMuonCoordsS0, &b_nMuonCoordsS0);
   fChain->SetBranchAddress("nMuonCoordsS1", &nMuonCoordsS1, &b_nMuonCoordsS1);
   fChain->SetBranchAddress("nMuonCoordsS2", &nMuonCoordsS2, &b_nMuonCoordsS2);
   fChain->SetBranchAddress("nMuonCoordsS3", &nMuonCoordsS3, &b_nMuonCoordsS3);
   fChain->SetBranchAddress("nMuonCoordsS4", &nMuonCoordsS4, &b_nMuonCoordsS4);
   fChain->SetBranchAddress("nMuonTracks", &nMuonTracks, &b_nMuonTracks);
   Notify();
}

Bool_t MEntries::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void MEntries::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t MEntries::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef MEntries_cxx
