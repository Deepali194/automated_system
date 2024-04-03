import os
import pyttsx3
import webbrowser
from art import *
kn=''
sss=''
sg=''
mip=''
uip=''
def aws():
    pyttsx3.speak("Welcome to AWS World")
    pyttsx3.speak("Now I cal do Following things for you")
    while True:
        tprint("aws",font="block",chr_ignore=True)
        print("\t\t\t ----- Welcome to AWS Automation world  ----- \t\t\t")
        print("Please select anyone of the following")
        print("Press 1: Create Key pair")
        print("Press 2: Create Security Group and Rules")
        print("Press 3: Create Ec2 instance")
        print("Press 4: Create EBS volume")
        print("Press 5: Attach EBS volume to the instance")
        print("Press 6: Install Webserver inside Ec2 instance")
        print("Press 7: TO mount EBS volume to webserver directory")
        print("Press 8: Deploy webpages to the webserver")
        print("Press 9: Create S3 Bucket")
        print("Press 10: Put the data inside S3 bucket")
        print("Press 11: Create CloudFront Distribution")
        print("Press 12: Launching the CLoudfront distribution")
        print("Press 13: Launching the website")
        print("Press 14: Go Back")
        x = input("Please enter your choice: ")
        if(int(x)==1):
            pyttsx3.speak('Creating key pairs for you')
            pyttsx3.speak("Please enter Key pair name")
            na = input("enter key pair name: ")
            os.system('aws ec2 create-key-pair --key-name '+na+' --query KeyMaterial --output text>mykey.pem')
            pyttsx3.speak("Key Pair has been Created For you")
            os.system('aws ec2 describe-key-pairs --key-name '+na)
        elif(int(x)==2):
            pyttsx3.speak("Please enter Security group name")
            sg = input("Enter Security Group name: ")
            pyttsx3.speak("Creatng Security Group for you")
            os.system('aws ec2 create-security-group --group-name '+sg+' --description "security group for aws task" --vpc-id vpc-78c4d010')
            pyttsx3.speak("Security Group has been Created")
            pyttsx3.speak("Please Enter what rules you want to add to the security groups")
            rul1=input("Enter 1st Rule: ")
            rule2=input("Enter 2nd Rule: ")
            os.system('aws ec2 authorize-security-group-ingress --group-name '+sg+' --protocol tcp --port 22 --cidr 0.0.0.0/0')
            os.system('aws ec2 authorize-security-group-ingress --group-name '+sg+' --protocol tcp --port 80 --cidr 0.0.0.0/0')
            pyttsx3.speak("Rules has been Created Successfully")
        elif(int(x)==3):
            pyttsx3.speak("Please Give me instance Configuration")
            pyttsx3.speak("Enter the Instance type: ")
            it = input("Enter the Instance Type: ")
            pyttsx3.speak("Give me Key Pair name")
            kn = input("Enter the Key Pair Name: ")
            pyttsx3.speak("Eneter Security group name")
            sgn = input("Enter SecurityGroup name: ")
            pyttsx3.speak("Launching Ec2 instance for you")
            os.system('aws ec2 run-instances --key-name '+kn+' --image-id ami-0e306788ff2473ccb --instance-type '+it+'   --security-groups '+sgn+' --count 1')
            pyttsx3.speak("Instance has been launched Successfully")
        elif(int(x)==4):
            pyttsx3.speak("Creating EBS volume for you")
            pyttsx3.speak("Enter Availability-zone")
            az = input("Enter Availability Zone")
            os.system('aws ec2 create-volume --availability-zone '+az+' --volume-type gp2 --size 2 --tag-specifications "ResourceType=volume,Tags=[{Key=name,Value=ebs_for_task2}]"')
            pyttsx3.speak("EBS volume has been created")
        elif(int(x)==5):
            pyttsx3.speak("Enter The EBS volume ID")
            vid = input('Enter the Volume ID: ')
            pyttsx3.speak("Give me the Instance Id in which you want to attach the volume")
            iid =input("Enter the Instance ID")
            pyttsx3.speak("Attaching the EBS volume to the Running Instance")
            os.system('aws ec2 attach-volume --volume-id '+vid+' --instance-id '+iid+'  --device  /dev/xvdh')
        elif(int(x)==6):
            pyttsx3.speak("Please Provide the ip of Ec2 instance")
            ip = input('Enter The IP of instance: ')
            pyttsx3.speak("Installing WebServer Inside Ec2 instance")
            os.system('ssh -i mykey.pem ec2-user@'+ip+' sudo yum install httpd -y')
            os.system('ssh -i mykey.pem ec2-user@'+ip+' sudo systemctl start httpd')
            pyttsx3.speak("Webserver has been Installed")
        elif(int(x)==7):
            pyttsx3.speak("Mounting EBS volume for you")
            os.system('ssh -i mykey.pem ec2-user@'+ip+' sudo mkfs.ext4 /dev/xvdh')
            #os.system('ssh -i mykey.pem ec2-user@'+ip+' sudo rm -rf /var/www/html/*')
            os.system('ssh -i mykey.pem ec2-user@'+ip+' sudo mount /dev/xvdh /var/www/html')
            os.system('ssh -i mykey.pem ec2-user@'+ip+' sudo rm -rf /var/www/html/*')
            pyttsx3.speak("EBS volume has been mounted")
        elif(int(x)==8):
            pyttsx3.speak("deploying Webpages for you")
            os.system('ssh -i mykey.pem ec2-user@'+ip+' sudo yum install git -y')
            os.system('ssh -i mykey.pem ec2-user@'+ip+' "sudo git clone https://github.com/yogi456/test-web1.git /var/www/html/')
            pyttsx3.speak("Webpages have been deployed Successfully")
        elif(int(x)==9):
            pyttsx3.speak("Please provide the name you wanna give to s3")
            sss = input("Enter the name for s3 bucket")
            os.system('aws s3api create-bucket --bucket  '+sss+' --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1')
            pyttsx3.speak("S3 bucket has been Created")
        elif(int(x)==10):
            pyttsx3.speak("Putting the data inside s3 bucket")
            os.system('aws s3 cp building.jpg  s3://'+sss+'/data.jpg --acl public-read-write')
            pyttsx3.speak("Data has been copied Successfully")
        elif(int(x)==11):
            pyttsx3.speak('creating cloudfront distribution for you')
            os.system('aws cloudfront create-distribution   --origin-domain-name '+sss+'.s3.amazonaws.com  --default-root-object data.jpg')
        elif(int(x)==12):
            did = input("Enter distribution ID")
            mydomain = os.system('aws cloudfront get-distribution --id='+did+' --query Distribution.DomainName')
            #webbrowser.open(mydomain)
            print(mydomain)
            #webbrowser.open('http://d29lk1h18byza1.cloudfront.net')
        elif(int(x)==13):
            pyttsx3.speak("Launching Website for you")
            webbrowser.open('http://'+ip)
        else:
           menu1()
