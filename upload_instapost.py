from instabot import Bot
bot=Bot()
bot.login(username=input("Enter your id:"),password=input("Enter your password:"))
bot.upload_photo("D:\IMG20210907133228004.jpg",caption="Glowing Text Effect")
