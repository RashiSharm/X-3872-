#include <TH2.h>

double sumH(TH1 * h, double xmin, double xmax){
  double s=0.0;
  if( !h )return s;
  int n = h->GetNbinsX();
  for(int i=1; i<=n; ++i){
    double x = h->GetBinCenter(i);
    if( x<xmin )continue;
    if( x>xmax )break;
    s += h->GetBinContent(i);
  }
  return s;
}
   
