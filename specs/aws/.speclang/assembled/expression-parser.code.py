// spec:trace spec=/home/kara/totalstack/specs/aws/dynamodb/expression-parser.spec.py.md#expression-types
// spec:generated DO NOT EDIT — edit the spec instead

condition    → or_expr
or_expr      → and_expr ("OR" and_expr)*
and_expr     → not_expr ("AND" not_expr)*
not_expr     → "NOT" comparison | comparison
comparison   → primary (comparator primary | "BETWEEN" primary "AND" primary | "IN" "(" primary ("," primary)* ")")?
comparator   → "=" | "<>" | "<" | "<=" | ">" | ">="
primary      → function_call | value_ref | "(" condition ")" | path

### Functions
function_call → "attribute_exists(" path ")"
              | "attribute_not_exists(" path ")"
              | "attribute_type(" path "," type_literal ")"
              | "begins_with(" path "," substr_literal ")"
              | "contains(" path "," operand ")"
              | "size(" path ")"
              | "if_not_exists(" path "," default_value ")"
              | "list_append(" list_expr "," list_expr ")"

### UpdateExpression Grammar
update    → clause+
clause    → "SET" set_action ("," set_action)*
          | "REMOVE" path ("," path)*
          | "ADD" path value ("," path value)*
          | "DELETE" path value ("," path value)*
set_action → path "=" value_expr
           | path "+" "=" value_expr
           | path "-" "=" value_expr

### ProjectionExpression Grammar
projection → path ("," path)*

### KeyConditionExpression Grammar
key_condition → partition_key "=" ":" value
              | partition_key "=" ":" value "AND" sort_key comparator ":" value
              | partition_key "=" ":" value "AND" "begins_with(" sort_key "," ":" substr ")"
              | partition_key "=" ":" value "AND" sort_key "BETWEEN" ":" lo "AND" ":" hi

### Path Grammar
path        → identifier ("." identifier)* | identifier "[" digits "]"
identifier  → [a-zA-Z_][a-zA-Z0-9_]* | "#" placeholder

## DynamoDB Types

All values use DynamoDB typed dict format: `{"S": "string"}`, `{"N": "123"}`, `{"B": "base64"}`, `{"BOOL": true}`, `{"NULL": true}`, `{"L": [...]}`, `{"M": {...}}`, `{"SS": [...]}`, `{"NS": [...]}`, `{"BS": [...]}`.

## Implementation

# spec:trace: specs/aws/dynamodb/enriched-aws-reference.json
# spec:id: @specs/aws/dynamodb/expression-parser
# spec:implements: @kind:expression-parser

from typing import Optional, Dict, Any, List, Tuple, Union
from enum import Enum
import re


# ══════════════════════════════════════════════════════════
# Core Expression Parser
# ══════════════════════════════════════════════════════════

class ExpressionType(Enum):
    """Enumeration of DynamoDB expression types."""
    KEY_CONDITION = "KeyConditionExpression"
    FILTER = "FilterExpression"
    CONDITION = "ConditionExpression"
    UPDATE = "UpdateExpression"
    PROJECTION = "ProjectionExpression"


def parse_expression(
    expression: str,
    expression_type: ExpressionType,
    expression_attribute_names: Optional[Dict[str, str]] = None,
    expression_attribute_values: Optional[Dict[str, Any]] = None,
) -> "ExpressionAST":
    """
    Parse a DynamoDB expression string into an AST.

    Handles all expression types. Placeholders (#name, :value) are resolved
    during parsing via the internal parser.

    Returns an ExpressionAST that can be:
        - evaluated against an item (conditions, filters, key conditions)
        - applied to an item (update expressions)
        - used to project attributes (projection expressions)
    """
    names = expression_attribute_names or {}
    values = expression_attribute_values or {}

    parser = _ExpressionParser(expression, names, values)
    return parser.parse(expression_type)


