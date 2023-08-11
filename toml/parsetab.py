
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACH APOSTROFE APR ASPA ATC ATO BOOLEAN CHAR COMMENT DATE DOT_SEP DOUBLEAPOSTROFE DOUBLEASPA ESCAPE ESC_BACKSPACE ESC_CRETURN ESC_FF ESC_HEX4 ESC_HEX8 ESC_NL ESC_QUOTE ESC_REVERSE ESC_TAB FCH FLOAT FPR IGUAL INTEGER MINUS NEWLINE TIME TRIPLEAPOSTROFE TRIPLEASPA TWODOT_SEP UNDERSCORE VIRGULA WHITESPACETOML : TITLES GROUPSTITLES : KVALUE EXPRESSION TITLESTITLES :GROUPS : SECCAO EXPRESSION GROUPSGROUPS : SECCAO : TABLE EXPRESSION ATRIBUICOESSECCAO :ATRIBUICOES : KVALUE EXPRESSION ATRIBUICOESATRIBUICOES :EXPRESSION : COMMENT EXPRESSIONEXPRESSION : NEWLINE EXPRESSIONEXPRESSION :KVALUE : KEY kvwhitespace IGUAL kvwhitespace VALUEkvwhitespace : WHITESPACEkvwhitespace :KEY : SIMPLEKEYKEY : DOTKEYSIMPLEKEY : QUOTEDKEYSIMPLEKEY : UNQUOTEDKEYUNQUOTEDKEY : OCCURRENCES UNQUOTEDKEYAUXUNQUOTEDKEYAUX : OCCURRENCES UNQUOTEDKEYAUXUNQUOTEDKEYAUX :OCCURRENCES : CHAROCCURRENCES : INTEGEROCCURRENCES : MINUSOCCURRENCES : UNDERSCOREQUOTEDKEY : BASICSTRINGQUOTEDKEY : LITERALSTRINGDOTKEY : SIMPLEKEY DOT_SEP SIMPLEKEY DOTSIMPKEYDOTSIMPKEY : DOT_SEP SIMPLEKEY DOTSIMPKEYDOTSIMPKEY : VALUE : STRINGVALUE : BOOLEANVALUE : INTEGERVALUE : ARRAYVALUE : INLINETABLEVALUE : DATETIMEDATETIME : LOCALDATETIMEDATETIME : LOCALDATEDATETIME : LOCALTIMELOCALDATETIME : LOCALDATE LOCALTIMELOCALDATE : DATELOCALTIME : TIMEVALUE : FLOATSTRING : MULTILINEBASICSTRINGSTRING : BASICSTRINGSTRING : MLLITERALSTRINGSTRING : LITERALSTRINGBASICSTRING : ASPA BC ASPABC : BASICCHAR BCBC :BASICCHAR : BASICUNESCAPEDBASICCHAR : ESCAPEDBASICUNESCAPED : WHITESPACEBASICUNESCAPED : CHARBASICUNESCAPED : INTEGERBASICUNESCAPED : FLOATBASICUNESCAPED : MINUSBASICUNESCAPED : APOSTROFEBASICUNESCAPED : ESCAPEDBASICUNESCAPED : DOT_SEPBASICUNESCAPED : TWODOT_SEPESCAPED : ESC_QUOTEESCAPED : ESC_REVERSEESCAPED : ESC_BACKSPACEESCAPED : ESC_FFESCAPED : ESC_NLESCAPED : ESC_CRETURNESCAPED : ESC_TABESCAPED : ESC_HEX4ESCAPED : ESC_HEX8MULTILINEBASICSTRING : TRIPLEASPA MLNL MLBASICBODY TRIPLEASPAMLNL : NEWLINEMLNL :MLBASICBODY : MLBCMLBC : CONTENTQUOTE MLBCMLBC :CONTENTQUOTE : MLBCONTENTCONTENTQUOTE : MLBQUOTESMLBCONTENT : MLBCHARMLBCONTENT : NEWLINEMLBCONTENT : MLBESCAPEDNLMLBCONTENT : TWODOT_SEPMLBCONTENT : DOT_SEPMLBCONTENT : VIRGULAMLBCHAR : MLBUNESCAPEDMLBCHAR : ESCAPEDMLBQUOTES : ASPAMLBQUOTES : DOUBLEASPAMLBQUOTES :MLBUNESCAPED : WHITESPACEMLBUNESCAPED : CHARMLBESCAPEDNL : ESCAPE NEWLINE WHNLWHNL : SPACENEWLINE WHNLWHNL :SPACENEWLINE : WHITESPACESPACENEWLINE : NEWLINELITERALSTRING : APOSTROFE LCH APOSTROFELCH : LITERALCHAR LCHLCH :LITERALCHAR : CHARLITERALCHAR : ESCAPEDLITERALCHAR : WHITESPACELITERALCHAR : TWODOT_SEPLITERALCHAR : ASPALITERALCHAR : ESCAPEMLLITERALSTRING : TRIPLEAPOSTROFE NLR MLLITERALBODY TRIPLEAPOSTROFENLR : NEWLINENLR :MLLITERALBODY : MLLCMLLC : MLLCONTENTQUOTES MLLCMLLCONTENTQUOTES : MLLCONTENTMLLCONTENTQUOTES : MLLQUOTESMLLC :MLLCONTENT : MLLCHARMLLCONTENT : NEWLINEMLLCHAR : CHARMLLCHAR : DOT_SEPMLLCHAR : WHITESPACEMLLCHAR : VIRGULAMLLQUOTES : DOUBLEAPOSTROFEMLLQUOTES : APOSTROFEMLLQUOTES :ARRAY : APR ARRAYVALUES WSCOMMENTNEWLINE FPRARRAYVALUES :ARRAYVALUES : WSCOMMENTNEWLINE VALUE WSCOMMENTNEWLINE ARRAYCONTEUDOARRAYCONTEUDO :ARRAYCONTEUDO : WSCOMMENTNEWLINE VIRGULA ARRAYVALUESWSCOMMENTNEWLINE :WSCOMMENTNEWLINE : INNERCOMMENT WSCOMMENTNEWLINEINNERCOMMENT : WHITESPACEINNERCOMMENT : COMMENTOUNAO NEWLINEINNERCOMMENT : NEWLINECOMMENTOUNAO : COMMENTCOMMENTOUNAO :TABLE : STDTABLETABLE : TABLEARRAYSTDTABLE : APR KEY FPRINLINETABLE : ACH FCHINLINETABLE : ACH INLINETABLEWS INLINEKVALUE INLINETABLEWS FCHINLINETABLEWS : INLINETABLEWS : WHITESPACEINLINEKVALUE : INLINEKVALUE INLINETABLEWS VIRGULA INLINETABLEWS KVALUEINLINEKVALUE : KVALUETABLEARRAY : ATO KEY ATC'
    
