# Generated from Math.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MathParser import MathParser
else:
    from MathParser import MathParser

# This class defines a complete generic visitor for a parse tree produced by MathParser.

class MathVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MathParser#expr.
    def visitExpr(self, ctx:MathParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#term.
    def visitTerm(self, ctx:MathParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#factor.
    def visitFactor(self, ctx:MathParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#number.
    def visitNumber(self, ctx:MathParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#identifier.
    def visitIdentifier(self, ctx:MathParser.IdentifierContext):
        return self.visitChildren(ctx)



del MathParser