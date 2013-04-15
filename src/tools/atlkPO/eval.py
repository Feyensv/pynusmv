"""
CTLK evaluation functions.
"""

from pynusmv.dd import BDD
from pynusmv.mc import eval_simple_expression
from pynusmv.utils import fixpoint as fp

from ..atlkFO.ast import (TrueExp, FalseExp, Init, Reachable,
                          Atom, Not, And, Or, Implies, Iff, 
                          AF, AG, AX, AU, AW, EF, EG, EX, EU, EW,
                          nK, nE, nD, nC, K, E, D, C,
                          CEF, CEG, CEX, CEU, CEW, CAF, CAG, CAX, CAU, CAW)
                          

from ..atlkFO.eval import (fair_states, ex, eg, eu, nk, ne, nd, nc)


def evalATLK(fsm, spec):
    """
    Return the BDD representing the set of states of fsm satisfying spec.
    
    fsm -- a MAS representing the system
    spec -- an AST-based ATLK specification
    """
    
    if type(spec) is TrueExp:
        return BDD.true(fsm.bddEnc.DDmanager)
        
    elif type(spec) is FalseExp:
        return BDD.false(fsm.bddEnc.DDmanager)
        
    elif type(spec) is Init:
        return fsm.init
        
    elif type(spec) is Reachable:
        return fsm.reachable_states
    
    elif type(spec) is Atom:
        return eval_simple_expression(fsm, spec.value)
        
    elif type(spec) is Not:
        return ~evalATLK(fsm, spec.child)
        
    elif type(spec) is And:
        return evalATLK(fsm, spec.left) & evalATLK(fsm, spec.right)
        
    elif type(spec) is Or:
        return evalATLK(fsm, spec.left) | evalATLK(fsm, spec.right)
        
    elif type(spec) is Implies:
        # a -> b = ~a | b
        return (~evalATLK(fsm, spec.left)) | evalATLK(fsm, spec.right)
        
    elif type(spec) is Iff:
        # a <-> b = (a & b) | (~a & ~b)
        l = evalATLK(fsm, spec.left)
        r = evalATLK(fsm, spec.right)
        return (l & r) | ((~l) & (~r))
        
    elif type(spec) is EX:
        return ex(fsm, evalATLK(fsm, spec.child))
        
    elif type(spec) is AX:
        # AX p = ~EX ~p
        return ~ex(fsm, ~evalATLK(fsm, spec.child))
        
    elif type(spec) is EG:
        return eg(fsm, evalATLK(fsm, spec.child))
        
    elif type(spec) is AG:
        # AG p = ~EF ~p = ~E[ true U ~p ]
        return ~eu(fsm,
                   BDD.true(fsm.bddEnc.DDmanager),
                   ~evalATLK(fsm, spec.child))
        
    elif type(spec) is EU:
        return eu(fsm, evalATLK(fsm, spec.left), evalATLK(fsm, spec.right))
        
    elif type(spec) is AU:
        # A[p U q] = ~E[~q W ~p & ~q] = ~(E[~q U ~p & ~q] | EG ~q)
        p = evalATLK(fsm, spec.left)
        q = evalATLK(fsm, spec.right)
        equpq = eu(fsm, ~q, ~q & ~p)
        egq = eg(fsm, ~q)
        return ~(equpq | egq)
        
    elif type(spec) is EF:
        # EF p = E[ true U p ]
        return eu(fsm,
                  BDD.true(fsm.bddEnc.DDmanager),
                  evalATLK(fsm, spec.child))    
        
    elif type(spec) is AF:
        # AF p = ~EG ~p
        return ~eg(fsm, ~evalATLK(fsm, spec.child))
        
    elif type(spec) is EW:
        # E[ p W q ] = E[ p U q ] | EG p
        return (eu(fsm, evalATLK(fsm, spec.left), evalATLK(fsm, spec.right)) |
                eg(fsm, evalATLK(fsm, spec.left)))
        
    elif type(spec) is AW:
        # A[p W q] = ~E[~q U ~p & ~q]
        p = evalATLK(fsm, spec.left)
        q = evalATLK(fsm, spec.right)
        return ~eu(fsm, ~q, ~p & ~q)
        
    elif type(spec) is nK:
        return nk(fsm, spec.agent.value, evalATLK(fsm, spec.child))
        
    elif type(spec) is K:
        # K<'a'> p = ~nK<'a'> ~p
        return ~nk(fsm, spec.agent.value, ~evalATLK(fsm, spec.child))
        
    elif type(spec) is nE:
        return ne(fsm,
                  [a.value for a in spec.group],
                  evalATLK(fsm, spec.child))
        
    elif type(spec) is E:
        # E<g> p = ~nE<g> ~p
        return ~ne(fsm,
                   [a.value for a in spec.group],
                   ~evalATLK(fsm, spec.child))
        
    elif type(spec) is nD:
        return nd(fsm,
                  [a.value for a in spec.group],
                  evalATLK(fsm, spec.child)) 
        
    elif type(spec) is D:
        # D<g> p = ~nD<g> ~p
        return ~nd(fsm,
                   [a.value for a in spec.group],
                   ~evalATLK(fsm, spec.child))
        
    elif type(spec) is nC:
        return nc(fsm,
                  [a.value for a in spec.group],
                  evalATLK(fsm, spec.child))
        
    elif type(spec) is C:
        # C<g> p = ~nC<g> ~p
        return ~nc(fsm,
                   [a.value for a in spec.group],
                   ~evalATLK(fsm, spec.child))
                   
    elif type(spec) in {CEX, CAX, CEG, CAG, CEU, CAU, CEF, CAF, CEW, CAW}:
        return eval_strat(fsm, spec)
        
    else:
        # TODO Generate error
        print("[ERROR] CTLK evalATLK: unrecognized specification type", spec)
        return None


