%module(package="pynusmv.nusmv.enc.bdd") bdd

%{
#include "../../../../nusmv/nusmv-config.h"
#include "../../../../nusmv/src/utils/defs.h"
#include "../../../../nusmv/src/utils/object.h"
#include "../../../../nusmv/src/enc/bdd/bdd.h" 
#include "../../../../nusmv/src/enc/bdd/BddEnc.h" 
#include "../../../../nusmv/src/enc/bdd/BddEncCache.h" 
%}

%feature("autodoc", 1);

%include ../../../../nusmv/src/utils/defs.h
%include ../../../../nusmv/src/utils/object.h
%include ../../../../nusmv/src/enc/bdd/bdd.h
%include ../../../../nusmv/src/enc/bdd/BddEnc.h
%include ../../../../nusmv/src/enc/bdd/BddEncCache.h