class ExpressionAST:
    """
    Abstract syntax tree for a parsed DynamoDB expression.

    Holds the resolved expression tree. Call evaluate(item) to test
    conditions/filters, apply(item) to mutate items, or project(item)
    to filter attributes.
    """

    def __init__(self, root: "ASTNode", expr_type: ExpressionType):
        self.root = root
        self.expr_type = expr_type

    def evaluate(self, item: Dict[str, Any]) -> bool:
        """Evaluate a condition/filter/key-condition against an item."""
        if self.expr_type == ExpressionType.PROJECTION:
            raise TypeError("Cannot evaluate a ProjectionExpression")
        if self.expr_type == ExpressionType.UPDATE:
            raise TypeError("Use apply() for UpdateExpression, not evaluate()")
        return bool(self.root.eval(item))

    def apply(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Apply an UpdateExpression to an item, returning the modified item."""
        if self.expr_type != ExpressionType.UPDATE:
            raise TypeError("apply() is only valid for UpdateExpression")
        self.root.eval(item)
        return item

    def project(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Apply a ProjectionExpression to extract specified attributes."""
        if self.expr_type != ExpressionType.PROJECTION:
            raise TypeError("project() is only valid for ProjectionExpression")
        result = self.root.eval(item)
        return result if result is not None else {}


# ══════════════════════════════════════════════════════════
# AST Nodes
# ══════════════════════════════════════════════════════════

class ASTNode:
    """Base class for expression AST nodes."""

    def eval(self, item: Dict[str, Any]) -> Any:
        raise NotImplementedError


class AttributeRef(ASTNode):
    """Reference to an item attribute: resolved name."""

    def __init__(self, name: str):
        self.name = name

    def eval(self, item: Dict[str, Any]) -> Any:
        return item.get(self.name)

    def __repr__(self):
        return f"AttributeRef({self.name})"


class ValueLiteral(ASTNode):
    """Literal value from ExpressionAttributeValues: :val placeholder."""

    def __init__(self, dyn_value: Dict[str, Any]):
        self.dyn_value = dyn_value

    def eval(self, item: Dict[str, Any]) -> Any:
        return self.dyn_value

    def __repr__(self):
        return f"ValueLiteral({self.dyn_value})"


class RawLiteral(ASTNode):
    """A raw Python value (used for unquoted identifiers in expressions)."""

    def __init__(self, value: Any):
        self.value = value

    def eval(self, item: Dict[str, Any]) -> Any:
        return self.value


class PathRef(ASTNode):
    """Nested path reference: a.b.c or a[0].b."""

    def __init__(self, path: List[str]):
        self.path = path

    def eval(self, item: Dict[str, Any]) -> Any:
        return _resolve_path(item, self.path)

    def __repr__(self):
        return f"PathRef({self.path})"


class UnaryOp(ASTNode):
    """Unary operation: NOT, attribute_exists(), attribute_not_exists(),
    attribute_type(), begins_with(), contains(), size().
    """

    def __init__(self, op: str, operand: ASTNode, extra: Optional[ASTNode] = None):
        self.op = op          # "NOT", "attribute_exists", "begins_with", etc.
        self.operand = operand
        self.extra = extra    # Second argument for binary-like functions

    def eval(self, item: Dict[str, Any]) -> Any:
        val = self.operand.eval(item)
        extra = self.extra.eval(item) if self.extra else None

        if self.op == "NOT":
            return not _truthy(val)
        elif self.op == "attribute_exists":
            return val is not None
        elif self.op == "attribute_not_exists":
            return val is None
        elif self.op == "attribute_type":
            # extra is the expected type string (e.g., "S", "N", "L", "M")
            expected_type = extra
            if isinstance(val, dict):
                actual_type = list(val.keys())[0] if val else None
                return actual_type == expected_type
            return False
        elif self.op == "begins_with":
            if _is_string(val) and _is_string(extra):
                return str(_unbox(val)).startswith(str(_unbox(extra)))
            return False
        elif self.op == "contains":
            return _contains(val, extra)
        elif self.op == "size":
            return _dynamo_size(val)
        else:
            raise ExpressionError(f"Unknown function: {self.op}")


class BinaryOp(ASTNode):
    """Binary comparison/arithmetic/logical operation."""

    COMPARATORS = {"=": True, "<>": True, "<": True, "<=": True, ">": True, ">=": True}
    ARITHMETIC = {"+": True, "-": True}
    LOGICAL = {"AND": True, "OR": True}

    def __init__(self, left: ASTNode, op: str, right: ASTNode):
        self.left = left
        self.op = op
        self.right = right

    def eval(self, item: Dict[str, Any]) -> Any:
        if self.op in self.LOGICAL:
            left_val = self.left.eval(item)
            if self.op == "AND":
                if not _truthy(left_val):
                    return False
                return _truthy(self.right.eval(item))
            elif self.op == "OR":
                if _truthy(left_val):
                    return True
                return _truthy(self.right.eval(item))

        left_val = _unbox(self.left.eval(item))
        right_val = _unbox(self.right.eval(item))

        if self.op in self.COMPARATORS:
            return _compare(left_val, self.op, right_val)
        elif self.op in self.ARITHMETIC:
            if self.op == "+":
                return _add(left_val, right_val)
            elif self.op == "-":
                return _subtract(left_val, right_val)

        raise ExpressionError(f"Unknown operator: {self.op}")


class BetweenOp(ASTNode):
    """BETWEEN operator: a BETWEEN :lo AND :hi."""

    def __init__(self, operand: ASTNode, lo: ASTNode, hi: ASTNode):
        self.operand = operand
        self.lo = lo
        self.hi = hi

    def eval(self, item: Dict[str, Any]) -> bool:
        val = _unbox(self.operand.eval(item))
        lo = _unbox(self.lo.eval(item))
        hi = _unbox(self.hi.eval(item))
        try:
            return lo <= val <= hi
        except TypeError:
            return False


class InOp(ASTNode):
    """IN operator: a IN (:v1, :v2, :v3)."""

    def __init__(self, operand: ASTNode, values: List[ASTNode]):
        self.operand = operand
        self.values = values

    def eval(self, item: Dict[str, Any]) -> bool:
        val = _unbox(self.operand.eval(item))
        for v in self.values:
            if _unbox(v.eval(item)) == val:
                return True
        return False


class SetAction(ASTNode):
    """SET clause in UpdateExpression."""

    def __init__(self, path: PathRef, value: ASTNode, op: Optional[str] = None):
        self.path = path       # Where to set
        self.value = value     # What to set
        self.op = op           # None for plain SET, "+" or "-" for compound

    def eval(self, item: Dict[str, Any]) -> None:
        new_val = self.value.eval(item)
        if self.op:
            # SET a = a + :val  or  SET a = a - :val
            existing = _resolve_path(item, self.path.path)
            unboxed_existing = _unbox(existing) if existing is not None else 0
            unboxed_new = _unbox(new_val)
            if self.op == "+":
                _set_path(item, self.path.path, _add(unboxed_existing, unboxed_new))
            elif self.op == "-":
                _set_path(item, self.path.path, _subtract(unboxed_existing, unboxed_new))
        else:
            _set_path(item, self.path.path, new_val)


class RemoveAction(ASTNode):
    """REMOVE clause in UpdateExpression."""

    def __init__(self, path: PathRef):
        self.path = path

    def eval(self, item: Dict[str, Any]) -> None:
        _delete_path(item, self.path.path)


class AddAction(ASTNode):
    """ADD clause in UpdateExpression — numeric add or set union."""

    def __init__(self, path: PathRef, value: ASTNode):
        self.path = path
        self.value = value

    def eval(self, item: Dict[str, Any]) -> None:
        existing_val = _resolve_path(item, self.path.path)
        new_val = self.value.eval(item)

        if isinstance(existing_val, (int, float)):
            # Numeric addition
            _set_path(item, self.path.path, existing_val + _unbox(new_val))
        elif isinstance(existing_val, set) or existing_val is None:
            # Set union
            raw = _unbox(new_val)
            if existing_val is None:
                existing_val = set()
            if isinstance(raw, set):
                _set_path(item, self.path.path, existing_val | raw)
            else:
                _set_path(item, self.path.path, existing_val | {raw})
        else:
            # Default numeric add on 0 if attribute doesn't exist
            raw = _unbox(new_val)
            if isinstance(raw, (int, float)):
                _set_path(item, self.path.path, raw)


class DeleteAction(ASTNode):
    """DELETE clause in UpdateExpression — remove elements from a set."""

    def __init__(self, path: PathRef, value: ASTNode):
        self.path = path
        self.value = value

    def eval(self, item: Dict[str, Any]) -> None:
        existing_val = _resolve_path(item, self.path.path)
        if existing_val is None:
            existing_val = set()
        if not isinstance(existing_val, set):
            raise ExpressionError("DELETE can only be used on set attributes")
        raw = _unbox(self.value.eval(item))
        if isinstance(raw, set):
            _set_path(item, self.path.path, existing_val - raw)
        else:
            _set_path(item, self.path.path, existing_val - {raw})


class UpdateExpr(ASTNode):
    """Composite update expression: SET ... REMOVE ... ADD ... DELETE ..."""

    def __init__(self, actions: List[ASTNode]):
        self.actions = actions

    def eval(self, item: Dict[str, Any]) -> None:
        for action in self.actions:
            action.eval(item)


class ProjectionList(ASTNode):
    """ProjectionExpression: comma-separated list of attribute names/paths."""

    def __init__(self, attributes: List[str], names: Dict[str, str]):
        self.attributes = attributes
        self.names = names

    def eval(self, item: Dict[str, Any]) -> Dict[str, Any]:
        projected: Dict[str, Any] = {}
        for attr in self.attributes:
            # Resolve expression attribute name placeholders
            resolved = attr
            for placeholder, attr_name in self.names.items():
                resolved = resolved.replace(placeholder, attr_name)

            # Direct top-level attribute
            if resolved in item:
                projected[resolved] = item[resolved]
            elif "." in resolved or "[" in resolved:
                # Nested path
                parts = _parse_path_segments(resolved)
                val = _resolve_path(item, parts)
                if val is not None:
                    # Reconstruct nested structure in projection
                    _set_path(projected, parts, val)
        return projected


# ══════════════════════════════════════════════════════════
# Internal Recursive-Descent Parser
# ══════════════════════════════════════════════════════════

class _ExpressionParser:
    """Recursive-descent parser for DynamoDB expressions."""

    # Token pattern: single-quoted strings, double-quoted strings,
    # placeholders (#name, :value), multi-char operators (<=, >=, <>),
    # keywords, identifiers with dotted paths and array indexes,
    # arithmetic operators, parens, commas, and any single non-whitespace.
    TOKEN_RE = re.compile(
        r"""
        (?:'[^']*')                   |  # Single-quoted string
        (?:"[^"]*")                   |  # Double-quoted string
        (?:[#:]\w+)                   |  # Expression attribute placeholder
        (?:<=|>=|<>|[=<>])            |  # Comparison operators
        (?:AND|OR|NOT|BETWEEN|IN|SET|REMOVE|ADD|DELETE|
           if_not_exists|list_append|
           attribute_exists|attribute_not_exists|
           attribute_type|begins_with|contains|size)\b |
        (?:\w+(?:\.\w+|\[\d+\])*)     |  # Identifiers with paths/indexes
        (?:[+\-])                     |  # Arithmetic operators
        ([(),])                       |  # Parens and commas
        (?:\S)
        """,
        re.VERBOSE | re.IGNORECASE,
    )

    # Functions that take exactly one path argument
    UNARY_FUNCTIONS = {
        "attribute_exists", "attribute_not_exists", "size"
    }
    # Functions that take a path and another argument
    BINARY_FUNCTIONS = {
        "attribute_type", "begins_with", "contains"
    }
    # Functions used in SET expressions
    SET_FUNCTIONS = {"if_not_exists", "list_append"}

    def __init__(
        self,
        expression: str,
        names: Dict[str, str],
        values: Dict[str, Any],
    ):
        self.expression = expression
        self.names = names        # e.g., {"#pk": "userId", "#sk": "timestamp"}
        self.values = values      # e.g., {":val": {"S": "hello"}, ":num": {"N": "42"}}
        self.tokens = self._tokenize(expression)
        self.pos = 0

    def _tokenize(self, expr: str) -> List[str]:
        tokens = []
        for m in self.TOKEN_RE.finditer(expr):
            tok = m.group(0).strip()
            if tok:
                tokens.append(tok)
        return tokens

    def peek(self) -> Optional[str]:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected: Optional[str] = None) -> str:
        token = self.peek()
        if token is None:
            raise ExpressionError(
                f"Unexpected end of expression at position {self.pos}"
            )
        if expected is not None and token.upper() != expected.upper():
            raise ExpressionError(
                f"Expected '{expected}' but got '{token}' at position {self.pos}"
            )
        self.pos += 1
        return token

    def parse(self, expr_type: ExpressionType) -> ExpressionAST:
        if expr_type == ExpressionType.PROJECTION:
            root = self._parse_projection()
        elif expr_type == ExpressionType.UPDATE:
            root = self._parse_update_expression()
        elif expr_type in (
            ExpressionType.KEY_CONDITION,
            ExpressionType.FILTER,
            ExpressionType.CONDITION,
        ):
            root = self._parse_condition()
        else:
            raise ExpressionError(f"Unknown expression type: {expr_type}")

        if self.peek() is not None:
            raise ExpressionError(
                f"Unexpected token after end of expression: {self.peek()}"
            )

        return ExpressionAST(root, expr_type)

    # ── Projection Expression ──────────────────────────────

    def _parse_projection(self) -> ProjectionList:
        attrs: List[str] = []
        while self.peek():
            attr = self._parse_identifier()
            attrs.append(attr)
            if self.peek() == ",":
                self.consume(",")
            else:
                break
        return ProjectionList(attrs, self.names)

    # ── Update Expression ──────────────────────────────────

    def _parse_update_expression(self) -> UpdateExpr:
        actions: List[ASTNode] = []

        while self.peek():
            keyword = self.peek().upper()
            if keyword == "SET":
                self.consume("SET")
                actions.extend(self._parse_set_clause())
            elif keyword == "REMOVE":
                self.consume("REMOVE")
                actions.extend(self._parse_remove_clause())
            elif keyword == "ADD":
                self.consume("ADD")
                actions.extend(self._parse_add_clause())
            elif keyword == "DELETE":
                self.consume("DELETE")
                actions.extend(self._parse_delete_clause())
            else:
                raise ExpressionError(
                    f"Expected SET/REMOVE/ADD/DELETE but got '{self.peek()}'"
                )

        return UpdateExpr(actions)

    def _parse_set_clause(self) -> List[SetAction]:
        actions: List[SetAction] = []
        while True:
            path = self._parse_path()
            op = None
            if self.peek() == "=":
                self.consume("=")
            elif self.peek() in ("+", "-"):
                op = self.consume()
                self.consume("=")

            value = self._parse_set_value()
            actions.append(SetAction(path, value, op))

            if self.peek() == ",":
                self.consume(",")
            else:
                break
        return actions

    def _parse_set_value(self) -> ASTNode:
        """Parse the right-hand side of a SET assignment."""
        token = self.peek()
        if token is None:
            raise ExpressionError("Expected value expression in SET clause")

        if token.startswith(":"):
            return self._parse_value()
        if token.upper() == "if_not_exists":
            return self._parse_function()
        if token.upper() == "list_append":
            return self._parse_function()

        # May be an attribute path, arithmetic expression, or raw value
        left = self._parse_primary()
        if self.peek() in ("+", "-"):
            op = self.consume()
            right = self._parse_primary()
            return BinaryOp(left, op, right)
        return left

    def _parse_remove_clause(self) -> List[RemoveAction]:
        actions: List[RemoveAction] = []
        while True:
            path = self._parse_path()
            actions.append(RemoveAction(path))
            if self.peek() == ",":
                self.consume(",")
            else:
                break
        return actions

    def _parse_add_clause(self) -> List[AddAction]:
        actions: List[AddAction] = []
        while True:
            path = self._parse_path()
            value = self._parse_value()  # ADD only accepts :val placeholders
            actions.append(AddAction(path, value))
            if self.peek() == ",":
                self.consume(",")
            else:
                break
        return actions

    def _parse_delete_clause(self) -> List[DeleteAction]:
        actions: List[DeleteAction] = []
        while True:
            path = self._parse_path()
            value = self._parse_value()  # DELETE only accepts :val placeholders
            actions.append(DeleteAction(path, value))
            if self.peek() == ",":
                self.consume(",")
            else:
                break
        return actions

    # ── Condition Expression ───────────────────────────────

    def _parse_condition(self) -> ASTNode:
        return self._parse_or()

    def _parse_or(self) -> ASTNode:
        left = self._parse_and()
        while self.peek() and self.peek().upper() == "OR":
            self.consume("OR")
            right = self._parse_and()
            left = BinaryOp(left, "OR", right)
        return left

    def _parse_and(self) -> ASTNode:
        left = self._parse_not()
        while self.peek() and self.peek().upper() == "AND":
            self.consume("AND")
            right = self._parse_not()
            left = BinaryOp(left, "AND", right)
        return left

    def _parse_not(self) -> ASTNode:
        if self.peek() and self.peek().upper() == "NOT":
            self.consume("NOT")
            operand = self._parse_comparison()
            return UnaryOp("NOT", operand)
        return self._parse_comparison()

    def _parse_comparison(self) -> ASTNode:
        left = self._parse_primary()

        peeked = self.peek()
        if peeked is None:
            return left

        if peeked.upper() == "BETWEEN":
            self.consume("BETWEEN")
            lo = self._parse_primary()
            self.consume("AND")
            hi = self._parse_primary()
            return BetweenOp(left, lo, hi)
        elif peeked.upper() == "IN":
            self.consume("IN")
            self.consume("(")
            values: List[ASTNode] = []
            while self.peek() != ")":
                values.append(self._parse_primary())
                if self.peek() == ",":
                    self.consume(",")
            self.consume(")")
            return InOp(left, values)
        elif peeked in ("=", "<>", "<", "<=", ">", ">="):
            op = self.consume()
            right = self._parse_primary()
            return BinaryOp(left, op, right)

        return left

    def _parse_primary(self) -> ASTNode:
        token = self.peek()
        if token is None:
            raise ExpressionError("Unexpected end of expression")

        # Function calls
        if token.lower() in (
            "attribute_exists",
            "attribute_not_exists",
            "attribute_type",
            "begins_with",
            "contains",
            "size",
            "if_not_exists",
            "list_append",
        ):
            return self._parse_function()

        # Expression attribute value placeholder (:val)
        if token.startswith(":"):
            return self._parse_value()

        # Parenthesized sub-expression
        if token == "(":
            self.consume("(")
            expr = self._parse_condition()
            self.consume(")")
            return expr

        # Attribute path or identifier
        return self._parse_path()

    def _parse_function(self) -> ASTNode:
        func_name = self.consume().lower()
        self.consume("(")

        operand = self._parse_primary()

        extra = None
        if self.peek() == ",":
            self.consume(",")
            extra = self._parse_primary()

        self.consume(")")

        # if_not_exists(path, default) — used in SET expressions
        if func_name == "if_not_exists":
            return IfNotExistsFunc(operand, extra) if extra else operand

        # list_append(list1, list2) — concatenate two lists
        if func_name == "list_append":
            return ListAppendFunc(operand, extra) if extra else operand

        return UnaryOp(func_name, operand, extra)

    def _parse_value(self) -> ValueLiteral:
        token = self.consume()
        if token not in self.values:
            raise ExpressionError(
                f"ExpressionAttributeValues missing for placeholder: {token}"
            )
        return ValueLiteral(self.values[token])

    def _parse_path(self) -> PathRef:
        """Parse an attribute path: #name, attr, a.b.c, a[0].b"""
        token = self.consume()

        # Resolve expression attribute name placeholder
        # e.g., "#pk" → "userId"
        resolved = token
        if token.startswith("#"):
            if token not in self.names:
                raise ExpressionError(
                    f"ExpressionAttributeNames missing for placeholder: {token}"
                )
            resolved = self.names[token]

        # Parse dotted access and array indexing
        segments = _parse_path_segments(resolved)

        # Continue consuming dotted segments
        while self.peek() == ".":
            self.consume(".")
            next_token = self.consume()
            next_resolved = next_token
            if next_token.startswith("#"):
                if next_token not in self.names:
                    raise ExpressionError(
                        f"ExpressionAttributeNames missing for placeholder: {next_token}"
                    )
                next_resolved = self.names[next_token]
            # Parse array indexes in the next segment
            extra_segments = _parse_path_segments(next_resolved)
            segments.extend(extra_segments)

        return PathRef(segments)

    def _parse_identifier(self) -> str:
        """Parse a plain attribute name or path for projection expressions."""
        token = self.consume()
        resolved = token
        if token.startswith("#"):
            if token not in self.names:
                raise ExpressionError(
                    f"ExpressionAttributeNames missing for placeholder: {token}"
                )
            resolved = self.names[token]
        # Handle dotted paths: #pk.#sk → resolved names
        while self.peek() == ".":
            self.consume(".")
            next_token = self.consume()
            next_resolved = next_token
            if next_token.startswith("#"):
                if next_token not in self.names:
                    raise ExpressionError(
                        f"ExpressionAttributeNames missing for placeholder: {next_token}"
                    )
                next_resolved = self.names[next_token]
            resolved += "." + next_resolved
        return resolved


