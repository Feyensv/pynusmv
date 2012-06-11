%module(package="pynusmv.nusmv.bmc") bmc

%{
#include "../../../nusmv/src/utils/defs.h"
#include "../../../nusmv/src/bmc/bmc.h" 
#include "../../../nusmv/src/bmc/bmcBmc.h" 
#include "../../../nusmv/src/bmc/bmcCheck.h" 
#include "../../../nusmv/src/bmc/bmcCmd.h" 
#include "../../../nusmv/src/bmc/bmcConv.h" 
#include "../../../nusmv/src/bmc/bmcDump.h" 
#include "../../../nusmv/src/bmc/bmcGen.h" 
#include "../../../nusmv/src/bmc/bmcModel.h" 
#include "../../../nusmv/src/bmc/bmcPkg.h" 
#include "../../../nusmv/src/bmc/bmcSimulate.h" 
#include "../../../nusmv/src/bmc/bmcTableau.h" 
#include "../../../nusmv/src/bmc/bmcUtils.h" 
%}

%include ../../../nusmv/src/utils/defs.h
%include ../../../nusmv/src/bmc/bmc.h
%include ../../../nusmv/src/bmc/bmcBmc.h
%include ../../../nusmv/src/bmc/bmcCheck.h
%include ../../../nusmv/src/bmc/bmcCmd.h
%include ../../../nusmv/src/bmc/bmcConv.h
%include ../../../nusmv/src/bmc/bmcDump.h
%include ../../../nusmv/src/bmc/bmcGen.h
%include ../../../nusmv/src/bmc/bmcModel.h
%include ../../../nusmv/src/bmc/bmcPkg.h
%include ../../../nusmv/src/bmc/bmcSimulate.h
%include ../../../nusmv/src/bmc/bmcTableau.h
%include ../../../nusmv/src/bmc/bmcUtils.h