import os

def cria_xml():
    for file_type in ["pos"]:
        for img in os.listdir((file_type)):
            if file_type == "neg":
                line = file_type+"/"+img+"\n"
                with open("teste.txt", "a") as f:
                    f.write(line)

cria_xml()