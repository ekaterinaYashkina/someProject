from aenum import Enum, skip


class Lexem(Enum):

    @skip
    class Hard_key(Enum):
#Hard keywords
        AS = "\\b(as)\\b.*"
        BREAK = "\\b(break)\\b.*"
        CLASS = "\\b(class)\\b.*"
        CONTINUE = "\\b(continue)\\b.*"
        DO = "\\b(do)\\b.*"
        ELSE = "\\b(else)\\b.*"
        FALSE = "\\b(false)\\b.*"
        FOR = "\\b(for)\\b.*"
        FUN = "\\b(fun)\\b.*"
        IF = "\\b(if)\\b.*"
        IN = "\\b(in)\\b.*"
        INTERFACE = "\\b(interface)\\b.*"
        IS = "\\b(is)\\b.*"
        NULL = "\\b(null)\\b.*"
        OBJECT = "\\b(object)\\b.*"
        PACKAGE = "\\b(package)\\b.*"
        RETURN = "\\b(return)\\b.*"
        SUPER = "\\b(super)\\b.*"
        THIS = "\\b(this)\\b.*"
        THROW = "\\b(throw)\\b.*"
        TRUE = "\\b(true)\\b.*"
        TRY = "\\b(try)\\b.*"
        TYPEALIAS = "\\b(typealias)\\b.*"
        VAL = "\\b(val)\\b.*"
        VAR = "\\b(var)\\b.*"
        WHEN = "\\b(when)\\b.*"
        WHILE = "\\b(while)\\b.*"

    @skip
    class Soft_key(Enum):
#Soft keywords
        BY = "\\b(by)\\b.*"
        CATCH = "\\b(catch)\\b.*"
        CONSTRUCTOR = "\\b(constructor)\\b.*"
        DELEGATE = "\\b(delegate)\\b.*"
        DYNAMIC = "\\b(dynamic)\\b.*"
        FIELD = "\\b(field)\\b.*"
        FILE = "\\b(file)\\b.*"
        FINALLY = "\\b(finally)\\b.*"
        GET = "\\b(get)\\b.*"
        IMPORT = "\\b(import)\\b.*"
        INIT = "\\b(init)\\b.*"
        PARAM = "\\b(param)\\b.*"
        PROPERTY = "\\b(property)\\b.*"
        RECEIVER = "\\b(receiver)\\b.*"
        SET = "\\b(set)\\b.*"
        SETPARAM = "\\b(setparam)\\b.*"
        WHERE = "\\b(where)\\b.*"

    @skip
    class Modifier(Enum):
#Modifier keywords
        ACTUAL = "\\b(actual)\\b.*"
        ABSTRACT = "\\b(abstract)\\b.*"
        ANNOTATION = "\\b(annotation)\\b.*"
        COMPANION = "\\b(companion)\\b.*"
        CONST = "\\b(const)\\b.*"
        CROSSINLINE = "\\b(crossinline)\\b.*"
        DATA = "\\b(data)\\b.*"
        ENUM = "\\b(enum)\\b.*"
        EXPECT = "\\b(expect)\\b.*"
        EXTERNAL = "\\b(external)\\b.*"
        FINAL = "\\b(final)\\b.*"
        INFIX = "\\b(infix)\\b.*"
        INNER = "\\b(inner)\\b.*"
        INTERNAL = "\\b(internal)\\b.*"
        LATEINIT = "\\b(lateinit)\\b.*"
        NOINLINE = "\\b(noinline)\\b.*"
        OPEN = "\\b(open)\\b.*"
        OPERATOR = "\\b(operator)\\b.*"
        OUT = "\\b(out)\\b.*"
        OVERRIDE = "\\b(override)\\b.*"
        PRIVATE = "\\b(private)\\b.*"
        PROTECTED = "\\b(protected)\\b.*"
        PUBLIC = "\\b(public)\\b.*"
        REIFIED = "\\b(reified)\\b.*"
        SEALED = "\\b(sealed)\\b.*"
        SUSPEND = "\\b(suspend)\\b.*"
        TAILREC = "\\b(tailrec)\\b.*"
        VARARG = "\\b(vararg)\\b.*"

#Special symbols:
    BLOCK_COMMENT = "(/\\*.*?\\*/).*"
    LINE_COMMENT = "(//(.*?)[\r$]?\n).*"
    SPACE = "( ).*"

#Identifier
    IDENTIFIER = "\\b([a-zA-Z]{1}[0-9a-zA-Z_]{0,31})\\b.*"

#Literals
    STRING_LITERAL = '\"(\\.|[^\\"])*\"'
    CHARACTER_LITERAL = r"\'(\\.|[^\\'])*\'"

#Operators
    PLUS = "((?!(\\+{2}|\\+=))\\+{1}).*"
    MINUS = "((?!(\\-{2}|\\-=))\\-{1}).*"
    MULTIPLY = "((?!\\*=)\\*).*"
    DIVIDE = "((?!/=)/).*"
    STRUCTURAL_EQUAL = "((?!={3})={2}).*"
    REFERENTIAL_EQUAL = "(===).*"
    ASSIGNMENT = "((?!={2})={1}).*"
    NOT_EQUAL = "(\\!=).*"
    CLOSE_CARET = "(>).*"
    OPEN_CARET = "(<).*"
    LESS_EQUAL = "(<=).*"
    BIG_EQUAL = "(>=).*"
    MODULO = "((?!%=)%).*"
    INCREMENT = "(\\+{2}).*"
    DECREMENT = "(\\-{2}).*"
    AUGMENTED_ASSIGNMENT = "((\\+|\\-|\\*|/|%){1}(=){1}).*"
    LOGICAL_AND = "(\\|{2}).*"
    LOGICAL_OR = "(\\&{2}).*"
    LOGICAL_NOT = "((?!(\\!=|!{2}))\\!{1}).*"
    ASSERT_NON_NULL = "(\\!{2}).*"
    OPEN_BRACE = "(\\[).*"
    CLOSE_BRACE = "(\\]).*"
    RANGE = "(\\.{2}).*"
    SUBSTITUTE = "(\\_).*"
    TEMPLATE = "$"

#Delimeters (calls):
    OUTER_REFERENCE = "(\\@).*"
    REFERENCE = "(\\:{2}).*"
    SAFE_CALL = "(\\?\\.).*"
    ELVIS = "(\\?:).*"
    NULLABLE = "((?!\\?(\\.|:))\\?).*"
    POINT_CALL = "((?!(\\.{2}|\\?))\\.{1}).*"

#Delimeters (separators):
    SEMICOLON = "(;).*"
    COMMA = "(,).*"
    ARROW_SEPARATOR = "(\\->).*"
    DECLARATION_SEPARATOR = "((?!\\:{2})\\:{1}).*"