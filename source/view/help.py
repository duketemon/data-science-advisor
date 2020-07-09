def get_help_view():
    return '\n'.join([
        "Hey! I'm a Data Science Advisor. You can control me by sending these commands:\n",
        "/courses - recommend courses (theory + practice)",
        "/lectures - recommend lectures (only theory)",
        "/practice_platforms - recommend platforms to practice your skills",
        "/essential_skills - list of essential skills for a position",
        "/interview - list of popular interview questions",
        "\nIf you have any ideas, please visit the repository of the project (https://github.com/duketemon/data-science-advisor)"
    ])
