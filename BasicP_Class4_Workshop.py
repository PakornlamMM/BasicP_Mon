# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    # วนลูปแสดงชื่อหนังพร้อมราคาตั๋ว
    for movie in movie_list:
        print(f"{movie['movie_name']} - ราคา: {movie['ticket_price']} บาท")


# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
def check_age(user_age, age_restriction):
    # TODO: ถ้า age_restriction เป็น 'G' ให้ผ่านเลย
    # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age
    
    if age_restriction == 'G':
        return True
    
    elif user_age >= age_restriction:
        return True
    else:
        return False


# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    # TODO: ถ้า genre เป็น 'Horror' บวกเพิ่ม 50 บาท

    if genre == 'Horror':
        base_price += 50
        return base_price
    else:
        return base_price
    
         

# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movie_list):
    # TODO: 
    # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
    # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
    # 3. รับอายุผู้ใช้
    # 4. ตรวจสอบอายุผ่าน check_age
    #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
    # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
    # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
    # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว
    show_movies(movie_list)

        
    userAgeInput = input("Enter your age : ")
    
    movieChoice = int(input("Which movie will you choose? (1-5) : ")) - 1 
    movieChosen = movie_list[movieChoice]

    if not check_age(userAgeInput, movieChosen['age_restriction']):

        return "Your age doesn't met requirement"



    soundtrackChoice = input("Which soundtrack will you choose? : ")
    chosenSoundtrack = "Soundtrack"
    
    if soundtrackChoice == "Thai":
        chosenSoundtrack = "Thai"
        print("You choose Thai Soundtrack")
    elif soundtrackChoice == "Soundtrack":
        chosenSoundtrack = "Soundtrack"
        print("You choose Original Soundtrack")
    else:
        print("There's no soundtrack you want there")


    
    ticket_price = calculate_price(movieChosen['ticket_price'], movieChosen['genre'])
    print(f'ซื้อสำเร็จ!! ท่านได้เลือกซื้อ {movieChosen['movie_name']} เสียง {chosenSoundtrack} ราคา {ticket_price} บาท')
    return userAgeInput, chosenSoundtrack, ticket_price
    
    


def main():
    # TODO: สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

   
    # รับค่าตัวเลือกเมนูจากผู้ใช้
    menu = input("เลือกเมนู: ")
    
    if menu == "1":
       print(show_movies(movies))
    if menu == "2":
       print(buy_ticket(movies))
    else:
        print("The Menu you want doesn't apper here")
       
    
    

# เรียก main เพื่อเริ่มโปรแกรม
main()

