import markdown
import sys 

text = sys.stdin.read()
print markdown.markdown(text)