def hamaster():
    mip = input("Enter master Ip")
    
    while True:
        #tprint("Name Node",font="block",chr_ignore=True)
        #tprint("NAME NODE ","rand")
        tprint("NAME NODE",font="cybermedum")
        print("Press 1: To copy the hadoop setup files: ")
        print("Press 2: TO install jdk in the Name node: ")
        print("Press 3: To install Hadoop in the Name node: ")
        print("Press 4: To check the JDK is installed or not: ")
        print("Press 5: To Check Hadoop is installed or not: ")
        print("Press 6: To Setup the Name Node configuration: ")
        print("Press 7: To Create Name Node Directory: ")
        print("Press 8: To Format the Master Node: ")
        print("Press 9: To start the Name node: ")
        print("Press 10: To see Hadoop is started or not: ")
        print("Press 11: To see the detailed report of Hadoop Cluster: ")
        print("Press 12: To go Back")
        hm = input("Please enter your Choice: ")
        if(int(hm)==1):
            pyttsx3.speak("Copying the hadoop setup files")
            os.system('scp -i myforaws.pem jdk-8u171-linux-x64.rpm ec2-user@'+mip+':/home/ec2-user')
            os.system('scp -i myforaws.pem hadoop-1.2.1-1.x86_64.rpm ec2-user@'+mip+':/home/ec2-user')
            pyttsx3.speak("FIles copied Successfully")
        elif(int(hm)==2):
            pyttsx3.speak("Installing JDk in the Name node")
            os.system('ssh -i myforaws.pem ec2-user@'+mip+' sudo rpm -ivh jdk-8u171-linux-x64.rpm')
        elif(int(hm)==3):
            pyttsx3.speak("Insatalling Hadoop in the Name Node")
            os.system('ssh -i myforaws.pem ec2-user@'+mip+' sudo rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force')
            pyttsx3.speak("Hadoop has been installed")
        elif(int(hm)==4):
            pyttsx3.speak("Checking JDK is installed or not")
            os.system('ssh -i myforaws.pem ec2-user@'+mip+' java -version')
        elif(int(hm)==5):
            pyttsx3.speak("Checking Hadoop is installed or not")
            os.system('ssh -i myforaws.pem ec2-user@'+mip+' hadoop version')
        elif(int(hm)==6):
            pyttsx3.speak("Setting Up namenode configuration")
            os.system('ssh -i myforaws.pem ec2-user@'+mip+' sudo rm -rf /etc/hadoop/core-site.xml')
            os.system('ssh -i myforaws.pem ec2-user@'+mip+' sudo rm -rf /etc/hadoop/hdfs-site.xml')
            os.system('scp -i myforaws.pem hadoop_master\core-site.xml ec2-user@'+mip+':/home/ec2-user/')
            os.system('scp -i myforaws.pem hadoop_master\hdfs-site.xml ec2-user@'+mip+':/home/ec2-user/')
            os.system('ssh -i myforaws.pem ec2-user@'+mip+' sudo cp  /home/ec2-user/core-site.xml /etc/hadoop')
            os.system('ssh -i myforaws.pem ec2-user@'+mip+' sudo cp /home/ec2-user/hdfs-site.xml /etc/hadoop')
            
        elif(int(hm)==7):
            pyttsx3.speak("Creating Name Node Directory")
            os.system('ssh -i myforaws.pem ec2-user@'+mip+' sudo mkdir /nn1')
            pyttsx3.speak("Name Node Directory has been created")
        elif(int(hm)==8):
            pyttsx3.speak("Formatting Name node")
            os.system('ssh -i myforaws.pem ec2-user@'+mip+' hadoop namenode -format')
        elif(int(hm)==9):
            pyttsx3.speak("Starting Name node")
            os.system('ssh -i myforaws.pem ec2-user@'+mip+' sudo hadoop-daemon.sh start namenode')
            pyttsx3.speak("Name node has been started")
        elif(int(hm)==10):
            pyttsx3.speak("Checking the Name node status")
            os.system('ssh -i myforaws.pem ec2-user@'+mip+' jps')
        elif(int(hm)==11):
            pyttsx3.speak("Showing report of hadoop cluster")
            os.system('ssh -i myforaws.pem ec2-user@'+mip+' sudo hadoop dfsadmin -report')
        else:
            hadoop()
            
