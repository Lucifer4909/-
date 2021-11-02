import aminofix

client = aminofix.Client()
client.login(email='588edeba7d@mohmal.club', password='Sherlock')
sub_client = aminofix.SubClient(comId='201946385', profile=client.profile)

file = open("hello.txt", "r+", encoding="UTF-8")
text = file.read()


oldUser = []
def bot():
    while True:
        x = sub_client.get_all_users(size=10000).profile
        for id, name in zip(x.userId, x.nickname):
            if id in oldUser:
                pass
            else:
                info = sub_client.get_wall_comments(userId=id, sorting="newest").content
                myString = ''.join(info)

                link = str(myString).lower().find("aminoapps")
                if int(link) != -1:
                    print(f"{name} уже поприветствован.")
                else:
                    try:
                        try:
                            sub_client.comment(message=text, userId=id)
                        except:
                            sub_client.comment(message=text, userId=id)
                    except:
                        pass
                    print(f"Только-что поприветствовались с {name}.")
                oldUser.append(id)

def launch():
    try:
        bot()
    except Exception as e:
        print(e)
        launch()

launch()