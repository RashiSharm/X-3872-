import os
from Gaudi.Configuration import *
#from Configurables import DaVinci, CondDB                                                                                     
from Configurables import CombineParticles, CondDB, DaVinci, DecayTreeTuple, FilterDesktop, GaudiSequencer, LoKi__Hybrid__TupleTool, TriggerTisTos, Hlt1TriggerTisTos, Hlt2TriggerTisTos
from Configurables import MCDecayTreeTuple, OfflineVertexFitter, TupleToolDecayTreeFitter, TupleToolDecay, TupleToolTISTOS, TupleToolTrigger
from PhysSelPython.Wrappers import AutomaticData, DataOnDemand, Selection, MergedSelection, SelectionSequence
from DecayTreeTuple.Configuration import *
from GaudiConf import IOHelper

# this file is for B to XKPIPI or K 4Pi 2Mu system
  
location = '/Event/AllStreams/Phys/FullDSTDiMuonJpsi2MuMuDetachedLine/Particles'
#location = '/Event/Dimuon/Phys/FullDSTDiMuonJpsi2MuMuDetachedLine/Particles'
#  gaudi sequence 1 on JPsi                                                                                    
Jpsi2MuMu = AutomaticData(Location = location)

_FilterJpsi = FilterDesktop("_FilterJpsi")
_FilterJpsi.Code = "(MINTREE('mu+'==ABSID, PIDmu) > 0.0)" \
                  "& (VFASPF(VCHI2PDOF) < 9.0)" \
                  "& (PT>1500*MeV)"\
                  "& (MM>3040*MeV) & (MM<3140*MeV) "\
                  "& (~INTREE(('mu+'==ABSID)&(THASINFO(LHCb.Track.CloneDist))))"\
                  "& (MAXTREE('mu+'==ABSID, TRCHI2DOF) < 4.0)"

                                                                                                               

FilterJpsi = Selection( "FilterJpsi",
                      Algorithm          = _FilterJpsi ,
                      RequiredSelections = [ Jpsi2MuMu ] )


# calling new particles from the .DST file                                                                     
kaons = DataOnDemand(Location = "/Event/Phys/StdAllLooseKaons/Particles")
pions = DataOnDemand(Location = "/Event/Phys/StdAllLoosePions/Particles")

# adding pion and JPsi to form X(3872)                                                                                             
_B2JPsiPipPim = CombineParticles( "_B2JPsiPipPim",
                                  DecayDescriptor = "X_1(3872) -> J/psi(1S)  pi- pi+",
                                  MotherCut       = "(VFASPF(VCHI2/VDOF)<9) & (MM<4100*MeV)",
                                  DaughtersCuts   = {"pi+": "(TRCHI2DOF<4) & (MIPCHI2DV(PRIMARY)>9) & (~THASINFO(LHCb.Track.CloneDist)) & (PIDK<5) & (TRGHOSTPROB<0.47)" },
                                 )

B2JPsiPipPim  = Selection( "B2JPsiPipPim",
                      Algorithm          = _B2JPsiPipPim ,
                           RequiredSelections = [ FilterJpsi , pions] )

# adding X(3872) to Pi- and K+ to form B0

_B2XKpPimPip = CombineParticles( "_B2XKpPimPip",
                                  DecayDescriptor = "[B+ -> X_1(3872) K+ pi- pi+]cc",
                                  MotherCut       = "(VFASPF(VCHI2/VDOF)<9) & (MM>4850*MeV) & (MM<6500*MeV) & (PT>2000*MeV) & (BPVLTIME()>0.00025) & (BPVVDCHI2 > 121.0) & (BPVDIRA > 0.9999) & (BPVIPCHI2() < 16.0)",
                                  DaughtersCuts   = { "K+" : "(TRCHI2DOF<4) & (MIPCHI2DV(PRIMARY)>9) & (~THASINFO(LHCb.Track.CloneDist)) & (PIDK>0) & (TRGHOSTPROB<0.47)",
                                                      "pi+": "(TRCHI2DOF<4) & (MIPCHI2DV(PRIMARY)>9) & (~THASINFO(LHCb.Track.CloneDist)) & (PIDK<5) & (TRGHOSTPROB<0.47)"} ,
                            )                        