def dnode():
    pyttsx3.speak("Welcome to HADOOP DATA NODE")
    sip=input('Enter slave IP')
    while True:
        tprint("DATA NODE",font="cybermedum")
        print("Press 1: To copy the hadoop setup files: ")
        print("Press 2: TO install jdk in the DATA  node: ")
        print("Press 3: To install JDK in the DATA node: ")
        print("Press 4: To check the JDK is installed or not: ")
        print("Press 5: To Check Hadoop is installed or not: ")
        print("Press 6: To Setup the DATA Node configuration: ")
        print("Press 7: To Create DATA Node Directory: ")
        print("Press 8: To start the DATA node: ")
        print("Press 9: To see Hadoop is started or not: ")
        print("Press 10: To see the detailed report of Hadoop Cluster: ")
        print("Press 11: To go Main Menu")
        hdn = input("Please enter your Choice: ")
        if(int(hdn)==1):
            pyttsx3.speak("Copying the hadoop setup files")
            os.system('scp -i myforaws.pem jdk-8u171-linux-x64.rpm ec2-user@'+sip+':/home/ec2-user')
            os.system('scp -i myforaws.pem hadoop-1.2.1-1.x86_64.rpm ec2-user@'+sip+':/home/ec2-user')
            pyttsx3.speak("FIles copied Successfully")
        elif(int(hdn)==2):
            pyttsx3.speak("Installing JDK In the Data node")
            os.system('ssh -i myforaws.pem ec2-user@'+sip+' sudo rpm -ivh jdk-8u171-linux-x64.rpm')
        elif(int(hdn)==3):
            pyttsx3.speak("Installing Hadoop in the DATA node")
            os.system('ssh -i myforaws.pem ec2-user@'+sip+' sudo rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force')
            
        elif(int(hdn)==4):
            pyttsx3.speak("Checking JDK is installed or not")
            os.system('ssh -i myforaws.pem ec2-user@'+sip+' java -version')
            
        elif(int(hdn)==5):
            pyttsx3.speak("CHecking Hadoop is installed or not")
            os.system('ssh -i myforaws.pem ec2-user@'+sip+' hadoop version')

        elif(int(hdn)==6):
            pyttsx3.speak("Configuring data node")
            os.system('ssh -i myforaws.pem ec2-user@'+sip+' sudo rm -rf /etc/hadoop/core-site.xml')
            os.system('ssh -i myforaws.pem ec2-user@'+sip+' sudo rm -rf /etc/hadoop/hdfs-site.xml')
            os.system('scp -i myforaws.pem hadoop_master\hadoop_slave\core-site.xml ec2-user@'+sip+':/home/ec2-user')
            os.system('scp -i myforaws.pem hadoop_master\hadoop_slave\hdfs-site.xml ec2-user@'+sip+':/home/ec2-user/')
            os.system('ssh -i myforaws.pem ec2-user@'+sip+' sudo cp  /home/ec2-user/core-site.xml /etc/hadoop')
            os.system('ssh -i myforaws.pem ec2-user@'+sip+' sudo cp /home/ec2-user/hdfs-site.xml /etc/hadoop')

            
        elif(int(hdn)==7):
            pyttsx3.speak("Creating Data node directory")
            os.system('ssh -i myforaws.pem ec2-user@'+sip+' sudo mkdir /dn1')
        elif(int(hdn)==8):
            pyttsx3.speak("Starting data node")
            os.system('ssh -i myforaws.pem ec2-user@'+sip+' sudo hadoop-daemon.sh start datanode')
            pyttsx3.speak("Data node has been started")
        elif(int(hdn)==10):
            pyttsx3.speak("Showing detailed report of hadoop cluster")
            os.system('ssh -i myforaws.pem ec2-user@'+sip+' sudo hadoop dfsadmin -report')
        elif(int(hdn)==9):
            pyttsx3.speak("CHeckinh data node services")
            os.system('ssh -i myforaws.pem ec2-user@'+sip+' sudo jps')
        else:
            menu1()


