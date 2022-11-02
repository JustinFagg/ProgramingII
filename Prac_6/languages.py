"""
Client code to use the programming_language class.
"""

from Prac_6.programming_language import ProgrammingLanguage


def main():
    """Test code for Programming_language class"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    programming_languages=[python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in programming_languages:
        if language.is_dynamic():
            print(language.name)


main()