B2XKpPimPip  = Selection( "B2XKpPimPip",
                      Algorithm          = _B2XKpPimPip ,
                           RequiredSelections = [ B2JPsiPipPim , pions, kaons] )


SeqB2XKpPimPip = SelectionSequence("SeqB2XKpPimPip", TopSelection = B2XKpPimPip)
seq = SeqB2XKpPimPip.sequence()



nTuple = DecayTreeTuple('Bp2XK4Pi')
nTuple.TupleName = 'nTuple'
nTuple.Inputs = [SeqB2XKpPimPip.outputLocation()]
nTuple.Decay  = '[B+ --> ^(X_1(3872) -> ^(J/psi(1S) -> ^mu+ ^mu-) ^pi+ ^pi-) ^K+ ^pi- ^pi+ ]CC'
nTuple.addBranches({
    'Bp'       : '^([B+ --> (X_1(3872) -> (J/psi(1S) -> mu+ mu-) pi+ pi-) K+ pi- pi+ ]CC)',
    'X'        : '[B+ --> ^(X_1(3872) -> (J/psi(1S) -> mu+ mu-) pi+ pi-) K+ pi- pi+ ]CC',
    'Jpsi'     : '[B+ --> (X_1(3872) -> ^(J/psi(1S) -> mu+ mu-) pi+ pi-) K+ pi- pi+ ]CC',
    'Mu0'      : '[B+ --> (X_1(3872) -> (J/psi(1S) -> ^mu+ mu-) pi+ pi-) K+ pi- pi+ ]CC',
    'Mu1'      : '[B+ --> (X_1(3872) -> (J/psi(1S) -> mu+ ^mu-) pi+ pi-) K+ pi- pi+ ]CC',
    'Pi0'       : '[B+ --> (X_1(3872) -> (J/psi(1S) -> mu+ mu-) ^pi+ pi-) K+ pi- pi+ ]CC',
    'Pi1'       : '[B+ --> (X_1(3872) -> (J/psi(1S) -> mu+ mu-) pi+ ^pi-) K+ pi- pi+ ]CC',
    'Pi2'       : '[B+ --> (X_1(3872) -> (J/psi(1S) -> mu+ mu-) pi+ pi-) K+ ^pi- pi+ ]CC',
    'Pi3'       : '[B+ --> (X_1(3872) -> (J/psi(1S) -> mu+ mu-) pi+ pi-) K+ pi- ^pi+ ]CC',
    'K'       : '[B+ --> (X_1(3872) -> (J/psi(1S) -> mu+ mu-) pi+ pi-) ^K+ pi- pi+ ]CC'
    })


# ToolLists
nTuple.ToolList =   [
    "TupleToolEventInfo", #run no., event no., B polarity, etc.                                                                
    "TupleToolPrimaries",
#    "TupleToolGeometry", #vertex info, etc.                                                                                   
#    "TupleToolKinematic", #momenta and mass, etc.                                                                             
    "TupleToolRecoStats"
]

nTuple.Bp.ToolList =  [
#    "TupleToolAngles",                                                                                                        
#    "TupleToolGeometry" #vertex info, etc.                                                                                    
    "TupleToolTISTOS",
#    "TupleToolTrackInfo", #GhostProb, CloneDist, Track type, etc.                                                             
    "TupleToolPropertime","TupleToolKinematic",
    "TupleToolGeometry" #vertex info, etc.                                                                                     
]

nTuple.Jpsi.ToolList = [
   "TupleToolKinematic"
]

nTuple.Mu0.ToolList = [
    "TupleToolPid","TupleToolKinematic",
    "TupleToolGeometry" #vertex info, etc.                                                                                     
]

nTuple.Mu1.ToolList = [
    "TupleToolPid","TupleToolKinematic",
    "TupleToolGeometry" #vertex info, etc.                                                                                     
]