# ══════════════════════════════════════════════════════════
# Special Function Nodes
# ══════════════════════════════════════════════════════════

class IfNotExistsFunc(ASTNode):
    """if_not_exists(path, default_value) — returns path value if it exists, else default."""

    def __init__(self, path_expr: ASTNode, default_expr: ASTNode):
        self.path_expr = path_expr
        self.default_expr = default_expr

    def eval(self, item: Dict[str, Any]) -> Any:
        val = self.path_expr.eval(item)
        if val is not None:
            return val
        return self.default_expr.eval(item)


class ListAppendFunc(ASTNode):
    """list_append(list1, list2) — concatenate two lists."""

    def __init__(self, list1: ASTNode, list2: ASTNode):
        self.list1 = list1
        self.list2 = list2

    def eval(self, item: Dict[str, Any]) -> Any:
        v1 = _unbox(self.list1.eval(item))
        v2 = _unbox(self.list2.eval(item))
        if isinstance(v1, list) and isinstance(v2, list):
            return v1 + v2
        raise ExpressionError("list_append requires two list arguments")


# ══════════════════════════════════════════════════════════
# Value Helpers — DynamoDB typed value boxing/unboxing
# ══════════════════════════════════════════════════════════

def _unbox(dyn_val: Any) -> Any:
    """Extract the raw Python value from a DynamoDB-typed dict.

    {"S": "hello"} → "hello", {"N": "42"} → 42, {"BOOL": true} → True, etc.
    Returns the value as-is if not a typed dict.
    """
    if not isinstance(dyn_val, dict) or len(dyn_val) != 1:
        return dyn_val
    key = list(dyn_val.keys())[0]
    raw = dyn_val[key]
    if key == "N":
        try:
            return int(raw)
        except (ValueError, TypeError):
            try:
                return float(raw)
            except (ValueError, TypeError):
                return raw
    elif key == "S":
        return raw
    elif key == "B":
        return raw  # binary value as-is
    elif key == "BOOL":
        return bool(raw)
    elif key == "NULL":
        return None
    elif key == "L":
        return [_unbox(item) for item in raw]
    elif key == "M":
        return {k: _unbox(v) for k, v in raw.items()}
    elif key == "SS":
        return set(raw)
    elif key == "NS":
        return set(raw)
    elif key == "BS":
        return set(raw)
    return raw


