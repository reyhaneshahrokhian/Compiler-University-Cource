// Generated from /home/reyhan/Desktop/study/uni/4022/Compiler/HW/HW2/TypeChecker.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link TypeCheckerParser}.
 */
public interface TypeCheckerListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(TypeCheckerParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(TypeCheckerParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by the {@code expr3}
	 * labeled alternative in {@link TypeCheckerParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr3(TypeCheckerParser.Expr3Context ctx);
	/**
	 * Exit a parse tree produced by the {@code expr3}
	 * labeled alternative in {@link TypeCheckerParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr3(TypeCheckerParser.Expr3Context ctx);
	/**
	 * Enter a parse tree produced by the {@code expr2}
	 * labeled alternative in {@link TypeCheckerParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr2(TypeCheckerParser.Expr2Context ctx);
	/**
	 * Exit a parse tree produced by the {@code expr2}
	 * labeled alternative in {@link TypeCheckerParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr2(TypeCheckerParser.Expr2Context ctx);
	/**
	 * Enter a parse tree produced by the {@code expr1}
	 * labeled alternative in {@link TypeCheckerParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr1(TypeCheckerParser.Expr1Context ctx);
	/**
	 * Exit a parse tree produced by the {@code expr1}
	 * labeled alternative in {@link TypeCheckerParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr1(TypeCheckerParser.Expr1Context ctx);
	/**
	 * Enter a parse tree produced by the {@code term2}
	 * labeled alternative in {@link TypeCheckerParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm2(TypeCheckerParser.Term2Context ctx);
	/**
	 * Exit a parse tree produced by the {@code term2}
	 * labeled alternative in {@link TypeCheckerParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm2(TypeCheckerParser.Term2Context ctx);
	/**
	 * Enter a parse tree produced by the {@code term3}
	 * labeled alternative in {@link TypeCheckerParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm3(TypeCheckerParser.Term3Context ctx);
	/**
	 * Exit a parse tree produced by the {@code term3}
	 * labeled alternative in {@link TypeCheckerParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm3(TypeCheckerParser.Term3Context ctx);
	/**
	 * Enter a parse tree produced by the {@code term1}
	 * labeled alternative in {@link TypeCheckerParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm1(TypeCheckerParser.Term1Context ctx);
	/**
	 * Exit a parse tree produced by the {@code term1}
	 * labeled alternative in {@link TypeCheckerParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm1(TypeCheckerParser.Term1Context ctx);
	/**
	 * Enter a parse tree produced by the {@code factString}
	 * labeled alternative in {@link TypeCheckerParser#fact}.
	 * @param ctx the parse tree
	 */
	void enterFactString(TypeCheckerParser.FactStringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code factString}
	 * labeled alternative in {@link TypeCheckerParser#fact}.
	 * @param ctx the parse tree
	 */
	void exitFactString(TypeCheckerParser.FactStringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code factInteger}
	 * labeled alternative in {@link TypeCheckerParser#fact}.
	 * @param ctx the parse tree
	 */
	void enterFactInteger(TypeCheckerParser.FactIntegerContext ctx);
	/**
	 * Exit a parse tree produced by the {@code factInteger}
	 * labeled alternative in {@link TypeCheckerParser#fact}.
	 * @param ctx the parse tree
	 */
	void exitFactInteger(TypeCheckerParser.FactIntegerContext ctx);
	/**
	 * Enter a parse tree produced by the {@code factFloat}
	 * labeled alternative in {@link TypeCheckerParser#fact}.
	 * @param ctx the parse tree
	 */
	void enterFactFloat(TypeCheckerParser.FactFloatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code factFloat}
	 * labeled alternative in {@link TypeCheckerParser#fact}.
	 * @param ctx the parse tree
	 */
	void exitFactFloat(TypeCheckerParser.FactFloatContext ctx);
	/**
	 * Enter a parse tree produced by the {@code factExpr}
	 * labeled alternative in {@link TypeCheckerParser#fact}.
	 * @param ctx the parse tree
	 */
	void enterFactExpr(TypeCheckerParser.FactExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code factExpr}
	 * labeled alternative in {@link TypeCheckerParser#fact}.
	 * @param ctx the parse tree
	 */
	void exitFactExpr(TypeCheckerParser.FactExprContext ctx);
}