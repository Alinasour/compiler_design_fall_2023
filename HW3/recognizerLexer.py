# Generated from HW3/recognizer.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3\34")
        buf.write("\n\3\r\3\16\3\35\3\3\3\3\6\3\"\n\3\r\3\16\3#\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\5\4.\n\4\3\5\6\5\61\n\5\r\5\16")
        buf.write("\5\62\3\5\3\5\6\5\67\n\5\r\5\16\58\5\5;\n\5\3\6\3\6\6")
        buf.write("\6?\n\6\r\6\16\6@\3\6\3\6\6\6E\n\6\r\6\16\6F\7\6I\n\6")
        buf.write("\f\6\16\6L\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\6")
        buf.write("\7W\n\7\r\7\16\7X\3\b\6\b\\\n\b\r\b\16\b]\3\b\3\b\2\2")
        buf.write("\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2\t\3\2\62;\3\2))\t")
        buf.write("\2\'\'--/\60\62;C\\aac|\3\2BB\6\2/\60\62;C\\c|\4\2C\\")
        buf.write("c|\4\2\13\13\"\"\2k\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3")
        buf.write("\21\3\2\2\2\5\33\3\2\2\2\7)\3\2\2\2\t\60\3\2\2\2\13<\3")
        buf.write("\2\2\2\rM\3\2\2\2\17[\3\2\2\2\21\22\t\2\2\2\22\23\b\2")
        buf.write("\2\2\23\24\t\3\2\2\24\25\t\2\2\2\25\26\b\2\3\2\26\27\t")
        buf.write("\3\2\2\27\30\t\2\2\2\30\31\b\2\4\2\31\4\3\2\2\2\32\34")
        buf.write("\t\4\2\2\33\32\3\2\2\2\34\35\3\2\2\2\35\33\3\2\2\2\35")
        buf.write("\36\3\2\2\2\36\37\3\2\2\2\37!\t\5\2\2 \"\t\6\2\2! \3\2")
        buf.write("\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\13\2\2")
        buf.write("\2&\'\t\7\2\2\'(\b\3\5\2(\6\3\2\2\2)*\t\2\2\2*-\b\4\6")
        buf.write("\2+,\t\2\2\2,.\b\4\7\2-+\3\2\2\2-.\3\2\2\2.\b\3\2\2\2")
        buf.write("/\61\t\2\2\2\60/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62")
        buf.write("\63\3\2\2\2\63:\3\2\2\2\64\66\13\2\2\2\65\67\t\2\2\2\66")
        buf.write("\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29;\3\2\2")
        buf.write("\2:\64\3\2\2\2:;\3\2\2\2;\n\3\2\2\2<>\7x\2\2=?\t\2\2\2")
        buf.write(">=\3\2\2\2?@\3\2\2\2@>\3\2\2\2@A\3\2\2\2AJ\3\2\2\2BD\13")
        buf.write("\2\2\2CE\t\2\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2")
        buf.write("\2GI\3\2\2\2HB\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2K")
        buf.write("\f\3\2\2\2LJ\3\2\2\2MN\7j\2\2NO\7v\2\2OP\7v\2\2PQ\7r\2")
        buf.write("\2QR\7<\2\2RS\7\61\2\2ST\7\61\2\2TV\3\2\2\2UW\t\6\2\2")
        buf.write("VU\3\2\2\2WX\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y\16\3\2\2\2Z")
        buf.write("\\\t\b\2\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^_")
        buf.write("\3\2\2\2_`\b\b\b\2`\20\3\2\2\2\16\2\35#-\628:@FJX]\t\3")
        buf.write("\2\2\3\2\3\3\2\4\3\3\5\3\4\6\3\4\7\b\2\2")
        return buf.getvalue()


class recognizerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NATIONAL_NUMBER = 1
    EMAIL = 2
    POSTAL_CODE = 3
    DECIMAL_NUMBER = 4
    SOFTWARE_VERSION = 5
    WEBSITE_ADDRESS = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "NATIONAL_NUMBER", "EMAIL", "POSTAL_CODE", "DECIMAL_NUMBER", 
            "SOFTWARE_VERSION", "WEBSITE_ADDRESS", "WS" ]

    ruleNames = [ "NATIONAL_NUMBER", "EMAIL", "POSTAL_CODE", "DECIMAL_NUMBER", 
                  "SOFTWARE_VERSION", "WEBSITE_ADDRESS", "WS" ]

    grammarFileName = "recognizer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.NATIONAL_NUMBER_action 
            actions[1] = self.EMAIL_action 
            actions[2] = self.POSTAL_CODE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NATIONAL_NUMBER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            3
     

        if actionIndex == 1:
            2
     

        if actionIndex == 2:
            4
     

    def EMAIL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            2,
     

    def POSTAL_CODE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            5
     

        if actionIndex == 5:
            4
     


