class taskboss():


    def add_task(self,touser,username,name,des,due,now):
        with open(touser+".txt","a") as file:
            content = str(name)+"!"+str(now)+"@"+str(username)+"#"+str(des)+"$"+str(due)+"*False"
            file.write("\n")
            file.write(content)


    def get_task(self,username):
        read = []
        with open(username+".txt","r") as file:
            line = file.readline().strip()
            line = file.readline().strip()
            while True:
                line = file.readline().strip()
                if line:
                    read.append(line)
                else:
                    break
        for i in range(0,len(read)):
            read[i] = "Press "+str(i)+": "+"Task name :"+read[i]
            read[i] = read[i].replace("!"," | Date assigen: ")
            read[i] = read[i].replace("@"," | Assigen by: ")
            read[i] = read[i].replace("#"," | Description: ")
            read[i] = read[i].replace("$"," | Due date: ")
            read[i] = read[i].replace("*"," | Date competed: ")
        return read
    
    def admin_list(self):
       reads = []
       with open("userdetail.txt","r") as file:
            while True:
                line = file.readline().strip()
                if line:
                    reads.append(line)
                else:
                    return reads
                
            
    def login(self,username,password):
        read = []
        try:
            with open(username+".txt","r") as file:
                line = file.readline().strip()
                if password == line:
                    while True:
                        line = file.readline().strip()
                        if line:
                            read.append(line)
                        else:
                            break
            return read

        except FileNotFoundError:
            return "Invaild username_"+username
        

    
    

