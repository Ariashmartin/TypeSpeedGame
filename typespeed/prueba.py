
dif=int(input("Ingrese DIFICULTAD\n>>"))
name="Martin"
cond="1"
vidas=""
if dif ==1:
    vidas="5"
if dif==4:
    vidas="None"
if dif >1 and dif <4:
    vidas="3"

lita=str(name +","+ cond +",0,"+vidas)

print(lita)