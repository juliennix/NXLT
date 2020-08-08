
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = 'e\x18z\xb0B;\xccC\xdb\xeb\xa0z\xb9\xa1\t\xa9'
    
_lr_action_items = {'NUMBER':([8,28,31,33,35,40,55,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,88,90,],[11,11,47,50,60,47,50,-50,-51,-53,98,-48,-49,-52,100,47,-43,-42,50,60,50,50,50,50,50,50,110,]),'LOR':([49,97,98,99,100,],[77,-46,-47,-44,-45,]),'WHILE':([10,15,19,21,25,29,30,32,36,38,39,42,43,65,92,93,94,111,113,114,115,117,120,121,122,123,126,127,128,129,131,132,134,135,137,139,140,142,144,146,147,],[17,17,-11,17,-15,17,-18,-14,-10,-12,-13,-16,-17,17,17,17,17,17,17,17,17,17,17,17,17,17,-36,17,17,17,17,17,-38,-37,17,-32,17,-39,-34,-33,-35,]),'MINUS':([33,50,53,54,55,79,81,82,83,84,85,86,87,88,102,104,105,106,107,108,],[55,-59,-60,84,55,55,55,55,55,55,-60,-58,55,55,-60,-57,-56,-54,-55,84,]),'DIVIDE':([50,53,54,85,86,102,104,105,106,107,108,],[-59,-60,81,-60,-58,-60,-57,-56,81,81,81,]),'LE':([47,48,],[68,68,]),'RPAREN':([11,12,13,14,44,46,49,59,60,61,63,97,98,99,100,101,103,109,110,],[-9,27,-6,-8,-7,67,-40,89,-27,-26,91,-46,-47,-44,-45,-41,119,-28,-29,]),'NEWLINE':([1,6,9,16,18,22,23,26,27,37,41,45,50,51,52,53,54,65,67,85,86,89,91,92,95,102,104,105,106,107,108,111,116,118,119,122,124,125,130,133,136,138,141,143,145,],[5,10,15,30,32,38,39,43,-5,62,64,66,-59,-20,-21,-60,-19,93,96,-60,-58,-24,112,113,117,-60,-57,-56,-54,-55,-23,120,126,128,-25,131,134,135,139,142,-30,144,146,-31,147,]),'NE':([47,48,],[70,70,]),'LT':([47,48,],[72,72,]),'COMMA':([11,13,14,20,50,54,56,57,58,59,60,61,85,86,103,104,105,106,107,108,109,110,],[-9,28,-8,34,-59,-19,87,-22,34,90,-27,-26,-60,-58,90,-57,-56,-54,-55,-23,-28,-29,]),'PLUS':([50,53,54,85,86,102,104,105,106,107,108,],[-59,-60,83,-60,-58,-60,-57,-56,-54,-55,83,]),'IDENTIFIER':([0,2,3,7,8,10,15,19,21,25,28,29,30,31,32,33,34,35,36,38,39,40,42,43,55,62,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,88,90,92,93,94,111,113,114,115,117,120,121,122,123,126,127,128,129,131,132,134,135,137,139,140,142,144,146,147,],[4,-2,4,-1,14,20,20,-11,20,-15,14,20,-18,48,-14,53,58,61,-10,-12,-13,48,-16,-17,85,-4,20,-3,-50,-51,-53,97,-48,-49,-52,99,48,-43,-42,102,61,85,85,85,85,85,85,109,20,20,20,20,20,20,20,20,20,20,20,20,-36,20,20,20,20,20,-38,-37,20,-32,20,-39,-34,-33,-35,]),'$end':([2,3,7,62,66,],[-2,0,-1,-4,-3,]),'GT':([47,48,],[73,73,]),'RBRACE':([19,21,25,29,30,32,36,38,39,42,43,94,114,115,121,123,126,127,129,132,134,135,137,139,140,142,144,146,147,],[-11,37,-15,45,-18,-14,-10,-12,-13,-16,-17,116,124,125,130,133,-36,136,138,141,-38,-37,143,-32,145,-39,-34,-33,-35,]),'EQUALS':([20,53,58,102,],[33,79,88,79,]),'ELSE':([25,139,144,146,147,],[41,-32,-34,-33,-35,]),'GE':([47,48,],[69,69,]),'LAND':([49,97,98,99,100,],[78,-46,-47,-44,-45,]),'LPAREN':([4,17,20,24,53,],[8,31,35,40,80,]),'TIMES':([50,53,54,85,86,102,104,105,106,107,108,],[-59,-60,82,-60,-58,-60,-57,-56,82,82,82,]),'EQ':([47,48,],[74,74,]),'IF':([10,15,19,21,25,29,30,32,36,38,39,42,43,65,92,93,94,111,113,114,115,117,120,121,122,123,126,127,128,129,131,132,134,135,137,139,140,142,144,146,147,],[24,24,-11,24,-15,24,-18,-14,-10,-12,-13,-16,-17,24,24,24,24,24,24,24,24,24,24,24,24,24,-36,24,24,24,24,24,-38,-37,24,-32,24,-39,-34,-33,-35,]),'LBRACE':([1,5,27,41,64,67,91,96,112,],[6,9,-5,65,92,95,111,118,122,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([10,15,65,92,93,111,113,117,120,122,128,131,],[21,29,94,114,115,121,123,127,129,132,137,140,]),'condition_list':([31,40,76,],[46,63,101,]),'head':([0,3,],[1,1,]),'function_definition':([0,3,],[2,7,]),'parralel_assignment':([10,15,21,29,34,65,92,93,94,111,113,114,115,117,120,121,122,123,127,128,129,131,132,137,140,],[18,18,18,18,56,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'assignment':([10,15,21,29,33,34,65,79,92,93,94,111,113,114,115,117,120,121,122,123,127,128,129,131,132,137,140,],[22,22,22,22,51,57,22,51,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'if_block':([10,15,21,29,65,92,93,94,111,113,114,115,117,120,121,122,123,127,128,129,131,132,137,140,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'parameters_list':([35,80,],[59,103,]),'function_call':([10,15,21,29,65,92,93,94,111,113,114,115,117,120,121,122,123,127,128,129,131,132,137,140,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'comp_symbol':([47,48,],[71,75,]),'comb_symbol':([49,],[76,]),'while_block':([10,15,21,29,65,92,93,94,111,113,114,115,117,120,121,122,123,127,128,129,131,132,137,140,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'program':([0,],[3,]),'argument_list':([8,28,],[12,44,]),'statement':([10,15,21,29,65,92,93,94,111,113,114,115,117,120,121,122,123,127,128,129,131,132,137,140,],[19,19,36,36,19,19,19,36,19,19,36,36,19,19,36,19,36,36,19,36,19,36,36,36,]),'multiple_assignment':([10,15,21,29,33,65,79,92,93,94,111,113,114,115,117,120,121,122,123,127,128,129,131,132,137,140,],[23,23,23,23,52,23,52,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'argument_declaration':([8,28,],[13,13,]),'expression':([33,55,79,81,82,83,84,87,88,],[54,86,54,104,105,106,107,108,54,]),'condition':([31,40,76,],[49,49,49,]),'else_block':([25,],[42,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program function_definition','program',2,'p_program','test.py',159),
  ('program -> function_definition','program',1,'p_program','test.py',160),
  ('function_definition -> head NEWLINE LBRACE NEWLINE body RBRACE NEWLINE','function_definition',7,'p_function_definition','test.py',171),
  ('function_definition -> head LBRACE NEWLINE body RBRACE NEWLINE','function_definition',6,'p_function_definition','test.py',172),
  ('head -> IDENTIFIER LPAREN argument_list RPAREN','head',4,'p_head','test.py',180),
  ('argument_list -> argument_declaration','argument_list',1,'p_argument_list','test.py',185),
  ('argument_list -> argument_declaration COMMA argument_list','argument_list',3,'p_argument_list','test.py',186),
  ('argument_declaration -> IDENTIFIER','argument_declaration',1,'p_argument_declaration','test.py',194),
  ('argument_declaration -> NUMBER','argument_declaration',1,'p_argument_declaration','test.py',195),
  ('body -> body statement','body',2,'p_body','test.py',200),
  ('body -> statement','body',1,'p_body','test.py',201),
  ('statement -> assignment NEWLINE','statement',2,'p_statement','test.py',209),
  ('statement -> multiple_assignment NEWLINE','statement',2,'p_statement','test.py',210),
  ('statement -> parralel_assignment NEWLINE','statement',2,'p_statement','test.py',211),
  ('statement -> if_block','statement',1,'p_statement','test.py',212),
  ('statement -> if_block else_block','statement',2,'p_statement','test.py',213),
  ('statement -> while_block NEWLINE','statement',2,'p_statement','test.py',214),
  ('statement -> function_call NEWLINE','statement',2,'p_statement','test.py',215),
  ('assignment -> IDENTIFIER EQUALS expression','assignment',3,'p_assignment','test.py',225),
  ('multiple_assignment -> assignment','multiple_assignment',1,'p_multiple_assignment','test.py',231),
  ('multiple_assignment -> IDENTIFIER EQUALS multiple_assignment','multiple_assignment',3,'p_multiple_assignment','test.py',232),
  ('parralel_assignment -> assignment','parralel_assignment',1,'p_parralel_assignment','test.py',241),
  ('parralel_assignment -> IDENTIFIER COMMA parralel_assignment COMMA expression','parralel_assignment',5,'p_parralel_assignment','test.py',242),
  ('function_call -> IDENTIFIER LPAREN parameters_list RPAREN','function_call',4,'p_function_call','test.py',251),
  ('function_call -> IDENTIFIER EQUALS IDENTIFIER LPAREN parameters_list RPAREN','function_call',6,'p_function_call','test.py',252),
  ('parameters_list -> IDENTIFIER','parameters_list',1,'p_parameters_list','test.py',260),
  ('parameters_list -> NUMBER','parameters_list',1,'p_parameters_list','test.py',261),
  ('parameters_list -> parameters_list COMMA IDENTIFIER','parameters_list',3,'p_parameters_list','test.py',262),
  ('parameters_list -> parameters_list COMMA NUMBER','parameters_list',3,'p_parameters_list','test.py',263),
  ('while_block -> WHILE LPAREN condition_list RPAREN LBRACE NEWLINE body RBRACE','while_block',8,'p_while_block','test.py',271),
  ('while_block -> WHILE LPAREN condition_list RPAREN NEWLINE LBRACE NEWLINE body RBRACE','while_block',9,'p_while_block','test.py',272),
  ('if_block -> IF LPAREN condition_list RPAREN LBRACE body RBRACE NEWLINE','if_block',8,'p_if_block','test.py',282),
  ('if_block -> IF LPAREN condition_list RPAREN NEWLINE LBRACE body RBRACE NEWLINE','if_block',9,'p_if_block','test.py',283),
  ('if_block -> IF LPAREN condition_list RPAREN LBRACE NEWLINE body RBRACE NEWLINE','if_block',9,'p_if_block','test.py',284),
  ('if_block -> IF LPAREN condition_list RPAREN NEWLINE LBRACE NEWLINE body RBRACE NEWLINE','if_block',10,'p_if_block','test.py',285),
  ('else_block -> ELSE LBRACE body RBRACE NEWLINE','else_block',5,'p_else_block','test.py',296),
  ('else_block -> ELSE LBRACE NEWLINE body RBRACE NEWLINE','else_block',6,'p_else_block','test.py',297),
  ('else_block -> ELSE NEWLINE LBRACE body RBRACE NEWLINE','else_block',6,'p_else_block','test.py',298),
  ('else_block -> ELSE NEWLINE LBRACE NEWLINE body RBRACE NEWLINE','else_block',7,'p_else_block','test.py',299),
  ('condition_list -> condition','condition_list',1,'p_condition_list','test.py',309),
  ('condition_list -> condition comb_symbol condition_list','condition_list',3,'p_condition_list','test.py',310),
  ('comb_symbol -> LAND','comb_symbol',1,'p_comb_symbol','test.py',320),
  ('comb_symbol -> LOR','comb_symbol',1,'p_comb_symbol','test.py',321),
  ('condition -> IDENTIFIER comp_symbol IDENTIFIER','condition',3,'p_condition','test.py',325),
  ('condition -> IDENTIFIER comp_symbol NUMBER','condition',3,'p_condition','test.py',326),
  ('condition -> NUMBER comp_symbol IDENTIFIER','condition',3,'p_condition','test.py',327),
  ('condition -> NUMBER comp_symbol NUMBER','condition',3,'p_condition','test.py',328),
  ('comp_symbol -> LT','comp_symbol',1,'p_comp_symbol','test.py',338),
  ('comp_symbol -> GT','comp_symbol',1,'p_comp_symbol','test.py',339),
  ('comp_symbol -> LE','comp_symbol',1,'p_comp_symbol','test.py',340),
  ('comp_symbol -> GE','comp_symbol',1,'p_comp_symbol','test.py',341),
  ('comp_symbol -> EQ','comp_symbol',1,'p_comp_symbol','test.py',342),
  ('comp_symbol -> NE','comp_symbol',1,'p_comp_symbol','test.py',343),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','test.py',347),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','test.py',348),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','test.py',349),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','test.py',350),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','test.py',358),
  ('expression -> NUMBER','expression',1,'p_expression_number','test.py',363),
  ('expression -> IDENTIFIER','expression',1,'p_expression_name','test.py',368),
]
