%module(package="pynusmv.nusmv.sexp") sexp

%{
#include "../../../nusmv/nusmv-config.h"
#include "../../../nusmv/src/utils/defs.h"
#include "../../../nusmv/src/sexp/SexpInliner.h" 
%}

%feature("autodoc", 1);

%include ../../../nusmv/src/utils/defs.h
%include ../../../nusmv/src/sexp/SexpInliner.h