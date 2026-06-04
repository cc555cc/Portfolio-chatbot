"""
Portfolio chatbot response database.
Defines intents, keywords, and Carson's portfolio info used to generate responses.
"""

INTENT_KEYWORDS = {
    "greeting": {
        "message": [
            "hello",
            "hi",
            "hey",
            "greetings",
            "welcome",
            "sup",
            "howdy",
            "hiya",
        ],
    },
    "about": {
        "name": [
            "name",
            "who",
            "person",
            "carson",
            "yourself",
            "you",
        ],
        "background": [
            "background",
            "about",
            "bio",
            "introduce",
            "story",
            "overview",
        ],
    },
    "resume": {
        "download": [
            "resume",
            "cv",
            "download",
            "pdf",
            "document",
            "file",
        ],
    },
    "skills": {
        "tech": [
            "skill",
            "technology",
            "language",
            "stack",
            "tool",
            "proficient",
            "know",
            "experience",
            "capable",
            "familiar",
        ],
    },
    "projects": {
        "list": [
            "project",
            "work",
            "built",
            "build",
            "create",
            "portfolio",
            "develop",
            "made",
            "application",
            "app",
        ],
    },
    "contact": {
        "reach": [
            "contact",
            "email",
            "reach",
            "hire",
            "connect",
            "message",
            "touch",
            "talk",
        ],
    },
    "education": {
        "school": [
            "school",
            "university",
            "degree",
            "study",
            "major",
            "college",
            "education",
            "graduate",
            "studying",
            "student",
        ],
    },
}

STOP_WORDS = [
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "by",
    "can",
    "could",
    "do",
    "for",
    "from",
    "get",
    "give",
    "has",
    "have",
    "help",
    "how",
    "i",
    "in",
    "is",
    "it",
    "like",
    "me",
    "my",
    "of",
    "on",
    "or",
    "our",
    "please",
    "tell",
    "than",
    "that",
    "the",
    "their",
    "there",
    "this",
    "to",
    "us",
    "want",
    "was",
    "we",
    "what",
    "when",
    "where",
    "which",
    "with",
    "would",
    "you",
    "your",
]

PORTFOLIO_INFO = {
    "greeting": {
        "responses": [
            "Hi there! I'm Carson's portfolio assistant. Ask me about his skills, projects, resume, or how to get in touch!",
            "Hello! I can help you learn more about Carson. What would you like to know?",
            "Hey! Ask me anything about Carson's background, projects, or contact info.",
        ],
    },
    "about": {
        "response": "I'm Carson — a developer with a passion for full-stack development and machine learning. I enjoy building tools that solve real problems.",
    },
    "resume": {
        "response": "Sure! Here's a download link to Carson's resume.",
        "action": "download_resume",
    },
    "skills": {
        "response": (
            "Carson's skills include:\n"
            "• Languages: Python, JavaScript, TypeScript, PHP\n"
            "• Frameworks: React, Next.js, TailwindCSS\n"
            "• Databases: MySQL\n"
            "• Tools: GitHub Actions, NLTK, Pandas"
        ),
    },
    "projects": {
        "response": (
            "Carson has worked on:\n"
            "• Student-Life Management Platform — TypeScript, React, Next.js, MySQL\n"
            "• Rule-based Chatbot — Python, NLTK, React\n"
            "• Battery SOH Chatbot — Python, Pandas\n"
            "• ML Papers Pipeline — Python, GitHub Actions, Discord webhook\n"
            "• EventSphere — an event management platform built with PHP and MySQL"
        ),
    },
    "contact": {
        "response": "You can reach Carson at carsonchan050505@gmail.com",
    },
    "education": {
        "response": "Carson is currently a student studying software engineering and computer science, with a strong interest in machine learning and full-stack development.",
    },
}