_lr_action_items = {'APR':([0,2,3,19,20,21,22,25,26,27,29,62,63,66,67,68,69,72,74,77,78,79,80,81,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,100,101,104,105,107,109,110,111,113,115,118,126,127,161,164,167,171,177,],[-3,23,-12,-12,-12,-136,-137,-3,-12,-12,-14,23,-9,-2,-10,-11,-15,-49,-98,-6,-12,-138,-145,97,-9,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-129,-38,-39,-40,-42,-43,-8,97,-129,-131,-133,-139,-41,-130,-132,-124,-72,-107,-140,-129,]),'ATO':([0,2,3,19,20,21,22,25,26,27,62,63,66,67,68,72,74,77,78,79,80,84,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,104,105,107,115,118,161,164,167,171,],[-3,24,-12,-12,-12,-136,-137,-3,-12,-12,24,-9,-2,-10,-11,-49,-98,-6,-12,-138,-145,-9,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-38,-39,-40,-42,-43,-8,-139,-41,-124,-72,-107,-140,]),'COMMENT':([0,2,3,19,20,21,22,25,26,27,62,63,66,67,68,72,74,77,78,79,80,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,100,101,104,105,107,108,110,111,113,115,118,125,126,127,161,162,164,167,170,171,177,180,],[-3,-7,26,26,26,-136,-137,-3,26,26,-7,-9,-2,-10,-11,-49,-98,-6,26,-138,-145,-9,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,114,-38,-39,-40,-42,-43,-8,114,114,-131,-133,-139,-41,114,-130,-132,-124,114,-72,-107,-126,-140,114,-128,]),'NEWLINE':([0,2,3,19,20,21,22,25,26,27,45,46,47,48,49,50,51,52,53,62,63,66,67,68,72,74,77,78,79,80,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,107,108,110,111,112,113,114,115,118,119,120,121,122,125,126,127,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,150,151,152,153,154,155,156,157,158,159,160,161,162,164,166,167,170,171,173,174,175,176,177,179,180,],[-3,-7,27,27,27,-136,-137,-3,27,27,-63,-64,-65,-66,-67,-68,-69,-70,-71,-7,-9,-2,-10,-11,-49,-98,-6,27,-138,-145,-9,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,113,-38,-39,-40,120,122,-42,-43,-8,113,113,-131,127,-133,-134,-139,-41,136,-73,154,-108,113,-130,-132,136,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,166,-91,-92,154,-112,-113,-115,-116,-121,-122,-117,-118,-119,-120,-124,113,-72,173,-107,-126,-140,-97,-93,173,-96,113,-94,-128,]),'$end':([0,1,2,3,18,19,20,21,22,25,26,27,62,63,66,67,68,72,74,76,77,78,79,80,84,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,104,105,107,115,118,161,164,167,171,],[-3,0,-5,-12,-1,-12,-12,-136,-137,-3,-12,-12,-5,-9,-2,-10,-11,-49,-98,-4,-6,-12,-138,-145,-9,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-38,-39,-40,-42,-43,-8,-139,-41,-124,-72,-107,-140,]),'ASPA':([0,3,12,13,20,21,22,23,24,25,26,27,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,63,67,68,69,72,73,74,78,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,105,109,110,111,113,115,116,117,118,119,120,126,127,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,161,164,166,167,171,172,173,174,175,176,177,178,179,],[12,-12,-51,60,-12,-136,-137,12,12,12,-12,-12,-14,12,72,-51,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,60,-101,-102,-103,-104,-105,-106,12,-10,-11,-15,-49,-50,-98,-12,-138,-145,12,12,12,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-129,-141,-38,-39,-40,-74,-42,-43,12,-129,-131,-133,-139,12,-142,-41,141,-73,-130,-132,141,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,-124,-72,-95,-107,-140,-141,-97,-93,-95,-96,-129,12,-94,]),'APOSTROFE':([0,3,12,13,20,21,22,23,24,25,26,27,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,67,68,69,72,74,75,78,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,105,109,110,111,113,115,116,117,118,121,122,126,127,150,151,152,153,154,155,156,157,158,159,160,161,164,167,171,172,177,178,],[13,-12,42,-100,-12,-136,-137,13,13,13,-12,-12,-14,13,42,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,74,-100,-101,-102,-103,-104,-105,-106,13,-10,-11,-15,-49,-98,-99,-12,-138,-145,13,13,13,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-129,-141,-38,-39,-40,-109,-42,-43,13,-129,-131,-133,-139,13,-142,-41,156,-108,-130,-132,156,-112,-113,-115,-116,-121,-122,-117,-118,-119,-120,-124,-72,-107,-140,-141,-129,13,]),'CHAR':([0,3,11,12,13,14,15,16,17,20,21,22,23,24,25,26,27,30,31,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,63,67,68,72,74,78,79,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,102,103,104,105,115,116,117,118,119,120,121,122,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,150,151,152,153,154,155,156,157,158,159,160,161,164,166,167,171,172,173,174,175,176,178,179,],[14,-12,14,38,56,-23,-24,-25,-26,-12,-136,-137,14,14,14,-12,-12,14,14,38,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,56,-101,-102,-103,-104,-105,-106,14,-10,-11,-49,-98,-12,-138,-145,14,14,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-141,-38,-39,-40,-74,-109,-42,-43,-139,14,-142,-41,147,-73,157,-108,147,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,157,-112,-113,-115,-116,-121,-122,-117,-118,-119,-120,-124,-72,-95,-107,-140,-141,-97,-93,-95,-96,14,-94,]),'INTEGER':([0,3,11,12,14,15,16,17,20,21,22,23,24,25,26,27,29,30,31,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,63,67,68,69,72,74,78,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,109,110,111,113,115,116,117,118,126,127,161,164,167,171,172,177,178,],[15,-12,15,39,-23,-24,-25,-26,-12,-136,-137,15,15,15,-12,-12,-14,15,15,39,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,15,-10,-11,-15,-49,-98,-12,-138,-145,88,15,15,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-129,-141,-38,-39,-40,-42,-43,88,-129,-131,-133,-139,15,-142,-41,-130,-132,-124,-72,-107,-140,-141,-129,15,]),'MINUS':([0,3,11,12,14,15,16,17,20,21,22,23,24,25,26,27,30,31,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,63,67,68,72,74,78,79,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,104,105,115,116,117,118,161,164,167,171,172,178,],[16,-12,16,41,-23,-24,-25,-26,-12,-136,-137,16,16,16,-12,-12,16,16,41,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,16,-10,-11,-49,-98,-12,-138,-145,16,16,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-141,-38,-39,-40,-42,-43,-139,16,-142,-41,-124,-72,-107,-140,-141,16,]),'UNDERSCORE':([0,3,11,14,15,16,17,20,21,22,23,24,25,26,27,30,31,63,67,68,72,74,78,79,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,104,105,115,116,117,118,161,164,167,171,172,178,],[17,-12,17,-23,-24,-25,-26,-12,-136,-137,17,17,17,-12,-12,17,17,17,-10,-11,-49,-98,-12,-138,-145,17,17,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-141,-38,-39,-40,-42,-43,-139,17,-142,-41,-124,-72,-107,-140,-141,17,]),'WHITESPACE':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,69,70,71,72,74,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,110,111,113,115,118,119,120,121,122,123,125,126,127,128,129,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,150,151,152,153,154,155,156,157,158,159,160,161,162,164,166,167,170,171,172,173,174,175,176,177,179,180,181,],[29,-16,-17,-18,-19,-27,-28,-22,37,58,-23,-24,-25,-26,-22,-20,37,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,58,-101,-102,-103,-104,-105,-106,29,-31,-21,-49,-98,-29,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,111,117,-38,-39,-40,-74,-109,-42,-43,-31,111,111,-131,-133,-139,-41,146,-73,159,-108,-30,111,-130,-132,117,-144,146,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,159,-112,-113,-115,-116,-121,-122,-117,-118,-119,-120,-124,111,-72,176,-107,-126,-140,117,-97,-93,176,-96,111,-94,-128,-143,]),'IGUAL':([4,5,6,7,8,9,10,11,14,15,16,17,28,29,31,32,70,71,72,74,83,106,123,],[-15,-16,-17,-18,-19,-27,-28,-22,-23,-24,-25,-26,69,-14,-22,-20,-31,-21,-49,-98,-29,-31,-30,]),'FPR':([5,6,7,8,9,10,11,14,15,16,17,31,32,64,70,71,72,74,83,86,87,88,89,90,91,92,93,94,95,96,97,99,100,101,104,105,106,108,110,111,113,115,118,123,124,125,126,127,161,162,164,167,170,171,177,180,],[-16,-17,-18,-19,-27,-28,-22,-23,-24,-25,-26,-22,-20,79,-31,-21,-49,-98,-29,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-125,-38,-39,-40,-42,-43,-31,-129,-129,-131,-133,-139,-41,-30,161,-129,-130,-132,-124,-127,-72,-107,-126,-140,-125,-128,]),'ATC':([5,6,7,8,9,10,11,14,15,16,17,31,32,65,70,71,72,74,83,106,123,],[-16,-17,-18,-19,-27,-28,-22,-23,-24,-25,-26,-22,-20,80,-31,-21,-49,-98,-29,-31,-30,]),'DOT_SEP':([5,7,8,9,10,11,12,14,15,16,17,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,70,71,72,74,102,103,106,119,120,121,122,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,150,151,152,153,154,155,156,157,158,159,160,166,173,174,175,176,179,],[30,-18,-19,-27,-28,-22,43,-23,-24,-25,-26,-22,-20,43,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,82,-21,-49,-98,-74,-109,82,139,-73,158,-108,139,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,158,-112,-113,-115,-116,-121,-122,-117,-118,-119,-120,-95,-97,-93,-95,-96,-94,]),'FLOAT':([12,29,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,69,81,97,109,110,111,113,126,127,177,],[40,-14,40,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-15,92,-129,92,-129,-131,-133,-130,-132,-129,]),'TWODOT_SEP':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,119,120,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,166,173,174,175,176,179,],[44,59,44,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,59,-101,-102,-103,-104,-105,-106,-74,138,-73,138,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,-95,-97,-93,-95,-96,-94,]),'ESC_QUOTE':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,119,120,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,166,173,174,175,176,179,],[45,45,45,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,45,-101,-102,-103,-104,-105,-106,-74,45,-73,45,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,-95,-97,-93,-95,-96,-94,]),'ESC_REVERSE':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,119,120,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,166,173,174,175,176,179,],[46,46,46,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,46,-101,-102,-103,-104,-105,-106,-74,46,-73,46,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,-95,-97,-93,-95,-96,-94,]),'ESC_BACKSPACE':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,119,120,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,166,173,174,175,176,179,],[47,47,47,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,47,-101,-102,-103,-104,-105,-106,-74,47,-73,47,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,-95,-97,-93,-95,-96,-94,]),'ESC_FF':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,119,120,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,166,173,174,175,176,179,],[48,48,48,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,48,-101,-102,-103,-104,-105,-106,-74,48,-73,48,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,-95,-97,-93,-95,-96,-94,]),'ESC_NL':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,119,120,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,166,173,174,175,176,179,],[49,49,49,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,49,-101,-102,-103,-104,-105,-106,-74,49,-73,49,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,-95,-97,-93,-95,-96,-94,]),'ESC_CRETURN':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,119,120,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,166,173,174,175,176,179,],[50,50,50,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,50,-101,-102,-103,-104,-105,-106,-74,50,-73,50,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,-95,-97,-93,-95,-96,-94,]),'ESC_TAB':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,119,120,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,166,173,174,175,176,179,],[51,51,51,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,51,-101,-102,-103,-104,-105,-106,-74,51,-73,51,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,-95,-97,-93,-95,-96,-94,]),'ESC_HEX4':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,119,120,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,166,173,174,175,176,179,],[52,52,52,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,52,-101,-102,-103,-104,-105,-106,-74,52,-73,52,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,-95,-97,-93,-95,-96,-94,]),'ESC_HEX8':([12,13,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,119,120,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,166,173,174,175,176,179,],[53,53,53,-52,-53,-54,-55,-56,-57,-58,-59,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,53,-101,-102,-103,-104,-105,-106,-74,53,-73,53,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,-95,-97,-93,-95,-96,-94,]),'ESCAPE':([13,45,46,47,48,49,50,51,52,53,55,56,57,58,59,60,61,102,119,120,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,166,173,174,175,176,179,],[61,-63,-64,-65,-66,-67,-68,-69,-70,-71,61,-101,-102,-103,-104,-105,-106,-74,145,-73,145,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,-95,-97,-93,-95,-96,-94,]),'BOOLEAN':([29,69,81,97,109,110,111,113,126,127,177,],[-14,-15,87,-129,87,-129,-131,-133,-130,-132,-129,]),'ACH':([29,69,81,97,109,110,111,113,126,127,177,],[-14,-15,98,-129,98,-129,-131,-133,-130,-132,-129,]),'TRIPLEASPA':([29,45,46,47,48,49,50,51,52,53,69,81,97,102,109,110,111,113,119,120,126,127,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,165,166,173,174,175,176,177,179,],[-14,-63,-64,-65,-66,-67,-68,-69,-70,-71,-15,102,-129,-74,102,-129,-131,-133,-77,-73,-130,-132,164,-75,-77,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,-76,-95,-97,-93,-95,-96,-129,-94,]),'TRIPLEAPOSTROFE':([29,69,81,97,103,109,110,111,113,121,122,126,127,148,149,150,151,152,153,154,155,156,157,158,159,160,168,177,],[-14,-15,103,-129,-109,103,-129,-131,-133,-114,-108,-130,-132,167,-110,-114,-112,-113,-115,-116,-121,-122,-117,-118,-119,-120,-111,-129,]),'DATE':([29,69,81,97,109,110,111,113,126,127,177,],[-14,-15,104,-129,104,-129,-131,-133,-130,-132,-129,]),'TIME':([29,69,81,97,100,104,109,110,111,113,126,127,177,],[-14,-15,105,-129,105,-42,105,-129,-131,-133,-130,-132,-129,]),'VIRGULA':([45,46,47,48,49,50,51,52,53,72,74,85,86,87,88,89,90,91,92,93,94,95,96,99,100,101,102,103,104,105,110,111,113,115,117,118,119,120,121,122,125,126,127,128,129,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,166,167,169,171,173,174,175,176,179,181,],[-63,-64,-65,-66,-67,-68,-69,-70,-71,-49,-98,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,-38,-39,-40,-74,-109,-42,-43,-129,-131,-133,-139,-142,-41,140,-73,160,-108,-129,-130,-132,-141,-144,140,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,160,-112,-113,-115,-116,-121,-122,-117,-118,-119,-120,-124,-129,172,-72,-95,-107,177,-140,-97,-93,-95,-96,-94,-143,]),'DOUBLEASPA':([45,46,47,48,49,50,51,52,53,102,119,120,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,166,173,174,175,176,179,],[-63,-64,-65,-66,-67,-68,-69,-70,-71,-74,142,-73,142,-78,-79,-80,-81,-82,-83,-84,-85,-88,-89,-86,-87,-91,-92,-95,-97,-93,-95,-96,-94,]),'FCH':([72,74,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,104,105,115,117,118,128,129,161,163,164,167,171,181,],[-49,-98,-13,-32,-33,-34,-35,-36,-37,-44,-45,-46,-47,-48,115,-38,-39,-40,-42,-43,-139,-142,-41,-141,-144,-124,171,-72,-107,-140,-143,]),'DOUBLEAPOSTROFE':([103,121,122,150,151,152,153,154,155,156,157,158,159,160,],[-109,155,-108,155,-112,-113,-115,-116,-121,-122,-117,-118,-119,-120,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'TOML':([0,],[1,]),'TITLES':([0,25,],[2,66,]),'KVALUE':([0,25,63,84,116,178,],[3,3,78,78,129,181,]),'KEY':([0,23,24,25,63,84,116,178,],[4,64,65,4,4,4,4,4,]),'SIMPLEKEY':([0,23,24,25,30,63,82,84,116,178,],[5,5,5,5,70,5,106,5,5,5,]),'DOTKEY':([0,23,24,25,63,84,116,178,],[6,6,6,6,6,6,6,6,]),'QUOTEDKEY':([0,23,24,25,30,63,82,84,116,178,],[7,7,7,7,7,7,7,7,7,7,]),'UNQUOTEDKEY':([0,23,24,25,30,63,82,84,116,178,],[8,8,8,8,8,8,8,8,8,8,]),'BASICSTRING':([0,23,24,25,30,63,81,82,84,109,116,178,],[9,9,9,9,9,9,94,9,9,94,9,9,]),'LITERALSTRING':([0,23,24,25,30,63,81,82,84,109,116,178,],[10,10,10,10,10,10,96,10,10,96,10,10,]),'OCCURRENCES':([0,11,23,24,25,30,31,63,82,84,116,178,],[11,31,11,11,11,11,31,11,11,11,11,11,]),'GROUPS':([2,62,],[18,76,]),'SECCAO':([2,62,],[19,19,]),'TABLE':([2,62,],[20,20,]),'STDTABLE':([2,62,],[21,21,]),'TABLEARRAY':([2,62,],[22,22,]),'EXPRESSION':([3,19,20,26,27,78,],[25,62,63,67,68,84,]),'kvwhitespace':([4,69,],[28,81,]),'UNQUOTEDKEYAUX':([11,31,],[32,71,]),'BC':([12,34,],[33,73,]),'BASICCHAR':([12,34,],[34,34,]),'BASICUNESCAPED':([12,34,],[35,35,]),'ESCAPED':([12,13,34,55,119,132,],[36,57,36,57,144,144,]),'LCH':([13,55,],[54,75,]),'LITERALCHAR':([13,55,],[55,55,]),'ATRIBUICOES':([63,84,],[77,107,]),'DOTSIMPKEY':([70,106,],[83,123,]),'VALUE':([81,109,],[85,125,]),'STRING':([81,109,],[86,86,]),'ARRAY':([81,109,],[89,89,]),'INLINETABLE':([81,109,],[90,90,]),'DATETIME':([81,109,],[91,91,]),'MULTILINEBASICSTRING':([81,109,],[93,93,]),'MLLITERALSTRING':([81,109,],[95,95,]),'LOCALDATETIME':([81,109,],[99,99,]),'LOCALDATE':([81,109,],[100,100,]),'LOCALTIME':([81,100,109,],[101,118,101,]),'ARRAYVALUES':([97,177,],[108,180,]),'WSCOMMENTNEWLINE':([97,108,110,125,162,177,],[109,124,126,162,169,109,]),'INNERCOMMENT':([97,108,110,125,162,177,],[110,110,110,110,110,110,]),'COMMENTOUNAO':([97,108,110,125,162,177,],[112,112,112,112,112,112,]),'INLINETABLEWS':([98,128,172,],[116,163,178,]),'MLNL':([102,],[119,]),'NLR':([103,],[121,]),'INLINEKVALUE':([116,],[128,]),'MLBASICBODY':([119,],[130,]),'MLBC':([119,132,],[131,165,]),'CONTENTQUOTE':([119,132,],[132,132,]),'MLBCONTENT':([119,132,],[133,133,]),'MLBQUOTES':([119,132,],[134,134,]),'MLBCHAR':([119,132,],[135,135,]),'MLBESCAPEDNL':([119,132,],[137,137,]),'MLBUNESCAPED':([119,132,],[143,143,]),'MLLITERALBODY':([121,],[148,]),'MLLC':([121,150,],[149,168,]),'MLLCONTENTQUOTES':([121,150,],[150,150,]),'MLLCONTENT':([121,150,],[151,151,]),'MLLQUOTES':([121,150,],[152,152,]),'MLLCHAR':([121,150,],[153,153,]),'ARRAYCONTEUDO':([162,],[170,]),'WHNL':([166,175,],[174,179,]),'SPACENEWLINE':([166,175,],[175,175,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> TOML","S'",1,None,None,None),
  ('TOML -> TITLES GROUPS','TOML',2,'p_TOML','tomyacc.py',7),
  ('TITLES -> KVALUE EXPRESSION TITLES','TITLES',3,'p_TITLES1','tomyacc.py',12),
  ('TITLES -> <empty>','TITLES',0,'p_TITLES2','tomyacc.py',17),
  ('GROUPS -> SECCAO EXPRESSION GROUPS','GROUPS',3,'p_GROUPS1','tomyacc.py',21),
  ('GROUPS -> <empty>','GROUPS',0,'p_GROUPS2','tomyacc.py',26),
  ('SECCAO -> TABLE EXPRESSION ATRIBUICOES','SECCAO',3,'p_SECCAO1','tomyacc.py',30),
  ('SECCAO -> <empty>','SECCAO',0,'p_SECCAO2','tomyacc.py',37),
  ('ATRIBUICOES -> KVALUE EXPRESSION ATRIBUICOES','ATRIBUICOES',3,'p_ATRIBUICOES1','tomyacc.py',41),
  ('ATRIBUICOES -> <empty>','ATRIBUICOES',0,'p_ATRIBUICOES2','tomyacc.py',46),
  ('EXPRESSION -> COMMENT EXPRESSION','EXPRESSION',2,'p_EXPRESSION1','tomyacc.py',50),
  ('EXPRESSION -> NEWLINE EXPRESSION','EXPRESSION',2,'p_EXPRESSION2','tomyacc.py',54),
  ('EXPRESSION -> <empty>','EXPRESSION',0,'p_EXPRESSION3','tomyacc.py',58),
  ('KVALUE -> KEY kvwhitespace IGUAL kvwhitespace VALUE','KVALUE',5,'p_KVALUE','tomyacc.py',62),
  ('kvwhitespace -> WHITESPACE','kvwhitespace',1,'p_kvwhitespace1','tomyacc.py',70),
  ('kvwhitespace -> <empty>','kvwhitespace',0,'p_kvwhitespace2','tomyacc.py',74),
  ('KEY -> SIMPLEKEY','KEY',1,'p_KEY1','tomyacc.py',78),
  ('KEY -> DOTKEY','KEY',1,'p_KEY2','tomyacc.py',82),
  ('SIMPLEKEY -> QUOTEDKEY','SIMPLEKEY',1,'p_SIMPLEKEY1','tomyacc.py',87),
  ('SIMPLEKEY -> UNQUOTEDKEY','SIMPLEKEY',1,'p_SIMPLEKEY2','tomyacc.py',91),
  ('UNQUOTEDKEY -> OCCURRENCES UNQUOTEDKEYAUX','UNQUOTEDKEY',2,'p_UNQUOTEDKEY1','tomyacc.py',96),
  ('UNQUOTEDKEYAUX -> OCCURRENCES UNQUOTEDKEYAUX','UNQUOTEDKEYAUX',2,'p_UNQUOTEDKEY2','tomyacc.py',101),
  ('UNQUOTEDKEYAUX -> <empty>','UNQUOTEDKEYAUX',0,'p_UNQUOTEDKEY3','tomyacc.py',106),
  ('OCCURRENCES -> CHAR','OCCURRENCES',1,'p_OCCURRENCES1','tomyacc.py',110),
  ('OCCURRENCES -> INTEGER','OCCURRENCES',1,'p_OCCURRENCES2','tomyacc.py',114),
  ('OCCURRENCES -> MINUS','OCCURRENCES',1,'p_OCCURRENCES3','tomyacc.py',119),
  ('OCCURRENCES -> UNDERSCORE','OCCURRENCES',1,'p_OCCURRENCES4','tomyacc.py',124),
  ('QUOTEDKEY -> BASICSTRING','QUOTEDKEY',1,'p_QUOTEDKEY1','tomyacc.py',129),
  ('QUOTEDKEY -> LITERALSTRING','QUOTEDKEY',1,'p_QUOTEDKEY2','tomyacc.py',134),
  ('DOTKEY -> SIMPLEKEY DOT_SEP SIMPLEKEY DOTSIMPKEY','DOTKEY',4,'p_DOTKEY','tomyacc.py',138),
  ('DOTSIMPKEY -> DOT_SEP SIMPLEKEY DOTSIMPKEY','DOTSIMPKEY',3,'p_DOTSIMPKEY1','tomyacc.py',142),
  ('DOTSIMPKEY -> <empty>','DOTSIMPKEY',0,'p_DOTSIMPKEY2','tomyacc.py',147),
  ('VALUE -> STRING','VALUE',1,'p_VALUE1','tomyacc.py',151),
  ('VALUE -> BOOLEAN','VALUE',1,'p_VALUE2','tomyacc.py',156),
  ('VALUE -> INTEGER','VALUE',1,'p_VALUE3','tomyacc.py',160),
  ('VALUE -> ARRAY','VALUE',1,'p_VALUE4','tomyacc.py',164),
  ('VALUE -> INLINETABLE','VALUE',1,'p_VALUE5','tomyacc.py',168),
  ('VALUE -> DATETIME','VALUE',1,'p_VALUE6','tomyacc.py',173),
  ('DATETIME -> LOCALDATETIME','DATETIME',1,'p_DATETIME1','tomyacc.py',177),
  ('DATETIME -> LOCALDATE','DATETIME',1,'p_DATETIME2','tomyacc.py',181),
  ('DATETIME -> LOCALTIME','DATETIME',1,'p_DATETIME3','tomyacc.py',185),
  ('LOCALDATETIME -> LOCALDATE LOCALTIME','LOCALDATETIME',2,'p_LOCALDATETIME','tomyacc.py',189),
  ('LOCALDATE -> DATE','LOCALDATE',1,'p_LOCALDATE','tomyacc.py',193),
  ('LOCALTIME -> TIME','LOCALTIME',1,'p_LOCALTIME','tomyacc.py',197),
  ('VALUE -> FLOAT','VALUE',1,'p_VALUE7','tomyacc.py',201),
  ('STRING -> MULTILINEBASICSTRING','STRING',1,'p_STRING1','tomyacc.py',207),
  ('STRING -> BASICSTRING','STRING',1,'p_STRING2','tomyacc.py',212),
  ('STRING -> MLLITERALSTRING','STRING',1,'p_STRING3','tomyacc.py',217),
  ('STRING -> LITERALSTRING','STRING',1,'p_STRING4','tomyacc.py',221),
  ('BASICSTRING -> ASPA BC ASPA','BASICSTRING',3,'p_BASICSTRING','tomyacc.py',226),
  ('BC -> BASICCHAR BC','BC',2,'p_BC','tomyacc.py',231),
  ('BC -> <empty>','BC',0,'p_BC2','tomyacc.py',235),
  ('BASICCHAR -> BASICUNESCAPED','BASICCHAR',1,'p_BASICCHAR1','tomyacc.py',239),
  ('BASICCHAR -> ESCAPED','BASICCHAR',1,'p_BASICCHAR2','tomyacc.py',244),
  ('BASICUNESCAPED -> WHITESPACE','BASICUNESCAPED',1,'p_BASICUNESCAPED1','tomyacc.py',248),
  ('BASICUNESCAPED -> CHAR','BASICUNESCAPED',1,'p_BASICUNESCAPED2','tomyacc.py',252),
  ('BASICUNESCAPED -> INTEGER','BASICUNESCAPED',1,'p_BASICUNESCAPED3','tomyacc.py',256),
  ('BASICUNESCAPED -> FLOAT','BASICUNESCAPED',1,'p_BASICUNESCAPED4','tomyacc.py',260),
  ('BASICUNESCAPED -> MINUS','BASICUNESCAPED',1,'p_BASICUNESCAPED5','tomyacc.py',264),
  ('BASICUNESCAPED -> APOSTROFE','BASICUNESCAPED',1,'p_BASICUNESCAPED6','tomyacc.py',268),
  ('BASICUNESCAPED -> ESCAPED','BASICUNESCAPED',1,'p_BASICUNESCAPED7','tomyacc.py',272),
  ('BASICUNESCAPED -> DOT_SEP','BASICUNESCAPED',1,'p_BASICUNESCAPED8','tomyacc.py',276),
  ('BASICUNESCAPED -> TWODOT_SEP','BASICUNESCAPED',1,'p_BASICUNESCAPED9','tomyacc.py',280),
  ('ESCAPED -> ESC_QUOTE','ESCAPED',1,'p_ESCAPED1','tomyacc.py',286),
  ('ESCAPED -> ESC_REVERSE','ESCAPED',1,'p_ESCAPED2','tomyacc.py',291),
  ('ESCAPED -> ESC_BACKSPACE','ESCAPED',1,'p_ESCAPED3','tomyacc.py',296),
  ('ESCAPED -> ESC_FF','ESCAPED',1,'p_ESCAPED4','tomyacc.py',301),
  ('ESCAPED -> ESC_NL','ESCAPED',1,'p_ESCAPED5','tomyacc.py',306),
  ('ESCAPED -> ESC_CRETURN','ESCAPED',1,'p_ESCAPED6','tomyacc.py',311),
  ('ESCAPED -> ESC_TAB','ESCAPED',1,'p_ESCAPED7','tomyacc.py',316),
  ('ESCAPED -> ESC_HEX4','ESCAPED',1,'p_ESCAPED8','tomyacc.py',321),
  ('ESCAPED -> ESC_HEX8','ESCAPED',1,'p_ESCAPED9','tomyacc.py',326),
  ('MULTILINEBASICSTRING -> TRIPLEASPA MLNL MLBASICBODY TRIPLEASPA','MULTILINEBASICSTRING',4,'p_MULTILINEBASICSTRING','tomyacc.py',331),
  ('MLNL -> NEWLINE','MLNL',1,'p_MLNL1','tomyacc.py',335),
  ('MLNL -> <empty>','MLNL',0,'p_MLNL2','tomyacc.py',339),
  ('MLBASICBODY -> MLBC','MLBASICBODY',1,'p_MLBASICBODY','tomyacc.py',343),
  ('MLBC -> CONTENTQUOTE MLBC','MLBC',2,'p_MLBC1','tomyacc.py',347),
  ('MLBC -> <empty>','MLBC',0,'p_MLBC2','tomyacc.py',351),
  ('CONTENTQUOTE -> MLBCONTENT','CONTENTQUOTE',1,'p_CONTENTQUOTE1','tomyacc.py',355),
  ('CONTENTQUOTE -> MLBQUOTES','CONTENTQUOTE',1,'p_CONTENTQUOTE2','tomyacc.py',359),
  ('MLBCONTENT -> MLBCHAR','MLBCONTENT',1,'p_MLBCONTENT1','tomyacc.py',363),
  ('MLBCONTENT -> NEWLINE','MLBCONTENT',1,'p_MLBCONTENT2','tomyacc.py',367),
  ('MLBCONTENT -> MLBESCAPEDNL','MLBCONTENT',1,'p_MLBCONTENT3','tomyacc.py',371),
  ('MLBCONTENT -> TWODOT_SEP','MLBCONTENT',1,'p_MLBCONTENT4','tomyacc.py',375),
  ('MLBCONTENT -> DOT_SEP','MLBCONTENT',1,'p_MLBCONTENT5','tomyacc.py',379),
  ('MLBCONTENT -> VIRGULA','MLBCONTENT',1,'p_MLBCONTENT6','tomyacc.py',383),
  ('MLBCHAR -> MLBUNESCAPED','MLBCHAR',1,'p_MLBCHAR1','tomyacc.py',387),
  ('MLBCHAR -> ESCAPED','MLBCHAR',1,'p_MLBCHAR2','tomyacc.py',391),
  ('MLBQUOTES -> ASPA','MLBQUOTES',1,'p_MLBQUOTES1','tomyacc.py',395),
  ('MLBQUOTES -> DOUBLEASPA','MLBQUOTES',1,'p_MLBQUOTES2','tomyacc.py',399),
  ('MLBQUOTES -> <empty>','MLBQUOTES',0,'p_MLBQUOTES3','tomyacc.py',403),
  ('MLBUNESCAPED -> WHITESPACE','MLBUNESCAPED',1,'p_MLBUNESCAPED1','tomyacc.py',407),
  ('MLBUNESCAPED -> CHAR','MLBUNESCAPED',1,'p_MLBUNESCAPED2','tomyacc.py',411),
  ('MLBESCAPEDNL -> ESCAPE NEWLINE WHNL','MLBESCAPEDNL',3,'p_MLBESCAPEDNL','tomyacc.py',415),
  ('WHNL -> SPACENEWLINE WHNL','WHNL',2,'p_WHNL1','tomyacc.py',420),
  ('WHNL -> <empty>','WHNL',0,'p_WHNL2','tomyacc.py',424),
  ('SPACENEWLINE -> WHITESPACE','SPACENEWLINE',1,'p_SPACENEWLINE1','tomyacc.py',428),
  ('SPACENEWLINE -> NEWLINE','SPACENEWLINE',1,'p_SPACENEWLINE2','tomyacc.py',432),
  ('LITERALSTRING -> APOSTROFE LCH APOSTROFE','LITERALSTRING',3,'p_LITERALSTRING','tomyacc.py',436),
  ('LCH -> LITERALCHAR LCH','LCH',2,'p_LCH1','tomyacc.py',441),
  ('LCH -> <empty>','LCH',0,'p_LCH2','tomyacc.py',445),
  ('LITERALCHAR -> CHAR','LITERALCHAR',1,'p_LITERALCHAR1','tomyacc.py',449),
  ('LITERALCHAR -> ESCAPED','LITERALCHAR',1,'p_LITERALCHAR2','tomyacc.py',453),
  ('LITERALCHAR -> WHITESPACE','LITERALCHAR',1,'p_LITERALCHAR3','tomyacc.py',457),
  ('LITERALCHAR -> TWODOT_SEP','LITERALCHAR',1,'p_LITERALCHAR4','tomyacc.py',461),
  ('LITERALCHAR -> ASPA','LITERALCHAR',1,'p_LITERALCHAR5','tomyacc.py',465),
  ('LITERALCHAR -> ESCAPE','LITERALCHAR',1,'p_LITERALCHAR6','tomyacc.py',469),
  ('MLLITERALSTRING -> TRIPLEAPOSTROFE NLR MLLITERALBODY TRIPLEAPOSTROFE','MLLITERALSTRING',4,'p_MLLITERALSTRING','tomyacc.py',473),
  ('NLR -> NEWLINE','NLR',1,'p_NLR1','tomyacc.py',477),
  ('NLR -> <empty>','NLR',0,'p_NLR2','tomyacc.py',481),
  ('MLLITERALBODY -> MLLC','MLLITERALBODY',1,'p_MLLITERALBODY','tomyacc.py',485),
  ('MLLC -> MLLCONTENTQUOTES MLLC','MLLC',2,'p_MLLC1','tomyacc.py',489),
  ('MLLCONTENTQUOTES -> MLLCONTENT','MLLCONTENTQUOTES',1,'p_MLLCONTENTQUOTES1','tomyacc.py',493),
  ('MLLCONTENTQUOTES -> MLLQUOTES','MLLCONTENTQUOTES',1,'p_MLLCONTENTQUOTES2','tomyacc.py',497),
  ('MLLC -> <empty>','MLLC',0,'p_MLLC2','tomyacc.py',501),
  ('MLLCONTENT -> MLLCHAR','MLLCONTENT',1,'p_MLLCONTENT1','tomyacc.py',505),
  ('MLLCONTENT -> NEWLINE','MLLCONTENT',1,'p_MLLCONTENT2','tomyacc.py',509),
  ('MLLCHAR -> CHAR','MLLCHAR',1,'p_MLLCHAR1','tomyacc.py',513),
  ('MLLCHAR -> DOT_SEP','MLLCHAR',1,'p_MLLCHAR2','tomyacc.py',517),
  ('MLLCHAR -> WHITESPACE','MLLCHAR',1,'p_MLLCHAR3','tomyacc.py',521),
  ('MLLCHAR -> VIRGULA','MLLCHAR',1,'p_MLLCHAR4','tomyacc.py',525),
  ('MLLQUOTES -> DOUBLEAPOSTROFE','MLLQUOTES',1,'p_MLLQUOTES1','tomyacc.py',529),
  ('MLLQUOTES -> APOSTROFE','MLLQUOTES',1,'p_MLLQUOTES2','tomyacc.py',533),
  ('MLLQUOTES -> <empty>','MLLQUOTES',0,'p_MLLQUOTES3','tomyacc.py',541),
  ('ARRAY -> APR ARRAYVALUES WSCOMMENTNEWLINE FPR','ARRAY',4,'p_ARRAY','tomyacc.py',545),
  ('ARRAYVALUES -> <empty>','ARRAYVALUES',0,'p_ARRAYVALUES1','tomyacc.py',549),
  ('ARRAYVALUES -> WSCOMMENTNEWLINE VALUE WSCOMMENTNEWLINE ARRAYCONTEUDO','ARRAYVALUES',4,'p_ARRAYVALUES2','tomyacc.py',553),
  ('ARRAYCONTEUDO -> <empty>','ARRAYCONTEUDO',0,'p_ARRAYVALUES3','tomyacc.py',559),
  ('ARRAYCONTEUDO -> WSCOMMENTNEWLINE VIRGULA ARRAYVALUES','ARRAYCONTEUDO',3,'p_ARRAYVALUES4','tomyacc.py',563),
  ('WSCOMMENTNEWLINE -> <empty>','WSCOMMENTNEWLINE',0,'p_WSCOMMENTNEWLINE1','tomyacc.py',567),
  ('WSCOMMENTNEWLINE -> INNERCOMMENT WSCOMMENTNEWLINE','WSCOMMENTNEWLINE',2,'p_WSCOMMENTNEWLINE2','tomyacc.py',572),
  ('INNERCOMMENT -> WHITESPACE','INNERCOMMENT',1,'p_INNERCOMMENT1','tomyacc.py',575),
  ('INNERCOMMENT -> COMMENTOUNAO NEWLINE','INNERCOMMENT',2,'p_INNERCOMMENT2','tomyacc.py',578),
  ('INNERCOMMENT -> NEWLINE','INNERCOMMENT',1,'p_INNERCOMMENT3','tomyacc.py',581),
  ('COMMENTOUNAO -> COMMENT','COMMENTOUNAO',1,'p_COMMENTOUNAO1','tomyacc.py',584),
  ('COMMENTOUNAO -> <empty>','COMMENTOUNAO',0,'p_COMMENTOUNAO2','tomyacc.py',588),
  ('TABLE -> STDTABLE','TABLE',1,'p_TABLE1','tomyacc.py',591),
  ('TABLE -> TABLEARRAY','TABLE',1,'p_TABLE2','tomyacc.py',595),
  ('STDTABLE -> APR KEY FPR','STDTABLE',3,'p_STDTABLE','tomyacc.py',599),
  ('INLINETABLE -> ACH FCH','INLINETABLE',2,'p_INLINETABLE','tomyacc.py',607),
  ('INLINETABLE -> ACH INLINETABLEWS INLINEKVALUE INLINETABLEWS FCH','INLINETABLE',5,'p_INLINETABLE2','tomyacc.py',611),
  ('INLINETABLEWS -> <empty>','INLINETABLEWS',0,'p_INLINETABLEWS1','tomyacc.py',615),
  ('INLINETABLEWS -> WHITESPACE','INLINETABLEWS',1,'p_INLINETABLEWS2','tomyacc.py',618),
  ('INLINEKVALUE -> INLINEKVALUE INLINETABLEWS VIRGULA INLINETABLEWS KVALUE','INLINEKVALUE',5,'p_INLINEKVALUE','tomyacc.py',621),
  ('INLINEKVALUE -> KVALUE','INLINEKVALUE',1,'p_INLINEKVALUE2','tomyacc.py',627),
  ('TABLEARRAY -> ATO KEY ATC','TABLEARRAY',3,'p_TABLEARRAY1','tomyacc.py',631),
]