nTuple.Pi0.ToolList = [
    "TupleToolPid","TupleToolKinematic","TupleToolGeometry"
]

nTuple.Pi1.ToolList = [
    "TupleToolPid","TupleToolKinematic",
    "TupleToolGeometry" #vertex info, etc.
]

nTuple.Pi2.ToolList = [
    "TupleToolPid","TupleToolKinematic","TupleToolGeometry"
]

nTuple.Pi3.ToolList = [
    "TupleToolPid","TupleToolKinematic","TupleToolGeometry"
]

nTuple.K.ToolList = [
    "TupleToolPid","TupleToolKinematic",
    "TupleToolGeometry" #vertex info, etc.                                                              
]

nTuple.X.ToolList = [
    "TupleToolKinematic"
]
nTuple.Bp.addTool(TupleToolTISTOS, name = "TupleToolTISTOS")

nTuple.Bp.TupleToolTISTOS.TriggerList = [
    "L0DiMuonDecision",
    "L0MuonDecision",
    "Hlt1DiMuonHighMassDecision",
    "Hlt1TrackMuonDecision",
    "Hlt1TrackMVADecision",
    "Hlt2DiMuonDetachedJPsiDecision"]

nTuple.Bp.TupleToolTISTOS.VerboseL0 = True
nTuple.Bp.TupleToolTISTOS.VerboseHlt1 = True
nTuple.Bp.TupleToolTISTOS.VerboseHlt2 = True
nTuple.Bp.TupleToolTISTOS.addTool(TriggerTisTos());
nTuple.Bp.TupleToolTISTOS.TriggerTisTos.TOSFracMuon = 0
nTuple.Bp.TupleToolTISTOS.TriggerTisTos.TOSFracEcal = 0
nTuple.Bp.TupleToolTISTOS.TriggerTisTos.TOSFracHcal = 0
nTuple.Bp.TupleToolTISTOS.addTool(Hlt1TriggerTisTos());
nTuple.Bp.TupleToolTISTOS.Hlt1TriggerTisTos.TOSFracMuon = 0
nTuple.Bp.TupleToolTISTOS.Hlt1TriggerTisTos.TOSFracEcal = 0
nTuple.Bp.TupleToolTISTOS.Hlt1TriggerTisTos.TOSFracHcal = 0
nTuple.Bp.TupleToolTISTOS.addTool(Hlt2TriggerTisTos());
nTuple.Bp.TupleToolTISTOS.Hlt2TriggerTisTos.TOSFracMuon = 0
nTuple.Bp.TupleToolTISTOS.Hlt2TriggerTisTos.TOSFracEcal = 0
nTuple.Bp.TupleToolTISTOS.Hlt2TriggerTisTos.TOSFracHcal = 0
nTuple.Bp.TupleToolTISTOS.TriggerTisTos.PropertiesPrint = True
nTuple.Bp.TupleToolTISTOS.Hlt1TriggerTisTos.PropertiesPrint = True
nTuple.Bp.TupleToolTISTOS.Hlt2TriggerTisTos.PropertiesPrint = True

