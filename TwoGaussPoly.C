class TwoGaussPoly {
  // TwoGaussians and quadratic polynomial  
 public:
  Double_t operator()(Double_t *v, Double_t *par){
    Double_t binWidth = 1.0;
   if( par[9]>0.0 )binWidth=par[9];
    Double_t y=v[0]-par[1];
    Double_t arg = 0.0;
    Double_t x2=0.00001; 
    if( par[2] != 0 ) {arg =y/par[2]; x2=par[2];}
    Double_t fitval = par[0]*binWidth*exp(-0.5*arg*arg)/(2.506628*x2);  
    Double_t y2=v[0]-par[4];
    Double_t arg2 = 0.0;
    Double_t x22=0.00001; 
    if( par[5] != 0 ) {arg2 =y2/par[5]; x22=par[5];}
    fitval += par[3]*binWidth*exp(-0.5*arg2*arg2)/(2.506628*x22);  
    if( par[10] == 0.0 ){
      fitval += par[6] + par[7]*y + par[8]*y*y;     
    } else {
      fitval += fabs(par[6] + par[7]*y + par[8]*y*y);     
    }
    return fitval;
  }
};
//  GaussPoly * fGP = new GaussPoly()
//  TF1  * bkg = new TF1("bkg",fGP,3600.,3900.,9,"TwuGaussPoly")
