# Generated from HW3/sdf.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("_\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3\32\n\3\r")
        buf.write("\3\16\3\33\3\3\3\3\6\3 \n\3\r\3\16\3!\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\5\4,\n\4\3\5\6\5/\n\5\r\5\16\5\60\3\5")
        buf.write("\3\5\6\5\65\n\5\r\5\16\5\66\5\59\n\5\3\6\3\6\6\6=\n\6")
        buf.write("\r\6\16\6>\3\6\3\6\6\6C\n\6\r\6\16\6D\7\6G\n\6\f\6\16")
        buf.write("\6J\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\6\7U\n\7")
        buf.write("\r\7\16\7V\3\b\6\bZ\n\b\r\b\16\b[\3\b\3\b\2\2\t\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\3\2\b\3\2\62;\t\2\'\'--/\60\62")
        buf.write(";C\\aac|\3\2BB\6\2/\60\62;C\\c|\4\2C\\c|\4\2\13\13\"\"")
        buf.write("\2i\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5\31")
        buf.write("\3\2\2\2\7\'\3\2\2\2\t.\3\2\2\2\13:\3\2\2\2\rK\3\2\2\2")
        buf.write("\17Y\3\2\2\2\21\22\t\2\2\2\22\23\b\2\2\2\23\24\t\2\2\2")
        buf.write("\24\25\b\2\3\2\25\26\t\2\2\2\26\27\b\2\4\2\27\4\3\2\2")
        buf.write("\2\30\32\t\3\2\2\31\30\3\2\2\2\32\33\3\2\2\2\33\31\3\2")
        buf.write("\2\2\33\34\3\2\2\2\34\35\3\2\2\2\35\37\t\4\2\2\36 \t\5")
        buf.write("\2\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"")
        buf.write("#\3\2\2\2#$\13\2\2\2$%\t\6\2\2%&\b\3\5\2&\6\3\2\2\2\'")
        buf.write("(\t\2\2\2(+\b\4\6\2)*\t\2\2\2*,\b\4\7\2+)\3\2\2\2+,\3")
        buf.write("\2\2\2,\b\3\2\2\2-/\t\2\2\2.-\3\2\2\2/\60\3\2\2\2\60.")
        buf.write("\3\2\2\2\60\61\3\2\2\2\618\3\2\2\2\62\64\13\2\2\2\63\65")
        buf.write("\t\2\2\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66")
        buf.write("\67\3\2\2\2\679\3\2\2\28\62\3\2\2\289\3\2\2\29\n\3\2\2")
        buf.write("\2:<\7x\2\2;=\t\2\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?")
        buf.write("\3\2\2\2?H\3\2\2\2@B\13\2\2\2AC\t\2\2\2BA\3\2\2\2CD\3")
        buf.write("\2\2\2DB\3\2\2\2DE\3\2\2\2EG\3\2\2\2F@\3\2\2\2GJ\3\2\2")
        buf.write("\2HF\3\2\2\2HI\3\2\2\2I\f\3\2\2\2JH\3\2\2\2KL\7j\2\2L")
        buf.write("M\7v\2\2MN\7v\2\2NO\7r\2\2OP\7<\2\2PQ\7\61\2\2QR\7\61")
        buf.write("\2\2RT\3\2\2\2SU\t\5\2\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2\2")
        buf.write("VW\3\2\2\2W\16\3\2\2\2XZ\t\7\2\2YX\3\2\2\2Z[\3\2\2\2[")
        buf.write("Y\3\2\2\2[\\\3\2\2\2\\]\3\2\2\2]^\b\b\b\2^\20\3\2\2\2")
        buf.write("\16\2\33!+\60\668>DHV[\t\3\2\2\3\2\3\3\2\4\3\3\5\3\4\6")
        buf.write("\3\4\7\b\2\2")
        return buf.getvalue()


class sdfLexer(Lexer):

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

    grammarFileName = "sdf.g4"

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
     


