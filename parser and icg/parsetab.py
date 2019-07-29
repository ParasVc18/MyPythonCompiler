
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightUMINUSCOL COMMENT DEF DIVIDE ELIF ELSE EQ EQUALS ERROR FLOAT FUNC GLOBAL GRT GRTEQ ID IF IMPORT INDENT INTEGER LAMBDA LBRACE LPAREN LSR LSREQ MINUS NAME NEWLINE NUMBER PLUS PRINT RBRACE RPAREN STRING TIMES WHILE WHITEstatement : WHILE LPAREN expression RPAREN COL statementstatement : IF LPAREN expression RPAREN COL statement ELIF LPAREN expression RPAREN statement\n               | IF LPAREN expression RPAREN COL statement ELSE COL statement\n\t       | IF LPAREN expression RPAREN COL statementstatement : NAME EQUALS expressionstatement : expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : NUMBERexpression : NAME'
    
_lr_action_items = {'WHILE':([0,29,30,36,39,],[2,2,2,2,2,]),'IF':([0,29,30,36,39,],[5,5,5,5,5,]),'NAME':([0,3,7,9,12,13,14,15,16,17,29,30,35,36,39,],[6,11,11,11,11,11,11,11,11,11,6,6,11,6,6,]),'MINUS':([0,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,29,30,35,36,37,39,],[7,7,13,-14,7,-13,7,13,-14,7,7,7,7,7,7,-11,13,-12,-7,-8,-9,-10,13,13,7,7,7,7,13,7,]),'LPAREN':([0,2,3,5,7,9,12,13,14,15,16,17,29,30,33,35,36,39,],[3,9,3,16,3,3,3,3,3,3,3,3,3,3,35,3,3,3,]),'NUMBER':([0,3,7,9,12,13,14,15,16,17,29,30,35,36,39,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'$end':([1,4,6,8,11,18,20,21,22,23,24,26,31,32,38,40,],[0,-6,-14,-13,-14,-11,-12,-7,-8,-9,-10,-5,-1,-4,-3,-2,]),'ELIF':([4,6,8,11,18,20,21,22,23,24,26,31,32,38,40,],[-6,-14,-13,-14,-11,-12,-7,-8,-9,-10,-5,-1,33,-3,-2,]),'ELSE':([4,6,8,11,18,20,21,22,23,24,26,31,32,38,40,],[-6,-14,-13,-14,-11,-12,-7,-8,-9,-10,-5,-1,34,-3,-2,]),'PLUS':([4,6,8,10,11,18,19,20,21,22,23,24,25,26,37,],[12,-14,-13,12,-14,-11,12,-12,-7,-8,-9,-10,12,12,12,]),'TIMES':([4,6,8,10,11,18,19,20,21,22,23,24,25,26,37,],[14,-14,-13,14,-14,-11,14,-12,14,14,-9,-10,14,14,14,]),'DIVIDE':([4,6,8,10,11,18,19,20,21,22,23,24,25,26,37,],[15,-14,-13,15,-14,-11,15,-12,15,15,-9,-10,15,15,15,]),'EQUALS':([6,],[17,]),'RPAREN':([8,10,11,18,19,20,21,22,23,24,25,37,],[-13,20,-14,-11,27,-12,-7,-8,-9,-10,28,39,]),'COL':([27,28,34,],[29,30,36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,29,30,36,39,],[1,31,32,38,40,]),'expression':([0,3,7,9,12,13,14,15,16,17,29,30,35,36,39,],[4,10,18,19,21,22,23,24,25,26,4,4,37,4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> WHILE LPAREN expression RPAREN COL statement','statement',6,'p_while','pyac.py',184),
  ('statement -> IF LPAREN expression RPAREN COL statement ELIF LPAREN expression RPAREN statement','statement',11,'p_check_if','pyac.py',188),
  ('statement -> IF LPAREN expression RPAREN COL statement ELSE COL statement','statement',9,'p_check_if','pyac.py',189),
  ('statement -> IF LPAREN expression RPAREN COL statement','statement',6,'p_check_if','pyac.py',190),
  ('statement -> NAME EQUALS expression','statement',3,'p_statement_assign','pyac.py',197),
  ('statement -> expression','statement',1,'p_statement_expr','pyac.py',201),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','pyac.py',205),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','pyac.py',206),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','pyac.py',207),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','pyac.py',208),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','pyac.py',215),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','pyac.py',219),
  ('expression -> NUMBER','expression',1,'p_expression_number','pyac.py',223),
  ('expression -> NAME','expression',1,'p_expression_name','pyac.py',227),
]