def cex(fsm, agents, phi, strat=None):
    """
    Return the set of states of strat satisfying <agents> X phi
    under full observability in strat.
    If strat is None, strat is considered true.
    
    fsm -- a MAS representing the system
    agents -- a list of agents names
    phi -- a BDD representing the set of states of fsm satisfying phi
    strat -- a BDD representing allowed state/inputs pairs, or None
    """        
    nfair = nfair_gamma(fsm, agents, strat)
    
    return fsm.pre_strat(phi | nfair, agents, strat)
    

def ceu(fsm, agents, phi, psi, strat=None):
    """
    Return the set of states of strat satisfying <agents>[phi U psi]
    under full observability in strat.
    If strat is None, strat is considered true.
    
    fsm -- a MAS representing the system
    agents -- a list of agents names
    phi -- a BDD representing the set of states of fsm satisfying phi
    psi -- a BDD representing the set of states of fsm satisfying psi
    strat -- a BDD representing allowed state/inputs pairs, or None
    
    """
    
    if len(fsm.fairness_constraints) == 0:
        return fp(lambda Z : psi | (phi & fsm.pre_strat(Z, agents, strat)),
                  BDD.false(fsm.bddEnc.DDmanager))
    else:
        nfair = nfair_gamma(fsm, agents, strat)
        def inner(Z):
            res = psi
            for f in fsm.fairness_constraints:
                nf = ~f
                res = res | fsm.pre_strat(fp(lambda Y :
                                             (phi | psi | nfair) &
                                             (Z | nf) &
                                             (psi |
                                              fsm.pre_strat(Y, agents, strat)),
                                             BDD.true(fsm.bddEnc.DDmanager)),
                                              agents, strat)
            return (psi | phi | nfair) & res
        return fp(inner, BDD.false(fsm.bddEnc.DDmanager))
    

def cew(fsm, agents, phi, psi, strat=None):
    """
    Return the set of states of strat satisfying <agents>[phi W psi]
    under full observability in strat.
    If strat is None, strat is considered true.
    
    fsm -- a MAS representing the system
    agents -- a list of agents names
    phi -- a BDD representing the set of states of fsm satisfying phi
    psi -- a BDD representing the set of states of fsm satisfying psi
    strat -- a BDD representing allowed state/inputs pairs, or None
    
    """    
    nfair = nfair_gamma(fsm, agents, strat)
    
    return fp(lambda Y : (psi | phi | nfair) &
                         (psi | fsm.pre_strat(Y, agents, strat)),
              BDD.true(fsm.bddEnc.DDmanager))
    
    
