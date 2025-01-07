#include <TH1.h>
#include <TF1.h>
#include "sumH.h"
#include "TwoGaussPoly.C"

class NDoubleGFit
{
  // negative Gauss parameters means fix them, amplitude=0.0 means eliminate
  // npoly: -1 none; 0 flat; 1 linear; 2 quadratic
  // abspoly: !=0 means abs(poly)
 public:
  TF1 * fit(TH1 * h, double xmin, double xmax, double a1f, double xm1, double sig1, double a2f, double xm2f, double sig2f, int npoly, int abspoly){

    double xm2 = xm2f;
    double sig2 = sig2f;
    if( a2f == 0.0 ){
      xm2 = -fabs(xm1);
      sig2 = -fabs(sig1);
    }


    double para[6];
    para[0]=a1f;
    para[1]=xm1;
    para[2]=sig1;
    para[3]=a2f;
    para[4]=xm2;
    para[5]=sig2;

    // magic number for automatic amplitude estimator 

    double a1=a1f;
    if( a1 == 44.0 ){
      double x6s = sumH(h,fabs(xm1)-2*fabs(sig1),fabs(xm1)+2*fabs(sig1));
      double x6m = sumH(h,fabs(xm1)-6*fabs(sig1),fabs(xm1)-4*fabs(sig1));
      double x6p = sumH(h,fabs(xm1)+4*fabs(sig1),fabs(xm1)+6*fabs(sig1));
      a1 = x6s - (x6m + x6p);      
      if( a1 < 10.0 )a1 = 10.0;
    }

    double a2=a2f;
    if( a2 == 44.0 ){
      double x6s = sumH(h,fabs(xm2)-2*fabs(sig2),fabs(xm2)+2*fabs(sig2));
      double x6m = sumH(h,fabs(xm2)-6*fabs(sig2),fabs(xm2)-4*fabs(sig2));
      double x6p = sumH(h,fabs(xm2)+4*fabs(sig2),fabs(xm2)+6*fabs(sig2));
      a2 = x6s - (x6m + x6p);
      if( a2 < 10.0 )a2 = 10.0;
    }

    double binWidth = h->GetBinCenter(2)-h->GetBinCenter(1);

    TwoGaussPoly * fFun = new TwoGaussPoly();
    TF1 * fitfun = new TF1("fitfun",fFun,xmin,xmax,11,"TwoGaussPoly");
    
    fitfun->FixParameter(9,binWidth);
    fitfun->FixParameter(10,abspoly);

    fitfun->SetParameter(0,fabs(a1));
    fitfun->SetParameter(1,fabs(xm1));
    fitfun->SetParameter(2,fabs(sig1));

    fitfun->SetParameter(3,fabs(a2));
    fitfun->SetParameter(4,fabs(xm2));
    fitfun->SetParameter(5,fabs(sig2));

    if( npoly > -1 ){
      double x6m = sumH(h,fabs(xm1)-6*fabs(sig1),fabs(xm1)-4*fabs(sig1));
      double x6p = sumH(h,fabs(xm1)+4*fabs(sig1),fabs(xm1)+6*fabs(sig1));
      double xv = (x6p+x6m)*0.5;
      double fact = binWidth / (2*fabs(sig1));
      if( xv == 0.0 ){xv = 1.0; }
      fitfun->SetParameter(6, xv*fact );
      fitfun->SetParError(6, sqrt(xv)*fact );    
      if( npoly > 0 ){
	fitfun->SetParameter(7, (x6p-x6m)/(10*fabs(sig1))*fact );
	xv = sqrt(x6p+x6m)/(10*fabs(sig1))*fact;
	if( xv == 0.0 ){xv = 0.1;}
	fitfun->SetParError(7, xv );
 	if( npoly > 1 ){ 
	  fitfun->SetParameter(8, 0.);
	  fitfun->SetParError(8, xv/10.);
	} else {
	  fitfun->FixParameter(8, 0.);
	}
      } else {
	fitfun->FixParameter(7, 0.);
	fitfun->FixParameter(8, 0.);
      }
    } else {
      fitfun->FixParameter(6, 0.);
      fitfun->FixParameter(7, 0.);
      fitfun->FixParameter(8, 0.);
    }

    for(int i=0;i<6;++i){      
      fitfun->FixParameter(i,fitfun->GetParameter(i));      
    }
    fitfun->SetRange(xmin,xmax);


    if( npoly>-1 ){
      h->Fit("fitfun","LL","",xmin,xmax);
    }

    for(int i=0;i<3;++i){
      if( para[i]>0.0 ){ 
	fitfun->ReleaseParameter(i);
	fitfun->SetParError(i,fitfun->GetParameter(i)*0.1);
      }
    }

    //    if( para[3] != 0.0 ){
    //  h->Fit("fitfun","LL","",xmin,xmax);
    //    }

    for(int i=3;i<6;++i){
      if( para[i]>0.0 ){ 
	fitfun->ReleaseParameter(i);
	fitfun->SetParError(i,fitfun->GetParameter(i)*0.1);
      }
    }

    h->Fit("fitfun","LL","",xmin,xmax);
    TF1 * fitres = h->GetFunction("fitfun");
    /*
    double a0 = fitres->GetParameter(6);
    double a1 = fitres->GetParameter(7);
    double a2 = fitres->GetParameter(8);
    double x0 = fitres->GetParameter(4) - fitres->GetParameter(1); 
    return (a0+a1*x0+a2*x0*x0);
    //return (fitres->GetParameter(0));
    */
    return fitres;
  } 
  TF1 * fit(TH1 * h, double xmin, double xmax, double a1, double xm1, double sig1, double a2, double xm2f, double sig2f, int npoly){
    return fit(h,xmin,xmax,a1,xm1,sig1,a2,xm2f,sig2f,npoly,0);
  }
  TF1 * fit(TH1 * h, double xmin, double xmax, double a1, double xm1, double sig1, double a2, double xm2f, double sig2f){
    return fit(h,xmin,xmax,a1,xm1,sig1,a2,xm2f,sig2f,2,0);
  }
  TF1 * fit(TH1 * h, double xmin, double xmax, double a1, double xm1, double sig1){
    return fit(h,xmin,xmax,a1,xm1,sig1,0.0,0.0,0.0);
  }
  TF1 * fit(TH1 * h, double xmin, double xmax, double a1, double xm1, double sig1,int npoly){
    return fit(h,xmin,xmax,a1,xm1,sig1,0.0,0.0,0.0,npoly);
  }
  TF1 * fit(TH1 * h, double xmin, double xmax, double a1, double xm1, double sig1,int npoly, int abspoly){
    return fit(h,xmin,xmax,a1,xm1,sig1,0.0,0.0,0.0,npoly, abspoly);
  }
};