def _is_string(dyn_val: Any) -> bool:
    """Check if a DynamoDB value is a string type."""
    if isinstance(dyn_val, dict):
        return "S" in dyn_val
    return isinstance(dyn_val, str)


def _contains(container: Any, needle: Any) -> bool:
    """DynamoDB contains() function semantics."""
    needle_unboxed = _unbox(needle) if isinstance(needle, dict) else needle
    container_unboxed = _unbox(container) if isinstance(container, dict) else container

    if isinstance(container_unboxed, str):
        return str(needle_unboxed) in container_unboxed
    if isinstance(container_unboxed, list):
        return needle_unboxed in container_unboxed
    if isinstance(container_unboxed, set):
        return needle_unboxed in container_unboxed
    if isinstance(container, dict) and "M" in container:
        # For maps, check if the value exists in the map keys
        return str(needle_unboxed) in str(container["M"])
    return False


def _dynamo_size(val: Any) -> int:
    """Calculate DynamoDB logical size of a value (used by size() function)."""
    if val is None:
        return 0
    if isinstance(val, str):
        return len(val.encode("utf-8"))
    if isinstance(val, (int, float)):
        return len(str(val).encode("utf-8"))
    if isinstance(val, bool):
        return 1
    if isinstance(val, dict):
        if not val:
            return 0
        key = list(val.keys())[0]
        raw = val[key]
        if key == "S":
            return len(raw.encode("utf-8"))
        if key == "N":
            return len(raw.encode("utf-8"))
        if key == "B":
            return len(raw)
        if key == "L":
            return len(raw)  # Number of elements in list
        if key == "M":
            return len(raw)  # Number of key-value pairs
        if key == "SS":
            return len(raw)
        if key == "NS":
            return len(raw)
        if key == "BS":
            return len(raw)
        if key == "BOOL":
            return 1
        if key == "NULL":
            return 0
    if isinstance(val, list):
        return len(val)
    if isinstance(val, set):
        return len(val)
    return len(str(val).encode("utf-8"))


