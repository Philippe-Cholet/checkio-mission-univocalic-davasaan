MAX_CODE_LENGTH = 300
FORBIDDEN_CHARS = 'eiou*/.'

# runner is probably 'python-3' (or 'js-node' when allowed).
COMMENT_MARK = {
    'python-3': '#',
    'js-node': '//',
}


def sanitize_code(code: str, runner: str) -> str:
    comment_mark = COMMENT_MARK.get(runner)
    res = []
    for line in code.splitlines():
        # Exclude empty lines.
        if not line.strip():
            continue
        # Exclude commented lines.
        if comment_mark and line.lstrip().startswith(comment_mark):
            continue
        # NOTE: It does not exclude comments at the end of a line.
        # It would be more complicated, because comment mark can be in quotes.
        res.append(line)
    return '\n'.join(res)


def inspector(code: str, runner: str = None):
    # Clear the code of empty lines and commented lines.
    code = sanitize_code(code, runner)

    code_length = len(code)
    if code_length > MAX_CODE_LENGTH:
        return False, (f'The code is too long ({code_length}). '
                       f'It must be shorter than {MAX_CODE_LENGTH} symbols.')

    forbidden_chars = ''.join(c for c in FORBIDDEN_CHARS if c in code)
    if forbidden_chars:
        return False, ('Your code maybe returns correct answers, but it '
                       f'contains forbidden characters: "{forbidden_chars}".')

    return True, f'Code length: {code_length}'
