__author__ = 'v-mudrak-8l'

class JSConstants:

    operators = "!= !== % & && * ** + - / : < << <= == === > >= >> >>> ? ^ | || =".split(' ')

    #                   Read the keywordDictionary key-value pair below as:
    #                   --------------------------------------------------
    # 'keyword' : [(requires newline)?True:False, [(array of disqualifiers for new line with offset)]
    #                                                           offset here is minus any whitespaces
    keywordDictionary = {
                   'abstract'       :   [True],
                   'async'          :   [True],
                   'arguments'      :   [False, ['(', -1]],
                   'boolean'        :   [False, ['(', -1]],
                   'break'          :   [True],
                   'byte'           :   [False, ['(', -1]],
                   'case'           :   [True],
                   'catch'          :   [True],
                   'const'          :   [True],
                   'continue'       :   [True],
                   'debugger'       :   [True],
                   'default'        :   [True],
                   'delete'         :   [True],
                   'do'             :   [True],
                   'double'         :   [False, ['(', -1]],
                   'else'           :   [True],
                   'enum'           :   [False, ['(', -1]],
                   'eval'           :   [False, ['(', -1]],
                   'export'         :   [True],
                   'extends'        :   [False],
                   'false'          :   [False],
                   'final'          :   [False, ['(', -1]],
                   'finally'        :   [True],
                   'float'          :   [False, ['(', -1]],
                   'for'            :   [True],
                   'function'       :   [True],
                   'goto'           :   [True],
                   'if'             :   [True],
                   'implements'     :   [False],
                   'import'         :   [True],
                   'in'             :   [False],
                   'instanceof'     :   [False],
                   'int'            :   [False, ['(', -1]],
                   'interface'      :   [True],
                   'let'            :   [True],
                   'long'           :   [False, ['(', -1]],
                   'native'         :   [False, ['(', -1]],
                   'new'            :   [False, ['(', -1]],
                   'null'           :   [True],
                   'package'        :   [True],
                   'private'        :   [False, ['(', -1]],
                   'protected'      :   [False, ['(', -1]],
                   'public'         :   [False, ['(', -1]],
                   'return'         :   [True],
                   'short'          :   [False, ['(', -1]],
                   'static'         :   [False, ['(', -1]],
                   'super'          :   [False, ['(', -1]],
                   'switch'         :   [True],
                   'synchronized'   :   [False, ['(', -1]],
                   'this'           :   [False, ['(', -1]],
                   'throw'          :   [True],
                   'throws'         :   [False],
                   'transient'      :   [False, ['(', -1]],
                   'true'           :   [False],
                   'try'            :   [True],
                   'typeof'         :   [False],
                   'var'            :   [True],
                   'void'           :   [True],
                   'volatile'       :   [True],
                   'while'          :   [True],
                   'with'           :   [True],
                   'yield'          :   [True]
                   }
    openCurl = '{'
    closeCurl = '}'
    openSquare = '['
    closeSquare = ']'
    openRound = '('
    closeRound = ')'
    lineEnders = {'}' : -1,';' : 1}