def _truthy(dyn_val: Any) -> bool:
    """Determine if a DynamoDB value is truthy for condition evaluation."""
    if dyn_val is None:
        return False
    if isinstance(dyn_val, bool):
        return dyn_val
    if isinstance(dyn_val, dict):
        if not dyn_val:
            return False
        key = list(dyn_val.keys())[0]
        if key == "NULL":
            return False
        if key == "BOOL":
            return bool(dyn_val[key])
        return True
    if isinstance(dyn_val, (int, float)):
        return True
    if isinstance(dyn_val, str):
        return len(dyn_val) > 0
    if isinstance(dyn_val, (list, set)):
        return len(dyn_val) > 0
    return True


def _compare(left: Any, op: str, right: Any) -> bool:
    """Compare two unboxed values using DynamoDB comparator semantics."""
    try:
        if op == "=":
            return left == right
        elif op == "<>":
            return left != right
        elif op == "<":
            return left < right
        elif op == "<=":
            return left <= right
        elif op == ">":
            return left > right
        elif op == ">=":
            return left >= right
    except TypeError:
        return False
    return False


def _add(left: Any, right: Any) -> Any:
    """Add two values (numeric addition or list concatenation)."""
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        return left + right
    if isinstance(left, list) and isinstance(right, list):
        return left + right
    if isinstance(left, str) and isinstance(right, str):
        return left + right
    raise ExpressionError(f"Cannot add {type(left)} and {type(right)}")


