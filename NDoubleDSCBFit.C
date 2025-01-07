#include <TH1.h>
#include <TF1.h>
#include "sumH.h"
#include <iostream>
#include <TMath.h>
#include <time.h>       /* time_t, struct tm, time, localtime, strftime */
#include <string>       // std::string_name
#include <sstream>      // std::ostringstream
#include "TwoDSCBPoly.C"

class NDoubleDSCBFit
{
  // negative Gauss parameters means fix them, amplitude=0.0 means eliminate
  // npoly: -1 none; 0 flat; 1 linear; 2 quadratic
  // abspoly: !=0 means abs(poly)
 public:

  string method;
  TF1 * fitfun;
  string fitfun_name;

  NDoubleDSCBFit(string _method="LL"){ method=_method; }

  TF1 * fit(TH1 * h, double xmin, double xmax, 
	    double a1f, double xm1, double sig1, 
	    double nL, double alphaL, double nRf, double alphaRf, 
	    double a2f, double xm2f, double sig2f, 
	    int npoly, int abspoly){


    
    double xm2 = xm2f;
    double sig2 = sig2f;
    if( a2f == 0.0 ){
      xm2 = -fabs(xm1);
      sig2 = -fabs(sig1);
    }

    double nR=nRf;
    //    if( nR==0.0 )nR=nL;

    double alphaR=alphaRf;
    //     if( alphaR==0.0 )alphaR=alphaL;


    double para[16];
    para[0]=a1f;
    para[1]=xm1;
    para[2]=sig1;

    para[3]= nL;
    para[4]= alphaL;
    para[5]= nR;
    para[6]= alphaR;

    para[7]=a2f;
    para[8]=xm2;
    para[9]=sig2;

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


    time_t rawtime;
    struct tm * timeinfo;
    time (&rawtime);
    timeinfo = localtime (&rawtime);
    std::ostringstream oss;
    oss << "fitfun_" << timeinfo->tm_zone << "_" << 1900+timeinfo->tm_year << "_" << 1+timeinfo->tm_mon << "_" << timeinfo->tm_mday << "_" << timeinfo->tm_hour << "_" << timeinfo->tm_min << "_" << timeinfo->tm_sec;
    fitfun_name = oss.str();
    TwoDSCBPoly * fFun = new TwoDSCBPoly();
    //    TF1 * fitfun = new TF1("fitfun",fFun,xmin,xmax,16,"TwoDSCBPoly");
    fitfun = new TF1(fitfun_name.c_str(),fFun,xmin,xmax,16); 
    fitfun->SetNpx(1000); // default is 100; help plotting it with accuracy

    
    fitfun->FixParameter(15,binWidth);
    fitfun->FixParameter(14,abspoly);

    fitfun->SetParameter(0,fabs(a1));
    fitfun->SetParameter(1,fabs(xm1));
    fitfun->SetParameter(2,fabs(sig1));

    fitfun->SetParameter(3,fabs(nL));
    fitfun->SetParameter(4,fabs(alphaL));
    fitfun->SetParameter(5,fabs(nR));
    fitfun->SetParameter(6,fabs(alphaR));

    fitfun->SetParameter(7,fabs(a2));
    fitfun->SetParameter(8,fabs(xm2));
    fitfun->SetParameter(9,fabs(sig2));

    if( npoly > -1 ){
      double x6m = sumH(h,fabs(xm1)-6*fabs(sig1),fabs(xm1)-4*fabs(sig1));
      double x6p = sumH(h,fabs(xm1)+4*fabs(sig1),fabs(xm1)+6*fabs(sig1));
      double xv = (x6p+x6m)*0.5;
      double fact = binWidth / (2*fabs(sig1));
      if( xv == 0.0 ){xv = 1.0; }
      fitfun->SetParameter(10, xv*fact );
      fitfun->SetParError(10, sqrt(xv)*fact );    
      if( npoly > 0 ){
	fitfun->SetParameter(11, (x6p-x6m)/(10*fabs(sig1))*fact );
	xv = sqrt(x6p+x6m)/(10*fabs(sig1))*fact;
	if( xv == 0.0 ){xv = 0.1;}
	fitfun->SetParError(11, xv );
 	if( npoly > 1 ){ 
	  fitfun->SetParameter(12, 0.);
	  fitfun->SetParError(12, xv/10.);
	  if( npoly > 2 ){ 
	    fitfun->SetParameter(13, 0.);
	    fitfun->SetParError(13, xv/100.);
	  } else {
	    fitfun->FixParameter(13, 0.);
	  }
	} else {
	  fitfun->FixParameter(12, 0.);
	  fitfun->FixParameter(13, 0.);
	}
      } else {
	fitfun->FixParameter(11, 0.);
	fitfun->FixParameter(12, 0.);
	fitfun->FixParameter(13, 0.);
      }
    } else {
      fitfun->FixParameter(10, 0.);
      fitfun->FixParameter(11, 0.);
      fitfun->FixParameter(12, 0.);
      fitfun->FixParameter(13, 0.);
    }

    for(int i=0;i<10;++i){      
      fitfun->FixParameter(i,fitfun->GetParameter(i));      
    }
    fitfun->SetRange(xmin,xmax);


    if( npoly>-1 ){
      h->Fit(fitfun_name.c_str(),method.c_str(),"",xmin,xmax);
    }

    for(int i=0;i<3;++i){
      if( para[i]>0.0 ){ 
	fitfun->ReleaseParameter(i);
	fitfun->SetParError(i,fitfun->GetParameter(i)*0.1);
      }
    }

    //    if( para[3] != 0.0 ){
    //  h->Fit(fitfun_name.c_str(),method.c_str(),"",xmin,xmax);
    //    }

    for(int i=7;i<10;++i){
      if( para[i]>0.0 ){ 
	fitfun->ReleaseParameter(i);
	fitfun->SetParError(i,fitfun->GetParameter(i)*0.1);
      }
    }

    h->Fit(fitfun_name.c_str(),method.c_str(),"",xmin,xmax);


    bool doit(false);
    for(int i=3;i<7;++i){
      if( para[i]>0.0 ){ 
	fitfun->ReleaseParameter(i);
	fitfun->SetParError(i,fitfun->GetParameter(i)*0.1);
	doit=true;
      }
    }

    if(doit)h->Fit(fitfun_name.c_str(),method.c_str(),"",xmin,xmax);


    TF1 * fitres = h->GetFunction(fitfun_name.c_str());
    /*
    double a0 = fitres->GetParameter(6);
    double a1 = fitres->GetParameter(7);
    double a2 = fitres->GetParameter(8);
    double x0 = fitres->GetParameter(4) - fitres->GetParameter(1); 
    return (a0+a1*x0+a2*x0*x0);
    //return (fitres->GetParameter(0));
    */
      for(int ires=0; ires<14; ires +=7 ){
	if( fitres->GetParError(ires) > 0.0 ){
	  if( fitres->GetParameter(ires) != 0.0 ){
	    std::cout << " signal component " << ires/7 << " naive signifiance " << fitres->GetParameter(ires)/fitres->GetParError(ires) << std::endl;
	  }
	}
      }
    std::cout << " Fit with method=" << method.c_str() << std::endl;
      std::cout << " Bins " << fitres->GetNumberFitPoints() 
		<< " Fit parameters " << fitres->GetNumberFreeParameters()
		<< " chi2 " << fitres->GetChisquare() 
		<< " NDF " << fitres->GetNDF();
      if( fitres->GetNDF() ){
	std::cout << " chi2/NDF " << fitres->GetChisquare()/fitres->GetNDF();
      }
      std::cout << " Probability (%) " << fitres->GetProb()*100 << std::endl; 

    return fitres;
  } 


