class taskboss():

    # coded by zoha & hammad

    def signup(self,username,password):
        users = []
        with open("userdetail.txt","r") as file:#checking amount of users in system
            while True:
                line = file.readline().strip()
                if line:
                    users.append(line)
                else:
                    break

        if len(users) == 0:# deciding set admin or  not
            is_admin = True
            with open("userdetail.txt","a") as file:
                file.write(str(username))
        else:
            is_admin = False
            with open("userdetail.txt","a") as file:
                file.write("\n")
                file.write(str(username))

        with open(username+".txt","a") as file:#creating user's own detail file and adding
            file.write(str(password))
            file.write("\n")
            file.write(str(is_admin))
        return "Account Created Successfully"
        
     # coded by huzaifa

    def remove_task(self,r_task,username): #removing a particular task from the list
        reads = []
        loc = r_task.find("|")
        find = r_task[20:loc-1]
        with open(username+".txt","r") as file:
            while True:
                line = file.readline().strip()
                if line:
                    reads.append(line)
                else:
                    break
        for read in reads:
            loc = read.find("!")
            if read[0:loc] == find and loc != -1:
                reads.remove(read)
                break

        with open(username+".txt","w") as file:
            file.write(reads[0])
            reads.remove(reads[0])
            for read in reads:
                file.write("\n")
                file.write(read)

        return "Successfull"
        

        



    def add_task(self,touser,username,name,des,due,now): #adding tasks to other people's tasklist
        with open(touser+".txt","a") as file:
            content = str(name)+"!"+str(now)+"@"+str(username)+"#"+str(des)+"$"+str(due)+"*False"
            file.write("\n")
            file.write(content)

    def get_task(self,username):  #getting all tasks from the users tasklist
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
            read[i] = read[i].replace("!"," | Date Assigen: ")
            read[i] = read[i].replace("@"," | Assigen By: ")
            read[i] = read[i].replace("#"," | Description: ")
            read[i] = read[i].replace("$"," | Due Date: ")
            read[i] = read[i].replace("*"," | Date Competed: ")
        return read
    
    # coded by mian fardan
    
    def admin_list(self):  #returning list of all registered users
       reads = []
       with open("userdetail.txt","r") as file:
            while True:
                line = file.readline().strip()
                if line:
                    reads.append(line)
                else:
                    return reads
                
            
    def login(self,username,password):  # logging in
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
                else:
                    return "Incorrect Password"
            return read
        except FileNotFoundError:
            return "Invaild Username_"+username
        

    
    