def _subtract(left: Any, right: Any) -> Any:
    """Subtract two numeric values."""
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        return left - right
    raise ExpressionError(f"Cannot subtract {type(left)} and {type(right)}")


# ══════════════════════════════════════════════════════════
# Path Helpers — read/write/delete nested paths
# ══════════════════════════════════════════════════════════

def _parse_path_segments(path_str: str) -> List[str]:
    """Split a path string like 'Orders[0].ProductName' into segments."""
    # Split on dots then flatten array indexes
    parts = re.split(r"\.", path_str)
    flat: List[str] = []
    for segment in parts:
        # Split on array index: "Orders[0]" → ["Orders", "0"]
        sub_parts = re.split(r"\[(\d+)\]", segment)
        for p in sub_parts:
            if p:
                flat.append(p)
    return flat


def _resolve_path(item: Dict[str, Any], path: List[str]) -> Any:
    """Resolve a nested path in a DynamoDB item dict."""
    current: Any = item
    for segment in path:
        if current is None:
            return None
        if isinstance(current, dict):
            current = current.get(segment)
        elif isinstance(current, list):
            try:
                idx = int(segment)
                current = current[idx] if 0 <= idx < len(current) else None
            except (ValueError, IndexError):
                return None
        else:
            return None
    return current


def _set_path(item: Dict[str, Any], path: List[str], value: Any) -> None:
    """Set a value at a nested path, creating intermediate dicts/lists as needed."""
    if not path:
        return
    current = item
    for i, segment in enumerate(path[:-1]):
        if segment not in current:
            # Peek ahead: if next segment is numeric, create a list
            next_seg = path[i + 1]
            try:
                int(next_seg)
                current[segment] = []
            except ValueError:
                current[segment] = {}
        current = current[segment]
        if isinstance(current, list):
            # Ensure list is large enough
            try:
                idx = int(path[i + 1])
                while len(current) <= idx:
                    current.append({})
                current = current[idx]
            except (ValueError, IndexError):
                pass

    last = path[-1]
    if isinstance(current, list):
        try:
            idx = int(last)
            while len(current) <= idx:
                current.append(None)
            current[idx] = value
        except ValueError:
            raise ExpressionError(f"Cannot set non-index key '{last}' on list")
    else:
        current[last] = value