def ceg(fsm, agents, phi, strat=None):
    """
    Return the set of states of strat satisfying <agents> G phi
    under full observability in strat.
    If strat is None, strat is considered true.
    
    fsm -- a MAS representing the system
    agents -- a list of agents names
    phi -- a BDD representing the set of states of fsm satisfying phi
    strat -- a BDD representing allowed state/inputs pairs, or None
    
    """    
    nfair = nfair_gamma(fsm, agents, strat)
    
    return fp(lambda Y : (phi | nfair) & fsm.pre_strat(Y, agents, strat),
              BDD.true(fsm.bddEnc.DDmanager))


def nfair_gamma(fsm, agents, strat=None):
    """
    Return the set of states of strat
    in which agents can avoid a fair path in strat.
    If strat is None, it is considered true.
    
    fsm -- the model
    agents -- a list of agents names
    strat -- a BDD representing allowed state/inputs pairs, or None
    
    """    
    if len(fsm.fairness_constraints) == 0:
        return BDD.false(fsm.bddEnc.DDmanager)
    else:
        def inner(Z):
            res = BDD.false(fsm.bddEnc.DDmanager)
            for f in fsm.fairness_constraints:
                nf = ~f
                res = res | fsm.pre_strat(fp(lambda Y :
                                              (Z | nf) &
                                              fsm.pre_strat(Y, agents, strat),
                                              BDD.true(fsm.bddEnc.DDmanager)),
                                             agents, strat)
            return res
        return fp(inner, BDD.false(fsm.bddEnc.DDmanager))              
              
def cex_si(fsm, agents, phi, strat=None):
    """
    Return the set of state/inputs pairs of strat satisfying <agents> X phi
    under full observability in strat.
    If strat is None, strat is considered true.
    
    fsm -- a MAS representing the system
    agents -- a list of agents names
    phi -- a BDD representing the set of states of fsm satisfying phi
    strat -- a BDD representing allowed state/inputs pairs, or None
    """
        
    return fsm.pre_strat_si(phi | nfair_gamma_si(fsm, agents, strat),
                            agents, strat)
    

def ceu_si(fsm, agents, phi, psi, strat=None):
    """
    Return the set of state/inputs pairs of strat satisfying <agents>[phi U psi]
    under full observability in strat.
    If strat is None, strat is considered true.
    
    fsm -- a MAS representing the system
    agents -- a list of agents names
    phi -- a BDD representing the set of states of fsm satisfying phi
    psi -- a BDD representing the set of states of fsm satisfying psi
    strat -- a BDD representing allowed state/inputs pairs, or None
    
    """
    if len(fsm.fairness_constraints) == 0:
        return fp(lambda Z : psi | (phi & fsm.pre_strat_si(Z, agents, strat)),
                  BDD.false(fsm.bddEnc.DDmanager))
    else:
        nfair = nfair_gamma_si(fsm, agents, strat)
        def inner(Z):
            res = psi
            for f in fsm.fairness_constraints:
                nf = ~f
                res = res | fsm.pre_strat_si(fp(lambda Y :
                                                 (phi | psi | nfair) &
                                                 (Z | nf) &
                                                 (psi |
                                                  fsm.pre_strat_si(Y, agents,
                                                                   strat)
                                                 ),
                                              BDD.true(fsm.bddEnc.DDmanager)),
                                              agents, strat)
            return (psi | phi | nfair) & res
        return fp(inner, BDD.false(fsm.bddEnc.DDmanager))
    

def cew_si(fsm, agents, phi, psi, strat=None):
    """
    Return the set of state/inputs pairs of strat satisfying <agents>[phi W psi]
    under full observability in strat.
    If strat is None, strat is considered true.
    
    fsm -- a MAS representing the system
    agents -- a list of agents names
    phi -- a BDD representing the set of states of fsm satisfying phi
    psi -- a BDD representing the set of states of fsm satisfying psi
    strat -- a BDD representing allowed state/inputs pairs, or None
    
    """
    
    nfair = nfair_gamma_si(fsm, agents, strat)
    
    return fp(lambda Y : (psi | phi | nfair) &
                         (psi | fsm.pre_strat_si(Y, agents, strat)),
              BDD.true(fsm.bddEnc.DDmanager))
    
    
