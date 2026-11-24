import re

tech_keywords={"python", "django", "drf", "rest", "api", "postgresql", "postgres",
    "mysql", "sqlite", "sql", "react", "nextjs", "typescript", "javascript",
    "node", "nodejs", "docker", "git", "github", "linux", "aws", "html", "css",
    "redis", "celery", "tailwind", "oop", "orm"}

def extract_keywords(text:str)->set[str]:
    words=set(re.findall(r"[a-z0-9\+\#\.]+",text.lower()))
    return words.intersection(tech_keywords)

def calculate_match(skill:str,desc:str)->tuple[int,list[str]]:
    desc_keyword=extract_keywords(desc)
    if not desc_keyword:
        return 0,[]
    
    skillkey=extract_keywords(skill)
    matched=desc_keyword.intersection(skillkey)
    missing=sorted(desc_keyword-skillkey)

    score=round((len(matched)/len(desc_keyword))*100)
    return score,missing