  TF1 * refit(TH1 * h, double xmin, double xmax){
    fitfun->FixParameter(15,h->GetBinCenter(2)-h->GetBinCenter(1));
    h->Fit(fitfun_name.c_str(),method.c_str(),"",xmin,xmax);
    TF1 * fitres = h->GetFunction(fitfun_name.c_str());
    ////    print();
      for(int ires=0; ires<14; ires +=7 ){
	if( fitres->GetParError(ires) > 0.0 ){
	  if( fitres->GetParameter(ires) != 0.0 ){
	    std::cout << " signal component " << ires/5 << " naive signifiance " << fitres->GetParameter(ires)/fitres->GetParError(ires) << std::endl;
	  }
	}
      }
    std::cout << " Fit with method=" << method.c_str() << std::endl; 
    std::cout << " Bins " << fitres->GetNumberFitPoints()  
		<< " Fit parameters " << fitres->GetNumberFreeParameters()
		<< " chi2 " << fitres->GetChisquare() 
		<< " NDF " << fitres->GetNDF();
    if( fitres->GetNDF() ){
      std::cout << " chi2/NDF " << fitres->GetChisquare()/fitres->GetNDF();
    }
    std::cout << " Probability (%) " << fitres->GetProb()*100 << std::endl; 
    return fitres;
  }

