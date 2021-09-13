
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CADENA CHAR DECIMAL DIFERENTES DIV DOSP DPUNTOS ENTERO ID IGUALAR IGUALES MAS MAY MAYOIGUAL MEN MENOIGUAL MENOS MOD PARAB PARC POR POT PTCOMA RBOOL RCHAR RELSE RELSEIF REND RFLOT RFOR RIF RIN RINT RNOTHING RPRINTLN RSTRING RWHILEinit       : instruccionesinstrucciones  : instrucciones instruccioninstrucciones  : instruccioninstruccion  : imprimirins fins\n                    | DECLARACIONES fins\n                    | if_instr fins\n                    | while_instr fins\n                    | for_inst fins\n    \n    fins   : PTCOMAinstruccion        : error PTCOMAimprimirins    : RPRINTLN PARAB expresion PARCif_instr : RIF expresion instrucciones RENDif_instr : RIF expresion instrucciones elifinst RELSE instrucciones RENDelifinst : elifinst elifinstruelifinst : elifinstruelifinstru : RELSEIF expresion instruccioneswhile_instr : RWHILE expresion instrucciones REND\n    for_inst : RFOR ID RIN expresion DPUNTOS expresion instrucciones REND DECLARACIONES : DECLA_COM \n                     | DECLA_SIM   \n                     DECLA_SIM : ID IGUALAR expresion DECLA_COM : ID IGUALAR expresion DOSP TIPOS TIPOS : RINT\n             | RFLOT\n             | RBOOL\n             | RCHAR\n             | RSTRING\n             expresion    : expresion MAS expresion\n                    | expresion MENOS expresion\n                    | expresion POR expresion\n                    | expresion DIV expresion\n                    | expresion POT expresion\n                    | expresion MOD expresion\n                    | expresion MAY expresion\n                    | expresion MEN expresion\n                    | expresion MAYOIGUAL expresion\n                    | expresion MENOIGUAL expresion\n                    | expresion IGUALES expresion\n                    | expresion DIFERENTES expresion\n    expresion    : PARAB expresion PARCexpresion : IDexpresion : ENTEROexpresion : DECIMALexpresion : CADENAexpresion : CHAR'
    
