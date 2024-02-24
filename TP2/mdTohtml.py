import re
import sys

# Ler o conteúdo do arquivo .md
with open("teste.md", "r", encoding="utf-8") as file:
    md_content = file.read()

def convert_line(line):
    h1 = re.compile("^(\#) (.*)")
    h2 = re.compile("^(\#\#) (.*)")
    h3 = re.compile("^(\#\#\#) (.*)")
    link = re.compile("^\[(.*)\]\((.*)\)")
    img = re.compile("!\[(.*)\]\((.+)\)")
    b = re.compile("(\*\*)(.*)(\*\*)")
    i = re.compile("(\*)(.*)(\*)")
    list = re.compile("^\d+\.(.+)$")

    line = re.sub(h1,r'<h1>\2</h1>', line)
    line = re.sub(h2,r'<h2>\2</h2>', line)
    line = re.sub(h3,r'<h3>\2</h3>', line)
    line = re.sub(link,r'<a href="\2">\1</a>', line)
    line = re.sub(img,r'<img src="\2" alt="\1"/>', line)
    line = re.sub(b,r'<b>\2</b>', line)
    line = re.sub(i,r'<i>\2</i>', line)
    line = re.sub(list, r'<li>\1</li>', line)
    return line

def convertelistas(listas):
    resultado = "<ol>\n"
    for item in listas:
        resultado += f"     <li>{item}</li>\n"
    resultado += "</ol>"
    return resultado


def main(inp):
    if len(inp) == 3:
        lines = []
        listas = []
        with open(inp[1]) as in_file: 
            for line in in_file:
                # Guardar as linhas do ficheiro numa lista
                lines.append(line)
                
        with open(inp[2], "w") as output_file:
            output_file.write("<html>\n")
            i = 0
            while i < len(lines):
                line = convert_line(lines[i]) 
                match_list = re.findall("^\d+\. (.+)", lines[i])
                if match_list:
                    listas.append(match_list[0])
                else:
                    if listas:
                        output_file.write(convertelistas(listas))
                        listas = []
                    else:
                        output_file.write(line)
                i += 1
                
            if listas:
                output_file.write(convertelistas(listas))
            output_file.write("\n</html>")

if __name__ == "__main__":
    main(sys.argv)