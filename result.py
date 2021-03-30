import demo

resultJson=demo.printJson()
fhw=open("json.txt","w")
fhw.write(resultJson)
fhw.close()