def _delete_path(item: Dict[str, Any], path: List[str]) -> None:
    """Delete a value at a nested path."""
    if not path:
        return
    current = item
    for segment in path[:-1]:
        if isinstance(current, dict):
            current = current.get(segment)
        elif isinstance(current, list):
            try:
                idx = int(segment)
                current = current[idx] if 0 <= idx < len(current) else None
            except ValueError:
                return
        else:
            return
        if current is None:
            return

    last = path[-1]
    if isinstance(current, dict):
        current.pop(last, None)
    elif isinstance(current, list):
        try:
            idx = int(last)
            if 0 <= idx < len(current):
                current.pop(idx)
        except ValueError:
            pass


# ══════════════════════════════════════════════════════════
# Convenience Functions
# ══════════════════════════════════════════════════════════

def evaluate_condition(
    condition_expression: str,
    expression_attribute_names: Optional[Dict[str, str]],
    expression_attribute_values: Optional[Dict[str, Any]],
    item: Dict[str, Any],
) -> bool:
    """
    Evaluate a ConditionExpression against an item.

    Used by PutItem, UpdateItem, DeleteItem for conditional writes.
    Returns True if the write should proceed, False if it should be rejected
    (ConditionalCheckFailedException).
    """
    ast = parse_expression(
        condition_expression,
        ExpressionType.CONDITION,
        expression_attribute_names,
        expression_attribute_values,
    )
    return ast.evaluate(item)