_lr_action_items = {'error':([0,2,3,17,18,19,20,21,22,23,24,26,28,29,30,31,32,33,37,51,59,60,61,62,63,64,65,66,67,68,69,70,71,75,77,85,86,87,89,],[9,9,-3,-2,-4,-9,-5,-6,-7,-8,-10,9,-41,-42,-43,-44,-45,9,9,9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,9,9,9,9,9,9,]),'RPRINTLN':([0,2,3,17,18,19,20,21,22,23,24,26,28,29,30,31,32,33,37,51,59,60,61,62,63,64,65,66,67,68,69,70,71,75,77,85,86,87,89,],[10,10,-3,-2,-4,-9,-5,-6,-7,-8,-10,10,-41,-42,-43,-44,-45,10,10,10,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,10,10,10,10,10,10,]),'RIF':([0,2,3,17,18,19,20,21,22,23,24,26,28,29,30,31,32,33,37,51,59,60,61,62,63,64,65,66,67,68,69,70,71,75,77,85,86,87,89,],[13,13,-3,-2,-4,-9,-5,-6,-7,-8,-10,13,-41,-42,-43,-44,-45,13,13,13,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,13,13,13,13,13,13,]),'RWHILE':([0,2,3,17,18,19,20,21,22,23,24,26,28,29,30,31,32,33,37,51,59,60,61,62,63,64,65,66,67,68,69,70,71,75,77,85,86,87,89,],[14,14,-3,-2,-4,-9,-5,-6,-7,-8,-10,14,-41,-42,-43,-44,-45,14,14,14,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,14,14,14,14,14,14,]),'RFOR':([0,2,3,17,18,19,20,21,22,23,24,26,28,29,30,31,32,33,37,51,59,60,61,62,63,64,65,66,67,68,69,70,71,75,77,85,86,87,89,],[15,15,-3,-2,-4,-9,-5,-6,-7,-8,-10,15,-41,-42,-43,-44,-45,15,15,15,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,15,15,15,15,15,15,]),'ID':([0,2,3,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,58,59,60,61,62,63,64,65,66,67,68,69,70,71,75,77,78,85,86,87,89,],[16,16,-3,28,28,34,-2,-4,-9,-5,-6,-7,-8,-10,28,16,28,-41,-42,-43,-44,-45,16,28,16,28,28,28,28,28,28,28,28,28,28,28,28,16,28,28,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,16,16,28,16,16,16,16,]),'$end':([1,2,3,17,18,19,20,21,22,23,24,],[0,-1,-3,-2,-4,-9,-5,-6,-7,-8,-10,]),'REND':([3,17,18,19,20,21,22,23,24,37,51,85,89,],[-3,-2,-4,-9,-5,-6,-7,-8,-10,55,72,88,90,]),'RELSEIF':([3,17,18,19,20,21,22,23,24,37,56,57,76,86,],[-3,-2,-4,-9,-5,-6,-7,-8,-10,58,58,-15,-14,-16,]),'RELSE':([3,17,18,19,20,21,22,23,24,56,57,76,86,],[-3,-2,-4,-9,-5,-6,-7,-8,-10,75,-15,-14,-16,]),'PTCOMA':([4,5,6,7,8,9,11,12,28,29,30,31,32,53,54,55,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,80,81,82,83,84,88,90,],[19,19,19,19,19,24,-19,-20,-41,-42,-43,-44,-45,-21,-11,-12,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-17,-22,-23,-24,-25,-26,-27,-13,-18,]),'PARAB':([10,13,14,25,27,35,38,39,40,41,42,43,44,45,46,47,48,49,52,58,78,],[25,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'ENTERO':([13,14,25,27,35,38,39,40,41,42,43,44,45,46,47,48,49,52,58,78,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'DECIMAL':([13,14,25,27,35,38,39,40,41,42,43,44,45,46,47,48,49,52,58,78,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'CADENA':([13,14,25,27,35,38,39,40,41,42,43,44,45,46,47,48,49,52,58,78,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'CHAR':([13,14,25,27,35,38,39,40,41,42,43,44,45,46,47,48,49,52,58,78,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'IGUALAR':([16,],[35,]),'MAS':([26,28,29,30,31,32,33,36,50,53,59,60,61,62,63,64,65,66,67,68,69,70,71,73,77,87,],[38,-41,-42,-43,-44,-45,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-40,38,38,38,]),'MENOS':([26,28,29,30,31,32,33,36,50,53,59,60,61,62,63,64,65,66,67,68,69,70,71,73,77,87,],[39,-41,-42,-43,-44,-45,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-40,39,39,39,]),'POR':([26,28,29,30,31,32,33,36,50,53,59,60,61,62,63,64,65,66,67,68,69,70,71,73,77,87,],[40,-41,-42,-43,-44,-45,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-40,40,40,40,]),'DIV':([26,28,29,30,31,32,33,36,50,53,59,60,61,62,63,64,65,66,67,68,69,70,71,73,77,87,],[41,-41,-42,-43,-44,-45,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-40,41,41,41,]),'POT':([26,28,29,30,31,32,33,36,50,53,59,60,61,62,63,64,65,66,67,68,69,70,71,73,77,87,],[42,-41,-42,-43,-44,-45,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-40,42,42,42,]),'MOD':([26,28,29,30,31,32,33,36,50,53,59,60,61,62,63,64,65,66,67,68,69,70,71,73,77,87,],[43,-41,-42,-43,-44,-45,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-40,43,43,43,]),'MAY':([26,28,29,30,31,32,33,36,50,53,59,60,61,62,63,64,65,66,67,68,69,70,71,73,77,87,],[44,-41,-42,-43,-44,-45,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-40,44,44,44,]),'MEN':([26,28,29,30,31,32,33,36,50,53,59,60,61,62,63,64,65,66,67,68,69,70,71,73,77,87,],[45,-41,-42,-43,-44,-45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-40,45,45,45,]),'MAYOIGUAL':([26,28,29,30,31,32,33,36,50,53,59,60,61,62,63,64,65,66,67,68,69,70,71,73,77,87,],[46,-41,-42,-43,-44,-45,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-40,46,46,46,]),'MENOIGUAL':([26,28,29,30,31,32,33,36,50,53,59,60,61,62,63,64,65,66,67,68,69,70,71,73,77,87,],[47,-41,-42,-43,-44,-45,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-40,47,47,47,]),'IGUALES':([26,28,29,30,31,32,33,36,50,53,59,60,61,62,63,64,65,66,67,68,69,70,71,73,77,87,],[48,-41,-42,-43,-44,-45,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-40,48,48,48,]),'DIFERENTES':([26,28,29,30,31,32,33,36,50,53,59,60,61,62,63,64,65,66,67,68,69,70,71,73,77,87,],[49,-41,-42,-43,-44,-45,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-40,49,49,49,]),'PARC':([28,29,30,31,32,36,50,59,60,61,62,63,64,65,66,67,68,69,70,71,],[-41,-42,-43,-44,-45,54,71,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,]),'DOSP':([28,29,30,31,32,53,59,60,61,62,63,64,65,66,67,68,69,70,71,],[-41,-42,-43,-44,-45,74,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,]),'DPUNTOS':([28,29,30,31,32,59,60,61,62,63,64,65,66,67,68,69,70,71,73,],[-41,-42,-43,-44,-45,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,78,]),'RIN':([34,],[52,]),'RINT':([74,],[80,]),'RFLOT':([74,],[81,]),'RBOOL':([74,],[82,]),'RCHAR':([74,],[83,]),'RSTRING':([74,],[84,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,26,33,75,77,87,],[2,37,51,85,86,89,]),'instruccion':([0,2,26,33,37,51,75,77,85,86,87,89,],[3,17,3,3,17,17,3,3,17,17,3,17,]),'imprimirins':([0,2,26,33,37,51,75,77,85,86,87,89,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'DECLARACIONES':([0,2,26,33,37,51,75,77,85,86,87,89,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'if_instr':([0,2,26,33,37,51,75,77,85,86,87,89,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'while_instr':([0,2,26,33,37,51,75,77,85,86,87,89,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'for_inst':([0,2,26,33,37,51,75,77,85,86,87,89,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'DECLA_COM':([0,2,26,33,37,51,75,77,85,86,87,89,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'DECLA_SIM':([0,2,26,33,37,51,75,77,85,86,87,89,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'fins':([4,5,6,7,8,],[18,20,21,22,23,]),'expresion':([13,14,25,27,35,38,39,40,41,42,43,44,45,46,47,48,49,52,58,78,],[26,33,36,50,53,59,60,61,62,63,64,65,66,67,68,69,70,73,77,87,]),'elifinst':([37,],[56,]),'elifinstru':([37,56,],[57,76,]),'TIPOS':([74,],[79,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',156),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instruccion','grammar.py',160),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','grammar.py',166),
  ('instruccion -> imprimirins fins','instruccion',2,'p_instruccion','grammar.py',173),
  ('instruccion -> DECLARACIONES fins','instruccion',2,'p_instruccion','grammar.py',174),
  ('instruccion -> if_instr fins','instruccion',2,'p_instruccion','grammar.py',175),
  ('instruccion -> while_instr fins','instruccion',2,'p_instruccion','grammar.py',176),
  ('instruccion -> for_inst fins','instruccion',2,'p_instruccion','grammar.py',177),
  ('fins -> PTCOMA','fins',1,'p_fins','grammar.py',182),
  ('instruccion -> error PTCOMA','instruccion',2,'p_instruccion_error','grammar.py',185),
  ('imprimirins -> RPRINTLN PARAB expresion PARC','imprimirins',4,'p_imprimirins','grammar.py',190),
  ('if_instr -> RIF expresion instrucciones REND','if_instr',4,'p_if_instr','grammar.py',194),
  ('if_instr -> RIF expresion instrucciones elifinst RELSE instrucciones REND','if_instr',7,'p_else_instr','grammar.py',201),
  ('elifinst -> elifinst elifinstru','elifinst',2,'p_elifinst','grammar.py',205),
  ('elifinst -> elifinstru','elifinst',1,'p_elifinst2','grammar.py',211),
  ('elifinstru -> RELSEIF expresion instrucciones','elifinstru',3,'p_elifinstru','grammar.py',218),
  ('while_instr -> RWHILE expresion instrucciones REND','while_instr',4,'p_while','grammar.py',222),
  ('for_inst -> RFOR ID RIN expresion DPUNTOS expresion instrucciones REND','for_inst',8,'p_for_inst','grammar.py',227),
  ('DECLARACIONES -> DECLA_COM','DECLARACIONES',1,'p_DECLARACIONES','grammar.py',231),
  ('DECLARACIONES -> DECLA_SIM','DECLARACIONES',1,'p_DECLARACIONES','grammar.py',232),
  ('DECLA_SIM -> ID IGUALAR expresion','DECLA_SIM',3,'p_DECLA_SIM','grammar.py',236),
  ('DECLA_COM -> ID IGUALAR expresion DOSP TIPOS','DECLA_COM',5,'p_DECLA_COM','grammar.py',239),
  ('TIPOS -> RINT','TIPOS',1,'p_TIPOS','grammar.py',243),
  ('TIPOS -> RFLOT','TIPOS',1,'p_TIPOS','grammar.py',244),
  ('TIPOS -> RBOOL','TIPOS',1,'p_TIPOS','grammar.py',245),
  ('TIPOS -> RCHAR','TIPOS',1,'p_TIPOS','grammar.py',246),
  ('TIPOS -> RSTRING','TIPOS',1,'p_TIPOS','grammar.py',247),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion','grammar.py',261),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion','grammar.py',262),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion','grammar.py',263),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion','grammar.py',264),
  ('expresion -> expresion POT expresion','expresion',3,'p_expresion','grammar.py',265),
  ('expresion -> expresion MOD expresion','expresion',3,'p_expresion','grammar.py',266),
  ('expresion -> expresion MAY expresion','expresion',3,'p_expresion','grammar.py',267),
  ('expresion -> expresion MEN expresion','expresion',3,'p_expresion','grammar.py',268),
  ('expresion -> expresion MAYOIGUAL expresion','expresion',3,'p_expresion','grammar.py',269),
  ('expresion -> expresion MENOIGUAL expresion','expresion',3,'p_expresion','grammar.py',270),
  ('expresion -> expresion IGUALES expresion','expresion',3,'p_expresion','grammar.py',271),
  ('expresion -> expresion DIFERENTES expresion','expresion',3,'p_expresion','grammar.py',272),
  ('expresion -> PARAB expresion PARC','expresion',3,'p_expresion_agrup','grammar.py',303),
  ('expresion -> ID','expresion',1,'p_expresion_ID','grammar.py',307),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','grammar.py',311),
  ('expresion -> DECIMAL','expresion',1,'p_primitivo_decimal','grammar.py',315),
  ('expresion -> CADENA','expresion',1,'p_primitivo_cadena','grammar.py',319),
  ('expresion -> CHAR','expresion',1,'p_primitivo_caracter','grammar.py',323),
]