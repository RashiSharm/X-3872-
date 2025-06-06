void comp()
{
    
    TFile *f1 = TFile::Open("/home/rsharm18/work/Rootfile/June_25/Kaon_excitations/hist_files/Data/Kaon_excitations_with_cc_jpsipipi.root");
    TH1D *h1= (TH1D*)f1->Get("hcc1");
    
    h1->SetLineWidth(3);
    h1->SetLineColor(2);
    
    TFile *f2 = TFile::Open("/home/rsharm18/work/Rootfile/June_25/Kaon_excitations/hist_files/cc_MC/Kaon_excitations_with_cc_jpsipipi.root");
    TH1D *h2 = (TH1D*)f2->Get("hcc1");
    h2->SetLineWidth(2);
    h2->SetLineColor(4);
    h2->Draw();
    h1->Draw("SAME");

    h2->SaveAs("trail.root");
    
}