def ceg_si(fsm, agents, phi, strat=None):
    """
    Return the set of state/inputs pairs of strat satisfying <agents> G phi
    under full observability in strat.
    If strat is None, strat is considered true.
    
    fsm -- a MAS representing the system
    agents -- a list of agents names
    phi -- a BDD representing the set of states of fsm satisfying phi
    strat -- a BDD representing allowed state/inputs pairs, or None
    
    """
    nfair = nfair_gamma_si(fsm, agents, strat)
    
    return fp(lambda Y : (phi | nfair) & fsm.pre_strat_si(Y, agents, strat),
              BDD.true(fsm.bddEnc.DDmanager))


def nfair_gamma_si(fsm, agents, strat=None):
    """
    Return the set of state/inputs pairs of strat
    in which agents can avoid a fair path in strat.
    If strat is None, it is considered true.
    
    fsm -- the model
    agents -- a list of agents names
    strat -- a BDD representing allowed state/inputs pairs, or None
    
    """    
    if len(fsm.fairness_constraints) == 0:
        return BDD.false(fsm.bddEnc.DDmanager)
    else:
        def inner(Z):
            res = BDD.false(fsm.bddEnc.DDmanager)
            for f in fsm.fairness_constraints:
                nf = ~f
                res = res | fsm.pre_strat_si(fp(lambda Y :
                                                 (Z | nf) &
                                                 fsm.pre_strat_si(Y, agents,
                                                                  strat),
                                             BDD.true(fsm.bddEnc.DDmanager)),
                                             agents, strat)
            return res
        return fp(inner, BDD.false(fsm.bddEnc.DDmanager))
    
    
def split(fsm, strats, gamma):
    """
    Split strats into all its non-conflicting greatest subsets.
    
    fsm -- the model
    strats -- a BDD representing a set of states/inputs pairs
    gamma -- a set of agents of fsm
    
    """
    if strats.is_false():
        return {strats}
    
    # Get one equivalence class
    si = fsm.pick_one_state_inputs(strats)
    s = si.forsome(fsm.bddEnc.inputsCube)
    eqs = fsm.equivalent_states(s, gamma)
    eqcl = strats & eqs
    
    # Remove eqcl from strats
    strats = strats - eqcl
    
    # Get ngamma cube
    ngamma_cube = fsm.bddEnc.inputsCube - fsm.inputs_cube_for_agents(gamma)
    
    # Split eqcl into non-conflicting subsetes
    # (if eqcl is already non-conflicting, only one iteration is done)
    eqcls = set()
    while eqcl.isnot_false():
        si = fsm.pick_one_state_inputs(eqcl)
        ncss = eqcl & si.forsome(fsm.bddEnc.statesCube).forsome(ngamma_cube)
        eqcls.add(ncss)
        eqcl = eqcl - ncss
        
    # Combine NCSSs with strategies of restricted strats
    unistrats = set()
    for strat in split(fsm, strats, gamma):
        for ncss in eqcls:
            unistrats.add(strat | ncss)
            
    return unistrats
    

def eval_strat(fsm, spec):
    """
    Return the BDD representing the set of states of fsm satisfying spec.
    spec is a strategic operator <G> pi.
    
    fsm -- a MAS representing the system;
    spec -- an AST-based ATLK specification with a top strategic operator.
    
    """
    sat = BDD.false(fsm.bddEnc.DDmanager)
    agents = {atom.value for atom in spec.group}
    strats = split(fsm, fsm.protocol(agents), agents)
    for strat in strats:
        if type(spec) is CEX:
            winning = cex(fsm, agents, evalATLK(fsm, spec.child), strat)
#            winning = cex_si(fsm, agents,
#                             evalATLK(fsm, spec.child), strat).forsome(
#                      fsm.bddEnc.inputsCube)

        elif type(spec) is CAX:
            # [g] X p = ~<g> X ~p
            winning = ~cex(fsm, agents, ~evalATLK(fsm, spec.child), strat)
