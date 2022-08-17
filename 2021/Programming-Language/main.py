import language_files.lexer
from language_files.parser import generate_syntax_tree
from language_files.interpreter import traverse_syntax_tree
root = generate_syntax_tree(language_files.lexer.return_tokens())

traverse_syntax_tree(root)