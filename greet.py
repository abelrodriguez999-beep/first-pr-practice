def greet(name):
    """Return a friendly greeting for name."""
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"
