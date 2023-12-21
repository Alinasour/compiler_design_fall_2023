# Generated from HW4/Password.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PasswordParser import PasswordParser
else:
    from PasswordParser import PasswordParser

# This class defines a complete listener for a parse tree produced by PasswordParser.
class PasswordListener(ParseTreeListener):

    # Enter a parse tree produced by PasswordParser#startRule.
    def enterStartRule(self, ctx:PasswordParser.StartRuleContext):
        pass

    # Exit a parse tree produced by PasswordParser#startRule.
    def exitStartRule(self, ctx:PasswordParser.StartRuleContext):
        pass


    # Enter a parse tree produced by PasswordParser#password.
    def enterPassword(self, ctx:PasswordParser.PasswordContext):
        pass

    # Exit a parse tree produced by PasswordParser#password.
    def exitPassword(self, ctx:PasswordParser.PasswordContext):
        pass


    # Enter a parse tree produced by PasswordParser#isValidPassword.
    def enterIsValidPassword(self, ctx:PasswordParser.IsValidPasswordContext):
        pass

    # Exit a parse tree produced by PasswordParser#isValidPassword.
    def exitIsValidPassword(self, ctx:PasswordParser.IsValidPasswordContext):
        pass


    # Enter a parse tree produced by PasswordParser#charCount.
    def enterCharCount(self, ctx:PasswordParser.CharCountContext):
        pass

    # Exit a parse tree produced by PasswordParser#charCount.
    def exitCharCount(self, ctx:PasswordParser.CharCountContext):
        pass


    # Enter a parse tree produced by PasswordParser#hasSymbol.
    def enterHasSymbol(self, ctx:PasswordParser.HasSymbolContext):
        pass

    # Exit a parse tree produced by PasswordParser#hasSymbol.
    def exitHasSymbol(self, ctx:PasswordParser.HasSymbolContext):
        pass


    # Enter a parse tree produced by PasswordParser#hasUppercase.
    def enterHasUppercase(self, ctx:PasswordParser.HasUppercaseContext):
        pass

    # Exit a parse tree produced by PasswordParser#hasUppercase.
    def exitHasUppercase(self, ctx:PasswordParser.HasUppercaseContext):
        pass


