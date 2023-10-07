
class MovieTicket:
    
    def __init__(self,rows,coloumns):
        self.rows = rows
        self.coloumns =  coloumns
        self.user_details={}
    def ShowtheSeats(self):
        for i in  range(self.rows+1):
            for j in range(self.coloumns+1):
                if i == 0 and j == 0:
                    print(" ",end=" ")
                elif j == 0:
                    print(i,end=" ")  
                elif i == 0:
                    print(j,end= " ")
                elif self.isBooked(i,j):
                    print("B",end= " ")                
                else :
                    print("S",end=" ") 
            print() 
    def BuyTicket(self):
        row = int(input("Enter the row number : "))
        coloumns = int(input("Enter the coloumn number : "))
        seat = str(row) + str(coloumns)
        total_seats = self.rows * self.coloumns 
        if total_seats <= 60:
            ticket_price = 10
        else:
            if row < (self.rows//2):
                ticket_price = 10
            else:
                ticket_price = 8
        buy_choice=int(input(f"Your selected seat number is {seat} and total price is {ticket_price} if you want to book \nEnter \n1.Yes \n2.No\n"))
        if buy_choice == 1:
            name=input("Enter Your Name : ")
            gender = input("Enter Your Gender (Male/Female) : ")
            age=int(input("Enter Your Age : "))
            phone_num=int(input("Enter Your Mobile Number : "))
            self.user_details[seat] = [name,gender,age,phone_num,ticket_price]
            print("*****Booket Ticket Successfully*****")
        if buy_choice == 2:
            print("No Problem Thank You for Connecting !!!!")
            exit()
    def isBooked(self,i,j):
        seat= str(i) + str(j)
        if seat in self.user_details.keys():
            return True
        else:
            return False
            
    def Statistics(self):
        price=[]
        count=0
        for i in self.user_details.keys():
            count+=1
        total_seats=self.rows*self.coloumns   
        perentage_booked = (count/total_seats)*100
        current_income=0
        for j in self.user_details.values():
            price.append(j[4])
        for k in price:
            current_income+=k
            
        if total_seats<=60:
            total_income=total_seats*10
        else:
            first_half=self.coloumns*(self.rows//2)
            second_half=total_seats-first_half
            total_income = first_half*10 + second_half*8
        print(f"Percentage of Ticket Booked is : {perentage_booked}")
        print(f"Number of Purchased Tickets is : {count}") 
        print(f"Current Income is : {current_income}")
        print(f"Total Income is : {total_income}")
        
    def get_user_info(self):
        rows=int(input("Enter the row number of seat for which you want the info. : "))
        coloumn=int(input("Enter the coloumn number of seat for which you want the info. : "))
        
        seat_no = str(rows)+str(coloumn)

        if seat_no in self.user_details.keys():
            user = self.user_details.values[seat_no]
            print(f"\nName : {user[0]}")
            print(f"Gender : {user[1]}")
            print(f"Age : {user[2]}")
            print(f"Ticket Price : {user[3]}")
            print(f"Phone No. : {user[4]}\n")
        else:
            print(f"The seat number you were looking for has not been booked!!!")