consJpsipipipiK = nTuple.Bp.addTupleTool('LoKi::Hybrid::TupleTool/Cons_JpsipipipiK')
consJpsipipipiK.Preambulo = [ 
    "Mu0  = '[B+ --> (X_1(3872) -> (J/psi(1S) -> ^mu+ mu-) pi+ pi-) K+ pi- pi+ ]CC'",
    "Mu1  = '[B+ --> (X_1(3872) -> (J/psi(1S) -> mu+ ^mu-) pi+ pi-) K+ pi- pi+ ]CC'",
    "Jpsi = '[B+ --> (X_1(3872) -> ^(J/psi(1S) -> mu+ mu-) pi+ pi-) K+ pi- pi+ ]CC'",
    "Pi0  = '[B+ --> (X_1(3872) -> (J/psi(1S) -> mu+ mu-) ^pi+ pi-) K+ pi- pi+ ]CC'",
    "Pi1  = '[B+ --> (X_1(3872) -> (J/psi(1S) -> mu+ mu-) pi+ ^pi-) K+ pi- pi+ ]CC'",
    "Pi2  = '[B+ --> (X_1(3872) -> (J/psi(1S) -> mu+ mu-) pi+ pi-) K+ ^pi- pi+ ]CC'",
    "Pi3  = '[B+ --> (X_1(3872) -> (J/psi(1S) -> mu+ mu-) pi+ pi-) K+ pi- ^pi+ ]CC'",
    "K    = '[B+ --> (X_1(3872) -> (J/psi(1S) -> mu+ mu-) pi+ pi-) ^K+ pi- pi+ ]CC'",
    "X    = '[B+ --> ^(X_1(3872) -> (J/psi(1S) -> mu+ mu-) pi+ pi-) K+ pi- pi+ ]CC'",
#######   Mu0, Mu1 momentum   ########                                                                  
    "px_mu0 = CHILD(Mu0,PX)",
    "py_mu0 = CHILD(Mu0,PY)",
    "pz_mu0 = CHILD(Mu0,PZ)",
                                                               
    "px_mu1 = CHILD(Mu1,PX)",
    "py_mu1 = CHILD(Mu1,PY)",
    "pz_mu1 = CHILD(Mu1,PZ)",

#######  Pi0, Pi1, Pi2  momentum  #########                                                              
    "px_pi0 = CHILD(Pi0,PX)",
    "py_pi0 = CHILD(Pi0,PY)",
    "pz_pi0 = CHILD(Pi0,PZ)",

    "px_pi1 = CHILD(Pi1,PX)",
    "py_pi1 = CHILD(Pi1,PY)",
    "pz_pi1 = CHILD(Pi1,PZ)",
    
    "px_pi2 = CHILD(Pi2,PX)",
    "py_pi2 = CHILD(Pi2,PY)",
    "pz_pi2 = CHILD(Pi2,PZ)",

    "px_pi3 = CHILD(Pi3,PX)",
    "py_pi3 = CHILD(Pi3,PY)",
    "pz_pi3 = CHILD(Pi3,PZ)",

#######  kaon momentum  #########  
    "px_k = CHILD(K,PX)",
    "py_k = CHILD(K,PY)",
    "pz_k = CHILD(K,PZ)",

####### X mass #######                                                                            
    "x_m = CHILD(X,M)"]


