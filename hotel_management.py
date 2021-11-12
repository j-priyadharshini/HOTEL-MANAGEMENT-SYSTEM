import mysql.connector as ms
import datetime
import time
# import cfonts


class hotelfarecal:
    now = datetime.datetime.now()

    def __init__(self, rt='', s=0, p=0, r=0, t=0, a=1800, name='', address='', cindate='', coutdate='', rno=0, checkid=0):

        print("WELCOME TO HOTEL CALIFORNIA")

        self.rt = rt

        self.r = r

        self.t = t

        self.p = p

        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno
        self.checkid = checkid

    def connectos(self):
        cnx = ms.connect( user='root', password='makeuprani', database='hotel_mgmt')
        try:

            cur = cnx.cursor()
            cur.execute("Select * from customer ;")
            d = cur.fetchall()

            cnx.commit()
        except:
            print("Error in connection")

    def roomrent(self):

        print("We have the following rooms for you:-")
        cnx = ms.connect(user='root', password='makeuprani', host='localhost', database='hotel_mgmt')
        cur = cnx.cursor()
        cur.execute('Select * from `room rent`;')
        d = cur.fetchall()
        for i in d:
            print(i[0], ' ---- ', i[1], '\n')
        x = (input("Enter Your Choice Please->"))

        return x

    def inpututdata(self):

        self.name = input("Enter your name:")
        self.address = input("Enter your address:")
        self.cindate = input("Enter your check in date:")
        self.coutdate = input("Enter your checkout date:")
        cnx = ms.connect( user='root', password='makeuprani', host='localhost', database='hotel_mgmt')
        cur = cnx.cursor()
        cur.execute("Select max(checkid) from customer")
        d = cur.fetchall()

        str1 = ','.join([str(i) for i in d])  # values = ','.join([str(i) for i in value_list])
        str2 = str1[1:]
        str3 = str2[:1]
        val = int(str3)

        if cur.rowcount == 0:
            self.checkid = 1
        else:
            self.checkid = val + 1
            cur.execute("Select max(roomno) from customer")
            d = cur.fetchall()
            str4 = ','.join([str(i) for i in d])
            str5 = str4[1:]
            str6 = str5[:1]
            valr = int(str6)

        if cur.rowcount == 0:
            # print(cur.rowcount,'  fdgdfgdffgfd')
            self.rno = 1

        else:
            self.rno = valr + 1

            # print(d[0],'  fdgdfgdffgfd464564564')

        # print(self.rno,'sdfsdfsfds')

        roomchoice = self.roomrent()
        x = int(input('Enter the number of days you will be spending with us\t'))
        cur.execute('''INSERT INTO `customer`(`Name`, `Address`,
             `checkindate`,`checkoutdate`,`roomno`, `checkid`) values ('%s','%s','%s','%s',%d,%d)''' % (self.name, self.address, self.cindate, self.coutdate, self.rno, self.checkid))
        print("Your room no.:", self.rno, "\n")
        print("check id is:", self.checkid, "\n")
        cur.execute("INSERT INTO `rooms`(`checkid`, `roomtype`, `noofdays`) VALUES (%d,'%s',%d)" % (self.checkid, roomchoice, x))
        cnx.commit()
        print("Thank you for registering!")

    def restaurentbill(self):
        try:
            cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='makeuprani', host='localhost', database='hotel_mgmt')
            cur = cnx.cursor()
            f = int(input("Enter your check in id"))
            cur.execute("Select * from customer where checkid='%d'" % (f))
            d = cur.fetchall()
            if cur.rowcount != 0:
                print("RESTAURANT MENU", font='chrome', colors=['red', 'green', 'blue'], align='center', space=True)
                cur.execute("Select * from menu;")
                d = cur.fetchall()
                for i in d:
                    print(i[0], "-----", i[1], "",)
                print("press 1 to exit")
                while (1):
                    try:

                        c = input("Enter your choice:")
                        if c == '1':
                            break
                        else:
                            cur.execute("Select price from menu where item ='%s'" % (c))
                            if cur.rowcount != 0:
                                # print(cur.rowcount)
                                d = cur.fetchall()
                                st = ','.join([str(i) for i in d])

                                st1 = st[1:]
                                st2 = st1[:4]
                                j1 = int(st2)
                                qu = int(input("Enter the quantity : "))

                                self.r += (j1 * qu)
                            else:
                                print("Sorry we dont have that on the menu")
                    except:
                        print("Sorry we dont have that on the menu")
                print("Total food Cost=Rs", self.r, "\n")
                now = datetime.datetime.now()
                dt = now.strftime("%Y-%m-%d")
                cur.execute("INSERT INTO `restaurant`(`checkid`, `bill`, `date`) VALUES (%d,%d,'%s')" % (f, self.r, dt))
                cnx.commit()
            else:
                print("Incorrect check id. Please choose 1 in  the main menu to register.")
                # cnx = ms.connect(unix_socket= '/Applications/MAMP/tmp/mysql/mysql.sock',user='root', password='root',host='localhost', database='hotel_mgmt')
                # cur=cnx.cursor()
        except:
            print("Our chef seems to have some personal issues. Please visit us later. :(")

    def laundrybill(self):
        try:
            now = datetime.datetime.now()
            cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='makeuprani', host='localhost', database='hotel_mgmt')
            cur = cnx.cursor()
            dt = now.strftime("%Y-%m-%d")

            f = int(input("Enter your check in id"))
            cur.execute("Select * from customer where checkid='%d'" % (f))
            d = cur.fetchall()
            if cur.rowcount != 0:
                print("LAUNDRY MENU")
                cur.execute("Select * from laundrymenu;")
                d = cur.fetchall()
                for i in d:
                    print(i[0], "-----", i[1], "")
                print("press 1 to exit")
                while (1):
                    try:

                        c = input("Enter your choice : ")
                        if c == '1':
                            break
                        else:
                            cur.execute("Select price from laundrymenu where cloth ='%s'" % (c.upper()))
                            if cur.rowcount != 0:
                                # print(cur.rowcount)
                                d = cur.fetchall()
                                st = ','.join([str(i) for i in d])

                                st1 = st[1:]
                                st2 = st1[:4]
                                j1 = int(st2)

                                qu = int(input("Enter the quantity : "))

                                self.t += (j1 * qu)
                            else:
                                print("Please wash that yourself. ^_^")
                    except:
                        print("Please wash that yourself.  ^_^")
                print("Total Laundary Cost=Rs", self.t)
                cur.execute("INSERT INTO `laundry`(`checkid`, `price`, `date`) VALUES (%d,%d,'%s')" % (f, self.t, dt))
                cnx.commit()
            else:
                print("Incorrect check id. Please choose 1 in  the main menu to register.")
                # cnx = ms.connect(unix_socket= '/Applications/MAMP/tmp/mysql/mysql.sock',user='root', password='root',host='localhost', database='hotel_mgmt')
                # cur=cnx.cursor()
        except:
            print("Our washing machine is currently busy with an Infosys project. Please contact the washing machine for further details. :(")

    def gamebill(self):
        try:
            now = datetime.datetime.now()
            cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='makeuprani', host='localhost', database='hotel_mgmt')
            cur = cnx.cursor()
            dt = now.strftime("%Y-%m-%d %H:%M:%S")

            f = int(input("Enter your check in id"))
            cur.execute("Select * from customer where checkid='%d'" % (f))
            d = cur.fetchall()
            if cur.rowcount != 0:
                print("GAME MENU", font='chrome')
                cur.execute("Select * from gamemenu;")
                d = cur.fetchall()
                for i in d:
                    print(i[0], "-----", i[1], "")
                print("Press 1 to exit")
                while (1):
                    try:

                        c = input("Enter your choice : ")
                        if c == '1':
                            break
                        else:
                            cur.execute("Select price from gamemenu where gamename ='%s'" % (c.upper()))
                            if cur.rowcount != 0:
                                # print(cur.rowcount)
                                d = cur.fetchall()
                                st = ','.join([str(i) for i in d])

                                st1 = st[1:]
                                st2 = st1[:4]
                                j1 = int(st2)

                                qu = int(input("Enter the number of hours : "))

                                self.p += (j1 * qu)
                            else:
                                print("Sorry we can't allow you to play that. :(")
                    except:
                        print("Sorry we can't allow you to play that. :(")
                print("Gaming Cost=Rs", self.p, "\n")
                cur.execute("INSERT INTO `game`(`checkid`, `price`, `gamedate`) VALUES (%d,%d,'%s')" % (f, self.p, dt))
                cnx.commit()
            else:
                print("Incorrect check id. Please choose 1 in  the main menu to register.")
                # cnx = ms.connect(unix_socket= '/Applications/MAMP/tmp/mysql/mysql.sock',user='root', password='root',host='localhost', database='hotel_mgmt')
                # cur=cnx.cursor()
        except:
            print("Your competitor is busy studying for the Infosys Foundation Programme 5.0. It's time you opened the .bat file as well. -_-")

    def display(self):
        print("HOTEL BILL")
        now = datetime.datetime.now()
        cnx = ms.connect(unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', user='root', password='makeuprani', host='localhost', database='hotel_mgmt')
        cur = cnx.cursor()
        dt = now.strftime("%Y-%m-%d")

        f = int(input("Enter your check in id"))
        cur.execute("select c.checkid,c.Name,c.checkindate,c.checkoutdate,c.roomno from customer c where c.checkid= %d ;" % (f))
        d = cur.fetchall()
        if cur.rowcount > 0:
            for row in d:
                self.name = row[1]
                self.cindate = row[2]
                self.coutdate = row[3]
                self.rno = row[4]
            cur.execute('''select  rr.price, r.noofdays from rooms r join `room rent`
               rr on rr.roomtype=r.roomtype where r.checkid=%d;
               ''' % (f))
            d = cur.fetchall()
            for row in d:
                self.s = int(row[0]) * int(row[1])

            cur.execute("select sum(r.bill) from restaurant r group by r.checkid having r.checkid=%d;" % (f))
            d = cur.fetchall()
            if cur.rowcount > 0:
                for row in d:
                    self.r = row[0]
            cur.execute("select sum(l.price)from laundry l GROUP by l.checkid having l.checkid=%d;" % (f))
            d = cur.fetchall()
            if cur.rowcount > 0:
                for row in d:
                    self.t = row[0]
            cur.execute("select sum(l.price)from game l GROUP by l.checkid having l.checkid=%d;" % (f))
            d = cur.fetchall()
            if cur.rowcount > 0:
                for row in d:
                    self.p = row[0]

            print("Customer details:")
            print("Customer name:\t", self.name)
            print("Check in date:\t", self.cindate)
            print("Check out date:\t", self.coutdate)
            print("Room no.\t", self.rno)
            print("Your Room rent is:\t", self.s)
            print("Your Food bill is:\t", self.r)
            print("Your laundary bill is:\t", self.t)
            print("Your Game bill is:\t", self.p)
            self.rt = self.s + self.t + self.p + self.r
            print("Your sub total bill is:\t", self.rt)
            print("Additional Service Charges are \t", self.a)
            print("Your grandtotal bill is:\t", self.rt + self.a, "\n")
        else:
            print("Incorrect check in id please make sure you enter the correct check in id")


# def print(text, *args, font='console', size=(150, 32), colors=['white'], background='transparent', align='left', line_height=1, space=False):
#     for i in args:
#         text += str(i)
        
     # ['black','red','green','yellow','blue','magenta','cyan','white','bright_black','bright_red','bright_green','bright_yellow','bright_blue','bright_magenta','bright_cyan','bright_white']
    # ['console','block','simpleBlock','simple','3d','simple3d','chrome','huge']



# def input(text, *args, font='console', size=(150, 32), colors=['blue'], background='transparent', align='left', line_height=1, space=False):
#     for i in args:
#         text.append(i)
#     inputs = text
#     print(text)
#     return inputut(inputs)


def main():
    a = hotelfarecal()
    a.connectos()
    # time.sleep(.5)
    while (1):
        print("1.Enter Customer Data")

        # print("2.Calculate rommrent")

        print("2.Calculate restaurant bill")

        print("3.Calculate laundry bill")

        print("4.Calculate Game bill")

        print("5.Show total cost")

        print("6.EXIT")

        b = int(input("Enter your choice:"))
        if (b == 1):
            a.inpututdata()
        elif (b == 2):
            a.restaurentbill()
        elif (b == 3):
            a.laundrybill()
        elif (b == 4):
            a.gamebill()
        elif (b == 5):
            a.display()
        elif (b == 6):
            quit()
        else:
            print("Error", space=True)


main()
