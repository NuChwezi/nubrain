def text_snippet_start(s, max_len=10):
    return s[:max_len] + ('...' if len(s) > max_len else '')

