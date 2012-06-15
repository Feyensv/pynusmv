%module(package="pynusmv.nusmv.compile.type_checking") type_checking

%{
#include "../../../../nusmv/nusmv-config.h"
#include "../../../../nusmv/src/utils/defs.h"
#include "../../../../nusmv/src/compile/type_checking/TypeChecker.h" 
%}

%feature("autodoc", 1);

%include ../../../../nusmv/src/utils/defs.h
%include ../../../../nusmv/src/compile/type_checking/TypeChecker.h