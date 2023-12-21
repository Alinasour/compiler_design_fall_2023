# Generated from HW4/Password.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("+\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\6\5\27\n\5\r\5\16\5\30\3")
        buf.write("\5\3\5\3\6\6\6\36\n\6\r\6\16\6\37\3\6\3\6\3\7\6\7%\n\7")
        buf.write("\r\7\16\7&\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2\'\2\16")
        buf.write("\3\2\2\2\4\21\3\2\2\2\6\23\3\2\2\2\b\26\3\2\2\2\n\35\3")
        buf.write("\2\2\2\f$\3\2\2\2\16\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2")
        buf.write("\2\2\21\22\5\6\4\2\22\5\3\2\2\2\23\24\b\4\1\2\24\7\3\2")
        buf.write("\2\2\25\27\7\3\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26\3")
        buf.write("\2\2\2\30\31\3\2\2\2\31\32\3\2\2\2\32\33\b\5\1\2\33\t")
        buf.write("\3\2\2\2\34\36\7\5\2\2\35\34\3\2\2\2\36\37\3\2\2\2\37")
        buf.write("\35\3\2\2\2\37 \3\2\2\2 !\3\2\2\2!\"\b\6\1\2\"\13\3\2")
        buf.write("\2\2#%\7\4\2\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2\2")
        buf.write("\2\'(\3\2\2\2()\b\7\1\2)\r\3\2\2\2\5\30\37&")
        return buf.getvalue()


class PasswordParser ( Parser ):

    grammarFileName = "Password.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "CHAR", "UPPER", "SYMBOL", "WS" ]

    RULE_startRule = 0
    RULE_password = 1
    RULE_isValidPassword = 2
    RULE_charCount = 3
    RULE_hasSymbol = 4
    RULE_hasUppercase = 5

    ruleNames =  [ "startRule", "password", "isValidPassword", "charCount", 
                   "hasSymbol", "hasUppercase" ]

    EOF = Token.EOF
    CHAR=1
    UPPER=2
    SYMBOL=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartRuleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def password(self):
            return self.getTypedRuleContext(PasswordParser.PasswordContext,0)


        def EOF(self):
            return self.getToken(PasswordParser.EOF, 0)

        def getRuleIndex(self):
            return PasswordParser.RULE_startRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartRule" ):
                listener.enterStartRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartRule" ):
                listener.exitStartRule(self)




    def startRule(self):

        localctx = PasswordParser.StartRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_startRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.password()
            self.state = 13
            self.match(PasswordParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PasswordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def isValidPassword(self):
            return self.getTypedRuleContext(PasswordParser.IsValidPasswordContext,0)


        def getRuleIndex(self):
            return PasswordParser.RULE_password

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassword" ):
                listener.enterPassword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassword" ):
                listener.exitPassword(self)




    def password(self):

        localctx = PasswordParser.PasswordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_password)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.isValidPassword()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IsValidPasswordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.isValid = None


        def getRuleIndex(self):
            return PasswordParser.RULE_isValidPassword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsValidPassword" ):
                listener.enterIsValidPassword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsValidPassword" ):
                listener.exitIsValidPassword(self)




    def isValidPassword(self):

        localctx = PasswordParser.IsValidPasswordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_isValidPassword)
        try:
            self.enterOuterAlt(localctx, 1)
             isValid = charCount() >= 8 && hasSymbol() && hasUppercase() 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharCountContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.count = None
            self._CHAR = None # Token

        def CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(PasswordParser.CHAR)
            else:
                return self.getToken(PasswordParser.CHAR, i)

        def getRuleIndex(self):
            return PasswordParser.RULE_charCount

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharCount" ):
                listener.enterCharCount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharCount" ):
                listener.exitCharCount(self)




    def charCount(self):

        localctx = PasswordParser.CharCountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_charCount)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 19
                localctx._CHAR = self.match(PasswordParser.CHAR)
                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PasswordParser.CHAR):
                    break

             localctx.count =  (None if localctx._CHAR is None else localctx._CHAR.text).length() 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HasSymbolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.hassSymbol = None
            self._SYMBOL = None # Token

        def SYMBOL(self, i:int=None):
            if i is None:
                return self.getTokens(PasswordParser.SYMBOL)
            else:
                return self.getToken(PasswordParser.SYMBOL, i)

        def getRuleIndex(self):
            return PasswordParser.RULE_hasSymbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHasSymbol" ):
                listener.enterHasSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHasSymbol" ):
                listener.exitHasSymbol(self)




    def hasSymbol(self):

        localctx = PasswordParser.HasSymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_hasSymbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                localctx._SYMBOL = self.match(PasswordParser.SYMBOL)
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PasswordParser.SYMBOL):
                    break

             localctx.hassSymbol =  (None if localctx._SYMBOL is None else localctx._SYMBOL.text).matches(".*[!@#$%^&*()-_+=].*") 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HasUppercaseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.hasUpper = None
            self._UPPER = None # Token

        def UPPER(self, i:int=None):
            if i is None:
                return self.getTokens(PasswordParser.UPPER)
            else:
                return self.getToken(PasswordParser.UPPER, i)

        def getRuleIndex(self):
            return PasswordParser.RULE_hasUppercase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHasUppercase" ):
                listener.enterHasUppercase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHasUppercase" ):
                listener.exitHasUppercase(self)




    def hasUppercase(self):

        localctx = PasswordParser.HasUppercaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_hasUppercase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 33
                localctx._UPPER = self.match(PasswordParser.UPPER)
                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PasswordParser.UPPER):
                    break

             localctx.hasUpper =  (None if localctx._UPPER is None else localctx._UPPER.text).matches(".*[A-Z].*") 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





