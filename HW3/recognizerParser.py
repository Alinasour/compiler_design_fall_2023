# Generated from HW3/recognizer.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\f\4\2\t\2\3\2\6\2\6\n\2\r\2\16\2\7\3\2\3\2\3\2\2\2\3")
        buf.write("\2\2\3\3\2\3\b\2\13\2\5\3\2\2\2\4\6\t\2\2\2\5\4\3\2\2")
        buf.write("\2\6\7\3\2\2\2\7\5\3\2\2\2\7\b\3\2\2\2\b\t\3\2\2\2\t\n")
        buf.write("\7\2\2\3\n\3\3\2\2\2\3\7")
        return buf.getvalue()


class recognizerParser ( Parser ):

    grammarFileName = "recognizer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "NATIONAL_NUMBER", "EMAIL", "POSTAL_CODE", 
                      "DECIMAL_NUMBER", "SOFTWARE_VERSION", "WEBSITE_ADDRESS", 
                      "WS" ]

    RULE_startRule = 0

    ruleNames =  [ "startRule" ]

    EOF = Token.EOF
    NATIONAL_NUMBER=1
    EMAIL=2
    POSTAL_CODE=3
    DECIMAL_NUMBER=4
    SOFTWARE_VERSION=5
    WEBSITE_ADDRESS=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(recognizerParser.EOF, 0)

        def NATIONAL_NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(recognizerParser.NATIONAL_NUMBER)
            else:
                return self.getToken(recognizerParser.NATIONAL_NUMBER, i)

        def EMAIL(self, i:int=None):
            if i is None:
                return self.getTokens(recognizerParser.EMAIL)
            else:
                return self.getToken(recognizerParser.EMAIL, i)

        def POSTAL_CODE(self, i:int=None):
            if i is None:
                return self.getTokens(recognizerParser.POSTAL_CODE)
            else:
                return self.getToken(recognizerParser.POSTAL_CODE, i)

        def DECIMAL_NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(recognizerParser.DECIMAL_NUMBER)
            else:
                return self.getToken(recognizerParser.DECIMAL_NUMBER, i)

        def SOFTWARE_VERSION(self, i:int=None):
            if i is None:
                return self.getTokens(recognizerParser.SOFTWARE_VERSION)
            else:
                return self.getToken(recognizerParser.SOFTWARE_VERSION, i)

        def WEBSITE_ADDRESS(self, i:int=None):
            if i is None:
                return self.getTokens(recognizerParser.WEBSITE_ADDRESS)
            else:
                return self.getToken(recognizerParser.WEBSITE_ADDRESS, i)

        def getRuleIndex(self):
            return recognizerParser.RULE_startRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartRule" ):
                listener.enterStartRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartRule" ):
                listener.exitStartRule(self)




    def startRule(self):

        localctx = recognizerParser.StartRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_startRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << recognizerParser.NATIONAL_NUMBER) | (1 << recognizerParser.EMAIL) | (1 << recognizerParser.POSTAL_CODE) | (1 << recognizerParser.DECIMAL_NUMBER) | (1 << recognizerParser.SOFTWARE_VERSION) | (1 << recognizerParser.WEBSITE_ADDRESS))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 5 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << recognizerParser.NATIONAL_NUMBER) | (1 << recognizerParser.EMAIL) | (1 << recognizerParser.POSTAL_CODE) | (1 << recognizerParser.DECIMAL_NUMBER) | (1 << recognizerParser.SOFTWARE_VERSION) | (1 << recognizerParser.WEBSITE_ADDRESS))) != 0)):
                    break

            self.state = 7
            self.match(recognizerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





