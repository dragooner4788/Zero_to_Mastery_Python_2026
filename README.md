# 🐍 Zero to Mastery: Python Developer Journey 2026

A documented journey from Technical Support Engineer to Software Developer

Systematic learning through hands-on projects, best practices, and real-world application

# 👨‍💻 About This Repository

This repository chronicles my transition from a Salesforce Technical Support Engineer to a full-stack software developer. Rather than just completing tutorials, I'm building a comprehensive portfolio that demonstrates:

- Systematic Learning: Structured progression through foundational concepts to advanced topics
- Best Practices: Clean code, proper documentation, and professional development workflows
- Real-World Application: Translating theoretical knowledge into practical implementations
- Growth Mindset: Visible learning progression, including mistakes and corrections

## Learning Objectives

1. Master Python Fundamentals: Build a rock-solid foundation in Python programming
2. Develop Professional Skills: Version control, documentation, testing, and code quality
3. Create Portfolio Projects: Showcase real-world applications and problem-solving abilities
4. Transition to Software Development: Leverage learning to secure a software development role

# 📚 Learning Resources

## Primary Course

- [Complete Python Developer in 2026: Zero to Mastery](https://zerotomastery.io/courses/learn-python/).
    - Comprehensive Python curriculum covering basics through advanced topics

## Supplemental Reading

- [Introduction to Computation and Programming Using Python](https://mitpress.mit.edu/9780262542364/introduction-to-computation-and-programming-using-python/) by *John V. Guttag*

# Tools & Environment

- **IDE**: Visual Studio Code
    - Jupyter extension
- **Python Version**: 3.11+
- **Version Control**: Git & Github
- **Documentation**: Markdown & Jupyter Notebooks

# 💡 Featured Code Examples

## Object-Oriented Programming: Person Class

A well-documented example demonstrating:

- Proper class structure and initialization
- Input validation and error handling
- Setter methods with type checking
- User input collection with validation loops

class Person:
    """
    A class representing a person with basic attributes and validation.
    
    Demonstrates: OOP principles, input validation, error handling
    """
    
    species = 'Homo Sapiens'  # Class attribute
    
    def __init__(self, first_name, last_name):
        """Initialize a Person with validated names."""
        self.first_name = first_name.strip().capitalize()
        self.last_name = last_name.strip().capitalize()
        
        # Instance attributes initialized to None
        self.age = None
        self.height = None
        # ... additional attributes
    
    def set_age(self, age):
        """Set age with validation."""
        if isinstance(age, str):
            raise TypeError("Age must be a number, not a string")
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.age = age

# 🎓 Learning Philosophy

Documentation-First Approach

Every code file includes:

- Clear purpose and learning objectives
- Inline comments explaining the "why," not just the "what"
- Reflection notes on challenges and solutions
- Date stamps to track progression

## Deliberate Practice

Rather than rushing through tutorials, I focus on:

- Understanding over memorization: Deep comprehension of concepts
- Multiple implementations: Solving problems different ways
- Error analysis: Learning from mistakes and debugging systematically
- Real-world application: Connecting theory to practical use cases

# Professional Development

Building habits that translate to professional software development:

- Clean, readable code following PEP 8 standards
- Meaningful commit messages and version control
- Comprehensive documentation
- Test-driven development (upcoming)

# 🛠️ Technical Skills Demonstrated

## Core Python

- Variables, data types, operators
- Control flow (conditionals, loops)
- Functions and scope
- Object-oriented programming
- Error handling and exceptions

## Software Engineering

- Git version control
- Code documentation
- Problem decomposition
- Debugging and testing strategies
- Clean code principles

## Tools & Technologies

- VS Code with Jupyter
- Git & GitHub
- Markdown documentation
- Virtual environments
- Command-line proficiency

*The journey of a thousand commits begins with a single line of code*