from gen.ArithmeticExpressionListener import ArithmeticExpressionListener


class CalculatorListener(ArithmeticExpressionListener):
    def __init__(self):
        self.result = 0

    def exitExpr(self, ctx):
        self.result = self.exitTerm(ctx.getChild(0))
        if ctx.getChildCount() == 1:
            return self.result

        for i in range(0, ctx.getChildCount() - 2, 2):
            op = ctx.getChild(i + 1).getText()
            if op == '+':
                self.result += self.exitTerm(ctx.getChild(i + 2))
            elif op == '-':
                self.result -= self.exitTerm(ctx.getChild(i + 2))
        return self.result

    def exitTerm(self, ctx):
        if ctx.getChildCount() == 1:
            return self.exitFactor(ctx.getChild(0))

        temp = self.exitFactor(ctx.getChild(0))
        for i in range(0, ctx.getChildCount() - 2, 2):
            op = ctx.getChild(i+1).getText()
            if op == '*':
                temp *= self.exitFactor(ctx.getChild(i + 2))
            elif op == '/':
                temp /= self.exitFactor(ctx.getChild(i + 2))
        return temp

    def exitFactor(self, ctx):
        if ctx.getChildCount() == 1:
            return float(ctx.getChild(0).getText())
        return self.exitExpr(ctx.getChild(1))