  TF1 * refit(TH1 * h){
    fitfun->FixParameter(15,h->GetBinCenter(2)-h->GetBinCenter(1));
    h->Fit(fitfun_name.c_str(),method.c_str(),"",fitfun->GetXmin(),fitfun->GetXmax());
    //    print();
    TF1 * fitres = h->GetFunction(fitfun_name.c_str());
      for(int ires=0; ires<14; ires +=7 ){
	if( fitres->GetParError(ires) > 0.0 ){
	  if( fitres->GetParameter(ires) != 0.0 ){
	    std::cout << " signal component " << ires/7 << " naive signifiance " << fitres->GetParameter(ires)/fitres->GetParError(ires) << std::endl;
	  }
	}
      }
    std::cout << " Fit with method=" << method.c_str() << std::endl;
      std::cout << " Bins " << fitres->GetNumberFitPoints() 
		<< " Fit parameters " << fitres->GetNumberFreeParameters()
		<< " chi2 " << fitres->GetChisquare() 
		<< " NDF " << fitres->GetNDF();
      if( fitres->GetNDF() ){
	std::cout << " chi2/NDF " << fitres->GetChisquare()/fitres->GetNDF();
      }
      std::cout << " Probability (%) " << fitres->GetProb()*100 << std::endl; 
    return fitres;
  }


  TF1 * fit(TH1 * h, double xmin, double xmax, double a1, double xm1, double sig1, 	    
	    double nL, double alphaL, double nR, double alphaR, 
	    double a2, double xm2f, double sig2f, int npoly){
    return fit(h,xmin,xmax,a1,xm1,sig1,nL,alphaL,nR,alphaR,a2,xm2f,sig2f,npoly,0);
  }
  TF1 * fit(TH1 * h, double xmin, double xmax, double a1, double xm1, double sig1, 	    
	    double nL, double alphaL, double nR, double alphaR, 
	    double a2, double xm2f, double sig2f){
    return fit(h,xmin,xmax,a1,xm1,sig1,nL,alphaL,nR,alphaR,a2,xm2f,sig2f,2,0);
  }
  TF1 * fit(TH1 * h, double xmin, double xmax, double a1, double xm1, double sig1, 	    
	    double nL, double alphaL, double nR, double alphaR){ 
    return fit(h,xmin,xmax,a1,xm1,sig1,nL,alphaL,nR,alphaR,0.0,0.0,0.0,2,0);
  }
  TF1 * fit(TH1 * h, double xmin, double xmax, double a1, double xm1, double sig1, 	    
	    double nL, double alphaL, double nR, double alphaR, int npoly){ 
    return fit(h,xmin,xmax,a1,xm1,sig1,nL,alphaL,nR,alphaR,0.0,0.0,0.0,npoly,0);
  }
  TF1 * fit(TH1 * h, double xmin, double xmax, double a1, double xm1, double sig1, 	    
	    double nL, double alphaL, double nR, double alphaR, int npoly, int abspoly){ 
    return fit(h,xmin,xmax,a1,xm1,sig1,nL,alphaL,nR,alphaR,0.0,0.0,0.0,npoly,abspoly);
  }
};
