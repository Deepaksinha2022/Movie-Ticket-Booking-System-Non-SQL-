from operation import MovieTicket
class Main:
    
    def execute(self,choice):
        if choice == 1:
            print("**************Show Seats***************")            
            movieticket_obj.ShowtheSeats()
            
        if choice == 2:
            print("**************Buy Tickets**************")
            movieticket_obj.BuyTicket()
            
        if choice == 3:
            print("************Statistics*****************")
            movieticket_obj.Statistics()
            
        if choice == 4:
            print("************Booked Ticket User Info***********")
            movieticket_obj.get_user_info()
            
        if choice == 5:
            print("Thank You for Connecting !!!!")
            exit()




if __name__ == "__main__":
    
    rows = int(input("Enter the number of rows : "))
    coloumns = int(input("Enter the number of seats in each row : "))
    main_obj = Main()
    movieticket_obj= MovieTicket(rows,coloumns)
    while True:
        choice = int(input(f"Enter\n1.Show the Seats \n2.Buy a Ticket \n3.Statistics \n4.Show Book Ticket user Info \n5.Exit\n"))
        main_obj.execute(choice)