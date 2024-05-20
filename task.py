from datetime import datetime
import time
class taskboss():

    def encode_filename(self,temp):
        result = ""
        for i in range(0,len(temp)):
            hold = ord(temp[0:1])
            hold += 1590
            temp = temp[1:len(temp)]
            result += chr(hold)
        return result
    
    def decode_filename(self):
        for i in range(0,len(result)):
            hold = ord(result[0:1])
            hold -= 1590
            result = result[1:len(result)]
            temp += chr(hold)
        
    def Indiviual_reporting(self,user):
        read = []
        c = 0
        p = 0
        user = self.encode_filename(user)
        with open(user+".txt","r") as file:
            line = file.readline().strip()
            line = file.readline().strip()
            while True:
                line = file.readline().strip()
                if line:
                    read.append(line)
                else:
                    break
        for k in range(0,len(read)):
            if "*False" in read[i]:
                p += 1
            else:
                c += 1
            temp = ""
            for i in range(0,len(read)):
                if temp:
                    if int(temp[temp.find("^")+1:len(temp)]) < int(read[i][read[i].find("^")+1:len(read[i])]):
                        temp2 = read[i]
                        read[i] = temp
                        read[i-1] = temp2
                        temp = ""
                    elif (temp[temp.find("^")+1:len(temp)]) == int(read[i][read[i].find("^")+1:len(read[i])]):
                        if datetime(datetime.strptime((temp[temp.find("$")+1:temp.find("*")]),'%Y-%m-%d %H:%M:%S.%f')) - datetime(datetime.strptime((read[i][read[i].find("$")+1:read[i].find("*")]),'%Y-%m-%d %H:%M:%S.%f')) > 0:
                            temp2 = read[i]
                            read[i] = temp
                            read[i-1] = temp2
                            temp = ""
                temp = read[i]

        for i in range(0,len(read)): 
            read[i] = "Task name :"+read[i]
            read[i] = read[i].replace("!"," | Date Assigen: ")
            read[i] = read[i].replace("@"," | Assigen By: ")
            read[i] = read[i].replace("#"," | Description: ")
            read[i] = read[i].replace("$"," | Due Date: ")
            read[i] = read[i].replace("*"," | Date Competed: ")
            read[i] = read[i].replace("^"," | Priority: ")
        return read,c,p

    def complete_task(self,user,c_task):
        print(c_task)
        reads = []
        temp = ""
        loc = c_task.find("|")
        find = c_task[20:loc-1]
        user = self.encode_filename(user)
        with open(user+".txt","r") as file:
            while True:
                line = file.readline().strip()
                if line:
                    reads.append(line)
                else:
                    break
        for read in reads:
            loc = read.find("!")
            if read[0:loc] == find and loc != -1:
                temp = read
                reads.remove(read)
                break
        hold = temp[temp.find("^"):len(temp)]
        temp = temp[0:temp.find("*")] + "*"+str(datetime.today())+hold
        reads.append(temp)
        with open(user+".txt","w") as file:
            file.write(reads[0])
            reads.remove(reads[0])
            for read in reads:
                file.write("\n")
                file.write(read)
        return "Sucessfull"

    def make_admin(self,user):# Fardan
        reads = []
        with open(user+".txt","r") as file:
            while True:
                line = file.readline().strip()
                if line:
                    reads.append(line)
                else:
                    break

        reads[1] = "True"
        user = self.encode_filename(user)
        with open(user+".txt","w") as file:
            file.write(reads[0])
            for i in range(1,len(reads)):
                file.write("\n")
                file.write(reads[i])
        return "Successfull"

    def reporting(self):# Fardan
        report = []
        username = self.admin_list()
        for user in username:
            all_task = []
            c = 0
            t = 0
            p = 0
            user = self.encode_filename(user)
            with open(user+".txt","r") as file :
                line = file.readline().strip()
                line = file.readline().strip()
                while True:
                    line = file.readline().strip()
                    if line:
                        all_task.append(line)
                    else:
                        break
            
            t = len(all_task)

            for tasks in all_task:
                if "*False" in tasks:
                    p += 1
            c = t - p

            report.append(user+" has "+str(t)+" Task(s) and have completed "+str(c)+" Task(s) and has "+str(p)+" Pendding Task(s)")
    
        return report

    def signup(self,username,password):# Hammad
        if len(username) <3 or len(password) < 3:
            return "Detail too short"
        users = []
        with open("userdetail.txt","r") as file:#checking amount of users in system
            while True:
                line = file.readline().strip()
                if line:
                    users.append(line)
                else:
                    break

        if len(users) == 0:# deciding set admin or  not
            is_admin = "True"
            with open("userdetail.txt","a") as file:
                file.write(str(username))
        else:
            is_admin = "False"
            with open("userdetail.txt","a") as file:
                file.write("\n")
                file.write(str(username))
        username = self.encode_filename(username)
        with open(username+".txt","a") as file:
            file.write(password)
            file.write("\n")
            file.write(is_admin)

        return "Account Created Successfully"
        
     # coded by huzaifa

    def remove_task(self,r_task,username): #removing a particular task from the list Huzaifa
        reads = []
        loc = r_task.find("|")
        find = r_task[20:loc-1]
        username = self.encode_filename(username)
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
    
    def add_task(self,touser,username,name,des,due,now,priority): #adding tasks to other people's tasklist huzaifa
        touser = self.encode_filename(touser)
        with open(touser+".txt","a") as file:
            content = str(name)+"!"+str(now)+"@"+str(username)+"#"+str(des)+"$"+str(due)+"*False"+"^"+priority
            file.write("\n")
            file.write(content)

    def get_task(self,username):  #getting all tasks from the users tasklist zoha
        read = []
        username = self.encode_filename(username)
        with open(username+".txt","r") as file:
            line = file.readline().strip()
            line = file.readline().strip()
            while True:
                line = file.readline().strip()
                if line:
                    if "*False" in line:
                        read.append(line)
                else:
                    break
        for k in range(0,len(read)):
            temp = ""
            for i in range(0,len(read)):
                if temp:
                    if int(temp[temp.find("^")+1:len(temp)]) < int(read[i][read[i].find("^")+1:len(read[i])]):
                        temp2 = read[i]
                        read[i] = temp
                        read[i-1] = temp2
                        temp = ""
                    elif (temp[temp.find("^")+1:len(temp)]) == int(read[i][read[i].find("^")+1:len(read[i])]):
                        if datetime(datetime.strptime((temp[temp.find("$")+1:temp.find("*")]),'%Y-%m-%d %H:%M:%S.%f')) - datetime(datetime.strptime((read[i][read[i].find("$")+1:read[i].find("*")]),'%Y-%m-%d %H:%M:%S.%f')) > 0:
                            temp2 = read[i]
                            read[i] = temp
                            read[i-1] = temp2
                            temp = ""
                temp = read[i]

        for i in range(0,len(read)): 
            read[i] = "Press "+str(i)+": "+"Task name :"+read[i]
            read[i] = read[i].replace("!"," | Date Assigen: ")
            read[i] = read[i].replace("@"," | Assigen By: ")
            read[i] = read[i].replace("#"," | Description: ")
            read[i] = read[i].replace("$"," | Due Date: ")
            read[i] = read[i].replace("*"," | Date Competed: ")
            read[i] = read[i].replace("^"," | Priority: ")
        return read
    
    # coded by mian fardan
    
    def admin_list(self):  #returning list of all registered users Abdul...
       reads = []
       with open("userdetail.txt","r") as file:
            while True:
                line = file.readline().strip()
                if line:
                    reads.append(line)
                else:
                    return reads
                
            
    def login(self,username,password):  # logging in zoha
        read = []
        try:
            username = self.encode_filename(username)
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
                    print("Incorrect usernsme or Password")
            return read
        except FileNotFoundError:
            print("Incorrect usernsme or Password")
        time.sleep(5)
        quit()