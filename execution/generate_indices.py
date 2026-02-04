import os
import re

docs_dir = 'docs/Book_Summaries'
categories = {
    'COMM': 'Communication',
    'DIGI': 'Digital & Technology',
    'FMLY': 'Family Dynamics',
    'FOUND': 'Foundational Parenting',
    'GLOB': 'Global & Cultural',
    'GNDR': 'Gender-Specific',
    'LIFE': 'Life Skills',
    'MENT': 'Mental Health',
    'SPEC': 'Special Needs',
    'TEEN': 'Teenagers',
    'MISC': 'Miscellaneous',
    'PRNT': 'Parent Self-Development'
}

def extract_metadata(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Simple YAML extraction
    meta = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            yaml_content = parts[1]
            # Extract title
            title_match = re.search(r'title:\s*"(.*)"', yaml_content)
            if title_match: meta['title'] = title_match.group(1)
            
            # Extract author
            author_match = re.search(r'author:\s*"(.*)"', yaml_content)
            if author_match: meta['author'] = author_match.group(1)
            
            # Extract key principles list
            kp_match = re.search(r'key_principles:\s*\[(.*)\]', yaml_content)
            if kp_match:
                # Basic comma separation, ignoring commas inside quotes
                principles = re.findall(r'"([^"]*)"', kp_match.group(1))
                meta['key_principles'] = principles
                
    return meta

for cat_code, cat_name in categories.items():
    cat_dir = os.path.join(docs_dir, cat_code)
    if not os.path.exists(cat_dir):
        continue
        
    index_path = os.path.join(cat_dir, 'index.md')
    
    # Get all markdown files in the directory except index.md
    files = [f for f in os.listdir(cat_dir) if f.endswith('.md') and f != 'index.md']
    files.sort()
    
    num_summaries = len(files)
    
    content = f"# {cat_name}\n"
    content += f"{num_summaries} summaries found\n\n"
    content += '<div class="grid cards" markdown="1">\n\n'
    
    for f in files:
        meta = extract_metadata(os.path.join(cat_dir, f))
        
        # Fallback to filename parsing if metadata fails
        raw_name = f.replace(".md", "")
        if " - " in raw_name:
            main_part = raw_name.split(" - ", 1)[1]
        else:
            main_part = raw_name
            
        if " by " in main_part:
            f_title, f_author = main_part.rsplit(" by ", 1)
        else:
            f_title = main_part
            f_author = "Expert Author"
            
        title = meta.get('title', f_title)
        author = meta.get('author', f_author)
        key_principles = meta.get('key_principles', [])
        
        content += f'- <span class="pw-badge" style="font-size: 0.65rem; margin-bottom: 12px; opacity: 0.8;">{cat_name}</span>\n'
        content += f'<div class="pw-book-title">{title}</div>\n'
        content += f'<div class="pw-book-author">by {author}</div>\n'
        content += '<div class="pw-tag-container">'
        if key_principles:
            for kp in key_principles[:2]:
                content += f'<span class="pw-micro-tag">{kp}</span> '
            if len(key_principles) > 2:
                content += f'<span class="pw-micro-tag" style="background: transparent; color: var(--pw-text-muted);">+ {len(key_principles)-2} more</span>'
        else:
            content += '<span class="pw-micro-tag">Key Insight</span> <span class="pw-micro-tag">Actionable</span>'
        content += '</div>\n'
        content += f'[Read Summary :octicons-arrow-right-24:]({f})\n'
        
    content += '</div>\n'
    
    with open(index_path, 'w') as out:
        out.write(content)

print(f"Generated card indices for {len(categories)} categories.")
