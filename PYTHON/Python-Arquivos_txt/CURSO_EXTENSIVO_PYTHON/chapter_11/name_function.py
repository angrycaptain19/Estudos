def get_formatted_name(first, last, middle=''):
    """Generate a neatly-formatted full name."""
    full_name = first + ' ' + middle + ' ' + last if middle else first + ' ' + last
    return full_name.title()
