// Generated from /home/reyhan/Desktop/study/uni/4022/Compiler/HW/HW2/TypeChecker.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link TypeCheckerParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface TypeCheckerVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link TypeCheckerParser#start}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStart(TypeCheckerParser.StartContext ctx);
	/**
	 * Visit a parse tree produced by the {@code expr3}
	 * labeled alternative in {@link TypeCheckerParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr3(TypeCheckerParser.Expr3Context ctx);
	/**
	 * Visit a parse tree produced by the {@code expr2}
	 * labeled alternative in {@link TypeCheckerParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr2(TypeCheckerParser.Expr2Context ctx);
	/**
	 * Visit a parse tree produced by the {@code expr1}
	 * labeled alternative in {@link TypeCheckerParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr1(TypeCheckerParser.Expr1Context ctx);
	/**
	 * Visit a parse tree produced by the {@code term2}
	 * labeled alternative in {@link TypeCheckerParser#term}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerm2(TypeCheckerParser.Term2Context ctx);
	/**
	 * Visit a parse tree produced by the {@code term3}
	 * labeled alternative in {@link TypeCheckerParser#term}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerm3(TypeCheckerParser.Term3Context ctx);
	/**
	 * Visit a parse tree produced by the {@code term1}
	 * labeled alternative in {@link TypeCheckerParser#term}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerm1(TypeCheckerParser.Term1Context ctx);
	/**
	 * Visit a parse tree produced by the {@code factString}
	 * labeled alternative in {@link TypeCheckerParser#fact}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFactString(TypeCheckerParser.FactStringContext ctx);
	/**
	 * Visit a parse tree produced by the {@code factInteger}
	 * labeled alternative in {@link TypeCheckerParser#fact}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFactInteger(TypeCheckerParser.FactIntegerContext ctx);
	/**
	 * Visit a parse tree produced by the {@code factFloat}
	 * labeled alternative in {@link TypeCheckerParser#fact}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFactFloat(TypeCheckerParser.FactFloatContext ctx);
	/**
	 * Visit a parse tree produced by the {@code factExpr}
	 * labeled alternative in {@link TypeCheckerParser#fact}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFactExpr(TypeCheckerParser.FactExprContext ctx);
}