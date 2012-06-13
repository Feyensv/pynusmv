# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.6
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_bool', [dirname(__file__)])
        except ImportError:
            import _bool
            return _bool
        if fp is not None:
            try:
                _mod = imp.load_module('_bool', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _bool = swig_import_helper()
    del swig_import_helper
else:
    import _bool
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


PRIuPTR = _bool.PRIuPTR
PRIdPTR = _bool.PRIdPTR
LLU = _bool.LLU
LLO = _bool.LLO
LLX = _bool.LLX
false = _bool.false
true = _bool.true
OUTCOME_GENERIC_ERROR = _bool.OUTCOME_GENERIC_ERROR
OUTCOME_PARSER_ERROR = _bool.OUTCOME_PARSER_ERROR
OUTCOME_SYNTAX_ERROR = _bool.OUTCOME_SYNTAX_ERROR
OUTCOME_FILE_ERROR = _bool.OUTCOME_FILE_ERROR
OUTCOME_SUCCESS_REQUIRED_HELP = _bool.OUTCOME_SUCCESS_REQUIRED_HELP
OUTCOME_SUCCESS = _bool.OUTCOME_SUCCESS

def Object_destroy(*args) -> "void" :
  return _bool.Object_destroy(*args)
Object_destroy = _bool.Object_destroy

def Object_copy(*args) -> "Object_ptr" :
  return _bool.Object_copy(*args)
Object_copy = _bool.Object_copy
BIT_VALUE_FALSE = _bool.BIT_VALUE_FALSE
BIT_VALUE_TRUE = _bool.BIT_VALUE_TRUE
BIT_VALUE_DONTCARE = _bool.BIT_VALUE_DONTCARE

def BitValues_create(*args) -> "BitValues_ptr" :
  return _bool.BitValues_create(*args)
BitValues_create = _bool.BitValues_create

def BitValues_destroy(*args) -> "void" :
  return _bool.BitValues_destroy(*args)
BitValues_destroy = _bool.BitValues_destroy

def BitValues_get_scalar_var(*args) -> "node_ptr" :
  return _bool.BitValues_get_scalar_var(*args)
BitValues_get_scalar_var = _bool.BitValues_get_scalar_var

def BitValues_get_size(*args) -> "size_t" :
  return _bool.BitValues_get_size(*args)
BitValues_get_size = _bool.BitValues_get_size

def BitValues_get_bits(*args) -> "NodeList_ptr" :
  return _bool.BitValues_get_bits(*args)
BitValues_get_bits = _bool.BitValues_get_bits

def BitValues_reset(*args) -> "void" :
  return _bool.BitValues_reset(*args)
BitValues_reset = _bool.BitValues_reset

def BitValues_get(*args) -> "BitValue" :
  return _bool.BitValues_get(*args)
BitValues_get = _bool.BitValues_get

def BitValues_get_value_from_expr(*args) -> "BitValue" :
  return _bool.BitValues_get_value_from_expr(*args)
BitValues_get_value_from_expr = _bool.BitValues_get_value_from_expr

def BitValues_set(*args) -> "void" :
  return _bool.BitValues_set(*args)
BitValues_set = _bool.BitValues_set

def BitValues_set_from_expr(*args) -> "void" :
  return _bool.BitValues_set_from_expr(*args)
BitValues_set_from_expr = _bool.BitValues_set_from_expr

def BitValues_set_from_values_list(*args) -> "void" :
  return _bool.BitValues_set_from_values_list(*args)
BitValues_set_from_values_list = _bool.BitValues_set_from_values_list

def BoolEnc_create(*args) -> "BoolEnc_ptr" :
  return _bool.BoolEnc_create(*args)
BoolEnc_create = _bool.BoolEnc_create

def BoolEnc_destroy(*args) -> "void" :
  return _bool.BoolEnc_destroy(*args)
BoolEnc_destroy = _bool.BoolEnc_destroy

def BoolEnc_is_var_bit(*args) -> "boolean" :
  return _bool.BoolEnc_is_var_bit(*args)
BoolEnc_is_var_bit = _bool.BoolEnc_is_var_bit

def BoolEnc_is_var_scalar(*args) -> "boolean" :
  return _bool.BoolEnc_is_var_scalar(*args)
BoolEnc_is_var_scalar = _bool.BoolEnc_is_var_scalar

def BoolEnc_get_scalar_var_from_bit(*args) -> "node_ptr" :
  return _bool.BoolEnc_get_scalar_var_from_bit(*args)
BoolEnc_get_scalar_var_from_bit = _bool.BoolEnc_get_scalar_var_from_bit

def BoolEnc_make_var_bit(*args) -> "node_ptr" :
  return _bool.BoolEnc_make_var_bit(*args)
BoolEnc_make_var_bit = _bool.BoolEnc_make_var_bit

def BoolEnc_get_index_from_bit(*args) -> "int" :
  return _bool.BoolEnc_get_index_from_bit(*args)
BoolEnc_get_index_from_bit = _bool.BoolEnc_get_index_from_bit

def BoolEnc_get_var_bits(*args) -> "NodeList_ptr" :
  return _bool.BoolEnc_get_var_bits(*args)
BoolEnc_get_var_bits = _bool.BoolEnc_get_var_bits

def BoolEnc_get_var_encoding(*args) -> "node_ptr" :
  return _bool.BoolEnc_get_var_encoding(*args)
BoolEnc_get_var_encoding = _bool.BoolEnc_get_var_encoding

def BoolEnc_get_values_bool_encoding(*args) -> "node_ptr" :
  return _bool.BoolEnc_get_values_bool_encoding(*args)
BoolEnc_get_values_bool_encoding = _bool.BoolEnc_get_values_bool_encoding

def BoolEnc_scalar_layer_to_bool_layer(*args) -> "char const *" :
  return _bool.BoolEnc_scalar_layer_to_bool_layer(*args)
BoolEnc_scalar_layer_to_bool_layer = _bool.BoolEnc_scalar_layer_to_bool_layer

def BoolEnc_is_bool_layer(*args) -> "boolean" :
  return _bool.BoolEnc_is_bool_layer(*args)
BoolEnc_is_bool_layer = _bool.BoolEnc_is_bool_layer

def BoolEnc_get_value_from_var_bits(*args) -> "node_ptr" :
  return _bool.BoolEnc_get_value_from_var_bits(*args)
BoolEnc_get_value_from_var_bits = _bool.BoolEnc_get_value_from_var_bits

def BoolEnc_get_var_mask(*args) -> "node_ptr" :
  return _bool.BoolEnc_get_var_mask(*args)
BoolEnc_get_var_mask = _bool.BoolEnc_get_var_mask
# This file is compatible with both classic and new-style classes.