def upfile():
    uip = input("Enter Your slave IP")
    while True:
        print("Press 1: to upload the file")
        print("Press 2: to see all the files")
        print("Press 3: To Read the file")
        print("Press 4: to go back")
        myc = input("Enter your choice: ")
        if(int(myc)==1):
            os.system('ssh -i myforaws.pem ec2-user@'+uip+' sudo hadoop fs -put myfile.txt /')
        elif(int(myc)==2):
            os.system('ssh -i myforaws.pem ec2-user@'+uip+' sudo hadoop fs -ls /')
        elif(int(myc)==3):
            os.system('ssh -i myforaws.pem ec2-user@'+uip+' sudo hadoop fs -cat /myfile.txt')

        else:
            menu1()



def hadoop():
    pyttsx3.speak("Welcome to the hadoop world")
    while True:
        tprint("Hadoop",font="block",chr_ignore=True)
        print("Press 1: To Configure Name Node")
        print("Press 2: To configure Slave Nodes")
        print("Press 3: Uploading files to hadoop cluster")
        print("Press 4: To Go Back")
        hnn=input("Enter your choice: ")
        if(int(hnn)==1):
            hamaster()
        elif(int(hnn)==2):
            dnode()
        elif(int(hnn)==3):
            upfile()
        else:
            menu1()


    
def elhadoop():
    print("hello")
    
def linux():
    pyttsx3.speak('Welcome to Linux automation')
    while True:
        tprint("LINUX",font="cybermedum")
        print("Press 1: TO run date command")
        print("Press 2: To see the calender")
        print("Press 3: To see the disk details")
        print("Press 4: To see the all User Details")
        print("Press 5: To see the basic Os details")
        print('Press 6: To see the CPU details')
        print("Press 7: To see The memory details")
        print("Press 8: TO go back")
        lin = input("Please enter your choice: ")
        if(int(lin)==1):
            pyttsx3.speak("Running date command")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 date')
        elif(int(lin)==2):
            pyttsx3.speak("Showing calender to you")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 cal')
        elif(int(lin)==3):
            pyttsx3.speak("Showing disk details")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo fdisk -l')
        elif(int(lin)==4):
            pyttsx3.speak("Showing all user details")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo cat /etc/passwd')
        elif(int(lin)==5):
            pyttsx3.speak("Showing basic os details")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 cat /etc/os-release')
        elif(int(lin)==6):
            pyttsx3.speak("Showing basic CPU Details")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 lscpu')
        elif(int(lin)==7):
            pyttsx3.speak("Showing memory details")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 free -h')
        else:
            menu1()


