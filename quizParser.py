# Generated from quiz1/quiz.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\4")
        buf.write("\23\4\2\t\2\4\3\t\3\3\2\3\2\3\2\7\2\n\n\2\f\2\16\2\r\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\2\2\4\2\4\2\2\2\21\2\13\3\2\2\2")
        buf.write("\4\20\3\2\2\2\6\7\5\4\3\2\7\b\7\4\2\2\b\n\3\2\2\2\t\6")
        buf.write("\3\2\2\2\n\r\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\16\3")
        buf.write("\2\2\2\r\13\3\2\2\2\16\17\7\2\2\3\17\3\3\2\2\2\20\21\7")
        buf.write("\3\2\2\21\5\3\2\2\2\3\13")
        return buf.getvalue()


class quizParser ( Parser ):

    grammarFileName = "quiz.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "NUMBER", "NON_NUMBER" ]

    RULE_parse = 0
    RULE_number = 1

    ruleNames =  [ "parse", "number" ]

    EOF = Token.EOF
    NUMBER=1
    NON_NUMBER=2

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(quizParser.EOF, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(quizParser.NumberContext)
            else:
                return self.getTypedRuleContext(quizParser.NumberContext,i)


        def NON_NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(quizParser.NON_NUMBER)
            else:
                return self.getToken(quizParser.NON_NUMBER, i)

        def getRuleIndex(self):
            return quizParser.RULE_parse

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = quizParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==quizParser.NUMBER:
                self.state = 4
                self.number()
                self.state = 5
                self.match(quizParser.NON_NUMBER)
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
            self.match(quizParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(quizParser.NUMBER, 0)

        def getRuleIndex(self):
            return quizParser.RULE_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = quizParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(quizParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





