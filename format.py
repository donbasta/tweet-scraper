def Tweet(t):
    output = f"{t.id_str} {t.datestamp} {t.timestamp} {t.timezone} "
    output += f"<{t.username}> {t.tweet}"
    return output