def evaluate_filter(
    filter_expression: str,
    expression_attribute_names: Optional[Dict[str, str]],
    expression_attribute_values: Optional[Dict[str, Any]],
    item: Dict[str, Any],
) -> bool:
    """
    Evaluate a FilterExpression against an item.

    Used by Query and Scan for server-side post-filtering.
    """
    ast = parse_expression(
        filter_expression,
        ExpressionType.FILTER,
        expression_attribute_names,
        expression_attribute_values,
    )
    return ast.evaluate(item)


def evaluate_key_condition(
    key_condition_expression: str,
    expression_attribute_values: Optional[Dict[str, Any]],
    item: Dict[str, Any],
    key_schema: List[Dict[str, str]],
) -> bool:
    """
    Evaluate a KeyConditionExpression against an item.

    Determines if an item's key attributes match the query condition.
    Only supports partition key equality and sort key range conditions.
    """
    ast = parse_expression(
        key_condition_expression,
        ExpressionType.KEY_CONDITION,
        expression_attribute_values=expression_attribute_values,
    )
    return ast.evaluate(item)


def apply_update(
    update_expression: str,
    expression_attribute_names: Optional[Dict[str, str]],
    expression_attribute_values: Optional[Dict[str, Any]],
    item: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Apply an UpdateExpression to an item.

    Returns the modified item. The original item dict is mutated in-place
    and also returned for convenience.
    """
    ast = parse_expression(
        update_expression,
        ExpressionType.UPDATE,
        expression_attribute_names,
        expression_attribute_values,
    )
    ast.apply(item)
    return item


def apply_projection(
    projection_expression: str,
    expression_attribute_names: Optional[Dict[str, str]],
    item: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Apply a ProjectionExpression to extract specified attributes.

    Returns a new dict containing only the projected attributes.
    """
    ast = parse_expression(
        projection_expression,
        ExpressionType.PROJECTION,
        expression_attribute_names,
    )
    return ast.project(item)


class ExpressionError(Exception):
    """Expression parsing or evaluation error."""
    pass