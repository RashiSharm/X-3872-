Pre-analysis: Containts two classes. Once all the root files are recieved from ganga, MEntries.C/h ensures the removal of Multiple Entries across the data set. Command for running: root -l MEntries.C ; MEntries k ; k.Loop(). Output file is called SEntries.root
              The Second class SubReso.C/h generates and adds new branches, using Sentries.root as the input and the output is called subreso.root. Note that J/psi reflection removal hasn't been performed here.

sideband_analysis_R : This file is the complete analysis, where signal, background and B sideband analysis is done all in 1. The _R stands for the simultaneous sideband fitting done as opposed to Upper and Lower sideband which was done for comparision .Run it in lhcbdev as lb-py sideband_analysis_R.             

All the other .C files are used by fitting.

.gitignore : forces git to ignore all the * file types listed in it. Currently .pdf and .root are ignored.