consJpsipipipiK.Variables = {
#                   PV + J/psi Mass constraints ======================                                                               

#-----  X variables -------                                                                                                          
'Jpsi_X_M'      : "DTF_FUN(x_m,True,'J/psi(1S)')",
#-----  B variables -------                      

'Jpsi_B_M'      : "DTF_FUN(M,True,'J/psi(1S)')",
'Jpsi_B_ctau'   : "DTF_CTAU(0,True,strings(['J/psi(1S)']))",

#                   B + PV + J/psi Mass constraints ======================                                                                                                                  
'B_Chi2NDoF' : "DTF_CHI2NDOF(True,strings(['J/psi(1S)','B+']))",
'Jpsi_Chi2NDoF' : "DTF_CHI2NDOF(True,strings(['J/psi(1S)']))",
#                                                                                                                                                                                            
'B_mu0_px' : "DTF_FUN(px_mu0,True,strings(['J/psi(1S)','B+']))",
'B_mu0_py' : "DTF_FUN(py_mu0,True,strings(['J/psi(1S)','B+']))",
'B_mu0_pz' : "DTF_FUN(pz_mu0,True,strings(['J/psi(1S)','B+']))",
#                                                                                                                                                                                            
'B_mu1_px' : "DTF_FUN(px_mu1,True,strings(['J/psi(1S)','B+']))",
'B_mu1_py' : "DTF_FUN(py_mu1,True,strings(['J/psi(1S)','B+']))",
'B_mu1_pz' : "DTF_FUN(pz_mu1,True,strings(['J/psi(1S)','B+']))",
#                                                                                                                                                                                            
'B_pi0_px'  : "DTF_FUN(px_pi0,True,strings(['J/psi(1S)','B+']))",
'B_pi0_py'  : "DTF_FUN(py_pi0,True,strings(['J/psi(1S)','B+']))",
'B_pi0_pz'  : "DTF_FUN(pz_pi0,True,strings(['J/psi(1S)','B+']))",
#                                                                                              
'B_pi1_px'  : "DTF_FUN(px_pi1,True,strings(['J/psi(1S)','B+']))",
'B_pi1_py'  : "DTF_FUN(py_pi1,True,strings(['J/psi(1S)','B+']))",
'B_pi1_pz'  : "DTF_FUN(pz_pi1,True,strings(['J/psi(1S)','B+']))",
#                                                                                                                                                                                            
'B_pi2_px'  : "DTF_FUN(px_pi2,True,strings(['J/psi(1S)','B+']))",
'B_pi2_py'  : "DTF_FUN(py_pi2,True,strings(['J/psi(1S)','B+']))",
'B_pi2_pz'  : "DTF_FUN(pz_pi2,True,strings(['J/psi(1S)','B+']))",
#
'B_pi3_px'  : "DTF_FUN(px_pi3,True,strings(['J/psi(1S)','B+']))",
'B_pi3_py'  : "DTF_FUN(py_pi3,True,strings(['J/psi(1S)','B+']))",
'B_pi3_pz'  : "DTF_FUN(pz_pi3,True,strings(['J/psi(1S)','B+']))",

# kaon needed?                                                                                     
'B_K_px'  : "DTF_FUN(px_k,True,strings(['J/psi(1S)','B+']))",
'B_K_py'  : "DTF_FUN(py_k,True,strings(['J/psi(1S)','B+']))",
'B_K_pz'  : "DTF_FUN(pz_k,True,strings(['J/psi(1S)','B+']))",
#         
'B_X_M'    : "DTF_FUN(x_m,True,strings(['J/psi(1S)','B+']))"
}


dv = DaVinci()

dv.UserAlgorithms += [seq, nTuple]
dv.InputType = 'DST'

dv.TupleFile = 'self_4pi_MC_cc.root'
#dv.TupleFile = '2018_ntuple_B0_2_X_PiK_data_33.root'

dv.PrintFreq = 1000
dv.DataType  = '2011' #'2012' #'2015' #'2016' #'2017' #'2018'
dv.Simulation = True  #False for DATA
dv.Lumi = not dv.Simulation
dv.EvtMax = -1

# 2011
# X and cc
dv.CondDBtag = 'sim-20160614-1-vc-mu100'
dv.DDDBtag  = 'dddb-20170721-1'

# 2012
# X and cc
# dv.CondDBtag = 'sim-20160321-2-vc-mu100'
# dv.DDDBtag  = 'dddb-20170721-2'

# 2015
# X and cc
# dv.CondDBtag = 'sim-20161124-vc-mu100'
# dv.DDDBtag  = 'dddb-20170721-3'

#2016 MC
# X and cc
# dv.CondDBtag = 'sim-20170721-2-vc-mu100'
# dv.DDDBtag  = 'dddb-20170721-3'

#2017 MC
# X and cc
# dv.CondDBtag = 'sim-20190430-1-vc-mu100'
# dv.DDDBtag  = 'dddb-20170721-3'

# 2018 MC
# X and cc
# dv.CondDBtag = 'sim-20190430-vc-mu100'
# dv.DDDBtag  = 'dddb-20170721-3'


#IOHelper().inputFiles(['./00077434_00001529_1.dimuon.dst'] , clear = True)

#IOHelper().inputFiles(['./00183056_00000011_7.AllStreams.dst','./00183056_00000022_7.AllStreams.dst','./00183056_00000026_7.AllStreams.dst','./00183056_00000027_7.AllStreams.dst','./00183056_00000031_7.AllStreams.dst','./00183056_00000038_7.AllStreams.dst','./00183056_00000064_7.AllStreams.dst','./00183056_00000073_7.AllStreams.dst','./00183056_00000083_7.AllStreams.dst','./00183056_00000115_7.AllStreams.dst'], clear=True)
