# Generated from quiz1/quiz.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .quizParser import quizParser
else:
    from quizParser import quizParser

# This class defines a complete generic visitor for a parse tree produced by quizParser.

class quizVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by quizParser#parse.
    def visitParse(self, ctx:quizParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by quizParser#number.
    def visitNumber(self, ctx:quizParser.NumberContext):
        return self.visitChildren(ctx)



del quizParser