def docker():
    print("Welcome to docker")
    pyttsx3.speak("Welcome to Docker Automation")
    pyttsx3.speak("Now I can Do following things")
    while True:
        tprint("DOCKER",font="cybermedum")
        print("Press 1: Install Docker-ce ")
        print("Press 2: To check Docker-ce is installed or not")
        print("Press 3: To check Docker Services status")
        print("Press 4: TO start docker services")
        print("Press 5: Download the docker Image")
        print("Press 6: List all the docker images")
        print("Press 7: Launch the docker container")
        print("Press 8: How many docker Container is runnintg")
        print("Press 9: To Install Webserver Inside container")
        print("Press 10: Deploy the code to the webserver")
        print("Press 11: Start the webserver")
        print("press 12: Launch the website")
        print("Press 13: Install Python inside docker container")
        print("Press 14: Run the Python code inside docker container")
        y=int(input("Enter your Choice: "))
        if(y==1):
            pyttsx3.speak("Installing Docker community edition for you")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo yum install docker-ce -y --nobest')
            pyttsx3.speak("Docker has been installed successfully")
        elif(y==2):
            pyttsx3.speak("Checking docker is installed or not")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo rpm -q docker-ce')
        elif(y==3):
            pyttsx3.speak("Checking status of docker services")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo systemctl status docker')
        elif(y==4):
            pyttsx3.speak("Starting docker services")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo systemctl start docker')
            pyttsx3.speak("Docker services has been successfully started")
        elif(y==5):
            pyttsx3.speak("Please provide Image name ")
            a=input("Enter Image name: ")
            pyttsx3.speak("Please provide tags for image")
            b=input("Enter tag details: ")
            pyttsx3.speak("Pulling Image for you")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo docker pull '+a+':'+b)
            pyttsx3.speak(" container Image has been successfully pulled")
        elif(y==6):
            pyttsx3.speak("Showing docker images")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo docker images')
        elif(y==7):
            pyttsx3.speak("please provide image name")
            x=input("Enter Docker Image name: ")
            pyttsx3.speak("Please Provide the Tag ")
            y= input("Enter tag: ")
            pyttsx3.speak("plese Provide the name you wanna give to container")
            n = input("Enter container name: ")
            pyttsx3.speak("Launching docker container For you")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo docker run -dit --name '+n+' -p 1224:80 '+x+ ':'+y+' ')
            pyttsx3.speak('Your conatainer named'+n+'has been launched')
        elif(y==8):
            pyttsx3.speak("Showing all the containers")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo docker ps')
        elif(y==9):
            pyttsx3.speak("Installing Webserver inside container")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo docker exec '+n+' yum install httpd -y')
        elif(y==10):
            pyttsx3.speak("Copying web pages for you")
           # os.system("ssh -i myforaws.pem ec2-user@13.233.254.216 sudo mkdir /home/ec2-user/mydata")
            #os.system("ssh -i myforaws.pem ec2-user@13.233.254.216 sudo git clone https://github.com/yogi456/automaiton1.git /home/ec2-user/mydata/")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo docker cp  /home/ec2-user/index.html myos:/var/www/html')
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo docker cp /home/ec2-user/myp.py '+n+':/')
            pyttsx3.speak("Web pages have been successfully deployed")
        elif(y==11):
            pyttsx3.speak("Starting Webserver for you")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo docker exec myos /usr/sbin/httpd')
        elif(y==12):
            pyttsx3.speak("Launching website for you")
            webbrowser.open("http://13.233.252.13:1224")
        elif(y==13):
            pyttsx3.speak("Installing Python inside docker container")
            os.system('ssh -i myforaws.pem ec2-user@13.233.252.13 sudo docker exec myos yum install python36 -y')
        elif(y==14):
            os.system("ssh -i myforaws.pem ec2-user@13.233.252.13 sudo docker exec myos python3 /myp.py")
        else:
            exit()

def menu1():
    print("Welcome to the world of Automation")
    print("Please Choose what you want me to do")
    print("Press 1: Creating High Availability Architecture")
    print("Press 2: Setting Up Hadoop Cluster")
    print("Press 3: To Run basic Linux commands")   
    print("Press 4: TO Install docker and Webserver Inside it")
    print("Press 5: Exit the Program")
    c = input('Enter your choice: ')
    if(int(c)==1):
        aws()
    elif(int(c)==2):
        hadoop()
    elif(int(c)==3):
        linux()
    elif(int(c)==4):
        docker()
    else:
        exit()
    

menu1()

 #mydomain =  os.system('aws cloudfront get-distribution --id='+did+' --query Distribution.DomainName')
