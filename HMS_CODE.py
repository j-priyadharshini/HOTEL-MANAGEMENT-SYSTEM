import mysql.connector as ms
import datetime
import time
import os
# import cfonts

room= 3
class hotelfarecal:
    now = datetime.datetime.now()

    def __init__(self, r_type='', Noofdays=0, bill=0.0, firstname='',lastname='',email='',country='', user_address='', checkindate='', checkoutdate='', rno=0, userid=0):

        print('WELCOME TO HOTEL CALIFORNIA')

        self.r_type = r_type
       
        self.Noofdays = Noofdays
        self.bill = bill
        self.firstname = firstname
        self.lastname = lastname
        self.user_address = user_address
        self.checkindate = checkindate
        self.checkoutdate = checkoutdate
        self.rno = rno
        self.email=email
        self.country=country

        self.userid = userid

    def connectos(self):
        cnx = ms.connect( user='root', password='makeuprani', database='hotel_mgmt')
        try:

            cur = cnx.cursor()
            cur.execute('Select * from customer ;')
            d = cur.fetchall()

            cnx.commit()
        except:
            print('Error in connection')


    def inputdata(self):
        global room
        # ('clear')
        self.firstname = input('Enter your first name:')
        self.lastname = input('Enter your last name:')
        self.user_address = input('Enter your user_address:')
        self.country=input('Enter your country:')
        self.email=input('Enter your E-mail user_address:')
        # ('clear')
        self.checkindate = input('Enter your check in date:')
        self.checkoutdate = input('Enter your checkout date:')
        v = int(input('Enter your room type:- \n \n1.Single cot = Rs.1500 per day \n2.Double cot = Rs.2500 per day\n'))
        if v==1:
            self.r_type ='Single cot'
            am =1500
        else:
            self.r_type = 'Double cot' 
            am =2500   
        cnx = ms.connect( user='root', password='makeuprani', host='localhost', database='hotel_mgmt')
        cur = cnx.cursor()
        cur.execute("Select max(userid) from customer")
        d = cur.fetchall()
        if d== None:
            self.userid=1
        else:    

            val=int(d[0][0]) +1
            self.userid = val

        cur.execute("Select max(rno) from customer")
        d = cur.fetchall()
        if d== None:
            self.rno=100
        else:    
            val=int(d[0][0]) +1
            self.userid = val 
       
        #     self.userid = 1
        # else:
        #     self.userid = v + 1
        #     cur.execute("Select max(rno) from customer")
        #     d = cur.fetchall()
        #     str4 = ','.join([str(i) for i in d])
        #     str5 = str4[1:]
        #     str6 = str5[:1]
        #     valr = int(str6)

        # if cur.rowcount == 0:
        #     # print(cur.rowcount,'  fdgdfgdffgfd')
        #     self.rno = 1

        # else:
        #     self.rno = valr + 1



        x = int(input('Enter the number of days you will be spending with us\t'))
        self.Noofdays = x
        # ('clear')    
        self.bill= x* am
        print('Your room no.:', self.rno, '\n')
        print('User id is:', self.userid, '\n')
        print('Your bill :',self.bill,'\n','\n')
        # sql="INSERT INTO customer('firstname',lastname, user_address,email,country, checkindate, checkoutdate,r_type,rno,bill,userid,Noofdays)  values ('%s','%s','%s','%s','%s','%s','%s','%s',%f,%d,%d)"
        # val=(self.firstname, self.lastname,self.user_address,self.email,self.country, self.checkindate, self.checkoutdate,self.r_type,self.rno,self.bill,self.userid,self.Noofdays)
        # cur.execute(sql,val)
        # print("INSERT INTO customer(firstname,lastname, user_address,email,country, checkindate, checkoutdate,r_type,rno,bill,userid,Noofdays)  values ('%s','%s','%s','%s','%s','%s','%s','%s',%d,%f,%d,%d)" 
        # % (self.firstname, self.lastname,self.user_address,self.email,self.country, self.checkindate, self.checkoutdate,self.r_type,self.rno,self.bill,self.userid,self.Noofdays))
        cur.execute("INSERT INTO customer(firstname,lastname, user_address,email,country, checkindate, checkoutdate,r_type,rno,bill,userid,Noofdays)  values ('%s','%s','%s','%s','%s','%s','%s','%s',%d,%f,%d,%d)"%(self.firstname, self.lastname,self.user_address,self.email,self.country, self.checkindate, self.checkoutdate,self.r_type,self.rno,self.bill,self.userid,self.Noofdays))
        cnx.commit()
        cur.execute("INSERT INTO rooms(userid, r_type, bill) VALUES (%d,'%s',%f)" % (self.userid,  self.r_type, self.bill))
        cnx.commit()
        cur.close()
        cnx.close()
        print('Thank you for registering!')


    # def update(self):
    #     id=int(input('To update your details ,please provide your User_id'))
    #     cnx = ms.connect( user='root', password='makeuprani', host='localhost', database='hotel_mgmt')
    #     cur = cnx.cursor()
    #     while(1):
    #         print('Choose your option:-\n \n1.Change room type\n 2.Change the check-in date\n 3.Change the check-out date\n 4.EXIT\n\n\n')
    #         b = int(input('Enter your choice:'))
    #         if (b == 1):
    #             r=int(input('Change to single cot -1\nChange to double cot'))
    #             if(r==1):
    #                 t='Single cot'
                    
    #             else:
    #                 t='Double cot'

    #             cur.execute('update customer ')        
    #         elif (b == 2):
    #             update()
    #         elif (b == 3):
    #             cancel()
    #         elif (b == 4):
    #             quit()
    #         else:
    #             print('Error', space=True)    

    def cancel(self):
        cnx = ms.connect( user='root', password='makeuprani', host='localhost', database='hotel_mgmt')
        cur = cnx.cursor()
        id=int(input('TO cancel your registration ,please provide your User_id'))
        cur.execute("select userid from customer")
        d = cur.fetchall()
        flag=False
        for i in d:
            if i[0]== id:
                cur.execute('delete from customer where userid = %d' % id)
                cnx.commit()
                cur.execute('delete from rooms where userid = %d' % id)
                cnx.commit()
               
                flag= True
        if not flag:
            print("User ID does not exist.\nTry again")
        else:
       
        # ('clear')
            print('Your registration has been cancelled !')
       
        cur.close()
        cnx.close()

    def user(self):
        # ('clr')
        print('\n1.Enter Customer Data')
        # print('2.Update customer details')
        print('2.Cancel your registration')
        print('3.EXIT\n\n\n')

        b = int(input('Enter your choice:'))
        if (b == 1):
            self.inputdata()
        # elif (b == 2):
        #     self.update()
        elif (b == 2):
            self.cancel()
        elif (b == 3):
            quit()
        else:
            print('Error', space=True)
    def view_customers(self):
        cnx = ms.connect( user='root', password='makeuprani', host='localhost', database='hotel_mgmt')
        cur = cnx.cursor()
        cur.execute("select * from customer")
        d = cur.fetchall()
        for i in d:
            s=""
            for x in i:
                s = s+'   '+str(x)
            print(s, '\n')
        cnx.commit()
        cur.close()
        cnx.close()
    def view_rooms(self): 
        cnx = ms.connect( user='root', password='makeuprani', host='localhost', database='hotel_mgmt')
        cur = cnx.cursor()       
        cur.execute("select * from rooms")
        d = cur.fetchall()
        for i in d:
            s=""
            for x in i:
                s = s+'  '+str(x)
            print(s, '\n')
        cnx.commit()
        cur.close()
        cnx.close()

    def receptionist(self):
      while(1):

            num=int(input('\n1.To view customer details\n2.To view room details\n3.EXIT\n\n\n'))
            if num==1:
                self.view_customers()
            elif num==2:
                self.view_rooms()
            else:
                quit()
    def add_rec(self):
            rec_id = int(input('Enter the receptionist ID:'))
            rec_name = input('Enter the receptionist name:')
            address = input('Enter the receptionist address:')
            salary=float(input('Enter the receptionist monthly salary:'))
            email=input('Enter the receptionist email id:')
            cnx = ms.connect( user='root', password='makeuprani', host='localhost', database='hotel_mgmt')
            cur = cnx.cursor()
            print("\nReceptionist added successfully !!\n")
            cur.execute("insert into receptionist(rec_id,rec_name,rec_address,email,salary) values (%d,'%s','%s','%s',%f)" % (rec_id,rec_name,address,email,salary))
            cnx.commit()
            cur.close()
            cnx.close()
    def view_rec(self):
        cnx = ms.connect( user='root', password='makeuprani', host='localhost', database='hotel_mgmt')
        cur = cnx.cursor()
        cur.execute("select * from receptionist")
        d = cur.fetchall()
        for i in d:
            s=""
            for x in i:
                s = s+'    '+str(x)
            print(s, '\n')
        cnx.commit()
        cur.close()
        cnx.close()
    def rem_rec(self):
        cnx = ms.connect( user='root', password='makeuprani', host='localhost', database='hotel_mgmt')
        cur = cnx.cursor()
        id=int(input('To remove a receptionist ,please provide respective id number : '))
        cur.execute("select rec_id from receptionist")
        d = cur.fetchall()
        flag=False
        for i in d:
            if i[0]== id:
                cur.execute("delete from receptionist where rec_id = %d" % (id))
                cnx.commit()
                flag=True
                
        if not flag:
            print("REceptionist with ID does not exist.\nTry again")
        else:
        
            # ('clear')
            print('Receptionist with id ',id,'has been removed !')

        cur.close()
        cnx.close()
    def manager(self):
       
        while(1):
            num=int(input('\n1.To view customer details\n2.To view room details\n3.To view receptionist details\n4.Add new receptionist\n5.Delete receptionist details\n6.EXIT\n\n\n\n'))
            if num==1:
                self.view_customers()
            elif num==2:
                self.view_rooms()
            elif num==3:
                self.view_rec()
            elif num==4:
                self.add_rec()
            elif num==5:
                self.rem_rec()
            elif num==6:
                quit()    
            else:
                print("Enter valid choice")        


def main():
    a = hotelfarecal()
    a.connectos()
    # time.sleep(.5)
    while (1):
        print('\n1.User Login')
        print('2.Receptionist Login')
        print('3.Manager Login')
        print('4.EXIT\n\n\n')

        b = int(input('Enter your choice:'))
        if (b == 1):
            a.user()
        elif (b == 2):
            a.receptionist()
        elif (b == 3):
            a.manager()
        elif (b == 4):
            quit()
        else:
            print('Error', space=True)


main()