#            winning = ~(cex_si(fsm, agents,
#                               ~evalATLK(fsm, spec.child), strat)).forsome(
#                        fsm.bddEnc.inputsCube)

        elif type(spec) is CEG:
            winning = ceg(fsm, agents, evalATLK(fsm, spec.child), strat)
#            winning = ceg_si(fsm, agents,
#                             evalATLK(fsm, spec.child), strat).forsome(
#                      fsm.bddEnc.inputsCube)

        elif type(spec) is CAG:
            # [g] G p = ~<g> F ~p
            winning= ~ceu(fsm, agents, BDD.true(fsm.bddEnc.DDmanager),
                          ~evalATLK(fsm, spec.child), strat)
#            winning= ~(ceu_si(fsm, agents,
#                              BDD.true(fsm.bddEnc.DDmanager),
#                              ~evalATLK(fsm, spec.child), strat).forsome(
#                       fsm.bddEnc.inputsCube))

        elif type(spec) is CEU:
            winning = ceu(fsm, agents, evalATLK(fsm, spec.left),
                          evalATLK(fsm, spec.right), strat)
#            winning = ceu_si(fsm, agents,
#                             evalATLK(fsm, spec.left),
#                             evalATLK(fsm, spec.right), strat).forsome(
#                      fsm.bddEnc.inputsCube)

        elif type(spec) is CAU:
            # [g][p U q] = ~<g>[ ~q W ~p & ~q ]
            winning =  ~cew(fsm, agents, ~evalATLK(fsm, spec.right),
                            ~evalATLK(fsm, spec.right) &
                            ~evalATLK(fsm, spec.left), strat)
#            winning =  ~(cew_si(fsm, agents,
#                                ~evalATLK(fsm, spec.right),
#                                ~evalATLK(fsm, spec.right) &
#                                ~evalATLK(fsm, spec.left), strat).forsome(
#                         fsm.bddEnc.inputsCube))

        elif type(spec) is CEF:
            # <g> F p = <g>[true U p]
            winning = ceu(fsm, agents, BDD.true(fsm.bddEnc.DDmanager),
                          evalATLK(fsm, spec.child), strat)
#            winning = ceu_si(fsm, agents,
#                             BDD.true(fsm.bddEnc.DDmanager),
#                             evalATLK(fsm, spec.child), strat).forsome(
#                      fsm.bddEnc.inputsCube)

        elif type(spec) is CAF:
            # [g] F p = ~<g> G ~p
            winning = ~ceg(fsm, agents, ~evalATLK(fsm, spec.child), strat)
#            winning = ~(ceg_si(fsm, agents,
#                               ~evalATLK(fsm, spec.child), strat).forsome(
#                        fsm.bddEnc.inputsCube))

        elif type(spec) is CEW:
            winning = cew(fsm, agents, evalATLK(fsm, spec.left),
                          evalATLK(fsm, spec.right), strat)
#            winning = cew_si(fsm, agents,
#                             evalATLK(fsm, spec.left),
#                             evalATLK(fsm, spec.right), strat).forsome(
#                      fsm.bddEnc.inputsCube)

        elif type(spec) is CAW:
            # [g][p W q] = ~<g>[~q U ~p & ~q]
            winning = ~ceu(fsm, agents, ~evalATLK(fsm, spec.right),
                           ~evalATLK(fsm, spec.right) &
                           ~evalATLK(fsm, spec.left), strat)
#            winning = ~(ceu_si(fsm, agents,
#                               ~evalATLK(fsm, spec.right),
#                               ~evalATLK(fsm, spec.right) &
#                               ~evalATLK(fsm, spec.left), strat).forsome(
#                        fsm.bddEnc.inputsCube))
                        
        # Complete sat with states for which all states belong to winning
        
        # wineq is the set of states for which all equiv states are in winning
        nwinning = ~winning & fsm.bddEnc.statesInputsMask
        wineq = ~(fsm.equivalent_states(nwinning &
                  fsm.reachable_states, frozenset(agents))) & winning
        sat = sat | wineq
        
    return sat