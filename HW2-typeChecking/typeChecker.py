from antlr4 import *
from gen.TypeCheckerParser import TypeCheckerParser
from gen.TypeCheckerListener import TypeCheckerListener


class TypeCheckListener(TypeCheckerListener):
    def __init__(self):
        self.type = ""

    def get_type(self):
        return self.type

    def exitStart(self, ctx: TypeCheckerParser.StartContext):
        print("Type is ", ctx.getChild(0).type)

    def exitFactString(self, ctx: TypeCheckerParser.FactStringContext):
        ctx.type = "string"

    def exitFactInteger(self, ctx: TypeCheckerParser.FactIntegerContext):
        ctx.type = "integer"

    def exitFactFloat(self, ctx: TypeCheckerParser.FactFloatContext):
        ctx.type = "float"

    def exitFactExpr(self, ctx: TypeCheckerParser.FactExprContext):
        ctx.type = ctx.getChild(1).type

    # '+'
    def exitExpr1(self, ctx: TypeCheckerParser.Expr1Context):
        if ctx.getChild(0).type == "string" and (ctx.getChild(2).type == "float" or ctx.getChild(2).type == "integer" or ctx.getChild(2).type == "string"):
            ctx.type = "string"
        elif (ctx.getChild(0).type == "integer") and (ctx.getChild(2).type == "integer"):
            ctx.type = "integer"
        elif (ctx.getChild(0).type == "integer") and (ctx.getChild(2).type == "float"):
            ctx.type = "float"
        elif (ctx.getChild(0).type == "float") and (ctx.getChild(2).type == "integer"):
            ctx.type = "float"
        elif (ctx.getChild(0).type == "float") and (ctx.getChild(2).type == "float"):
            ctx.type = "float"
        elif ctx.getChild(2).type == "string":
            raise Exception("Type error: String cannot be concatenated to an Integer")
        else:
            raise Exception("Error")
        self.type = ctx.type

    # '-'
    def exitExpr2(self, ctx: TypeCheckerParser.Expr2Context):
        if (ctx.getChild(0).type == "integer") and (ctx.getChild(2).type == "integer"):
            ctx.type = "integer"
        elif (ctx.getChild(0).type == "integer") and (ctx.getChild(2).type == "float"):
            ctx.type = "float"
        elif (ctx.getChild(0).type == "float") and (ctx.getChild(2).type == "integer"):
            ctx.type = "float"
        elif (ctx.getChild(0).type == "float") and (ctx.getChild(2).type == "float"):
            ctx.type = "float"
        else:
            raise Exception("Error")
        self.type = ctx.type

    def exitExpr3(self, ctx: TypeCheckerParser.Expr3Context):
        ctx.type = ctx.getChild(0).type
        self.type = ctx.type

    # '*'
    def exitTerm1(self, ctx: TypeCheckerParser.Term1Context):
        if (ctx.getChild(0).type == "integer") and (ctx.getChild(2).type == "integer"):
            ctx.type = "integer"
        elif (ctx.getChild(0).type == "integer") and (ctx.getChild(2).type == "float"):
            ctx.type = "float"
        elif (ctx.getChild(0).type == "float") and (ctx.getChild(2).type == "integer"):
            ctx.type = "float"
        elif (ctx.getChild(0).type == "float") and (ctx.getChild(2).type == "float"):
            ctx.type = "float"
        elif (ctx.getChild(0).type == "string") or (ctx.getChild(2).type == "string"):
            raise Exception("Type error: String cannot be multiplied")
        else:
            raise Exception("Error")

    # '/'
    def exitTerm2(self, ctx: TypeCheckerParser.Term2Context):
        if (ctx.getChild(0).type == "integer" and ctx.getChild(2).type == "integer") or \
                (ctx.getChild(0).type == "integer") and (ctx.getChild(2).type == "float") or \
                (ctx.getChild(0).type == "float") and (ctx.getChild(2).type == "integer") or \
                (ctx.getChild(0).type == "float") and (ctx.getChild(2).type == "float"):
            ctx.type = "float"
        elif (ctx.getChild(0).type == "string") or (ctx.getChild(2).type == "string"):
            raise Exception("Type error: String cannot be divided")
        else:
            raise Exception("Error")

    def exitTerm3(self, ctx: TypeCheckerParser.Term3Context):
        ctx.type = ctx.getChild(0).type
