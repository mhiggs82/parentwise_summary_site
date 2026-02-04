import os

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
        # Extract title and author from naming convention "CODE-NNN - Title by Author"
        # Most files follow "COMM-001 - Title by Author.md"
        raw_name = f.replace(".md", "")
        
        # Remove prefix like "COMM-001 - "
        if " - " in raw_name:
            main_part = raw_name.split(" - ", 1)[1]
        else:
            main_part = raw_name
            
        if " by " in main_part:
            title, author = main_part.rsplit(" by ", 1)
        else:
            title = main_part
            author = "Expert Author"
            
        content += f'-   <span class="pw-badge" style="font-size: 0.6rem; margin-bottom: 8px;">{cat_name}</span>\n'
        content += f'    <div class="pw-book-title">{title}</div>\n'
        content += f'    <div class="pw-book-author">by {author}</div>\n'
        content += f'    <div class="pw-tag-container"><span class="pw-micro-tag">Key Insight</span> <span class="pw-micro-tag">Expert Review</span></div>\n'
        content += f'    [Read Summary :octicons-arrow-right-24:]({f})\n\n'
        
    content += '</div>\n'
    
    with open(index_path, 'w') as out:
        out.write(content)

print("Card-based category indices generated successfully.")
